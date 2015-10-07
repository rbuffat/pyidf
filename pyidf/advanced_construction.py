""" Data objects in group "Advanced Construction"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class SurfacePropertyHeatTransferAlgorithm(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm`
        Determines which Heat Balance Algorithm will be used for a specific surface
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'algorithm',
                                       {'name': u'Algorithm',
                                        'pyname': u'algorithm',
                                        'default': u'ConductionTransferFunction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ConductionTransferFunction',
                                                            u'MoisturePenetrationDepthConductionTransferFunction',
                                                            u'ConductionFiniteDifference',
                                                            u'CombinedHeatAndMoistureFiniteElement'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 2,
               'name': u'SurfaceProperty:HeatTransferAlgorithm',
               'pyname': u'SurfacePropertyHeatTransferAlgorithm',
               'required-object': False,
               'unique-object': False}

    @property
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def algorithm(self):
        """field `Algorithm`

        |  Default value: ConductionTransferFunction

        Args:
            value (str): value for IDD Field `Algorithm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `algorithm` or None if not set

        """
        return self["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """Corresponds to IDD field `Algorithm`"""
        self["Algorithm"] = value




class SurfacePropertyHeatTransferAlgorithmMultipleSurface(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm:MultipleSurface`
        Determines which Heat Balance Algorithm will be used for a group of surface types
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'surface type',
                                       {'name': u'Surface Type',
                                        'pyname': u'surface_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'AllExteriorSurfaces',
                                                            u'AllExteriorWalls',
                                                            u'AllExteriorRoofs',
                                                            u'AllExteriorFloors',
                                                            u'AllGroundContactSurfaces',
                                                            u'AllInteriorSurfaces',
                                                            u'AllInteriorWalls',
                                                            u'AllInteriorCeilings',
                                                            u'AllInteriorFloors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'algorithm',
                                       {'name': u'Algorithm',
                                        'pyname': u'algorithm',
                                        'default': u'ConductionTransferFunction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ConductionTransferFunction',
                                                            u'MoisturePenetrationDepthConductionTransferFunction',
                                                            u'ConductionFiniteDifference',
                                                            u'CombinedHeatAndMoistureFiniteElement'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 3,
               'name': u'SurfaceProperty:HeatTransferAlgorithm:MultipleSurface',
               'pyname': u'SurfacePropertyHeatTransferAlgorithmMultipleSurface',
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
    def surface_type(self):
        """field `Surface Type`

        Args:
            value (str): value for IDD Field `Surface Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_type` or None if not set

        """
        return self["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """Corresponds to IDD field `Surface Type`"""
        self["Surface Type"] = value

    @property
    def algorithm(self):
        """field `Algorithm`

        |  Default value: ConductionTransferFunction

        Args:
            value (str): value for IDD Field `Algorithm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `algorithm` or None if not set

        """
        return self["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """Corresponds to IDD field `Algorithm`"""
        self["Algorithm"] = value




class SurfacePropertyHeatTransferAlgorithmSurfaceList(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm:SurfaceList`
        Determines which Heat Balance Algorithm will be used for a list of surfaces
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface name 1',
                                                  {'name': u'Surface Name 1',
                                                   'pyname': u'surface_name_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'algorithm',
                                       {'name': u'Algorithm',
                                        'pyname': u'algorithm',
                                        'default': u'ConductionTransferFunction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ConductionTransferFunction',
                                                            u'MoisturePenetrationDepthConductionTransferFunction',
                                                            u'ConductionFiniteDifference',
                                                            u'CombinedHeatAndMoistureFiniteElement'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 3,
               'name': u'SurfaceProperty:HeatTransferAlgorithm:SurfaceList',
               'pyname': u'SurfacePropertyHeatTransferAlgorithmSurfaceList',
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
    def algorithm(self):
        """field `Algorithm`

        |  Default value: ConductionTransferFunction

        Args:
            value (str): value for IDD Field `Algorithm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `algorithm` or None if not set

        """
        return self["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """Corresponds to IDD field `Algorithm`"""
        self["Algorithm"] = value

    def add_extensible(self,
                       surface_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_name_1 (str): value for IDD Field `Surface Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_name_1 = self.check_value("Surface Name 1", surface_name_1)
        vals.append(surface_name_1)
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




class SurfacePropertyHeatTransferAlgorithmConstruction(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm:Construction`
        Determines which Heat Balance Algorithm will be used for surfaces that have a specific type of construction
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'algorithm',
                                       {'name': u'Algorithm',
                                        'pyname': u'algorithm',
                                        'default': u'ConductionTransferFunction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ConductionTransferFunction',
                                                            u'MoisturePenetrationDepthConductionTransferFunction',
                                                            u'ConductionFiniteDifference',
                                                            u'CombinedHeatAndMoistureFiniteElement'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'construction name',
                                       {'name': u'Construction Name',
                                        'pyname': u'construction_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 3,
               'name': u'SurfaceProperty:HeatTransferAlgorithm:Construction',
               'pyname': u'SurfacePropertyHeatTransferAlgorithmConstruction',
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
    def algorithm(self):
        """field `Algorithm`

        |  Default value: ConductionTransferFunction

        Args:
            value (str): value for IDD Field `Algorithm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `algorithm` or None if not set

        """
        return self["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """Corresponds to IDD field `Algorithm`"""
        self["Algorithm"] = value

    @property
    def construction_name(self):
        """field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `construction_name` or None if not set

        """
        return self["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """Corresponds to IDD field `Construction Name`"""
        self["Construction Name"] = value




class SurfaceControlMovableInsulation(DataObject):

    """ Corresponds to IDD object `SurfaceControl:MovableInsulation`
        Exterior or Interior Insulation on opaque surfaces
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'insulation type',
                                       {'name': u'Insulation Type',
                                        'pyname': u'insulation_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Outside',
                                                            u'Inside'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceControl:MovableInsulation',
               'pyname': u'SurfaceControlMovableInsulation',
               'required-object': False,
               'unique-object': False}

    @property
    def insulation_type(self):
        """field `Insulation Type`

        Args:
            value (str): value for IDD Field `Insulation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `insulation_type` or None if not set

        """
        return self["Insulation Type"]

    @insulation_type.setter
    def insulation_type(self, value=None):
        """Corresponds to IDD field `Insulation Type`"""
        self["Insulation Type"] = value

    @property
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def material_name(self):
        """field `Material Name`

        Args:
            value (str): value for IDD Field `Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `material_name` or None if not set

        """
        return self["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """Corresponds to IDD field `Material Name`"""
        self["Material Name"] = value

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




class SurfacePropertyOtherSideCoefficients(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:OtherSideCoefficients`
        This object sets the other side conditions for a surface in a variety of ways.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'combined convective/radiative film coefficient',
                                       {'name': u'Combined Convective/Radiative Film Coefficient',
                                        'pyname': u'combined_convective_or_radiative_film_coefficient',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'constant temperature',
                                       {'name': u'Constant Temperature',
                                        'pyname': u'constant_temperature',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'constant temperature coefficient',
                                       {'name': u'Constant Temperature Coefficient',
                                        'pyname': u'constant_temperature_coefficient',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'external dry-bulb temperature coefficient',
                                       {'name': u'External Dry-Bulb Temperature Coefficient',
                                        'pyname': u'external_drybulb_temperature_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'ground temperature coefficient',
                                       {'name': u'Ground Temperature Coefficient',
                                        'pyname': u'ground_temperature_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wind speed coefficient',
                                       {'name': u'Wind Speed Coefficient',
                                        'pyname': u'wind_speed_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'zone air temperature coefficient',
                                       {'name': u'Zone Air Temperature Coefficient',
                                        'pyname': u'zone_air_temperature_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'constant temperature schedule name',
                                       {'name': u'Constant Temperature Schedule Name',
                                        'pyname': u'constant_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sinusoidal variation of constant temperature coefficient',
                                       {'name': u'Sinusoidal Variation of Constant Temperature Coefficient',
                                        'pyname': u'sinusoidal_variation_of_constant_temperature_coefficient',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'period of sinusoidal variation',
                                       {'name': u'Period of Sinusoidal Variation',
                                        'pyname': u'period_of_sinusoidal_variation',
                                        'default': 24.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'previous other side temperature coefficient',
                                       {'name': u'Previous Other Side Temperature Coefficient',
                                        'pyname': u'previous_other_side_temperature_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum other side temperature limit',
                                       {'name': u'Minimum Other Side Temperature Limit',
                                        'pyname': u'minimum_other_side_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum other side temperature limit',
                                       {'name': u'Maximum Other Side Temperature Limit',
                                        'pyname': u'maximum_other_side_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 8,
               'name': u'SurfaceProperty:OtherSideCoefficients',
               'pyname': u'SurfacePropertyOtherSideCoefficients',
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
    def combined_convective_or_radiative_film_coefficient(self):
        """field `Combined Convective/Radiative Film Coefficient`

        |  if>0, this field becomes the exterior convective/radiative film coefficient
        |  and the other fields are used to calculate the outdoor air temperature
        |  then exterior surface temperature based on outdoor air and specified coefficient
        |  if<=0, then remaining fields calculate the outside surface temperature
        |  The following fields are used in the equation:
        |  OtherSideTemp=N2*N3 + N4*OutdoorDry-bulb + N5*GroundTemp + N6*WindSpeed*OutdoorDry-bulb + N7*TempZone + N9*TempPrev
        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Combined Convective/Radiative Film Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `combined_convective_or_radiative_film_coefficient` or None if not set

        """
        return self["Combined Convective/Radiative Film Coefficient"]

    @combined_convective_or_radiative_film_coefficient.setter
    def combined_convective_or_radiative_film_coefficient(self, value=None):
        """Corresponds to IDD field `Combined Convective/Radiative Film
        Coefficient`"""
        self["Combined Convective/Radiative Film Coefficient"] = value

    @property
    def constant_temperature(self):
        """field `Constant Temperature`

        |  This parameter will be overwritten by the values from the Constant Temperature Schedule Name (below) if one is present
        |  Units: C

        Args:
            value (float): value for IDD Field `Constant Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_temperature` or None if not set

        """
        return self["Constant Temperature"]

    @constant_temperature.setter
    def constant_temperature(self, value=None):
        """Corresponds to IDD field `Constant Temperature`"""
        self["Constant Temperature"] = value

    @property
    def constant_temperature_coefficient(self):
        """field `Constant Temperature Coefficient`

        |  This coefficient is used even with a Schedule.  It should normally be 1.0 in that case.
        |  This field is ignored if Sinusoidal Variation of Constant Temperature Coefficient = Yes.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Constant Temperature Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_temperature_coefficient` or None if not set

        """
        return self["Constant Temperature Coefficient"]

    @constant_temperature_coefficient.setter
    def constant_temperature_coefficient(self, value=1.0):
        """Corresponds to IDD field `Constant Temperature Coefficient`"""
        self["Constant Temperature Coefficient"] = value

    @property
    def external_drybulb_temperature_coefficient(self):
        """field `External Dry-Bulb Temperature Coefficient`


        Args:
            value (float): value for IDD Field `External Dry-Bulb Temperature Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `external_drybulb_temperature_coefficient` or None if not set
        """
        return self["External Dry-Bulb Temperature Coefficient"]

    @external_drybulb_temperature_coefficient.setter
    def external_drybulb_temperature_coefficient(self, value=None):
        """  Corresponds to IDD field `External Dry-Bulb Temperature Coefficient`

        """
        self["External Dry-Bulb Temperature Coefficient"] = value

    @property
    def ground_temperature_coefficient(self):
        """field `Ground Temperature Coefficient`

        Args:
            value (float): value for IDD Field `Ground Temperature Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ground_temperature_coefficient` or None if not set

        """
        return self["Ground Temperature Coefficient"]

    @ground_temperature_coefficient.setter
    def ground_temperature_coefficient(self, value=None):
        """Corresponds to IDD field `Ground Temperature Coefficient`"""
        self["Ground Temperature Coefficient"] = value

    @property
    def wind_speed_coefficient(self):
        """field `Wind Speed Coefficient`

        Args:
            value (float): value for IDD Field `Wind Speed Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_speed_coefficient` or None if not set

        """
        return self["Wind Speed Coefficient"]

    @wind_speed_coefficient.setter
    def wind_speed_coefficient(self, value=None):
        """Corresponds to IDD field `Wind Speed Coefficient`"""
        self["Wind Speed Coefficient"] = value

    @property
    def zone_air_temperature_coefficient(self):
        """field `Zone Air Temperature Coefficient`

        Args:
            value (float): value for IDD Field `Zone Air Temperature Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_air_temperature_coefficient` or None if not set

        """
        return self["Zone Air Temperature Coefficient"]

    @zone_air_temperature_coefficient.setter
    def zone_air_temperature_coefficient(self, value=None):
        """Corresponds to IDD field `Zone Air Temperature Coefficient`"""
        self["Zone Air Temperature Coefficient"] = value

    @property
    def constant_temperature_schedule_name(self):
        """field `Constant Temperature Schedule Name`

        |  Name of schedule for values of constant temperature.
        |  Schedule values replace any value specified in the field Constant Temperature.

        Args:
            value (str): value for IDD Field `Constant Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `constant_temperature_schedule_name` or None if not set

        """
        return self["Constant Temperature Schedule Name"]

    @constant_temperature_schedule_name.setter
    def constant_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Constant Temperature Schedule Name`"""
        self["Constant Temperature Schedule Name"] = value

    @property
    def sinusoidal_variation_of_constant_temperature_coefficient(self):
        """field `Sinusoidal Variation of Constant Temperature Coefficient`

        |  Optionally used to vary Constant Temperature Coefficient with unitary sine wave
        |  Default value: No

        Args:
            value (str): value for IDD Field `Sinusoidal Variation of Constant Temperature Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sinusoidal_variation_of_constant_temperature_coefficient` or None if not set

        """
        return self["Sinusoidal Variation of Constant Temperature Coefficient"]

    @sinusoidal_variation_of_constant_temperature_coefficient.setter
    def sinusoidal_variation_of_constant_temperature_coefficient(
            self,
            value="No"):
        """Corresponds to IDD field `Sinusoidal Variation of Constant
        Temperature Coefficient`"""
        self[
            "Sinusoidal Variation of Constant Temperature Coefficient"] = value

    @property
    def period_of_sinusoidal_variation(self):
        """field `Period of Sinusoidal Variation`

        |  Use with sinusoidal variation to define the time period
        |  Units: hr
        |  Default value: 24.0

        Args:
            value (float): value for IDD Field `Period of Sinusoidal Variation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `period_of_sinusoidal_variation` or None if not set

        """
        return self["Period of Sinusoidal Variation"]

    @period_of_sinusoidal_variation.setter
    def period_of_sinusoidal_variation(self, value=24.0):
        """Corresponds to IDD field `Period of Sinusoidal Variation`"""
        self["Period of Sinusoidal Variation"] = value

    @property
    def previous_other_side_temperature_coefficient(self):
        """field `Previous Other Side Temperature Coefficient`

        |  This coefficient multiplies the other side temperature result from the
        |  previous zone timestep

        Args:
            value (float): value for IDD Field `Previous Other Side Temperature Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `previous_other_side_temperature_coefficient` or None if not set

        """
        return self["Previous Other Side Temperature Coefficient"]

    @previous_other_side_temperature_coefficient.setter
    def previous_other_side_temperature_coefficient(self, value=None):
        """Corresponds to IDD field `Previous Other Side Temperature
        Coefficient`"""
        self["Previous Other Side Temperature Coefficient"] = value

    @property
    def minimum_other_side_temperature_limit(self):
        """field `Minimum Other Side Temperature Limit`

        |  This field specifies a lower limit for the other side temperature result.
        |  Blank indicates no limit
        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Other Side Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_other_side_temperature_limit` or None if not set

        """
        return self["Minimum Other Side Temperature Limit"]

    @minimum_other_side_temperature_limit.setter
    def minimum_other_side_temperature_limit(self, value=None):
        """Corresponds to IDD field `Minimum Other Side Temperature Limit`"""
        self["Minimum Other Side Temperature Limit"] = value

    @property
    def maximum_other_side_temperature_limit(self):
        """field `Maximum Other Side Temperature Limit`

        |  This field specifies an upper limit for the other side temperature result.
        |  Blank indicates no limit
        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Other Side Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_other_side_temperature_limit` or None if not set

        """
        return self["Maximum Other Side Temperature Limit"]

    @maximum_other_side_temperature_limit.setter
    def maximum_other_side_temperature_limit(self, value=None):
        """Corresponds to IDD field `Maximum Other Side Temperature Limit`"""
        self["Maximum Other Side Temperature Limit"] = value




class SurfacePropertyOtherSideConditionsModel(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:OtherSideConditionsModel`
        This object sets up modifying the other side conditions for a surface from other model results.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'type of modeling',
                                       {'name': u'Type of Modeling',
                                        'pyname': u'type_of_modeling',
                                        'default': u'GapConvectionRadiation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'GapConvectionRadiation',
                                                            u'UndergroundPipingSystemSurface',
                                                            u'GroundCoupledSurface'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceProperty:OtherSideConditionsModel',
               'pyname': u'SurfacePropertyOtherSideConditionsModel',
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
    def type_of_modeling(self):
        """field `Type of Modeling`

        |  GapConvectionRadiation provides boundary conditions for convection
        |  and linearized thermal radiation across a gap or cavity
        |  on the other side of the surface that are modeled separately.
        |  UndergroundPipingSystemSurface provides boundary conditions for
        |  surfaces in contact with PipingSystem:Underground domains
        |  GroundCoupledSurface provides boundary conditions for surfaces
        |  in contact with GroundDomain objects
        |  Default value: GapConvectionRadiation

        Args:
            value (str): value for IDD Field `Type of Modeling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `type_of_modeling` or None if not set

        """
        return self["Type of Modeling"]

    @type_of_modeling.setter
    def type_of_modeling(self, value="GapConvectionRadiation"):
        """Corresponds to IDD field `Type of Modeling`"""
        self["Type of Modeling"] = value




class SurfaceConvectionAlgorithmInsideAdaptiveModelSelections(DataObject):

    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the inside face, the side of the surface facing a thermal zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'simple buoyancy vertical wall equation source',
                                       {'name': u'Simple Buoyancy Vertical Wall Equation Source',
                                        'pyname': u'simple_buoyancy_vertical_wall_equation_source',
                                        'default': u'FohannoPolidoriVerticalWall',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'simple buoyancy vertical wall user curve name',
                                       {'name': u'Simple Buoyancy Vertical Wall User Curve Name',
                                        'pyname': u'simple_buoyancy_vertical_wall_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'simple buoyancy stable horizontal equation source',
                                       {'name': u'Simple Buoyancy Stable Horizontal Equation Source',
                                        'pyname': u'simple_buoyancy_stable_horizontal_equation_source',
                                        'default': u'AlamdariHammondStableHorizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'simple buoyancy stable horizontal equation user curve name',
                                       {'name': u'Simple Buoyancy Stable Horizontal Equation User Curve Name',
                                        'pyname': u'simple_buoyancy_stable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'simple buoyancy unstable horizontal equation source',
                                       {'name': u'Simple Buoyancy Unstable Horizontal Equation Source',
                                        'pyname': u'simple_buoyancy_unstable_horizontal_equation_source',
                                        'default': u'AlamdariHammondUnstableHorizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'simple buoyancy unstable horizontal equation user curve name',
                                       {'name': u'Simple Buoyancy Unstable Horizontal Equation User Curve Name',
                                        'pyname': u'simple_buoyancy_unstable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'simple buoyancy stable tilted equation source',
                                       {'name': u'Simple Buoyancy Stable Tilted Equation Source',
                                        'pyname': u'simple_buoyancy_stable_tilted_equation_source',
                                        'default': u'WaltonStableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'simple buoyancy stable tilted equation user curve name',
                                       {'name': u'Simple Buoyancy Stable Tilted Equation User Curve Name',
                                        'pyname': u'simple_buoyancy_stable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'simple buoyancy unstable tilted equation source',
                                       {'name': u'Simple Buoyancy Unstable Tilted Equation Source',
                                        'pyname': u'simple_buoyancy_unstable_tilted_equation_source',
                                        'default': u'WaltonUnstableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'simple buoyancy unstable tilted equation user curve name',
                                       {'name': u'Simple Buoyancy Unstable Tilted Equation User Curve Name',
                                        'pyname': u'simple_buoyancy_unstable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'simple buoyancy windows equation source',
                                       {'name': u'Simple Buoyancy Windows Equation Source',
                                        'pyname': u'simple_buoyancy_windows_equation_source',
                                        'default': u'ISO15099Windows',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'KaradagChilledCeiling',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'simple buoyancy windows equation user curve name',
                                       {'name': u'Simple Buoyancy Windows Equation User Curve Name',
                                        'pyname': u'simple_buoyancy_windows_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool vertical wall equation source',
                                       {'name': u'Floor Heat Ceiling Cool Vertical Wall Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_vertical_wall_equation_source',
                                        'default': u'KhalifaEq3WallAwayFromHeat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool vertical wall equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool stable horizontal equation source',
                                       {'name': u'Floor Heat Ceiling Cool Stable Horizontal Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_stable_horizontal_equation_source',
                                        'default': u'AlamdariHammondStableHorizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool stable horizontal equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool unstable horizontal equation source',
                                       {'name': u'Floor Heat Ceiling Cool Unstable Horizontal Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_unstable_horizontal_equation_source',
                                        'default': u'KhalifaEq4CeilingAwayFromHeat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool unstable horizontal equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool heated floor equation source',
                                       {'name': u'Floor Heat Ceiling Cool Heated Floor Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_heated_floor_equation_source',
                                        'default': u'AwbiHattonHeatedFloor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'AwbiHattonHeatedFloor',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool heated floor equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Heated Floor Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_heated_floor_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool chilled ceiling equation source',
                                       {'name': u'Floor Heat Ceiling Cool Chilled Ceiling Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_chilled_ceiling_equation_source',
                                        'default': u'KaradagChilledCeiling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'KaradagChilledCeiling',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool chilled ceiling equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool stable tilted equation source',
                                       {'name': u'Floor Heat Ceiling Cool Stable Tilted Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_stable_tilted_equation_source',
                                        'default': u'WaltonStableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool stable tilted equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool unstable tilted equation source',
                                       {'name': u'Floor Heat Ceiling Cool Unstable Tilted Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_unstable_tilted_equation_source',
                                        'default': u'WaltonUnstableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool unstable tilted equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'floor heat ceiling cool window equation source',
                                       {'name': u'Floor Heat Ceiling Cool Window Equation Source',
                                        'pyname': u'floor_heat_ceiling_cool_window_equation_source',
                                        'default': u'ISO15099Windows',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'floor heat ceiling cool window equation user curve name',
                                       {'name': u'Floor Heat Ceiling Cool Window Equation User Curve Name',
                                        'pyname': u'floor_heat_ceiling_cool_window_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating vertical wall equation source',
                                       {'name': u'Wall Panel Heating Vertical Wall Equation Source',
                                        'pyname': u'wall_panel_heating_vertical_wall_equation_source',
                                        'default': u'KhalifaEq6NonHeatedWalls',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating vertical wall equation user curve name',
                                       {'name': u'Wall Panel Heating Vertical Wall Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_vertical_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating heated wall equation source',
                                       {'name': u'Wall Panel Heating Heated Wall Equation Source',
                                        'pyname': u'wall_panel_heating_heated_wall_equation_source',
                                        'default': u'AwbiHattonHeatedWall',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq5WallNearHeat',
                                                            u'AwbiHattonHeatedWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating heated wall equation user curve name',
                                       {'name': u'Wall Panel Heating Heated Wall Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_heated_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating stable horizontal equation source',
                                       {'name': u'Wall Panel Heating Stable Horizontal Equation Source',
                                        'pyname': u'wall_panel_heating_stable_horizontal_equation_source',
                                        'default': u'AlamdariHammondStableHorizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating stable horizontal equation user curve name',
                                       {'name': u'Wall Panel Heating Stable Horizontal Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_stable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating unstable horizontal equation source',
                                       {'name': u'Wall Panel Heating Unstable Horizontal Equation Source',
                                        'pyname': u'wall_panel_heating_unstable_horizontal_equation_source',
                                        'default': u'KhalifaEq7Ceiling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'KhalifaEq7Ceiling',
                                                            u'KaradagChilledCeiling',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating unstable horizontal equation user curve name',
                                       {'name': u'Wall Panel Heating Unstable Horizontal Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_unstable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating stable tilted equation source',
                                       {'name': u'Wall Panel Heating Stable Tilted Equation Source',
                                        'pyname': u'wall_panel_heating_stable_tilted_equation_source',
                                        'default': u'WaltonStableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating stable tilted equation user curve name',
                                       {'name': u'Wall Panel Heating Stable Tilted Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_stable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating unstable tilted equation source',
                                       {'name': u'Wall Panel Heating Unstable Tilted Equation Source',
                                        'pyname': u'wall_panel_heating_unstable_tilted_equation_source',
                                        'default': u'WaltonUnstableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating unstable tilted equation user curve name',
                                       {'name': u'Wall Panel Heating Unstable Tilted Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_unstable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wall panel heating window equation source',
                                       {'name': u'Wall Panel Heating Window Equation Source',
                                        'pyname': u'wall_panel_heating_window_equation_source',
                                        'default': u'ISO15099Windows',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wall panel heating window equation user curve name',
                                       {'name': u'Wall Panel Heating Window Equation User Curve Name',
                                        'pyname': u'wall_panel_heating_window_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater vertical wall equation source',
                                       {'name': u'Convective Zone Heater Vertical Wall Equation Source',
                                        'pyname': u'convective_zone_heater_vertical_wall_equation_source',
                                        'default': u'FohannoPolidoriVerticalWall',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater vertical wall equation user curve name',
                                       {'name': u'Convective Zone Heater Vertical Wall Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_vertical_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater vertical walls near heater equation source',
                                       {'name': u'Convective Zone Heater Vertical Walls Near Heater Equation Source',
                                        'pyname': u'convective_zone_heater_vertical_walls_near_heater_equation_source',
                                        'default': u'KhalifaEq5WallNearHeat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq5WallNearHeat',
                                                            u'AwbiHattonHeatedWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater vertical walls near heater equation user curve name',
                                       {'name': u'Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater stable horizontal equation source',
                                       {'name': u'Convective Zone Heater Stable Horizontal Equation Source',
                                        'pyname': u'convective_zone_heater_stable_horizontal_equation_source',
                                        'default': u'AlamdariHammondStableHorizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater stable horizontal equation user curve name',
                                       {'name': u'Convective Zone Heater Stable Horizontal Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_stable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater unstable horizontal equation source',
                                       {'name': u'Convective Zone Heater Unstable Horizontal Equation Source',
                                        'pyname': u'convective_zone_heater_unstable_horizontal_equation_source',
                                        'default': u'KhalifaEq7Ceiling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'KhalifaEq7Ceiling',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater unstable horizontal equation user curve name',
                                       {'name': u'Convective Zone Heater Unstable Horizontal Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_unstable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater stable tilted equation source',
                                       {'name': u'Convective Zone Heater Stable Tilted Equation Source',
                                        'pyname': u'convective_zone_heater_stable_tilted_equation_source',
                                        'default': u'WaltonStableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater stable tilted equation user curve name',
                                       {'name': u'Convective Zone Heater Stable Tilted Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_stable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater unstable tilted equation source',
                                       {'name': u'Convective Zone Heater Unstable Tilted Equation Source',
                                        'pyname': u'convective_zone_heater_unstable_tilted_equation_source',
                                        'default': u'WaltonUnstableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater unstable tilted equation user curve name',
                                       {'name': u'Convective Zone Heater Unstable Tilted Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_unstable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convective zone heater windows equation source',
                                       {'name': u'Convective Zone Heater Windows Equation Source',
                                        'pyname': u'convective_zone_heater_windows_equation_source',
                                        'default': u'ISO15099Windows',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convective zone heater windows equation user curve name',
                                       {'name': u'Convective Zone Heater Windows Equation User Curve Name',
                                        'pyname': u'convective_zone_heater_windows_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'central air diffuser wall equation source',
                                       {'name': u'Central Air Diffuser Wall Equation Source',
                                        'pyname': u'central_air_diffuser_wall_equation_source',
                                        'default': u'GoldsteinNovoselacCeilingDiffuserWalls',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'central air diffuser wall equation user curve name',
                                       {'name': u'Central Air Diffuser Wall Equation User Curve Name',
                                        'pyname': u'central_air_diffuser_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'central air diffuser ceiling equation source',
                                       {'name': u'Central Air Diffuser Ceiling Equation Source',
                                        'pyname': u'central_air_diffuser_ceiling_equation_source',
                                        'default': u'FisherPedersenCeilingDiffuserCeiling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FisherPedersenCeilingDiffuserCeiling',
                                                            u'BeausoleilMorrisonMixedStableCeiling',
                                                            u'BeausoleilMorrisonMixedUnstableCeiling',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'central air diffuser ceiling equation user curve name',
                                       {'name': u'Central Air Diffuser Ceiling Equation User Curve Name',
                                        'pyname': u'central_air_diffuser_ceiling_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'central air diffuser floor equation source',
                                       {'name': u'Central Air Diffuser Floor Equation Source',
                                        'pyname': u'central_air_diffuser_floor_equation_source',
                                        'default': u'GoldsteinNovoselacCeilingDiffuserFloor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FisherPedersenCeilingDiffuserFloor',
                                                            u'BeausoleilMorrisonMixedStableFloor',
                                                            u'BeausoleilMorrisonMixedUnstableFloor',
                                                            u'GoldsteinNovoselacCeilingDiffuserFloor',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'central air diffuser floor equation user curve name',
                                       {'name': u'Central Air Diffuser Floor Equation User Curve Name',
                                        'pyname': u'central_air_diffuser_floor_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'central air diffuser window equation source',
                                       {'name': u'Central Air Diffuser Window Equation Source',
                                        'pyname': u'central_air_diffuser_window_equation_source',
                                        'default': u'GoldsteinNovoselacCeilingDiffuserWindow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'central air diffuser window equation user curve name',
                                       {'name': u'Central Air Diffuser Window Equation User Curve Name',
                                        'pyname': u'central_air_diffuser_window_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical zone fan circulation vertical wall equation source',
                                       {'name': u'Mechanical Zone Fan Circulation Vertical Wall Equation Source',
                                        'pyname': u'mechanical_zone_fan_circulation_vertical_wall_equation_source',
                                        'default': u'KhalifaEq3WallAwayFromHeat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'KhalifaEq3WallAwayFromHeat',
                                                            u'ASHRAEVerticalWall',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical zone fan circulation vertical wall equation user curve name',
                                       {'name': u'Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name',
                                        'pyname': u'mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical zone fan circulation stable horizontal equation source',
                                       {'name': u'Mechanical Zone Fan Circulation Stable Horizontal Equation Source',
                                        'pyname': u'mechanical_zone_fan_circulation_stable_horizontal_equation_source',
                                        'default': u'AlamdariHammondStableHorizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical zone fan circulation stable horizontal equation user curve name',
                                       {'name': u'Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name',
                                        'pyname': u'mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical zone fan circulation unstable horizontal equation source',
                                       {'name': u'Mechanical Zone Fan Circulation Unstable Horizontal Equation Source',
                                        'pyname': u'mechanical_zone_fan_circulation_unstable_horizontal_equation_source',
                                        'default': u'KhalifaEq4CeilingAwayFromHeat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical zone fan circulation unstable horizontal equation user curve name',
                                       {'name': u'Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name',
                                        'pyname': u'mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical zone fan circulation stable tilted equation source',
                                       {'name': u'Mechanical Zone Fan Circulation Stable Tilted Equation Source',
                                        'pyname': u'mechanical_zone_fan_circulation_stable_tilted_equation_source',
                                        'default': u'WaltonStableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical zone fan circulation stable tilted equation user curve name',
                                       {'name': u'Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name',
                                        'pyname': u'mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical zone fan circulation unstable tilted equation source',
                                       {'name': u'Mechanical Zone Fan Circulation Unstable Tilted Equation Source',
                                        'pyname': u'mechanical_zone_fan_circulation_unstable_tilted_equation_source',
                                        'default': u'WaltonUnstableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical zone fan circulation unstable tilted equation user curve name',
                                       {'name': u'Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name',
                                        'pyname': u'mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mechanical zone fan circulation window equation source',
                                       {'name': u'Mechanical Zone Fan Circulation Window Equation Source',
                                        'pyname': u'mechanical_zone_fan_circulation_window_equation_source',
                                        'default': u'ISO15099Windows',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical zone fan circulation window equation user curve name',
                                       {'name': u'Mechanical Zone Fan Circulation Window Equation User Curve Name',
                                        'pyname': u'mechanical_zone_fan_circulation_window_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime buoyancy assisting flow on walls equation source',
                                       {'name': u'Mixed Regime Buoyancy Assisting Flow on Walls Equation Source',
                                        'pyname': u'mixed_regime_buoyancy_assisting_flow_on_walls_equation_source',
                                        'default': u'BeausoleilMorrisonMixedAssistedWall',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ASHRAEVerticalWall',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime buoyancy assisting flow on walls equation user curve name',
                                       {'name': u'Mixed Regime Buoyancy Assisting Flow on Walls Equation User Curve Name',
                                        'pyname': u'mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime buoyancy opposing flow on walls equation source',
                                       {'name': u'Mixed Regime Buoyancy Opposing Flow on Walls Equation Source',
                                        'pyname': u'mixed_regime_buoyancy_opposing_flow_on_walls_equation_source',
                                        'default': u'BeausoleilMorrisonMixedOpposingWall',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ASHRAEVerticalWall',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime buoyancy opposing flow on walls equation user curve name',
                                       {'name': u'Mixed Regime Buoyancy Opposing Flow on Walls Equation User Curve Name',
                                        'pyname': u'mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime stable floor equation source',
                                       {'name': u'Mixed Regime Stable Floor Equation Source',
                                        'pyname': u'mixed_regime_stable_floor_equation_source',
                                        'default': u'BeausoleilMorrisonMixedStableFloor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeausoleilMorrisonMixedStableFloor',
                                                            u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime stable floor equation user curve name',
                                       {'name': u'Mixed Regime Stable Floor Equation User Curve Name',
                                        'pyname': u'mixed_regime_stable_floor_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime unstable floor equation source',
                                       {'name': u'Mixed Regime Unstable Floor Equation Source',
                                        'pyname': u'mixed_regime_unstable_floor_equation_source',
                                        'default': u'BeausoleilMorrisonMixedUnstableFloor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeausoleilMorrisonMixedUnstableFloor',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime unstable floor equation user curve name',
                                       {'name': u'Mixed Regime Unstable Floor Equation User Curve Name',
                                        'pyname': u'mixed_regime_unstable_floor_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime stable ceiling equation source',
                                       {'name': u'Mixed Regime Stable Ceiling Equation Source',
                                        'pyname': u'mixed_regime_stable_ceiling_equation_source',
                                        'default': u'BeausoleilMorrisonMixedStableCeiling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeausoleilMorrisonMixedStableCeiling',
                                                            u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime stable ceiling equation user curve name',
                                       {'name': u'Mixed Regime Stable Ceiling Equation User Curve Name',
                                        'pyname': u'mixed_regime_stable_ceiling_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime unstable ceiling equation source',
                                       {'name': u'Mixed Regime Unstable Ceiling Equation Source',
                                        'pyname': u'mixed_regime_unstable_ceiling_equation_source',
                                        'default': u'BeausoleilMorrisonMixedUnstableCeiling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeausoleilMorrisonMixedUnstableCeiling',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime unstable ceiling equation user curve name',
                                       {'name': u'Mixed Regime Unstable Ceiling Equation User Curve Name',
                                        'pyname': u'mixed_regime_unstable_ceiling_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mixed regime window equation source',
                                       {'name': u'Mixed Regime Window Equation Source',
                                        'pyname': u'mixed_regime_window_equation_source',
                                        'default': u'GoldsteinNovoselacCeilingDiffuserWindow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'ISO15099Windows',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mixed regime window equation user curve name',
                                       {'name': u'Mixed Regime Window Equation User Curve Name',
                                        'pyname': u'mixed_regime_window_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections',
               'pyname': u'SurfaceConvectionAlgorithmInsideAdaptiveModelSelections',
               'required-object': False,
               'unique-object': True}

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
    def simple_buoyancy_vertical_wall_equation_source(self):
        """field `Simple Buoyancy Vertical Wall Equation Source`

        |  Applies to zone with no HVAC or when HVAC is off
        |  This is for vertical walls
        |  Default value: FohannoPolidoriVerticalWall

        Args:
            value (str): value for IDD Field `Simple Buoyancy Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_vertical_wall_equation_source` or None if not set

        """
        return self["Simple Buoyancy Vertical Wall Equation Source"]

    @simple_buoyancy_vertical_wall_equation_source.setter
    def simple_buoyancy_vertical_wall_equation_source(
            self,
            value="FohannoPolidoriVerticalWall"):
        """Corresponds to IDD field `Simple Buoyancy Vertical Wall Equation
        Source`"""
        self["Simple Buoyancy Vertical Wall Equation Source"] = value

    @property
    def simple_buoyancy_vertical_wall_user_curve_name(self):
        """field `Simple Buoyancy Vertical Wall User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Buoyancy Vertical Wall User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_vertical_wall_user_curve_name` or None if not set

        """
        return self["Simple Buoyancy Vertical Wall User Curve Name"]

    @simple_buoyancy_vertical_wall_user_curve_name.setter
    def simple_buoyancy_vertical_wall_user_curve_name(self, value=None):
        """Corresponds to IDD field `Simple Buoyancy Vertical Wall User Curve
        Name`"""
        self["Simple Buoyancy Vertical Wall User Curve Name"] = value

    @property
    def simple_buoyancy_stable_horizontal_equation_source(self):
        """field `Simple Buoyancy Stable Horizontal Equation Source`

        |  Applies to zone with no HVAC or when HVAC is off
        |  This is for horizontal surfaces with heat flow directed for stable thermal stratification
        |  Default value: AlamdariHammondStableHorizontal

        Args:
            value (str): value for IDD Field `Simple Buoyancy Stable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_stable_horizontal_equation_source` or None if not set

        """
        return self["Simple Buoyancy Stable Horizontal Equation Source"]

    @simple_buoyancy_stable_horizontal_equation_source.setter
    def simple_buoyancy_stable_horizontal_equation_source(
            self,
            value="AlamdariHammondStableHorizontal"):
        """Corresponds to IDD field `Simple Buoyancy Stable Horizontal Equation
        Source`"""
        self["Simple Buoyancy Stable Horizontal Equation Source"] = value

    @property
    def simple_buoyancy_stable_horizontal_equation_user_curve_name(self):
        """field `Simple Buoyancy Stable Horizontal Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Buoyancy Stable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_stable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Simple Buoyancy Stable Horizontal Equation User Curve Name"]

    @simple_buoyancy_stable_horizontal_equation_user_curve_name.setter
    def simple_buoyancy_stable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Simple Buoyancy Stable Horizontal Equation
        User Curve Name`"""
        self[
            "Simple Buoyancy Stable Horizontal Equation User Curve Name"] = value

    @property
    def simple_buoyancy_unstable_horizontal_equation_source(self):
        """field `Simple Buoyancy Unstable Horizontal Equation Source`

        |  Applies to zone with no HVAC or when HVAC is off
        |  This is for passive horizontal surfaces with heat flow for unstable thermal stratification
        |  Default value: AlamdariHammondUnstableHorizontal

        Args:
            value (str): value for IDD Field `Simple Buoyancy Unstable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_unstable_horizontal_equation_source` or None if not set

        """
        return self["Simple Buoyancy Unstable Horizontal Equation Source"]

    @simple_buoyancy_unstable_horizontal_equation_source.setter
    def simple_buoyancy_unstable_horizontal_equation_source(
            self,
            value="AlamdariHammondUnstableHorizontal"):
        """Corresponds to IDD field `Simple Buoyancy Unstable Horizontal
        Equation Source`"""
        self["Simple Buoyancy Unstable Horizontal Equation Source"] = value

    @property
    def simple_buoyancy_unstable_horizontal_equation_user_curve_name(self):
        """field `Simple Buoyancy Unstable Horizontal Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Buoyancy Unstable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_unstable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Simple Buoyancy Unstable Horizontal Equation User Curve Name"]

    @simple_buoyancy_unstable_horizontal_equation_user_curve_name.setter
    def simple_buoyancy_unstable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Simple Buoyancy Unstable Horizontal
        Equation User Curve Name`"""
        self[
            "Simple Buoyancy Unstable Horizontal Equation User Curve Name"] = value

    @property
    def simple_buoyancy_stable_tilted_equation_source(self):
        """field `Simple Buoyancy Stable Tilted Equation Source`

        |  Applies to zone with no HVAC or when HVAC is off
        |  This is for tilted surfaces with heat flow for stable thermal stratification
        |  Default value: WaltonStableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Simple Buoyancy Stable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_stable_tilted_equation_source` or None if not set

        """
        return self["Simple Buoyancy Stable Tilted Equation Source"]

    @simple_buoyancy_stable_tilted_equation_source.setter
    def simple_buoyancy_stable_tilted_equation_source(
            self,
            value="WaltonStableHorizontalOrTilt"):
        """Corresponds to IDD field `Simple Buoyancy Stable Tilted Equation
        Source`"""
        self["Simple Buoyancy Stable Tilted Equation Source"] = value

    @property
    def simple_buoyancy_stable_tilted_equation_user_curve_name(self):
        """field `Simple Buoyancy Stable Tilted Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Buoyancy Stable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_stable_tilted_equation_user_curve_name` or None if not set

        """
        return self["Simple Buoyancy Stable Tilted Equation User Curve Name"]

    @simple_buoyancy_stable_tilted_equation_user_curve_name.setter
    def simple_buoyancy_stable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Simple Buoyancy Stable Tilted Equation
        User Curve Name`"""
        self["Simple Buoyancy Stable Tilted Equation User Curve Name"] = value

    @property
    def simple_buoyancy_unstable_tilted_equation_source(self):
        """field `Simple Buoyancy Unstable Tilted Equation Source`

        |  Applies to zone with no HVAC or when HVAC is off
        |  This is for tilted surfaces with heat flow for unstable thermal stratification
        |  Default value: WaltonUnstableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Simple Buoyancy Unstable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_unstable_tilted_equation_source` or None if not set

        """
        return self["Simple Buoyancy Unstable Tilted Equation Source"]

    @simple_buoyancy_unstable_tilted_equation_source.setter
    def simple_buoyancy_unstable_tilted_equation_source(
            self,
            value="WaltonUnstableHorizontalOrTilt"):
        """Corresponds to IDD field `Simple Buoyancy Unstable Tilted Equation
        Source`"""
        self["Simple Buoyancy Unstable Tilted Equation Source"] = value

    @property
    def simple_buoyancy_unstable_tilted_equation_user_curve_name(self):
        """field `Simple Buoyancy Unstable Tilted Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Buoyancy Unstable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_unstable_tilted_equation_user_curve_name` or None if not set

        """
        return self["Simple Buoyancy Unstable Tilted Equation User Curve Name"]

    @simple_buoyancy_unstable_tilted_equation_user_curve_name.setter
    def simple_buoyancy_unstable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Simple Buoyancy Unstable Tilted Equation
        User Curve Name`"""
        self[
            "Simple Buoyancy Unstable Tilted Equation User Curve Name"] = value

    @property
    def simple_buoyancy_windows_equation_source(self):
        """field `Simple Buoyancy Windows Equation Source`

        |  Applies to zone with no HVAC or when HVAC is off
        |  This is for all window surfaces
        |  Default value: ISO15099Windows

        Args:
            value (str): value for IDD Field `Simple Buoyancy Windows Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_windows_equation_source` or None if not set

        """
        return self["Simple Buoyancy Windows Equation Source"]

    @simple_buoyancy_windows_equation_source.setter
    def simple_buoyancy_windows_equation_source(self, value="ISO15099Windows"):
        """Corresponds to IDD field `Simple Buoyancy Windows Equation
        Source`"""
        self["Simple Buoyancy Windows Equation Source"] = value

    @property
    def simple_buoyancy_windows_equation_user_curve_name(self):
        """field `Simple Buoyancy Windows Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Buoyancy Windows Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simple_buoyancy_windows_equation_user_curve_name` or None if not set

        """
        return self["Simple Buoyancy Windows Equation User Curve Name"]

    @simple_buoyancy_windows_equation_user_curve_name.setter
    def simple_buoyancy_windows_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Simple Buoyancy Windows Equation User
        Curve Name`"""
        self["Simple Buoyancy Windows Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_vertical_wall_equation_source(self):
        """field `Floor Heat Ceiling Cool Vertical Wall Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for vertical walls
        |  Default value: KhalifaEq3WallAwayFromHeat

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_vertical_wall_equation_source` or None if not set

        """
        return self["Floor Heat Ceiling Cool Vertical Wall Equation Source"]

    @floor_heat_ceiling_cool_vertical_wall_equation_source.setter
    def floor_heat_ceiling_cool_vertical_wall_equation_source(
            self,
            value="KhalifaEq3WallAwayFromHeat"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Vertical Wall
        Equation Source`"""
        self["Floor Heat Ceiling Cool Vertical Wall Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name(self):
        """field `Floor Heat Ceiling Cool Vertical Wall Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"]

    @floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Vertical Wall
        Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_stable_horizontal_equation_source(self):
        """field `Floor Heat Ceiling Cool Stable Horizontal Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for passive horizontal surfaces with heat flow for stable thermal stratification
        |  Default value: AlamdariHammondStableHorizontal

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_horizontal_equation_source` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Stable Horizontal Equation Source"]

    @floor_heat_ceiling_cool_stable_horizontal_equation_source.setter
    def floor_heat_ceiling_cool_stable_horizontal_equation_source(
            self,
            value="AlamdariHammondStableHorizontal"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Stable Horizontal
        Equation Source`"""
        self[
            "Floor Heat Ceiling Cool Stable Horizontal Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name(
            self):
        """field `Floor Heat Ceiling Cool Stable Horizontal Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"]

    @floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Stable Horizontal
        Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_unstable_horizontal_equation_source(self):
        """field `Floor Heat Ceiling Cool Unstable Horizontal Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for passive horizontal surfaces with heat flow for unstable thermal stratification
        |  Default value: KhalifaEq4CeilingAwayFromHeat

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_horizontal_equation_source` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Unstable Horizontal Equation Source"]

    @floor_heat_ceiling_cool_unstable_horizontal_equation_source.setter
    def floor_heat_ceiling_cool_unstable_horizontal_equation_source(
            self,
            value="KhalifaEq4CeilingAwayFromHeat"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Unstable
        Horizontal Equation Source`"""
        self[
            "Floor Heat Ceiling Cool Unstable Horizontal Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name(
            self):
        """field `Floor Heat Ceiling Cool Unstable Horizontal Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"]

    @floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Unstable
        Horizontal Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_heated_floor_equation_source(self):
        """field `Floor Heat Ceiling Cool Heated Floor Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for a floor with active heating elements
        |  Default value: AwbiHattonHeatedFloor

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Heated Floor Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_heated_floor_equation_source` or None if not set

        """
        return self["Floor Heat Ceiling Cool Heated Floor Equation Source"]

    @floor_heat_ceiling_cool_heated_floor_equation_source.setter
    def floor_heat_ceiling_cool_heated_floor_equation_source(
            self,
            value="AwbiHattonHeatedFloor"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Heated Floor
        Equation Source`"""
        self["Floor Heat Ceiling Cool Heated Floor Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_heated_floor_equation_user_curve_name(self):
        """field `Floor Heat Ceiling Cool Heated Floor Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Heated Floor Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"]

    @floor_heat_ceiling_cool_heated_floor_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_heated_floor_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Heated Floor
        Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_chilled_ceiling_equation_source(self):
        """field `Floor Heat Ceiling Cool Chilled Ceiling Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for a ceiling with active cooling elements
        |  Default value: KaradagChilledCeiling

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Chilled Ceiling Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_chilled_ceiling_equation_source` or None if not set

        """
        return self["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"]

    @floor_heat_ceiling_cool_chilled_ceiling_equation_source.setter
    def floor_heat_ceiling_cool_chilled_ceiling_equation_source(
            self,
            value="KaradagChilledCeiling"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Chilled Ceiling
        Equation Source`"""
        self["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name(self):
        """field `Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"]

    @floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Chilled Ceiling
        Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_stable_tilted_equation_source(self):
        """field `Floor Heat Ceiling Cool Stable Tilted Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for tilted surfaces with heat flow for stable thermal stratification
        |  Default value: WaltonStableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_tilted_equation_source` or None if not set

        """
        return self["Floor Heat Ceiling Cool Stable Tilted Equation Source"]

    @floor_heat_ceiling_cool_stable_tilted_equation_source.setter
    def floor_heat_ceiling_cool_stable_tilted_equation_source(
            self,
            value="WaltonStableHorizontalOrTilt"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Stable Tilted
        Equation Source`"""
        self["Floor Heat Ceiling Cool Stable Tilted Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name(self):
        """field `Floor Heat Ceiling Cool Stable Tilted Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"]

    @floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Stable Tilted
        Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_unstable_tilted_equation_source(self):
        """field `Floor Heat Ceiling Cool Unstable Tilted Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for tilted surfaces with heat flow for unstable thermal stratification
        |  Default value: WaltonUnstableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_tilted_equation_source` or None if not set

        """
        return self["Floor Heat Ceiling Cool Unstable Tilted Equation Source"]

    @floor_heat_ceiling_cool_unstable_tilted_equation_source.setter
    def floor_heat_ceiling_cool_unstable_tilted_equation_source(
            self,
            value="WaltonUnstableHorizontalOrTilt"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Unstable Tilted
        Equation Source`"""
        self["Floor Heat Ceiling Cool Unstable Tilted Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name(self):
        """field `Floor Heat Ceiling Cool Unstable Tilted Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"]

    @floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Unstable Tilted
        Equation User Curve Name`"""
        self[
            "Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_window_equation_source(self):
        """field `Floor Heat Ceiling Cool Window Equation Source`

        |  Applies to zone with in-floor heating and/or in-ceiling cooling
        |  This is for all window surfaces
        |  Default value: ISO15099Windows

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Window Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_window_equation_source` or None if not set

        """
        return self["Floor Heat Ceiling Cool Window Equation Source"]

    @floor_heat_ceiling_cool_window_equation_source.setter
    def floor_heat_ceiling_cool_window_equation_source(
            self,
            value="ISO15099Windows"):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Window Equation
        Source`"""
        self["Floor Heat Ceiling Cool Window Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_window_equation_user_curve_name(self):
        """field `Floor Heat Ceiling Cool Window Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Window Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `floor_heat_ceiling_cool_window_equation_user_curve_name` or None if not set

        """
        return self["Floor Heat Ceiling Cool Window Equation User Curve Name"]

    @floor_heat_ceiling_cool_window_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_window_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Floor Heat Ceiling Cool Window Equation
        User Curve Name`"""
        self["Floor Heat Ceiling Cool Window Equation User Curve Name"] = value

    @property
    def wall_panel_heating_vertical_wall_equation_source(self):
        """field `Wall Panel Heating Vertical Wall Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for vertical walls that are not actively heated
        |  Default value: KhalifaEq6NonHeatedWalls

        Args:
            value (str): value for IDD Field `Wall Panel Heating Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_vertical_wall_equation_source` or None if not set

        """
        return self["Wall Panel Heating Vertical Wall Equation Source"]

    @wall_panel_heating_vertical_wall_equation_source.setter
    def wall_panel_heating_vertical_wall_equation_source(
            self,
            value="KhalifaEq6NonHeatedWalls"):
        """Corresponds to IDD field `Wall Panel Heating Vertical Wall Equation
        Source`"""
        self["Wall Panel Heating Vertical Wall Equation Source"] = value

    @property
    def wall_panel_heating_vertical_wall_equation_user_curve_name(self):
        """field `Wall Panel Heating Vertical Wall Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Vertical Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_vertical_wall_equation_user_curve_name` or None if not set

        """
        return self[
            "Wall Panel Heating Vertical Wall Equation User Curve Name"]

    @wall_panel_heating_vertical_wall_equation_user_curve_name.setter
    def wall_panel_heating_vertical_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wall Panel Heating Vertical Wall Equation
        User Curve Name`"""
        self[
            "Wall Panel Heating Vertical Wall Equation User Curve Name"] = value

    @property
    def wall_panel_heating_heated_wall_equation_source(self):
        """field `Wall Panel Heating Heated Wall Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for vertical walls that are being actively heated
        |  Default value: AwbiHattonHeatedWall

        Args:
            value (str): value for IDD Field `Wall Panel Heating Heated Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_heated_wall_equation_source` or None if not set

        """
        return self["Wall Panel Heating Heated Wall Equation Source"]

    @wall_panel_heating_heated_wall_equation_source.setter
    def wall_panel_heating_heated_wall_equation_source(
            self,
            value="AwbiHattonHeatedWall"):
        """Corresponds to IDD field `Wall Panel Heating Heated Wall Equation
        Source`"""
        self["Wall Panel Heating Heated Wall Equation Source"] = value

    @property
    def wall_panel_heating_heated_wall_equation_user_curve_name(self):
        """field `Wall Panel Heating Heated Wall Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Heated Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_heated_wall_equation_user_curve_name` or None if not set

        """
        return self["Wall Panel Heating Heated Wall Equation User Curve Name"]

    @wall_panel_heating_heated_wall_equation_user_curve_name.setter
    def wall_panel_heating_heated_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wall Panel Heating Heated Wall Equation
        User Curve Name`"""
        self["Wall Panel Heating Heated Wall Equation User Curve Name"] = value

    @property
    def wall_panel_heating_stable_horizontal_equation_source(self):
        """field `Wall Panel Heating Stable Horizontal Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for horizontal surfaces with heat flow directed for stable thermal stratification
        |  Default value: AlamdariHammondStableHorizontal

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_stable_horizontal_equation_source` or None if not set

        """
        return self["Wall Panel Heating Stable Horizontal Equation Source"]

    @wall_panel_heating_stable_horizontal_equation_source.setter
    def wall_panel_heating_stable_horizontal_equation_source(
            self,
            value="AlamdariHammondStableHorizontal"):
        """Corresponds to IDD field `Wall Panel Heating Stable Horizontal
        Equation Source`"""
        self["Wall Panel Heating Stable Horizontal Equation Source"] = value

    @property
    def wall_panel_heating_stable_horizontal_equation_user_curve_name(self):
        """field `Wall Panel Heating Stable Horizontal Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_stable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Wall Panel Heating Stable Horizontal Equation User Curve Name"]

    @wall_panel_heating_stable_horizontal_equation_user_curve_name.setter
    def wall_panel_heating_stable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wall Panel Heating Stable Horizontal
        Equation User Curve Name`"""
        self[
            "Wall Panel Heating Stable Horizontal Equation User Curve Name"] = value

    @property
    def wall_panel_heating_unstable_horizontal_equation_source(self):
        """field `Wall Panel Heating Unstable Horizontal Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for horizontal surfaces with heat flow directed for unstable thermal stratification
        |  Default value: KhalifaEq7Ceiling

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_unstable_horizontal_equation_source` or None if not set

        """
        return self["Wall Panel Heating Unstable Horizontal Equation Source"]

    @wall_panel_heating_unstable_horizontal_equation_source.setter
    def wall_panel_heating_unstable_horizontal_equation_source(
            self,
            value="KhalifaEq7Ceiling"):
        """Corresponds to IDD field `Wall Panel Heating Unstable Horizontal
        Equation Source`"""
        self["Wall Panel Heating Unstable Horizontal Equation Source"] = value

    @property
    def wall_panel_heating_unstable_horizontal_equation_user_curve_name(self):
        """field `Wall Panel Heating Unstable Horizontal Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_unstable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Wall Panel Heating Unstable Horizontal Equation User Curve Name"]

    @wall_panel_heating_unstable_horizontal_equation_user_curve_name.setter
    def wall_panel_heating_unstable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wall Panel Heating Unstable Horizontal
        Equation User Curve Name`"""
        self[
            "Wall Panel Heating Unstable Horizontal Equation User Curve Name"] = value

    @property
    def wall_panel_heating_stable_tilted_equation_source(self):
        """field `Wall Panel Heating Stable Tilted Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for tilted surfaces with heat flow for stable thermal stratification
        |  Default value: WaltonStableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_stable_tilted_equation_source` or None if not set

        """
        return self["Wall Panel Heating Stable Tilted Equation Source"]

    @wall_panel_heating_stable_tilted_equation_source.setter
    def wall_panel_heating_stable_tilted_equation_source(
            self,
            value="WaltonStableHorizontalOrTilt"):
        """Corresponds to IDD field `Wall Panel Heating Stable Tilted Equation
        Source`"""
        self["Wall Panel Heating Stable Tilted Equation Source"] = value

    @property
    def wall_panel_heating_stable_tilted_equation_user_curve_name(self):
        """field `Wall Panel Heating Stable Tilted Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_stable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Wall Panel Heating Stable Tilted Equation User Curve Name"]

    @wall_panel_heating_stable_tilted_equation_user_curve_name.setter
    def wall_panel_heating_stable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wall Panel Heating Stable Tilted Equation
        User Curve Name`"""
        self[
            "Wall Panel Heating Stable Tilted Equation User Curve Name"] = value

    @property
    def wall_panel_heating_unstable_tilted_equation_source(self):
        """field `Wall Panel Heating Unstable Tilted Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for tilted surfaces with heat flow for unstable thermal stratification
        |  Default value: WaltonUnstableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_unstable_tilted_equation_source` or None if not set

        """
        return self["Wall Panel Heating Unstable Tilted Equation Source"]

    @wall_panel_heating_unstable_tilted_equation_source.setter
    def wall_panel_heating_unstable_tilted_equation_source(
            self,
            value="WaltonUnstableHorizontalOrTilt"):
        """Corresponds to IDD field `Wall Panel Heating Unstable Tilted
        Equation Source`"""
        self["Wall Panel Heating Unstable Tilted Equation Source"] = value

    @property
    def wall_panel_heating_unstable_tilted_equation_user_curve_name(self):
        """field `Wall Panel Heating Unstable Tilted Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_unstable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Wall Panel Heating Unstable Tilted Equation User Curve Name"]

    @wall_panel_heating_unstable_tilted_equation_user_curve_name.setter
    def wall_panel_heating_unstable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wall Panel Heating Unstable Tilted
        Equation User Curve Name`"""
        self[
            "Wall Panel Heating Unstable Tilted Equation User Curve Name"] = value

    @property
    def wall_panel_heating_window_equation_source(self):
        """field `Wall Panel Heating Window Equation Source`

        |  Applies to zone with in-wall panel heating
        |  This is for all window surfaces
        |  Default value: ISO15099Windows

        Args:
            value (str): value for IDD Field `Wall Panel Heating Window Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_window_equation_source` or None if not set

        """
        return self["Wall Panel Heating Window Equation Source"]

    @wall_panel_heating_window_equation_source.setter
    def wall_panel_heating_window_equation_source(
            self,
            value="ISO15099Windows"):
        """Corresponds to IDD field `Wall Panel Heating Window Equation
        Source`"""
        self["Wall Panel Heating Window Equation Source"] = value

    @property
    def wall_panel_heating_window_equation_user_curve_name(self):
        """field `Wall Panel Heating Window Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Window Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wall_panel_heating_window_equation_user_curve_name` or None if not set

        """
        return self["Wall Panel Heating Window Equation User Curve Name"]

    @wall_panel_heating_window_equation_user_curve_name.setter
    def wall_panel_heating_window_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Wall Panel Heating Window Equation User
        Curve Name`"""
        self["Wall Panel Heating Window Equation User Curve Name"] = value

    @property
    def convective_zone_heater_vertical_wall_equation_source(self):
        """field `Convective Zone Heater Vertical Wall Equation Source`

        |  Applies to zone with convective heater
        |  This is for vertical walls not directly affected by heater
        |  Default value: FohannoPolidoriVerticalWall

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_vertical_wall_equation_source` or None if not set

        """
        return self["Convective Zone Heater Vertical Wall Equation Source"]

    @convective_zone_heater_vertical_wall_equation_source.setter
    def convective_zone_heater_vertical_wall_equation_source(
            self,
            value="FohannoPolidoriVerticalWall"):
        """Corresponds to IDD field `Convective Zone Heater Vertical Wall
        Equation Source`"""
        self["Convective Zone Heater Vertical Wall Equation Source"] = value

    @property
    def convective_zone_heater_vertical_wall_equation_user_curve_name(self):
        """field `Convective Zone Heater Vertical Wall Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_vertical_wall_equation_user_curve_name` or None if not set

        """
        return self[
            "Convective Zone Heater Vertical Wall Equation User Curve Name"]

    @convective_zone_heater_vertical_wall_equation_user_curve_name.setter
    def convective_zone_heater_vertical_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Vertical Wall
        Equation User Curve Name`"""
        self[
            "Convective Zone Heater Vertical Wall Equation User Curve Name"] = value

    @property
    def convective_zone_heater_vertical_walls_near_heater_equation_source(
            self):
        """field `Convective Zone Heater Vertical Walls Near Heater Equation
        Source`

        |  Applies to zone with convective heater
        |  This is for vertical walls that are directly affected by heater
        |  Walls are considered "near" when listed in field set for Fraction of Radiant Energy to Surface
        |  Default value: KhalifaEq5WallNearHeat

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Walls Near Heater Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_vertical_walls_near_heater_equation_source` or None if not set

        """
        return self[
            "Convective Zone Heater Vertical Walls Near Heater Equation Source"]

    @convective_zone_heater_vertical_walls_near_heater_equation_source.setter
    def convective_zone_heater_vertical_walls_near_heater_equation_source(
            self,
            value="KhalifaEq5WallNearHeat"):
        """Corresponds to IDD field `Convective Zone Heater Vertical Walls Near
        Heater Equation Source`"""
        self[
            "Convective Zone Heater Vertical Walls Near Heater Equation Source"] = value

    @property
    def convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name(
            self):
        """field `Convective Zone Heater Vertical Walls Near Heater Equation
        User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name` or None if not set

        """
        return self[
            "Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"]

    @convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name.setter
    def convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Vertical Walls Near
        Heater Equation User Curve Name`"""
        self[
            "Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"] = value

    @property
    def convective_zone_heater_stable_horizontal_equation_source(self):
        """field `Convective Zone Heater Stable Horizontal Equation Source`

        |  Applies to zone with convective heater
        |  This is for horizontal surfaces with heat flow directed for stable thermal stratification
        |  Default value: AlamdariHammondStableHorizontal

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_stable_horizontal_equation_source` or None if not set

        """
        return self["Convective Zone Heater Stable Horizontal Equation Source"]

    @convective_zone_heater_stable_horizontal_equation_source.setter
    def convective_zone_heater_stable_horizontal_equation_source(
            self,
            value="AlamdariHammondStableHorizontal"):
        """Corresponds to IDD field `Convective Zone Heater Stable Horizontal
        Equation Source`"""
        self[
            "Convective Zone Heater Stable Horizontal Equation Source"] = value

    @property
    def convective_zone_heater_stable_horizontal_equation_user_curve_name(
            self):
        """field `Convective Zone Heater Stable Horizontal Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_stable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Convective Zone Heater Stable Horizontal Equation User Curve Name"]

    @convective_zone_heater_stable_horizontal_equation_user_curve_name.setter
    def convective_zone_heater_stable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Stable Horizontal
        Equation User Curve Name`"""
        self[
            "Convective Zone Heater Stable Horizontal Equation User Curve Name"] = value

    @property
    def convective_zone_heater_unstable_horizontal_equation_source(self):
        """field `Convective Zone Heater Unstable Horizontal Equation Source`

        |  Applies to zone with convective heater
        |  This is for horizontal surfaces with heat flow directed for unstable thermal stratification
        |  Default value: KhalifaEq7Ceiling

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_unstable_horizontal_equation_source` or None if not set

        """
        return self[
            "Convective Zone Heater Unstable Horizontal Equation Source"]

    @convective_zone_heater_unstable_horizontal_equation_source.setter
    def convective_zone_heater_unstable_horizontal_equation_source(
            self,
            value="KhalifaEq7Ceiling"):
        """Corresponds to IDD field `Convective Zone Heater Unstable Horizontal
        Equation Source`"""
        self[
            "Convective Zone Heater Unstable Horizontal Equation Source"] = value

    @property
    def convective_zone_heater_unstable_horizontal_equation_user_curve_name(
            self):
        """field `Convective Zone Heater Unstable Horizontal Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_unstable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Convective Zone Heater Unstable Horizontal Equation User Curve Name"]

    @convective_zone_heater_unstable_horizontal_equation_user_curve_name.setter
    def convective_zone_heater_unstable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Unstable Horizontal
        Equation User Curve Name`"""
        self[
            "Convective Zone Heater Unstable Horizontal Equation User Curve Name"] = value

    @property
    def convective_zone_heater_stable_tilted_equation_source(self):
        """field `Convective Zone Heater Stable Tilted Equation Source`

        |  Applies to zone with convective heater
        |  This is for tilted surfaces with heat flow for stable thermal stratification
        |  Default value: WaltonStableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_stable_tilted_equation_source` or None if not set

        """
        return self["Convective Zone Heater Stable Tilted Equation Source"]

    @convective_zone_heater_stable_tilted_equation_source.setter
    def convective_zone_heater_stable_tilted_equation_source(
            self,
            value="WaltonStableHorizontalOrTilt"):
        """Corresponds to IDD field `Convective Zone Heater Stable Tilted
        Equation Source`"""
        self["Convective Zone Heater Stable Tilted Equation Source"] = value

    @property
    def convective_zone_heater_stable_tilted_equation_user_curve_name(self):
        """field `Convective Zone Heater Stable Tilted Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_stable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Convective Zone Heater Stable Tilted Equation User Curve Name"]

    @convective_zone_heater_stable_tilted_equation_user_curve_name.setter
    def convective_zone_heater_stable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Stable Tilted
        Equation User Curve Name`"""
        self[
            "Convective Zone Heater Stable Tilted Equation User Curve Name"] = value

    @property
    def convective_zone_heater_unstable_tilted_equation_source(self):
        """field `Convective Zone Heater Unstable Tilted Equation Source`

        |  Applies to zone with convective heater
        |  This is for tilted surfaces with heat flow for unstable thermal stratification
        |  Default value: WaltonUnstableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_unstable_tilted_equation_source` or None if not set

        """
        return self["Convective Zone Heater Unstable Tilted Equation Source"]

    @convective_zone_heater_unstable_tilted_equation_source.setter
    def convective_zone_heater_unstable_tilted_equation_source(
            self,
            value="WaltonUnstableHorizontalOrTilt"):
        """Corresponds to IDD field `Convective Zone Heater Unstable Tilted
        Equation Source`"""
        self["Convective Zone Heater Unstable Tilted Equation Source"] = value

    @property
    def convective_zone_heater_unstable_tilted_equation_user_curve_name(self):
        """field `Convective Zone Heater Unstable Tilted Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_unstable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Convective Zone Heater Unstable Tilted Equation User Curve Name"]

    @convective_zone_heater_unstable_tilted_equation_user_curve_name.setter
    def convective_zone_heater_unstable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Unstable Tilted
        Equation User Curve Name`"""
        self[
            "Convective Zone Heater Unstable Tilted Equation User Curve Name"] = value

    @property
    def convective_zone_heater_windows_equation_source(self):
        """field `Convective Zone Heater Windows Equation Source`

        |  Applies to zone with convective heater
        |  This is for all window surfaces
        |  Default value: ISO15099Windows

        Args:
            value (str): value for IDD Field `Convective Zone Heater Windows Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_windows_equation_source` or None if not set

        """
        return self["Convective Zone Heater Windows Equation Source"]

    @convective_zone_heater_windows_equation_source.setter
    def convective_zone_heater_windows_equation_source(
            self,
            value="ISO15099Windows"):
        """Corresponds to IDD field `Convective Zone Heater Windows Equation
        Source`"""
        self["Convective Zone Heater Windows Equation Source"] = value

    @property
    def convective_zone_heater_windows_equation_user_curve_name(self):
        """field `Convective Zone Heater Windows Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Windows Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convective_zone_heater_windows_equation_user_curve_name` or None if not set

        """
        return self["Convective Zone Heater Windows Equation User Curve Name"]

    @convective_zone_heater_windows_equation_user_curve_name.setter
    def convective_zone_heater_windows_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Convective Zone Heater Windows Equation
        User Curve Name`"""
        self["Convective Zone Heater Windows Equation User Curve Name"] = value

    @property
    def central_air_diffuser_wall_equation_source(self):
        """field `Central Air Diffuser Wall Equation Source`

        |  Applies to zone with mechanical forced central air with diffusers
        |  This is for all wall surfaces
        |  Default value: GoldsteinNovoselacCeilingDiffuserWalls

        Args:
            value (str): value for IDD Field `Central Air Diffuser Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_wall_equation_source` or None if not set

        """
        return self["Central Air Diffuser Wall Equation Source"]

    @central_air_diffuser_wall_equation_source.setter
    def central_air_diffuser_wall_equation_source(
            self,
            value="GoldsteinNovoselacCeilingDiffuserWalls"):
        """Corresponds to IDD field `Central Air Diffuser Wall Equation
        Source`"""
        self["Central Air Diffuser Wall Equation Source"] = value

    @property
    def central_air_diffuser_wall_equation_user_curve_name(self):
        """field `Central Air Diffuser Wall Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_wall_equation_user_curve_name` or None if not set

        """
        return self["Central Air Diffuser Wall Equation User Curve Name"]

    @central_air_diffuser_wall_equation_user_curve_name.setter
    def central_air_diffuser_wall_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Central Air Diffuser Wall Equation User
        Curve Name`"""
        self["Central Air Diffuser Wall Equation User Curve Name"] = value

    @property
    def central_air_diffuser_ceiling_equation_source(self):
        """field `Central Air Diffuser Ceiling Equation Source`

        |  Applies to zone with mechanical forced central air with diffusers
        |  This is for all ceiling surfaces
        |  Default value: FisherPedersenCeilingDiffuserCeiling

        Args:
            value (str): value for IDD Field `Central Air Diffuser Ceiling Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_ceiling_equation_source` or None if not set

        """
        return self["Central Air Diffuser Ceiling Equation Source"]

    @central_air_diffuser_ceiling_equation_source.setter
    def central_air_diffuser_ceiling_equation_source(
            self,
            value="FisherPedersenCeilingDiffuserCeiling"):
        """Corresponds to IDD field `Central Air Diffuser Ceiling Equation
        Source`"""
        self["Central Air Diffuser Ceiling Equation Source"] = value

    @property
    def central_air_diffuser_ceiling_equation_user_curve_name(self):
        """field `Central Air Diffuser Ceiling Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Ceiling Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_ceiling_equation_user_curve_name` or None if not set

        """
        return self["Central Air Diffuser Ceiling Equation User Curve Name"]

    @central_air_diffuser_ceiling_equation_user_curve_name.setter
    def central_air_diffuser_ceiling_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Central Air Diffuser Ceiling Equation User
        Curve Name`"""
        self["Central Air Diffuser Ceiling Equation User Curve Name"] = value

    @property
    def central_air_diffuser_floor_equation_source(self):
        """field `Central Air Diffuser Floor Equation Source`

        |  Applies to zone with mechanical forced central air with diffusers
        |  This is for all floor surfaces
        |  Default value: GoldsteinNovoselacCeilingDiffuserFloor

        Args:
            value (str): value for IDD Field `Central Air Diffuser Floor Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_floor_equation_source` or None if not set

        """
        return self["Central Air Diffuser Floor Equation Source"]

    @central_air_diffuser_floor_equation_source.setter
    def central_air_diffuser_floor_equation_source(
            self,
            value="GoldsteinNovoselacCeilingDiffuserFloor"):
        """Corresponds to IDD field `Central Air Diffuser Floor Equation
        Source`"""
        self["Central Air Diffuser Floor Equation Source"] = value

    @property
    def central_air_diffuser_floor_equation_user_curve_name(self):
        """field `Central Air Diffuser Floor Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Floor Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_floor_equation_user_curve_name` or None if not set

        """
        return self["Central Air Diffuser Floor Equation User Curve Name"]

    @central_air_diffuser_floor_equation_user_curve_name.setter
    def central_air_diffuser_floor_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Central Air Diffuser Floor Equation User
        Curve Name`"""
        self["Central Air Diffuser Floor Equation User Curve Name"] = value

    @property
    def central_air_diffuser_window_equation_source(self):
        """field `Central Air Diffuser Window Equation Source`

        |  Applies to zone with mechanical forced central air with diffusers
        |  This is for all window surfaces
        |  Default value: GoldsteinNovoselacCeilingDiffuserWindow

        Args:
            value (str): value for IDD Field `Central Air Diffuser Window Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_window_equation_source` or None if not set

        """
        return self["Central Air Diffuser Window Equation Source"]

    @central_air_diffuser_window_equation_source.setter
    def central_air_diffuser_window_equation_source(
            self,
            value="GoldsteinNovoselacCeilingDiffuserWindow"):
        """Corresponds to IDD field `Central Air Diffuser Window Equation
        Source`"""
        self["Central Air Diffuser Window Equation Source"] = value

    @property
    def central_air_diffuser_window_equation_user_curve_name(self):
        """field `Central Air Diffuser Window Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Window Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_air_diffuser_window_equation_user_curve_name` or None if not set

        """
        return self["Central Air Diffuser Window Equation User Curve Name"]

    @central_air_diffuser_window_equation_user_curve_name.setter
    def central_air_diffuser_window_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Central Air Diffuser Window Equation User
        Curve Name`"""
        self["Central Air Diffuser Window Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_vertical_wall_equation_source(self):
        """field `Mechanical Zone Fan Circulation Vertical Wall Equation
        Source`

        |  reference choice fields
        |  Default value: KhalifaEq3WallAwayFromHeat

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_vertical_wall_equation_source` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Vertical Wall Equation Source"]

    @mechanical_zone_fan_circulation_vertical_wall_equation_source.setter
    def mechanical_zone_fan_circulation_vertical_wall_equation_source(
            self,
            value="KhalifaEq3WallAwayFromHeat"):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Vertical
        Wall Equation Source`"""
        self[
            "Mechanical Zone Fan Circulation Vertical Wall Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name(
            self):
        """field `Mechanical Zone Fan Circulation Vertical Wall Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"]

    @mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Vertical
        Wall Equation User Curve Name`"""
        self[
            "Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_stable_horizontal_equation_source(
            self):
        """field `Mechanical Zone Fan Circulation Stable Horizontal Equation
        Source`

        |  reference choice fields
        |  Default value: AlamdariHammondStableHorizontal

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_horizontal_equation_source` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Stable Horizontal Equation Source"]

    @mechanical_zone_fan_circulation_stable_horizontal_equation_source.setter
    def mechanical_zone_fan_circulation_stable_horizontal_equation_source(
            self,
            value="AlamdariHammondStableHorizontal"):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Stable
        Horizontal Equation Source`"""
        self[
            "Mechanical Zone Fan Circulation Stable Horizontal Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name(
            self):
        """field `Mechanical Zone Fan Circulation Stable Horizontal Equation
        User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"]

    @mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Stable
        Horizontal Equation User Curve Name`"""
        self[
            "Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_source(
            self):
        """field `Mechanical Zone Fan Circulation Unstable Horizontal Equation
        Source`

        |  reference choice fields
        |  Default value: KhalifaEq4CeilingAwayFromHeat

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_horizontal_equation_source` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"]

    @mechanical_zone_fan_circulation_unstable_horizontal_equation_source.setter
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_source(
            self,
            value="KhalifaEq4CeilingAwayFromHeat"):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Unstable
        Horizontal Equation Source`"""
        self[
            "Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name(
            self):
        """field `Mechanical Zone Fan Circulation Unstable Horizontal Equation
        User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"]

    @mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Unstable
        Horizontal Equation User Curve Name`"""
        self[
            "Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_stable_tilted_equation_source(self):
        """field `Mechanical Zone Fan Circulation Stable Tilted Equation
        Source`

        |  reference choice fields
        |  Default value: WaltonStableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_tilted_equation_source` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Stable Tilted Equation Source"]

    @mechanical_zone_fan_circulation_stable_tilted_equation_source.setter
    def mechanical_zone_fan_circulation_stable_tilted_equation_source(
            self,
            value="WaltonStableHorizontalOrTilt"):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Stable
        Tilted Equation Source`"""
        self[
            "Mechanical Zone Fan Circulation Stable Tilted Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name(
            self):
        """field `Mechanical Zone Fan Circulation Stable Tilted Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"]

    @mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Stable
        Tilted Equation User Curve Name`"""
        self[
            "Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_tilted_equation_source(self):
        """field `Mechanical Zone Fan Circulation Unstable Tilted Equation
        Source`

        |  reference choice fields
        |  Default value: WaltonUnstableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Tilted Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_tilted_equation_source` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Unstable Tilted Equation Source"]

    @mechanical_zone_fan_circulation_unstable_tilted_equation_source.setter
    def mechanical_zone_fan_circulation_unstable_tilted_equation_source(
            self,
            value="WaltonUnstableHorizontalOrTilt"):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Unstable
        Tilted Equation Source`"""
        self[
            "Mechanical Zone Fan Circulation Unstable Tilted Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name(
            self):
        """field `Mechanical Zone Fan Circulation Unstable Tilted Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"]

    @mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Unstable
        Tilted Equation User Curve Name`"""
        self[
            "Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_window_equation_source(self):
        """field `Mechanical Zone Fan Circulation Window Equation Source`

        |  reference choice fields
        |  Default value: ISO15099Windows

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Window Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_window_equation_source` or None if not set

        """
        return self["Mechanical Zone Fan Circulation Window Equation Source"]

    @mechanical_zone_fan_circulation_window_equation_source.setter
    def mechanical_zone_fan_circulation_window_equation_source(
            self,
            value="ISO15099Windows"):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Window
        Equation Source`"""
        self["Mechanical Zone Fan Circulation Window Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_window_equation_user_curve_name(self):
        """field `Mechanical Zone Fan Circulation Window Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Window Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_zone_fan_circulation_window_equation_user_curve_name` or None if not set

        """
        return self[
            "Mechanical Zone Fan Circulation Window Equation User Curve Name"]

    @mechanical_zone_fan_circulation_window_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_window_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mechanical Zone Fan Circulation Window
        Equation User Curve Name`"""
        self[
            "Mechanical Zone Fan Circulation Window Equation User Curve Name"] = value

    @property
    def mixed_regime_buoyancy_assisting_flow_on_walls_equation_source(self):
        """field `Mixed Regime Buoyancy Assisting Flow on Walls Equation
        Source`

        |  reference choice fields
        |  Default value: BeausoleilMorrisonMixedAssistedWall

        Args:
            value (str): value for IDD Field `Mixed Regime Buoyancy Assisting Flow on Walls Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_buoyancy_assisting_flow_on_walls_equation_source` or None if not set

        """
        return self[
            "Mixed Regime Buoyancy Assisting Flow on Walls Equation Source"]

    @mixed_regime_buoyancy_assisting_flow_on_walls_equation_source.setter
    def mixed_regime_buoyancy_assisting_flow_on_walls_equation_source(
            self,
            value="BeausoleilMorrisonMixedAssistedWall"):
        """Corresponds to IDD field `Mixed Regime Buoyancy Assisting Flow on
        Walls Equation Source`"""
        self[
            "Mixed Regime Buoyancy Assisting Flow on Walls Equation Source"] = value

    @property
    def mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name(
            self):
        """field `Mixed Regime Buoyancy Assisting Flow on Walls Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Buoyancy Assisting Flow on Walls Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name` or None if not set

        """
        return self[
            "Mixed Regime Buoyancy Assisting Flow on Walls Equation User Curve Name"]

    @mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name.setter
    def mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mixed Regime Buoyancy Assisting Flow on
        Walls Equation User Curve Name`"""
        self[
            "Mixed Regime Buoyancy Assisting Flow on Walls Equation User Curve Name"] = value

    @property
    def mixed_regime_buoyancy_opposing_flow_on_walls_equation_source(self):
        """field `Mixed Regime Buoyancy Opposing Flow on Walls Equation Source`

        |  reference choice fields
        |  Default value: BeausoleilMorrisonMixedOpposingWall

        Args:
            value (str): value for IDD Field `Mixed Regime Buoyancy Opposing Flow on Walls Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_buoyancy_opposing_flow_on_walls_equation_source` or None if not set

        """
        return self[
            "Mixed Regime Buoyancy Opposing Flow on Walls Equation Source"]

    @mixed_regime_buoyancy_opposing_flow_on_walls_equation_source.setter
    def mixed_regime_buoyancy_opposing_flow_on_walls_equation_source(
            self,
            value="BeausoleilMorrisonMixedOpposingWall"):
        """Corresponds to IDD field `Mixed Regime Buoyancy Opposing Flow on
        Walls Equation Source`"""
        self[
            "Mixed Regime Buoyancy Opposing Flow on Walls Equation Source"] = value

    @property
    def mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name(
            self):
        """field `Mixed Regime Buoyancy Opposing Flow on Walls Equation User
        Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Buoyancy Opposing Flow on Walls Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name` or None if not set

        """
        return self[
            "Mixed Regime Buoyancy Opposing Flow on Walls Equation User Curve Name"]

    @mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name.setter
    def mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mixed Regime Buoyancy Opposing Flow on
        Walls Equation User Curve Name`"""
        self[
            "Mixed Regime Buoyancy Opposing Flow on Walls Equation User Curve Name"] = value

    @property
    def mixed_regime_stable_floor_equation_source(self):
        """field `Mixed Regime Stable Floor Equation Source`

        |  reference choice fields
        |  Default value: BeausoleilMorrisonMixedStableFloor

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Floor Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_stable_floor_equation_source` or None if not set

        """
        return self["Mixed Regime Stable Floor Equation Source"]

    @mixed_regime_stable_floor_equation_source.setter
    def mixed_regime_stable_floor_equation_source(
            self,
            value="BeausoleilMorrisonMixedStableFloor"):
        """Corresponds to IDD field `Mixed Regime Stable Floor Equation
        Source`"""
        self["Mixed Regime Stable Floor Equation Source"] = value

    @property
    def mixed_regime_stable_floor_equation_user_curve_name(self):
        """field `Mixed Regime Stable Floor Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Floor Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_stable_floor_equation_user_curve_name` or None if not set

        """
        return self["Mixed Regime Stable Floor Equation User Curve Name"]

    @mixed_regime_stable_floor_equation_user_curve_name.setter
    def mixed_regime_stable_floor_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Mixed Regime Stable Floor Equation User
        Curve Name`"""
        self["Mixed Regime Stable Floor Equation User Curve Name"] = value

    @property
    def mixed_regime_unstable_floor_equation_source(self):
        """field `Mixed Regime Unstable Floor Equation Source`

        |  reference choice fields
        |  Default value: BeausoleilMorrisonMixedUnstableFloor

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Floor Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_unstable_floor_equation_source` or None if not set

        """
        return self["Mixed Regime Unstable Floor Equation Source"]

    @mixed_regime_unstable_floor_equation_source.setter
    def mixed_regime_unstable_floor_equation_source(
            self,
            value="BeausoleilMorrisonMixedUnstableFloor"):
        """Corresponds to IDD field `Mixed Regime Unstable Floor Equation
        Source`"""
        self["Mixed Regime Unstable Floor Equation Source"] = value

    @property
    def mixed_regime_unstable_floor_equation_user_curve_name(self):
        """field `Mixed Regime Unstable Floor Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Floor Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_unstable_floor_equation_user_curve_name` or None if not set

        """
        return self["Mixed Regime Unstable Floor Equation User Curve Name"]

    @mixed_regime_unstable_floor_equation_user_curve_name.setter
    def mixed_regime_unstable_floor_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Mixed Regime Unstable Floor Equation User
        Curve Name`"""
        self["Mixed Regime Unstable Floor Equation User Curve Name"] = value

    @property
    def mixed_regime_stable_ceiling_equation_source(self):
        """field `Mixed Regime Stable Ceiling Equation Source`

        |  reference choice fields
        |  Default value: BeausoleilMorrisonMixedStableCeiling

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Ceiling Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_stable_ceiling_equation_source` or None if not set

        """
        return self["Mixed Regime Stable Ceiling Equation Source"]

    @mixed_regime_stable_ceiling_equation_source.setter
    def mixed_regime_stable_ceiling_equation_source(
            self,
            value="BeausoleilMorrisonMixedStableCeiling"):
        """Corresponds to IDD field `Mixed Regime Stable Ceiling Equation
        Source`"""
        self["Mixed Regime Stable Ceiling Equation Source"] = value

    @property
    def mixed_regime_stable_ceiling_equation_user_curve_name(self):
        """field `Mixed Regime Stable Ceiling Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Ceiling Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_stable_ceiling_equation_user_curve_name` or None if not set

        """
        return self["Mixed Regime Stable Ceiling Equation User Curve Name"]

    @mixed_regime_stable_ceiling_equation_user_curve_name.setter
    def mixed_regime_stable_ceiling_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Mixed Regime Stable Ceiling Equation User
        Curve Name`"""
        self["Mixed Regime Stable Ceiling Equation User Curve Name"] = value

    @property
    def mixed_regime_unstable_ceiling_equation_source(self):
        """field `Mixed Regime Unstable Ceiling Equation Source`

        |  reference choice fields
        |  Default value: BeausoleilMorrisonMixedUnstableCeiling

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Ceiling Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_unstable_ceiling_equation_source` or None if not set

        """
        return self["Mixed Regime Unstable Ceiling Equation Source"]

    @mixed_regime_unstable_ceiling_equation_source.setter
    def mixed_regime_unstable_ceiling_equation_source(
            self,
            value="BeausoleilMorrisonMixedUnstableCeiling"):
        """Corresponds to IDD field `Mixed Regime Unstable Ceiling Equation
        Source`"""
        self["Mixed Regime Unstable Ceiling Equation Source"] = value

    @property
    def mixed_regime_unstable_ceiling_equation_user_curve_name(self):
        """field `Mixed Regime Unstable Ceiling Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Ceiling Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_unstable_ceiling_equation_user_curve_name` or None if not set

        """
        return self["Mixed Regime Unstable Ceiling Equation User Curve Name"]

    @mixed_regime_unstable_ceiling_equation_user_curve_name.setter
    def mixed_regime_unstable_ceiling_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Mixed Regime Unstable Ceiling Equation
        User Curve Name`"""
        self["Mixed Regime Unstable Ceiling Equation User Curve Name"] = value

    @property
    def mixed_regime_window_equation_source(self):
        """field `Mixed Regime Window Equation Source`

        |  reference choice fields
        |  Default value: GoldsteinNovoselacCeilingDiffuserWindow

        Args:
            value (str): value for IDD Field `Mixed Regime Window Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_window_equation_source` or None if not set

        """
        return self["Mixed Regime Window Equation Source"]

    @mixed_regime_window_equation_source.setter
    def mixed_regime_window_equation_source(
            self,
            value="GoldsteinNovoselacCeilingDiffuserWindow"):
        """Corresponds to IDD field `Mixed Regime Window Equation Source`"""
        self["Mixed Regime Window Equation Source"] = value

    @property
    def mixed_regime_window_equation_user_curve_name(self):
        """field `Mixed Regime Window Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Window Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_regime_window_equation_user_curve_name` or None if not set

        """
        return self["Mixed Regime Window Equation User Curve Name"]

    @mixed_regime_window_equation_user_curve_name.setter
    def mixed_regime_window_equation_user_curve_name(self, value=None):
        """Corresponds to IDD field `Mixed Regime Window Equation User Curve
        Name`"""
        self["Mixed Regime Window Equation User Curve Name"] = value




class SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections(DataObject):

    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the outside face, the side of the surface facing away from the thermal zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'wind convection windward vertical wall equation source',
                                       {'name': u'Wind Convection Windward Vertical Wall Equation Source',
                                        'pyname': u'wind_convection_windward_vertical_wall_equation_source',
                                        'default': u'TARPWindward',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SimpleCombined',
                                                            u'TARPWindward',
                                                            u'MoWiTTWindward',
                                                            u'DOE2Windward',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'BlockenWindward',
                                                            u'EmmelVertical',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wind convection windward equation vertical wall user curve name',
                                       {'name': u'Wind Convection Windward Equation Vertical Wall User Curve Name',
                                        'pyname': u'wind_convection_windward_equation_vertical_wall_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wind convection leeward vertical wall equation source',
                                       {'name': u'Wind Convection Leeward Vertical Wall Equation Source',
                                        'pyname': u'wind_convection_leeward_vertical_wall_equation_source',
                                        'default': u'TARPLeeward',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SimpleCombined',
                                                            u'TARPLeeward',
                                                            u'MoWiTTLeeward',
                                                            u'DOE2Leeward',
                                                            u'EmmelVertical',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wind convection leeward vertical wall equation user curve name',
                                       {'name': u'Wind Convection Leeward Vertical Wall Equation User Curve Name',
                                        'pyname': u'wind_convection_leeward_vertical_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wind convection horizontal roof equation source',
                                       {'name': u'Wind Convection Horizontal Roof Equation Source',
                                        'pyname': u'wind_convection_horizontal_roof_equation_source',
                                        'default': u'ClearRoof',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SimpleCombined',
                                                            u'TARPWindward',
                                                            u'MoWiTTWindward',
                                                            u'DOE2Windward',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'BlockenWindward',
                                                            u'EmmelRoof',
                                                            u'ClearRoof',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wind convection horizontal roof user curve name',
                                       {'name': u'Wind Convection Horizontal Roof User Curve Name',
                                        'pyname': u'wind_convection_horizontal_roof_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'natural convection vertical wall equation source',
                                       {'name': u'Natural Convection Vertical Wall Equation Source',
                                        'pyname': u'natural_convection_vertical_wall_equation_source',
                                        'default': u'ASHRAEVerticalWall',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEVerticalWall',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'ISO15099Windows',
                                                            u'UserCurve',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'natural convection vertical wall equation user curve name',
                                       {'name': u'Natural Convection Vertical Wall Equation User Curve Name',
                                        'pyname': u'natural_convection_vertical_wall_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'natural convection stable horizontal equation source',
                                       {'name': u'Natural Convection Stable Horizontal Equation Source',
                                        'pyname': u'natural_convection_stable_horizontal_equation_source',
                                        'default': u'WaltonStableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonStableHorizontalOrTilt',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'UserCurve',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'natural convection stable horizontal equation user curve name',
                                       {'name': u'Natural Convection Stable Horizontal Equation User Curve Name',
                                        'pyname': u'natural_convection_stable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'natural convection unstable horizontal equation source',
                                       {'name': u'Natural Convection Unstable Horizontal Equation Source',
                                        'pyname': u'natural_convection_unstable_horizontal_equation_source',
                                        'default': u'WaltonUnstableHorizontalOrTilt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaltonUnstableHorizontalOrTilt',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'UserCurve',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'natural convection unstable horizontal equation user curve name',
                                       {'name': u'Natural Convection Unstable Horizontal Equation User Curve Name',
                                        'pyname': u'natural_convection_unstable_horizontal_equation_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections',
               'pyname': u'SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections',
               'required-object': False,
               'unique-object': True}

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
    def wind_convection_windward_vertical_wall_equation_source(self):
        """field `Wind Convection Windward Vertical Wall Equation Source`

        |  Default value: TARPWindward

        Args:
            value (str): value for IDD Field `Wind Convection Windward Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_convection_windward_vertical_wall_equation_source` or None if not set

        """
        return self["Wind Convection Windward Vertical Wall Equation Source"]

    @wind_convection_windward_vertical_wall_equation_source.setter
    def wind_convection_windward_vertical_wall_equation_source(
            self,
            value="TARPWindward"):
        """Corresponds to IDD field `Wind Convection Windward Vertical Wall
        Equation Source`"""
        self["Wind Convection Windward Vertical Wall Equation Source"] = value

    @property
    def wind_convection_windward_equation_vertical_wall_user_curve_name(self):
        """field `Wind Convection Windward Equation Vertical Wall User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wind Convection Windward Equation Vertical Wall User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_convection_windward_equation_vertical_wall_user_curve_name` or None if not set

        """
        return self[
            "Wind Convection Windward Equation Vertical Wall User Curve Name"]

    @wind_convection_windward_equation_vertical_wall_user_curve_name.setter
    def wind_convection_windward_equation_vertical_wall_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wind Convection Windward Equation Vertical
        Wall User Curve Name`"""
        self[
            "Wind Convection Windward Equation Vertical Wall User Curve Name"] = value

    @property
    def wind_convection_leeward_vertical_wall_equation_source(self):
        """field `Wind Convection Leeward Vertical Wall Equation Source`

        |  Default value: TARPLeeward

        Args:
            value (str): value for IDD Field `Wind Convection Leeward Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_convection_leeward_vertical_wall_equation_source` or None if not set

        """
        return self["Wind Convection Leeward Vertical Wall Equation Source"]

    @wind_convection_leeward_vertical_wall_equation_source.setter
    def wind_convection_leeward_vertical_wall_equation_source(
            self,
            value="TARPLeeward"):
        """Corresponds to IDD field `Wind Convection Leeward Vertical Wall
        Equation Source`"""
        self["Wind Convection Leeward Vertical Wall Equation Source"] = value

    @property
    def wind_convection_leeward_vertical_wall_equation_user_curve_name(self):
        """field `Wind Convection Leeward Vertical Wall Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wind Convection Leeward Vertical Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_convection_leeward_vertical_wall_equation_user_curve_name` or None if not set

        """
        return self[
            "Wind Convection Leeward Vertical Wall Equation User Curve Name"]

    @wind_convection_leeward_vertical_wall_equation_user_curve_name.setter
    def wind_convection_leeward_vertical_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Wind Convection Leeward Vertical Wall
        Equation User Curve Name`"""
        self[
            "Wind Convection Leeward Vertical Wall Equation User Curve Name"] = value

    @property
    def wind_convection_horizontal_roof_equation_source(self):
        """field `Wind Convection Horizontal Roof Equation Source`

        |  Default value: ClearRoof

        Args:
            value (str): value for IDD Field `Wind Convection Horizontal Roof Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_convection_horizontal_roof_equation_source` or None if not set

        """
        return self["Wind Convection Horizontal Roof Equation Source"]

    @wind_convection_horizontal_roof_equation_source.setter
    def wind_convection_horizontal_roof_equation_source(
            self,
            value="ClearRoof"):
        """Corresponds to IDD field `Wind Convection Horizontal Roof Equation
        Source`"""
        self["Wind Convection Horizontal Roof Equation Source"] = value

    @property
    def wind_convection_horizontal_roof_user_curve_name(self):
        """field `Wind Convection Horizontal Roof User Curve Name`

        |  The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wind Convection Horizontal Roof User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_convection_horizontal_roof_user_curve_name` or None if not set

        """
        return self["Wind Convection Horizontal Roof User Curve Name"]

    @wind_convection_horizontal_roof_user_curve_name.setter
    def wind_convection_horizontal_roof_user_curve_name(self, value=None):
        """Corresponds to IDD field `Wind Convection Horizontal Roof User Curve
        Name`"""
        self["Wind Convection Horizontal Roof User Curve Name"] = value

    @property
    def natural_convection_vertical_wall_equation_source(self):
        """field `Natural Convection Vertical Wall Equation Source`

        |  This is for vertical walls
        |  Default value: ASHRAEVerticalWall

        Args:
            value (str): value for IDD Field `Natural Convection Vertical Wall Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `natural_convection_vertical_wall_equation_source` or None if not set

        """
        return self["Natural Convection Vertical Wall Equation Source"]

    @natural_convection_vertical_wall_equation_source.setter
    def natural_convection_vertical_wall_equation_source(
            self,
            value="ASHRAEVerticalWall"):
        """Corresponds to IDD field `Natural Convection Vertical Wall Equation
        Source`"""
        self["Natural Convection Vertical Wall Equation Source"] = value

    @property
    def natural_convection_vertical_wall_equation_user_curve_name(self):
        """field `Natural Convection Vertical Wall Equation User Curve Name`

        |  The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Natural Convection Vertical Wall Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `natural_convection_vertical_wall_equation_user_curve_name` or None if not set

        """
        return self[
            "Natural Convection Vertical Wall Equation User Curve Name"]

    @natural_convection_vertical_wall_equation_user_curve_name.setter
    def natural_convection_vertical_wall_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Natural Convection Vertical Wall Equation
        User Curve Name`"""
        self[
            "Natural Convection Vertical Wall Equation User Curve Name"] = value

    @property
    def natural_convection_stable_horizontal_equation_source(self):
        """field `Natural Convection Stable Horizontal Equation Source`

        |  This is for horizontal surfaces with heat flow directed for stable thermal stratification
        |  Default value: WaltonStableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Natural Convection Stable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `natural_convection_stable_horizontal_equation_source` or None if not set

        """
        return self["Natural Convection Stable Horizontal Equation Source"]

    @natural_convection_stable_horizontal_equation_source.setter
    def natural_convection_stable_horizontal_equation_source(
            self,
            value="WaltonStableHorizontalOrTilt"):
        """Corresponds to IDD field `Natural Convection Stable Horizontal
        Equation Source`"""
        self["Natural Convection Stable Horizontal Equation Source"] = value

    @property
    def natural_convection_stable_horizontal_equation_user_curve_name(self):
        """field `Natural Convection Stable Horizontal Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Natural Convection Stable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `natural_convection_stable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Natural Convection Stable Horizontal Equation User Curve Name"]

    @natural_convection_stable_horizontal_equation_user_curve_name.setter
    def natural_convection_stable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Natural Convection Stable Horizontal
        Equation User Curve Name`"""
        self[
            "Natural Convection Stable Horizontal Equation User Curve Name"] = value

    @property
    def natural_convection_unstable_horizontal_equation_source(self):
        """field `Natural Convection Unstable Horizontal Equation Source`

        |  Default value: WaltonUnstableHorizontalOrTilt

        Args:
            value (str): value for IDD Field `Natural Convection Unstable Horizontal Equation Source`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `natural_convection_unstable_horizontal_equation_source` or None if not set

        """
        return self["Natural Convection Unstable Horizontal Equation Source"]

    @natural_convection_unstable_horizontal_equation_source.setter
    def natural_convection_unstable_horizontal_equation_source(
            self,
            value="WaltonUnstableHorizontalOrTilt"):
        """Corresponds to IDD field `Natural Convection Unstable Horizontal
        Equation Source`"""
        self["Natural Convection Unstable Horizontal Equation Source"] = value

    @property
    def natural_convection_unstable_horizontal_equation_user_curve_name(self):
        """field `Natural Convection Unstable Horizontal Equation User Curve
        Name`

        |  The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Natural Convection Unstable Horizontal Equation User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `natural_convection_unstable_horizontal_equation_user_curve_name` or None if not set

        """
        return self[
            "Natural Convection Unstable Horizontal Equation User Curve Name"]

    @natural_convection_unstable_horizontal_equation_user_curve_name.setter
    def natural_convection_unstable_horizontal_equation_user_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Natural Convection Unstable Horizontal
        Equation User Curve Name`"""
        self[
            "Natural Convection Unstable Horizontal Equation User Curve Name"] = value




class SurfaceConvectionAlgorithmInsideUserCurve(DataObject):

    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference temperature for convection heat transfer',
                                       {'name': u'Reference Temperature for Convection Heat Transfer',
                                        'pyname': u'reference_temperature_for_convection_heat_transfer',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MeanAirTemperature',
                                                            u'AdjacentAirTemperature',
                                                            u'SupplyAirTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hc function of temperature difference curve name',
                                       {'name': u'Hc Function of Temperature Difference Curve Name',
                                        'pyname': u'hc_function_of_temperature_difference_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hc function of temperature difference divided by height curve name',
                                       {'name': u'Hc Function of Temperature Difference Divided by Height Curve Name',
                                        'pyname': u'hc_function_of_temperature_difference_divided_by_height_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hc function of air change rate curve name',
                                       {'name': u'Hc Function of Air Change Rate Curve Name',
                                        'pyname': u'hc_function_of_air_change_rate_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hc function of air system volume flow rate divided by zone perimeter length curve name',
                                       {'name': u'Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name',
                                        'pyname': u'hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceConvectionAlgorithm:Inside:UserCurve',
               'pyname': u'SurfaceConvectionAlgorithmInsideUserCurve',
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
    def reference_temperature_for_convection_heat_transfer(self):
        """field `Reference Temperature for Convection Heat Transfer`

        |  Controls which temperature is differenced from surface temperature when using the Hc value

        Args:
            value (str): value for IDD Field `Reference Temperature for Convection Heat Transfer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_temperature_for_convection_heat_transfer` or None if not set

        """
        return self["Reference Temperature for Convection Heat Transfer"]

    @reference_temperature_for_convection_heat_transfer.setter
    def reference_temperature_for_convection_heat_transfer(self, value=None):
        """Corresponds to IDD field `Reference Temperature for Convection Heat
        Transfer`"""
        self["Reference Temperature for Convection Heat Transfer"] = value

    @property
    def hc_function_of_temperature_difference_curve_name(self):
        """field `Hc Function of Temperature Difference Curve Name`

        |  Curve's "x" is absolute value of delta-T (Surface temperature minus reference temperature, (C))

        Args:
            value (str): value for IDD Field `Hc Function of Temperature Difference Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hc_function_of_temperature_difference_curve_name` or None if not set

        """
        return self["Hc Function of Temperature Difference Curve Name"]

    @hc_function_of_temperature_difference_curve_name.setter
    def hc_function_of_temperature_difference_curve_name(self, value=None):
        """Corresponds to IDD field `Hc Function of Temperature Difference
        Curve Name`"""
        self["Hc Function of Temperature Difference Curve Name"] = value

    @property
    def hc_function_of_temperature_difference_divided_by_height_curve_name(
            self):
        """field `Hc Function of Temperature Difference Divided by Height Curve
        Name`

        |  Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        |  when used for an inside face the vertical length scale is the zone's interior height

        Args:
            value (str): value for IDD Field `Hc Function of Temperature Difference Divided by Height Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hc_function_of_temperature_difference_divided_by_height_curve_name` or None if not set

        """
        return self[
            "Hc Function of Temperature Difference Divided by Height Curve Name"]

    @hc_function_of_temperature_difference_divided_by_height_curve_name.setter
    def hc_function_of_temperature_difference_divided_by_height_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Hc Function of Temperature Difference
        Divided by Height Curve Name`"""
        self[
            "Hc Function of Temperature Difference Divided by Height Curve Name"] = value

    @property
    def hc_function_of_air_change_rate_curve_name(self):
        """field `Hc Function of Air Change Rate Curve Name`

        |  Curve's "x" is mechanical ACH (Air Changes per hour from mechanical air system), (1/hr)

        Args:
            value (str): value for IDD Field `Hc Function of Air Change Rate Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hc_function_of_air_change_rate_curve_name` or None if not set

        """
        return self["Hc Function of Air Change Rate Curve Name"]

    @hc_function_of_air_change_rate_curve_name.setter
    def hc_function_of_air_change_rate_curve_name(self, value=None):
        """Corresponds to IDD field `Hc Function of Air Change Rate Curve
        Name`"""
        self["Hc Function of Air Change Rate Curve Name"] = value

    @property
    def hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name(
            self):
        """field `Hc Function of Air System Volume Flow Rate Divided by Zone
        Perimeter Length Curve Name`

        |  Curve's "x" is mechanical system air flow rate (m3/s) divided by zone's length along
        |  exterior walls (m).

        Args:
            value (str): value for IDD Field `Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name` or None if not set

        """
        return self[
            "Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"]

    @hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name.setter
    def hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Hc Function of Air System Volume Flow Rate
        Divided by Zone Perimeter Length Curve Name`"""
        self[
            "Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"] = value




class SurfaceConvectionAlgorithmOutsideUserCurve(DataObject):

    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wind speed type for curve',
                                       {'name': u'Wind Speed Type for Curve',
                                        'pyname': u'wind_speed_type_for_curve',
                                        'default': u'HeightAdjust',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WeatherFile',
                                                            u'HeightAdjust',
                                                            u'ParallelComponent',
                                                            u'ParallelComponentHeightAdjust'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hf function of wind speed curve name',
                                       {'name': u'Hf Function of Wind Speed Curve Name',
                                        'pyname': u'hf_function_of_wind_speed_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hn function of temperature difference curve name',
                                       {'name': u'Hn Function of Temperature Difference Curve Name',
                                        'pyname': u'hn_function_of_temperature_difference_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hn function of temperature difference divided by height curve name',
                                       {'name': u'Hn Function of Temperature Difference Divided by Height Curve Name',
                                        'pyname': u'hn_function_of_temperature_difference_divided_by_height_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceConvectionAlgorithm:Outside:UserCurve',
               'pyname': u'SurfaceConvectionAlgorithmOutsideUserCurve',
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
    def wind_speed_type_for_curve(self):
        """field `Wind Speed Type for Curve`

        |  Default value: HeightAdjust

        Args:
            value (str): value for IDD Field `Wind Speed Type for Curve`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wind_speed_type_for_curve` or None if not set

        """
        return self["Wind Speed Type for Curve"]

    @wind_speed_type_for_curve.setter
    def wind_speed_type_for_curve(self, value="HeightAdjust"):
        """Corresponds to IDD field `Wind Speed Type for Curve`"""
        self["Wind Speed Type for Curve"] = value

    @property
    def hf_function_of_wind_speed_curve_name(self):
        """field `Hf Function of Wind Speed Curve Name`

        |  Curve's "x" is wind speed of the type determined in the previous field (m/s)

        Args:
            value (str): value for IDD Field `Hf Function of Wind Speed Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hf_function_of_wind_speed_curve_name` or None if not set

        """
        return self["Hf Function of Wind Speed Curve Name"]

    @hf_function_of_wind_speed_curve_name.setter
    def hf_function_of_wind_speed_curve_name(self, value=None):
        """Corresponds to IDD field `Hf Function of Wind Speed Curve Name`"""
        self["Hf Function of Wind Speed Curve Name"] = value

    @property
    def hn_function_of_temperature_difference_curve_name(self):
        """field `Hn Function of Temperature Difference Curve Name`

        |  Curve's "x" is absolute value of delta-T (Surface temperature minus air temperature, (C))

        Args:
            value (str): value for IDD Field `Hn Function of Temperature Difference Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hn_function_of_temperature_difference_curve_name` or None if not set

        """
        return self["Hn Function of Temperature Difference Curve Name"]

    @hn_function_of_temperature_difference_curve_name.setter
    def hn_function_of_temperature_difference_curve_name(self, value=None):
        """Corresponds to IDD field `Hn Function of Temperature Difference
        Curve Name`"""
        self["Hn Function of Temperature Difference Curve Name"] = value

    @property
    def hn_function_of_temperature_difference_divided_by_height_curve_name(
            self):
        """field `Hn Function of Temperature Difference Divided by Height Curve
        Name`

        |  Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        |  when used for an outside face the vertical length scale is the exterior facade's overall height

        Args:
            value (str): value for IDD Field `Hn Function of Temperature Difference Divided by Height Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hn_function_of_temperature_difference_divided_by_height_curve_name` or None if not set

        """
        return self[
            "Hn Function of Temperature Difference Divided by Height Curve Name"]

    @hn_function_of_temperature_difference_divided_by_height_curve_name.setter
    def hn_function_of_temperature_difference_divided_by_height_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Hn Function of Temperature Difference
        Divided by Height Curve Name`"""
        self[
            "Hn Function of Temperature Difference Divided by Height Curve Name"] = value




class SurfacePropertyConvectionCoefficients(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:ConvectionCoefficients`
        Allow user settable interior and/or exterior convection coefficients.
        Note that some other factors may limit the lower bounds for these values, such as
        for windows, the interior convection coefficient must be >.28,
        for trombe wall algorithm selection (zone), the interior convection coefficient must be >.1
        for TARP interior convection, the lower limit is also .1
        Minimum and maximum limits are set in HeatBalanceAlgorithm object.
        Defaults in HeatBalanceAlgorithm object are [.1,1000].
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 1 location',
                                       {'name': u'Convection Coefficient 1 Location',
                                        'pyname': u'convection_coefficient_1_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Outside',
                                                            u'Inside'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 1 type',
                                       {'name': u'Convection Coefficient 1 Type',
                                        'pyname': u'convection_coefficient_1_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Value',
                                                            u'Schedule',
                                                            u'UserCurve',
                                                            u'Simple',
                                                            u'SimpleCombined',
                                                            u'TARP',
                                                            u'DOE-2',
                                                            u'MoWitt',
                                                            u'AdaptiveConvectionAlgorithm',
                                                            u'ASHRAEVerticalWall',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'WaltonStableHorizontalOrTilt',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'FisherPedersenCeilingDiffuserCeiling',
                                                            u'FisherPedersenCeilingDiffuserFloor',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'KhalifaEq5WallNearHeat',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'KhalifaEq7Ceiling',
                                                            u'AwbiHattonHeatedFloor',
                                                            u'AwbiHattonHeatedWall',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'BeausoleilMorrisonMixedStableFloor',
                                                            u'BeausoleilMorrisonMixedUnstableFloor',
                                                            u'BeausoleilMorrisonMixedStableCeiling',
                                                            u'BeausoleilMorrisonMixedUnstableCeiling',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'KaradagChilledCeiling',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'GoldsteinNovoselacCeilingDiffuserFloor',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'EmmelVertical',
                                                            u'EmmelRoof',
                                                            u'ClearRoof'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 1',
                                       {'name': u'Convection Coefficient 1',
                                        'pyname': u'convection_coefficient_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'convection coefficient 1 schedule name',
                                       {'name': u'Convection Coefficient 1 Schedule Name',
                                        'pyname': u'convection_coefficient_1_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 1 user curve name',
                                       {'name': u'Convection Coefficient 1 User Curve Name',
                                        'pyname': u'convection_coefficient_1_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 2 location',
                                       {'name': u'Convection Coefficient 2 Location',
                                        'pyname': u'convection_coefficient_2_location',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Outside',
                                                            u'Inside'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 2 type',
                                       {'name': u'Convection Coefficient 2 Type',
                                        'pyname': u'convection_coefficient_2_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Value',
                                                            u'Schedule',
                                                            u'UserCurve',
                                                            u'Simple',
                                                            u'SimpleCombined',
                                                            u'TARP',
                                                            u'DOE-2',
                                                            u'MoWitt',
                                                            u'AdaptiveConvectionAlgorithm',
                                                            u'ASHRAEVerticalWall',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'WaltonStableHorizontalOrTilt',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'FisherPedersenCeilingDiffuserCeiling',
                                                            u'FisherPedersenCeilingDiffuserFloor',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'KhalifaEq5WallNearHeat',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'KhalifaEq7Ceiling',
                                                            u'AwbiHattonHeatedFloor',
                                                            u'AwbiHattonHeatedWall',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'BeausoleilMorrisonMixedStableFloor',
                                                            u'BeausoleilMorrisonMixedUnstableFloor',
                                                            u'BeausoleilMorrisonMixedStableCeiling',
                                                            u'BeausoleilMorrisonMixedUnstableCeiling',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'KaradagChilledCeiling',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'GoldsteinNovoselacCeilingDiffuserFloor',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'EmmelVertical',
                                                            u'EmmelRoof',
                                                            u'ClearRoof'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 2',
                                       {'name': u'Convection Coefficient 2',
                                        'pyname': u'convection_coefficient_2',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'convection coefficient 2 schedule name',
                                       {'name': u'Convection Coefficient 2 Schedule Name',
                                        'pyname': u'convection_coefficient_2_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 2 user curve name',
                                       {'name': u'Convection Coefficient 2 User Curve Name',
                                        'pyname': u'convection_coefficient_2_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceProperty:ConvectionCoefficients',
               'pyname': u'SurfacePropertyConvectionCoefficients',
               'required-object': False,
               'unique-object': False}

    @property
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def convection_coefficient_1_location(self):
        """field `Convection Coefficient 1 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_location` or None if not set

        """
        return self["Convection Coefficient 1 Location"]

    @convection_coefficient_1_location.setter
    def convection_coefficient_1_location(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 Location`"""
        self["Convection Coefficient 1 Location"] = value

    @property
    def convection_coefficient_1_type(self):
        """field `Convection Coefficient 1 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_type` or None if not set

        """
        return self["Convection Coefficient 1 Type"]

    @convection_coefficient_1_type.setter
    def convection_coefficient_1_type(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 Type`"""
        self["Convection Coefficient 1 Type"] = value

    @property
    def convection_coefficient_1(self):
        """field `Convection Coefficient 1`

        |  used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000
        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Convection Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convection_coefficient_1` or None if not set

        """
        return self["Convection Coefficient 1"]

    @convection_coefficient_1.setter
    def convection_coefficient_1(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1`"""
        self["Convection Coefficient 1"] = value

    @property
    def convection_coefficient_1_schedule_name(self):
        """field `Convection Coefficient 1 Schedule Name`

        |  used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_schedule_name` or None if not set

        """
        return self["Convection Coefficient 1 Schedule Name"]

    @convection_coefficient_1_schedule_name.setter
    def convection_coefficient_1_schedule_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 Schedule Name`"""
        self["Convection Coefficient 1 Schedule Name"] = value

    @property
    def convection_coefficient_1_user_curve_name(self):
        """field `Convection Coefficient 1 User Curve Name`

        |  used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_user_curve_name` or None if not set

        """
        return self["Convection Coefficient 1 User Curve Name"]

    @convection_coefficient_1_user_curve_name.setter
    def convection_coefficient_1_user_curve_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 User Curve
        Name`"""
        self["Convection Coefficient 1 User Curve Name"] = value

    @property
    def convection_coefficient_2_location(self):
        """field `Convection Coefficient 2 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_location` or None if not set

        """
        return self["Convection Coefficient 2 Location"]

    @convection_coefficient_2_location.setter
    def convection_coefficient_2_location(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 Location`"""
        self["Convection Coefficient 2 Location"] = value

    @property
    def convection_coefficient_2_type(self):
        """field `Convection Coefficient 2 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_type` or None if not set

        """
        return self["Convection Coefficient 2 Type"]

    @convection_coefficient_2_type.setter
    def convection_coefficient_2_type(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 Type`"""
        self["Convection Coefficient 2 Type"] = value

    @property
    def convection_coefficient_2(self):
        """field `Convection Coefficient 2`

        |  used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000
        |  Units: W/m2-K
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `Convection Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convection_coefficient_2` or None if not set

        """
        return self["Convection Coefficient 2"]

    @convection_coefficient_2.setter
    def convection_coefficient_2(self, value=0.1):
        """Corresponds to IDD field `Convection Coefficient 2`"""
        self["Convection Coefficient 2"] = value

    @property
    def convection_coefficient_2_schedule_name(self):
        """field `Convection Coefficient 2 Schedule Name`

        |  used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_schedule_name` or None if not set

        """
        return self["Convection Coefficient 2 Schedule Name"]

    @convection_coefficient_2_schedule_name.setter
    def convection_coefficient_2_schedule_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 Schedule Name`"""
        self["Convection Coefficient 2 Schedule Name"] = value

    @property
    def convection_coefficient_2_user_curve_name(self):
        """field `Convection Coefficient 2 User Curve Name`

        |  used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_user_curve_name` or None if not set

        """
        return self["Convection Coefficient 2 User Curve Name"]

    @convection_coefficient_2_user_curve_name.setter
    def convection_coefficient_2_user_curve_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 User Curve
        Name`"""
        self["Convection Coefficient 2 User Curve Name"] = value




class SurfacePropertyConvectionCoefficientsMultipleSurface(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:ConvectionCoefficients:MultipleSurface`
        Allow user settable interior and/or exterior convection coefficients.
        Note that some other factors may limit the lower bounds for these values, such as
        for windows, the interior convection coefficient must be >.28,
        for trombe wall algorithm selection (zone), the interior convection coefficient must be >.1
        for TARP interior convection, the lower limit is also .1
        Minimum and maximum limits are set in HeatBalanceAlgorithm object.
        Defaults in HeatBalanceAlgorithm object are [.1,1000].
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'surface type',
                                       {'name': u'Surface Type',
                                        'pyname': u'surface_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'AllExteriorSurfaces',
                                                            u'AllExteriorWindows',
                                                            u'AllExteriorWalls',
                                                            u'AllExteriorRoofs',
                                                            u'AllExteriorFloors',
                                                            u'AllInteriorSurfaces',
                                                            u'AllInteriorWalls',
                                                            u'AllInteriorWindows',
                                                            u'AllInteriorCeilings',
                                                            u'AllInteriorFloors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 1 location',
                                       {'name': u'Convection Coefficient 1 Location',
                                        'pyname': u'convection_coefficient_1_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Outside',
                                                            u'Inside'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 1 type',
                                       {'name': u'Convection Coefficient 1 Type',
                                        'pyname': u'convection_coefficient_1_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Value',
                                                            u'Schedule',
                                                            u'Simple',
                                                            u'SimpleCombined',
                                                            u'TARP',
                                                            u'DOE-2',
                                                            u'MoWitt',
                                                            u'AdaptiveConvectionAlgorithm',
                                                            u'ASHRAEVerticalWall',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'WaltonStableHorizontalOrTilt',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'FisherPedersenCeilingDiffuserCeiling',
                                                            u'FisherPedersenCeilingDiffuserFloor',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'KhalifaEq5WallNearHeat',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'KhalifaEq7Ceiling',
                                                            u'AwbiHattonHeatedFloor',
                                                            u'AwbiHattonHeatedWall',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'BeausoleilMorrisonMixedStableFloor',
                                                            u'BeausoleilMorrisonMixedUnstableFloor',
                                                            u'BeausoleilMorrisonMixedStableCeiling',
                                                            u'BeausoleilMorrisonMixedUnstableCeiling',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'KaradagChilledCeiling',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'GoldsteinNovoselacCeilingDiffuserFloor',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'BlockenWindard',
                                                            u'EmmelVertical',
                                                            u'EmmelRoof',
                                                            u'ClearRoof',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 1',
                                       {'name': u'Convection Coefficient 1',
                                        'pyname': u'convection_coefficient_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'convection coefficient 1 schedule name',
                                       {'name': u'Convection Coefficient 1 Schedule Name',
                                        'pyname': u'convection_coefficient_1_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 1 user curve name',
                                       {'name': u'Convection Coefficient 1 User Curve Name',
                                        'pyname': u'convection_coefficient_1_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 2 location',
                                       {'name': u'Convection Coefficient 2 Location',
                                        'pyname': u'convection_coefficient_2_location',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Outside',
                                                            u'Inside'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 2 type',
                                       {'name': u'Convection Coefficient 2 Type',
                                        'pyname': u'convection_coefficient_2_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Value',
                                                            u'Schedule',
                                                            u'Simple',
                                                            u'SimpleCombined',
                                                            u'TARP',
                                                            u'DOE-2',
                                                            u'MoWitt',
                                                            u'AdaptiveConvectionAlgorithm',
                                                            u'ASHRAEVerticalWall',
                                                            u'WaltonUnstableHorizontalOrTilt',
                                                            u'WaltonStableHorizontalOrTilt',
                                                            u'FisherPedersenCeilingDiffuserWalls',
                                                            u'FisherPedersenCeilingDiffuserCeiling',
                                                            u'FisherPedersenCeilingDiffuserFloor',
                                                            u'AlamdariHammondStableHorizontal',
                                                            u'AlamdariHammondUnstableHorizontal',
                                                            u'AlamdariHammondVerticalWall',
                                                            u'KhalifaEq3WallAwayFromHeat',
                                                            u'KhalifaEq4CeilingAwayFromHeat',
                                                            u'KhalifaEq5WallNearHeat',
                                                            u'KhalifaEq6NonHeatedWalls',
                                                            u'KhalifaEq7Ceiling',
                                                            u'AwbiHattonHeatedFloor',
                                                            u'AwbiHattonHeatedWall',
                                                            u'BeausoleilMorrisonMixedAssistedWall',
                                                            u'BeausoleilMorrisonMixedOpposingWall',
                                                            u'BeausoleilMorrisonMixedStableFloor',
                                                            u'BeausoleilMorrisonMixedUnstableFloor',
                                                            u'BeausoleilMorrisonMixedStableCeiling',
                                                            u'BeausoleilMorrisonMixedUnstableCeiling',
                                                            u'FohannoPolidoriVerticalWall',
                                                            u'KaradagChilledCeiling',
                                                            u'ISO15099Windows',
                                                            u'GoldsteinNovoselacCeilingDiffuserWindow',
                                                            u'GoldsteinNovoselacCeilingDiffuserWalls',
                                                            u'GoldsteinNovoselacCeilingDiffuserFloor',
                                                            u'NusseltJurges',
                                                            u'McAdams',
                                                            u'Mitchell',
                                                            u'BlockenWindard',
                                                            u'EmmelVertical',
                                                            u'EmmelRoof',
                                                            u'ClearRoof',
                                                            u'UserCurve'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'convection coefficient 2',
                                       {'name': u'Convection Coefficient 2',
                                        'pyname': u'convection_coefficient_2',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'convection coefficient 2 schedule name',
                                       {'name': u'Convection Coefficient 2 Schedule Name',
                                        'pyname': u'convection_coefficient_2_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'convection coefficient 2 user curve name',
                                       {'name': u'Convection Coefficient 2 User Curve Name',
                                        'pyname': u'convection_coefficient_2_user_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceProperty:ConvectionCoefficients:MultipleSurface',
               'pyname': u'SurfacePropertyConvectionCoefficientsMultipleSurface',
               'required-object': False,
               'unique-object': False}

    @property
    def surface_type(self):
        """field `Surface Type`

        Args:
            value (str): value for IDD Field `Surface Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_type` or None if not set

        """
        return self["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """Corresponds to IDD field `Surface Type`"""
        self["Surface Type"] = value

    @property
    def convection_coefficient_1_location(self):
        """field `Convection Coefficient 1 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_location` or None if not set

        """
        return self["Convection Coefficient 1 Location"]

    @convection_coefficient_1_location.setter
    def convection_coefficient_1_location(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 Location`"""
        self["Convection Coefficient 1 Location"] = value

    @property
    def convection_coefficient_1_type(self):
        """field `Convection Coefficient 1 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_type` or None if not set

        """
        return self["Convection Coefficient 1 Type"]

    @convection_coefficient_1_type.setter
    def convection_coefficient_1_type(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 Type`"""
        self["Convection Coefficient 1 Type"] = value

    @property
    def convection_coefficient_1(self):
        """field `Convection Coefficient 1`

        |  used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000
        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Convection Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convection_coefficient_1` or None if not set

        """
        return self["Convection Coefficient 1"]

    @convection_coefficient_1.setter
    def convection_coefficient_1(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1`"""
        self["Convection Coefficient 1"] = value

    @property
    def convection_coefficient_1_schedule_name(self):
        """field `Convection Coefficient 1 Schedule Name`

        |  used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_schedule_name` or None if not set

        """
        return self["Convection Coefficient 1 Schedule Name"]

    @convection_coefficient_1_schedule_name.setter
    def convection_coefficient_1_schedule_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 Schedule Name`"""
        self["Convection Coefficient 1 Schedule Name"] = value

    @property
    def convection_coefficient_1_user_curve_name(self):
        """field `Convection Coefficient 1 User Curve Name`

        |  used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_1_user_curve_name` or None if not set

        """
        return self["Convection Coefficient 1 User Curve Name"]

    @convection_coefficient_1_user_curve_name.setter
    def convection_coefficient_1_user_curve_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 1 User Curve
        Name`"""
        self["Convection Coefficient 1 User Curve Name"] = value

    @property
    def convection_coefficient_2_location(self):
        """field `Convection Coefficient 2 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_location` or None if not set

        """
        return self["Convection Coefficient 2 Location"]

    @convection_coefficient_2_location.setter
    def convection_coefficient_2_location(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 Location`"""
        self["Convection Coefficient 2 Location"] = value

    @property
    def convection_coefficient_2_type(self):
        """field `Convection Coefficient 2 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_type` or None if not set

        """
        return self["Convection Coefficient 2 Type"]

    @convection_coefficient_2_type.setter
    def convection_coefficient_2_type(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 Type`"""
        self["Convection Coefficient 2 Type"] = value

    @property
    def convection_coefficient_2(self):
        """field `Convection Coefficient 2`

        |  used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000
        |  Units: W/m2-K
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `Convection Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convection_coefficient_2` or None if not set

        """
        return self["Convection Coefficient 2"]

    @convection_coefficient_2.setter
    def convection_coefficient_2(self, value=0.1):
        """Corresponds to IDD field `Convection Coefficient 2`"""
        self["Convection Coefficient 2"] = value

    @property
    def convection_coefficient_2_schedule_name(self):
        """field `Convection Coefficient 2 Schedule Name`

        |  used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        |  Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_schedule_name` or None if not set

        """
        return self["Convection Coefficient 2 Schedule Name"]

    @convection_coefficient_2_schedule_name.setter
    def convection_coefficient_2_schedule_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 Schedule Name`"""
        self["Convection Coefficient 2 Schedule Name"] = value

    @property
    def convection_coefficient_2_user_curve_name(self):
        """field `Convection Coefficient 2 User Curve Name`

        |  used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 User Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `convection_coefficient_2_user_curve_name` or None if not set

        """
        return self["Convection Coefficient 2 User Curve Name"]

    @convection_coefficient_2_user_curve_name.setter
    def convection_coefficient_2_user_curve_name(self, value=None):
        """Corresponds to IDD field `Convection Coefficient 2 User Curve
        Name`"""
        self["Convection Coefficient 2 User Curve Name"] = value




class SurfacePropertiesVaporCoefficients(DataObject):

    """ Corresponds to IDD object `SurfaceProperties:VaporCoefficients`
        The interior and external vapor transfer coefficients.
        Normally these value are calculated using the heat convection coefficient values.
        Use this object to used fixed constant values.
        Units are kg/Pa.s.m2
        This will only work with the CombinedHeatAndMoistureFiniteElement algorithm for surfaces.
        Other algorithms will ignore these coefficients
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'constant external vapor transfer coefficient',
                                       {'name': u'Constant External Vapor Transfer Coefficient',
                                        'pyname': u'constant_external_vapor_transfer_coefficient',
                                        'default': u'No',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'external vapor coefficient value',
                                       {'name': u'External Vapor Coefficient Value',
                                        'pyname': u'external_vapor_coefficient_value',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/Pa-s-m2'}),
                                      (u'constant internal vapor transfer coefficient',
                                       {'name': u'Constant Internal vapor Transfer Coefficient',
                                        'pyname': u'constant_internal_vapor_transfer_coefficient',
                                        'default': u'No',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'internal vapor coefficient value',
                                       {'name': u'Internal Vapor Coefficient Value',
                                        'pyname': u'internal_vapor_coefficient_value',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/Pa-s-m2'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceProperties:VaporCoefficients',
               'pyname': u'SurfacePropertiesVaporCoefficients',
               'required-object': False,
               'unique-object': False}

    @property
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def constant_external_vapor_transfer_coefficient(self):
        """field `Constant External Vapor Transfer Coefficient`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Constant External Vapor Transfer Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `constant_external_vapor_transfer_coefficient` or None if not set

        """
        return self["Constant External Vapor Transfer Coefficient"]

    @constant_external_vapor_transfer_coefficient.setter
    def constant_external_vapor_transfer_coefficient(self, value="No"):
        """Corresponds to IDD field `Constant External Vapor Transfer
        Coefficient`"""
        self["Constant External Vapor Transfer Coefficient"] = value

    @property
    def external_vapor_coefficient_value(self):
        """field `External Vapor Coefficient Value`

        |  Units: kg/Pa-s-m2

        Args:
            value (float): value for IDD Field `External Vapor Coefficient Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `external_vapor_coefficient_value` or None if not set

        """
        return self["External Vapor Coefficient Value"]

    @external_vapor_coefficient_value.setter
    def external_vapor_coefficient_value(self, value=None):
        """Corresponds to IDD field `External Vapor Coefficient Value`"""
        self["External Vapor Coefficient Value"] = value

    @property
    def constant_internal_vapor_transfer_coefficient(self):
        """field `Constant Internal vapor Transfer Coefficient`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Constant Internal vapor Transfer Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `constant_internal_vapor_transfer_coefficient` or None if not set

        """
        return self["Constant Internal vapor Transfer Coefficient"]

    @constant_internal_vapor_transfer_coefficient.setter
    def constant_internal_vapor_transfer_coefficient(self, value="No"):
        """Corresponds to IDD field `Constant Internal vapor Transfer
        Coefficient`"""
        self["Constant Internal vapor Transfer Coefficient"] = value

    @property
    def internal_vapor_coefficient_value(self):
        """field `Internal Vapor Coefficient Value`

        |  Units: kg/Pa-s-m2

        Args:
            value (float): value for IDD Field `Internal Vapor Coefficient Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `internal_vapor_coefficient_value` or None if not set

        """
        return self["Internal Vapor Coefficient Value"]

    @internal_vapor_coefficient_value.setter
    def internal_vapor_coefficient_value(self, value=None):
        """Corresponds to IDD field `Internal Vapor Coefficient Value`"""
        self["Internal Vapor Coefficient Value"] = value




class SurfacePropertyExteriorNaturalVentedCavity(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:ExteriorNaturalVentedCavity`
        Used to describe the decoupled layer, or baffle, and the characteristics of the cavity
        and openings for naturally ventilated exterior surfaces. This object is also used in
        conjunction with the OtherSideConditionsModel.
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'boundary conditions model name',
                                       {'name': u'Boundary Conditions Model Name',
                                        'pyname': u'boundary_conditions_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'area fraction of openings',
                                       {'name': u'Area Fraction of Openings',
                                        'pyname': u'area_fraction_of_openings',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'thermal emissivity of exterior baffle material',
                                       {'name': u'Thermal Emissivity of Exterior Baffle Material',
                                        'pyname': u'thermal_emissivity_of_exterior_baffle_material',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'solar absorbtivity of exterior baffle',
                                       {'name': u'Solar Absorbtivity of Exterior Baffle',
                                        'pyname': u'solar_absorbtivity_of_exterior_baffle',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'height scale for buoyancy-driven ventilation',
                                       {'name': u'Height Scale for Buoyancy-Driven Ventilation',
                                        'pyname': u'height_scale_for_buoyancydriven_ventilation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'effective thickness of cavity behind exterior baffle',
                                       {'name': u'Effective Thickness of Cavity Behind Exterior Baffle',
                                        'pyname': u'effective_thickness_of_cavity_behind_exterior_baffle',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'ratio of actual surface area to projected surface area',
                                       {'name': u'Ratio of Actual Surface Area to Projected Surface Area',
                                        'pyname': u'ratio_of_actual_surface_area_to_projected_surface_area',
                                        'default': 1.0,
                                        'maximum': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.8,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'roughness of exterior surface',
                                       {'name': u'Roughness of Exterior Surface',
                                        'pyname': u'roughness_of_exterior_surface',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'VeryRough',
                                                            u'Rough',
                                                            u'MediumRough',
                                                            u'MediumSmooth',
                                                            u'Smooth',
                                                            u'VerySmooth'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'effectiveness for perforations with respect to wind',
                                       {'name': u'Effectiveness for Perforations with Respect to Wind',
                                        'pyname': u'effectiveness_for_perforations_with_respect_to_wind',
                                        'default': 0.25,
                                        'minimum>': 0.0,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'discharge coefficient for openings with respect to buoyancy driven flow',
                                       {'name': u'Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow',
                                        'pyname': u'discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow',
                                        'default': 0.65,
                                        'minimum>': 0.0,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceProperty:ExteriorNaturalVentedCavity',
               'pyname': u'SurfacePropertyExteriorNaturalVentedCavity',
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
    def boundary_conditions_model_name(self):
        """field `Boundary Conditions Model Name`

        |  Enter the name of a SurfaceProperty:OtherSideConditionsModel object

        Args:
            value (str): value for IDD Field `Boundary Conditions Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `boundary_conditions_model_name` or None if not set

        """
        return self["Boundary Conditions Model Name"]

    @boundary_conditions_model_name.setter
    def boundary_conditions_model_name(self, value=None):
        """Corresponds to IDD field `Boundary Conditions Model Name`"""
        self["Boundary Conditions Model Name"] = value

    @property
    def area_fraction_of_openings(self):
        """field `Area Fraction of Openings`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Area Fraction of Openings`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `area_fraction_of_openings` or None if not set

        """
        return self["Area Fraction of Openings"]

    @area_fraction_of_openings.setter
    def area_fraction_of_openings(self, value=None):
        """Corresponds to IDD field `Area Fraction of Openings`"""
        self["Area Fraction of Openings"] = value

    @property
    def thermal_emissivity_of_exterior_baffle_material(self):
        """field `Thermal Emissivity of Exterior Baffle Material`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Thermal Emissivity of Exterior Baffle Material`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_emissivity_of_exterior_baffle_material` or None if not set

        """
        return self["Thermal Emissivity of Exterior Baffle Material"]

    @thermal_emissivity_of_exterior_baffle_material.setter
    def thermal_emissivity_of_exterior_baffle_material(self, value=None):
        """Corresponds to IDD field `Thermal Emissivity of Exterior Baffle
        Material`"""
        self["Thermal Emissivity of Exterior Baffle Material"] = value

    @property
    def solar_absorbtivity_of_exterior_baffle(self):
        """field `Solar Absorbtivity of Exterior Baffle`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Solar Absorbtivity of Exterior Baffle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_absorbtivity_of_exterior_baffle` or None if not set

        """
        return self["Solar Absorbtivity of Exterior Baffle"]

    @solar_absorbtivity_of_exterior_baffle.setter
    def solar_absorbtivity_of_exterior_baffle(self, value=None):
        """Corresponds to IDD field `Solar Absorbtivity of Exterior Baffle`"""
        self["Solar Absorbtivity of Exterior Baffle"] = value

    @property
    def height_scale_for_buoyancydriven_ventilation(self):
        """field `Height Scale for Buoyancy-Driven Ventilation`

        |  Units: m

        Args:
            value (float): value for IDD Field `Height Scale for Buoyancy-Driven Ventilation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `height_scale_for_buoyancydriven_ventilation` or None if not set
        """
        return self["Height Scale for Buoyancy-Driven Ventilation"]

    @height_scale_for_buoyancydriven_ventilation.setter
    def height_scale_for_buoyancydriven_ventilation(self, value=None):
        """  Corresponds to IDD field `Height Scale for Buoyancy-Driven Ventilation`

        """
        self["Height Scale for Buoyancy-Driven Ventilation"] = value

    @property
    def effective_thickness_of_cavity_behind_exterior_baffle(self):
        """field `Effective Thickness of Cavity Behind Exterior Baffle`

        |  if corrugated, use average depth
        |  Units: m

        Args:
            value (float): value for IDD Field `Effective Thickness of Cavity Behind Exterior Baffle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_thickness_of_cavity_behind_exterior_baffle` or None if not set

        """
        return self["Effective Thickness of Cavity Behind Exterior Baffle"]

    @effective_thickness_of_cavity_behind_exterior_baffle.setter
    def effective_thickness_of_cavity_behind_exterior_baffle(self, value=None):
        """Corresponds to IDD field `Effective Thickness of Cavity Behind
        Exterior Baffle`"""
        self["Effective Thickness of Cavity Behind Exterior Baffle"] = value

    @property
    def ratio_of_actual_surface_area_to_projected_surface_area(self):
        """field `Ratio of Actual Surface Area to Projected Surface Area`

        |  this parameter is used to help account for corrugations in the collector
        |  Units: dimensionless
        |  Default value: 1.0
        |  value >= 0.8
        |  value <= 2.0

        Args:
            value (float): value for IDD Field `Ratio of Actual Surface Area to Projected Surface Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ratio_of_actual_surface_area_to_projected_surface_area` or None if not set

        """
        return self["Ratio of Actual Surface Area to Projected Surface Area"]

    @ratio_of_actual_surface_area_to_projected_surface_area.setter
    def ratio_of_actual_surface_area_to_projected_surface_area(
            self,
            value=1.0):
        """Corresponds to IDD field `Ratio of Actual Surface Area to Projected
        Surface Area`"""
        self["Ratio of Actual Surface Area to Projected Surface Area"] = value

    @property
    def roughness_of_exterior_surface(self):
        """field `Roughness of Exterior Surface`

        Args:
            value (str): value for IDD Field `Roughness of Exterior Surface`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `roughness_of_exterior_surface` or None if not set

        """
        return self["Roughness of Exterior Surface"]

    @roughness_of_exterior_surface.setter
    def roughness_of_exterior_surface(self, value=None):
        """Corresponds to IDD field `Roughness of Exterior Surface`"""
        self["Roughness of Exterior Surface"] = value

    @property
    def effectiveness_for_perforations_with_respect_to_wind(self):
        """field `Effectiveness for Perforations with Respect to Wind`

        |  Units: dimensionless
        |  Default value: 0.25
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Effectiveness for Perforations with Respect to Wind`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effectiveness_for_perforations_with_respect_to_wind` or None if not set

        """
        return self["Effectiveness for Perforations with Respect to Wind"]

    @effectiveness_for_perforations_with_respect_to_wind.setter
    def effectiveness_for_perforations_with_respect_to_wind(self, value=0.25):
        """Corresponds to IDD field `Effectiveness for Perforations with
        Respect to Wind`"""
        self["Effectiveness for Perforations with Respect to Wind"] = value

    @property
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(
            self):
        """field `Discharge Coefficient for Openings with Respect to Buoyancy
        Driven Flow`

        |  Units: dimensionless
        |  Default value: 0.65
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow` or None if not set

        """
        return self[
            "Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"]

    @discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow.setter
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(
            self,
            value=0.65):
        """Corresponds to IDD field `Discharge Coefficient for Openings with
        Respect to Buoyancy Driven Flow`"""
        self[
            "Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
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




class SurfacePropertySolarIncidentInside(DataObject):

    """ Corresponds to IDD object `SurfaceProperty:SolarIncidentInside`
        Used to provide incident solar radiation on the inside of the surface. Reference surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedule instead of calculating it.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'construction name',
                                       {'name': u'Construction Name',
                                        'pyname': u'construction_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inside surface incident sun solar radiation schedule name',
                                       {'name': u'Inside Surface Incident Sun Solar Radiation Schedule Name',
                                        'pyname': u'inside_surface_incident_sun_solar_radiation_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'SurfaceProperty:SolarIncidentInside',
               'pyname': u'SurfacePropertySolarIncidentInside',
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
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def construction_name(self):
        """field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `construction_name` or None if not set

        """
        return self["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """Corresponds to IDD field `Construction Name`"""
        self["Construction Name"] = value

    @property
    def inside_surface_incident_sun_solar_radiation_schedule_name(self):
        """field `Inside Surface Incident Sun Solar Radiation Schedule Name`

        Args:
            value (str): value for IDD Field `Inside Surface Incident Sun Solar Radiation Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inside_surface_incident_sun_solar_radiation_schedule_name` or None if not set

        """
        return self[
            "Inside Surface Incident Sun Solar Radiation Schedule Name"]

    @inside_surface_incident_sun_solar_radiation_schedule_name.setter
    def inside_surface_incident_sun_solar_radiation_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Inside Surface Incident Sun Solar
        Radiation Schedule Name`"""
        self[
            "Inside Surface Incident Sun Solar Radiation Schedule Name"] = value




class ComplexFenestrationPropertySolarAbsorbedLayers(DataObject):

    """ Corresponds to IDD object `ComplexFenestrationProperty:SolarAbsorbedLayers`
        Used to provide solar radiation absorbed in fenestration layers. References surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedules instead of calculating it.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fenestration surface',
                                       {'name': u'Fenestration Surface',
                                        'pyname': u'fenestration_surface',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'construction name',
                                       {'name': u'Construction Name',
                                        'pyname': u'construction_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 1 solar radiation absorbed schedule name',
                                       {'name': u'Layer 1 Solar Radiation Absorbed Schedule Name',
                                        'pyname': u'layer_1_solar_radiation_absorbed_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2 solar radiation absorbed schedule name',
                                       {'name': u'Layer 2 Solar Radiation Absorbed Schedule Name',
                                        'pyname': u'layer_2_solar_radiation_absorbed_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3 solar radiation absorbed schedule name',
                                       {'name': u'Layer 3 Solar Radiation Absorbed Schedule Name',
                                        'pyname': u'layer_3_solar_radiation_absorbed_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4 solar radiation absorbed schedule name',
                                       {'name': u'Layer 4 Solar Radiation Absorbed Schedule Name',
                                        'pyname': u'layer_4_solar_radiation_absorbed_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5 solar radiation absorbed schedule name',
                                       {'name': u'Layer 5 Solar Radiation Absorbed Schedule Name',
                                        'pyname': u'layer_5_solar_radiation_absorbed_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'ComplexFenestrationProperty:SolarAbsorbedLayers',
               'pyname': u'ComplexFenestrationPropertySolarAbsorbedLayers',
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
    def fenestration_surface(self):
        """field `Fenestration Surface`

        Args:
            value (str): value for IDD Field `Fenestration Surface`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fenestration_surface` or None if not set

        """
        return self["Fenestration Surface"]

    @fenestration_surface.setter
    def fenestration_surface(self, value=None):
        """Corresponds to IDD field `Fenestration Surface`"""
        self["Fenestration Surface"] = value

    @property
    def construction_name(self):
        """field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `construction_name` or None if not set

        """
        return self["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """Corresponds to IDD field `Construction Name`"""
        self["Construction Name"] = value

    @property
    def layer_1_solar_radiation_absorbed_schedule_name(self):
        """field `Layer 1 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 1 Solar Radiation Absorbed Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_1_solar_radiation_absorbed_schedule_name` or None if not set

        """
        return self["Layer 1 Solar Radiation Absorbed Schedule Name"]

    @layer_1_solar_radiation_absorbed_schedule_name.setter
    def layer_1_solar_radiation_absorbed_schedule_name(self, value=None):
        """Corresponds to IDD field `Layer 1 Solar Radiation Absorbed Schedule
        Name`"""
        self["Layer 1 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_2_solar_radiation_absorbed_schedule_name(self):
        """field `Layer 2 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 2 Solar Radiation Absorbed Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2_solar_radiation_absorbed_schedule_name` or None if not set

        """
        return self["Layer 2 Solar Radiation Absorbed Schedule Name"]

    @layer_2_solar_radiation_absorbed_schedule_name.setter
    def layer_2_solar_radiation_absorbed_schedule_name(self, value=None):
        """Corresponds to IDD field `Layer 2 Solar Radiation Absorbed Schedule
        Name`"""
        self["Layer 2 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_3_solar_radiation_absorbed_schedule_name(self):
        """field `Layer 3 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 3 Solar Radiation Absorbed Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3_solar_radiation_absorbed_schedule_name` or None if not set

        """
        return self["Layer 3 Solar Radiation Absorbed Schedule Name"]

    @layer_3_solar_radiation_absorbed_schedule_name.setter
    def layer_3_solar_radiation_absorbed_schedule_name(self, value=None):
        """Corresponds to IDD field `Layer 3 Solar Radiation Absorbed Schedule
        Name`"""
        self["Layer 3 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_4_solar_radiation_absorbed_schedule_name(self):
        """field `Layer 4 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 4 Solar Radiation Absorbed Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4_solar_radiation_absorbed_schedule_name` or None if not set

        """
        return self["Layer 4 Solar Radiation Absorbed Schedule Name"]

    @layer_4_solar_radiation_absorbed_schedule_name.setter
    def layer_4_solar_radiation_absorbed_schedule_name(self, value=None):
        """Corresponds to IDD field `Layer 4 Solar Radiation Absorbed Schedule
        Name`"""
        self["Layer 4 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_5_solar_radiation_absorbed_schedule_name(self):
        """field `Layer 5 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 5 Solar Radiation Absorbed Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5_solar_radiation_absorbed_schedule_name` or None if not set

        """
        return self["Layer 5 Solar Radiation Absorbed Schedule Name"]

    @layer_5_solar_radiation_absorbed_schedule_name.setter
    def layer_5_solar_radiation_absorbed_schedule_name(self, value=None):
        """Corresponds to IDD field `Layer 5 Solar Radiation Absorbed Schedule
        Name`"""
        self["Layer 5 Solar Radiation Absorbed Schedule Name"] = value




class ZonePropertyUserViewFactorsBySurfaceName(DataObject):

    """ Corresponds to IDD object `ZoneProperty:UserViewFactors:bySurfaceName`
        View factors for Surface to Surface in a zone.
        (Number of Surfaces)**2 must be entered.
    """
    _schema = {'extensible-fields': OrderedDict([(u'from surface 1',
                                                  {'name': u'From Surface 1',
                                                   'pyname': u'from_surface_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'to surface 1',
                                                  {'name': u'To Surface 1',
                                                   'pyname': u'to_surface_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'view factor 1',
                                                  {'name': u'View Factor 1',
                                                   'pyname': u'view_factor_1',
                                                   'maximum': 1.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
               'fields': OrderedDict([(u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': u'viewfactor',
               'group': u'Advanced Construction',
               'min-fields': 0,
               'name': u'ZoneProperty:UserViewFactors:bySurfaceName',
               'pyname': u'ZonePropertyUserViewFactorsBySurfaceName',
               'required-object': False,
               'unique-object': False}

    @property
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    def add_extensible(self,
                       from_surface_1=None,
                       to_surface_1=None,
                       view_factor_1=None,
                       ):
        """Add values for extensible fields.

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
        from_surface_1 = self.check_value("From Surface 1", from_surface_1)
        vals.append(from_surface_1)
        to_surface_1 = self.check_value("To Surface 1", to_surface_1)
        vals.append(to_surface_1)
        view_factor_1 = self.check_value("View Factor 1", view_factor_1)
        vals.append(view_factor_1)
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


