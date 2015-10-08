""" Data objects in group "Surface Construction Elements"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class Material(DataObject):

    """Corresponds to IDD object `Material` Regular materials described with
    full set of thermal properties."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'roughness',
                                       {'name': u'Roughness',
                                        'pyname': u'roughness',
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
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'maximum': 3.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'conductivity',
                                       {'name': u'Conductivity',
                                        'pyname': u'conductivity',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'density',
                                       {'name': u'Density',
                                        'pyname': u'density',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'specific heat',
                                       {'name': u'Specific Heat',
                                        'pyname': u'specific_heat',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'thermal absorptance',
                                       {'name': u'Thermal Absorptance',
                                        'pyname': u'thermal_absorptance',
                                        'default': 0.9,
                                        'minimum>': 0.0,
                                        'maximum': 0.99999,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'solar absorptance',
                                       {'name': u'Solar Absorptance',
                                        'pyname': u'solar_absorptance',
                                        'default': 0.7,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'visible absorptance',
                                       {'name': u'Visible Absorptance',
                                        'pyname': u'visible_absorptance',
                                        'default': 0.7,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 6,
               'name': u'Material',
               'pyname': u'Material',
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
    def roughness(self):
        """field `Roughness`

        Args:
            value (str): value for IDD Field `Roughness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `roughness` or None if not set

        """
        return self["Roughness"]

    @roughness.setter
    def roughness(self, value=None):
        """Corresponds to IDD field `Roughness`"""
        self["Roughness"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  IP-Units: in
        |  value <= 3.0

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def conductivity(self):
        """field `Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity` or None if not set

        """
        return self["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=None):
        """Corresponds to IDD field `Conductivity`"""
        self["Conductivity"] = value

    @property
    def density(self):
        """field `Density`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density` or None if not set

        """
        return self["Density"]

    @density.setter
    def density(self, value=None):
        """Corresponds to IDD field `Density`"""
        self["Density"] = value

    @property
    def specific_heat(self):
        """field `Specific Heat`

        |  Units: J/kg-K
        |  value >= 100.0

        Args:
            value (float): value for IDD Field `Specific Heat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat` or None if not set

        """
        return self["Specific Heat"]

    @specific_heat.setter
    def specific_heat(self, value=None):
        """Corresponds to IDD field `Specific Heat`"""
        self["Specific Heat"] = value

    @property
    def thermal_absorptance(self):
        """field `Thermal Absorptance`

        |  Default value: 0.9
        |  value <= 0.99999

        Args:
            value (float): value for IDD Field `Thermal Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_absorptance` or None if not set

        """
        return self["Thermal Absorptance"]

    @thermal_absorptance.setter
    def thermal_absorptance(self, value=0.9):
        """Corresponds to IDD field `Thermal Absorptance`"""
        self["Thermal Absorptance"] = value

    @property
    def solar_absorptance(self):
        """field `Solar Absorptance`

        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Solar Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_absorptance` or None if not set

        """
        return self["Solar Absorptance"]

    @solar_absorptance.setter
    def solar_absorptance(self, value=0.7):
        """Corresponds to IDD field `Solar Absorptance`"""
        self["Solar Absorptance"] = value

    @property
    def visible_absorptance(self):
        """field `Visible Absorptance`

        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Visible Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_absorptance` or None if not set

        """
        return self["Visible Absorptance"]

    @visible_absorptance.setter
    def visible_absorptance(self, value=0.7):
        """Corresponds to IDD field `Visible Absorptance`"""
        self["Visible Absorptance"] = value




class MaterialNoMass(DataObject):

    """ Corresponds to IDD object `Material:NoMass`
        Regular materials properties described whose principal description is R (Thermal Resistance)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'roughness',
                                       {'name': u'Roughness',
                                        'pyname': u'roughness',
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
                                      (u'thermal resistance',
                                       {'name': u'Thermal Resistance',
                                        'pyname': u'thermal_resistance',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.001,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2-K/W'}),
                                      (u'thermal absorptance',
                                       {'name': u'Thermal Absorptance',
                                        'pyname': u'thermal_absorptance',
                                        'default': 0.9,
                                        'minimum>': 0.0,
                                        'maximum': 0.99999,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'solar absorptance',
                                       {'name': u'Solar Absorptance',
                                        'pyname': u'solar_absorptance',
                                        'default': 0.7,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'visible absorptance',
                                       {'name': u'Visible Absorptance',
                                        'pyname': u'visible_absorptance',
                                        'default': 0.7,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 3,
               'name': u'Material:NoMass',
               'pyname': u'MaterialNoMass',
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
    def roughness(self):
        """field `Roughness`

        Args:
            value (str): value for IDD Field `Roughness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `roughness` or None if not set

        """
        return self["Roughness"]

    @roughness.setter
    def roughness(self, value=None):
        """Corresponds to IDD field `Roughness`"""
        self["Roughness"] = value

    @property
    def thermal_resistance(self):
        """field `Thermal Resistance`

        |  Units: m2-K/W
        |  value >= 0.001

        Args:
            value (float): value for IDD Field `Thermal Resistance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_resistance` or None if not set

        """
        return self["Thermal Resistance"]

    @thermal_resistance.setter
    def thermal_resistance(self, value=None):
        """Corresponds to IDD field `Thermal Resistance`"""
        self["Thermal Resistance"] = value

    @property
    def thermal_absorptance(self):
        """field `Thermal Absorptance`

        |  Default value: 0.9
        |  value <= 0.99999

        Args:
            value (float): value for IDD Field `Thermal Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_absorptance` or None if not set

        """
        return self["Thermal Absorptance"]

    @thermal_absorptance.setter
    def thermal_absorptance(self, value=0.9):
        """Corresponds to IDD field `Thermal Absorptance`"""
        self["Thermal Absorptance"] = value

    @property
    def solar_absorptance(self):
        """field `Solar Absorptance`

        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Solar Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_absorptance` or None if not set

        """
        return self["Solar Absorptance"]

    @solar_absorptance.setter
    def solar_absorptance(self, value=0.7):
        """Corresponds to IDD field `Solar Absorptance`"""
        self["Solar Absorptance"] = value

    @property
    def visible_absorptance(self):
        """field `Visible Absorptance`

        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Visible Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_absorptance` or None if not set

        """
        return self["Visible Absorptance"]

    @visible_absorptance.setter
    def visible_absorptance(self, value=0.7):
        """Corresponds to IDD field `Visible Absorptance`"""
        self["Visible Absorptance"] = value




class MaterialInfraredTransparent(DataObject):

    """ Corresponds to IDD object `Material:InfraredTransparent`
        Special infrared transparent material.  Similar to a Material:Nomass with low thermal resistance.
        High absorptance in both wavelengths.
        Area will be doubled internally to make internal radiant exchange accurate.
        Should be only material in single layer surface construction.
        All thermal properties are set internally. User needs only to supply name.
        Cannot be used with ConductionFiniteDifference solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 1,
               'name': u'Material:InfraredTransparent',
               'pyname': u'MaterialInfraredTransparent',
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




class MaterialAirGap(DataObject):

    """ Corresponds to IDD object `Material:AirGap`
        Air Space in Opaque Construction
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'thermal resistance',
                                       {'name': u'Thermal Resistance',
                                        'pyname': u'thermal_resistance',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2-K/W'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 2,
               'name': u'Material:AirGap',
               'pyname': u'MaterialAirGap',
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
    def thermal_resistance(self):
        """field `Thermal Resistance`

        |  Units: m2-K/W

        Args:
            value (float): value for IDD Field `Thermal Resistance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_resistance` or None if not set

        """
        return self["Thermal Resistance"]

    @thermal_resistance.setter
    def thermal_resistance(self, value=None):
        """Corresponds to IDD field `Thermal Resistance`"""
        self["Thermal Resistance"] = value




class MaterialRoofVegetation(DataObject):

    """ Corresponds to IDD object `Material:RoofVegetation`
        EcoRoof model, plant layer plus soil layer
        Implemented by Portland State University
        (Sailor et al., January, 2007)
        only one material must be referenced per simulation though the same EcoRoof material could be
        used in multiple constructions. New moisture redistribution scheme (2010) requires higher
        number of timesteps per hour (minimum 12 recommended).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'height of plants',
                                       {'name': u'Height of Plants',
                                        'pyname': u'height_of_plants',
                                        'default': 0.2,
                                        'minimum>': 0.005,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'leaf area index',
                                       {'name': u'Leaf Area Index',
                                        'pyname': u'leaf_area_index',
                                        'default': 1.0,
                                        'minimum>': 0.001,
                                        'maximum': 5.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'leaf reflectivity',
                                       {'name': u'Leaf Reflectivity',
                                        'pyname': u'leaf_reflectivity',
                                        'default': 0.22,
                                        'maximum': 0.5,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.05,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'leaf emissivity',
                                       {'name': u'Leaf Emissivity',
                                        'pyname': u'leaf_emissivity',
                                        'default': 0.95,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.8,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum stomatal resistance',
                                       {'name': u'Minimum Stomatal Resistance',
                                        'pyname': u'minimum_stomatal_resistance',
                                        'default': 180.0,
                                        'maximum': 300.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u's/m'}),
                                      (u'soil layer name',
                                       {'name': u'Soil Layer Name',
                                        'pyname': u'soil_layer_name',
                                        'default': u'Green Roof Soil',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'roughness',
                                       {'name': u'Roughness',
                                        'pyname': u'roughness',
                                        'default': u'MediumRough',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'VeryRough',
                                                            u'MediumRough',
                                                            u'Rough',
                                                            u'Smooth',
                                                            u'MediumSmooth',
                                                            u'VerySmooth'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'default': 0.1,
                                        'minimum>': 0.05,
                                        'maximum': 0.7,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'conductivity of dry soil',
                                       {'name': u'Conductivity of Dry Soil',
                                        'pyname': u'conductivity_of_dry_soil',
                                        'default': 0.35,
                                        'maximum': 1.5,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.2,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'density of dry soil',
                                       {'name': u'Density of Dry Soil',
                                        'pyname': u'density_of_dry_soil',
                                        'default': 1100.0,
                                        'maximum': 2000.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 300.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'specific heat of dry soil',
                                       {'name': u'Specific Heat of Dry Soil',
                                        'pyname': u'specific_heat_of_dry_soil',
                                        'default': 1200.0,
                                        'minimum>': 500.0,
                                        'maximum': 2000.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'thermal absorptance',
                                       {'name': u'Thermal Absorptance',
                                        'pyname': u'thermal_absorptance',
                                        'default': 0.9,
                                        'minimum>': 0.8,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'solar absorptance',
                                       {'name': u'Solar Absorptance',
                                        'pyname': u'solar_absorptance',
                                        'default': 0.7,
                                        'maximum': 0.9,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.4,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'visible absorptance',
                                       {'name': u'Visible Absorptance',
                                        'pyname': u'visible_absorptance',
                                        'default': 0.75,
                                        'minimum>': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'saturation volumetric moisture content of the soil layer',
                                       {'name': u'Saturation Volumetric Moisture Content of the Soil Layer',
                                        'pyname': u'saturation_volumetric_moisture_content_of_the_soil_layer',
                                        'default': 0.3,
                                        'minimum>': 0.1,
                                        'maximum': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'residual volumetric moisture content of the soil layer',
                                       {'name': u'Residual Volumetric Moisture Content of the Soil Layer',
                                        'pyname': u'residual_volumetric_moisture_content_of_the_soil_layer',
                                        'default': 0.01,
                                        'maximum': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.01,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'initial volumetric moisture content of the soil layer',
                                       {'name': u'Initial Volumetric Moisture Content of the Soil Layer',
                                        'pyname': u'initial_volumetric_moisture_content_of_the_soil_layer',
                                        'default': 0.1,
                                        'minimum>': 0.05,
                                        'maximum': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'moisture diffusion calculation method',
                                       {'name': u'Moisture Diffusion Calculation Method',
                                        'pyname': u'moisture_diffusion_calculation_method',
                                        'default': u'Advanced',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Simple',
                                                            u'Advanced'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 18,
               'name': u'Material:RoofVegetation',
               'pyname': u'MaterialRoofVegetation',
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
    def height_of_plants(self):
        """field `Height of Plants`

        |  The ecoroof module is designed for short plants and shrubs.
        |  Units: m
        |  Default value: 0.2
        |  value > 0.005
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Height of Plants`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `height_of_plants` or None if not set

        """
        return self["Height of Plants"]

    @height_of_plants.setter
    def height_of_plants(self, value=0.2):
        """Corresponds to IDD field `Height of Plants`"""
        self["Height of Plants"] = value

    @property
    def leaf_area_index(self):
        """field `Leaf Area Index`

        |  Entire surface is assumed covered, so decrease LAI accordingly.
        |  Units: dimensionless
        |  Default value: 1.0
        |  value > 0.001
        |  value <= 5.0

        Args:
            value (float): value for IDD Field `Leaf Area Index`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `leaf_area_index` or None if not set

        """
        return self["Leaf Area Index"]

    @leaf_area_index.setter
    def leaf_area_index(self, value=1.0):
        """Corresponds to IDD field `Leaf Area Index`"""
        self["Leaf Area Index"] = value

    @property
    def leaf_reflectivity(self):
        """field `Leaf Reflectivity`

        |  Leaf reflectivity (albedo) is typically 0.18-0.25
        |  Units: dimensionless
        |  Default value: 0.22
        |  value >= 0.05
        |  value <= 0.5

        Args:
            value (float): value for IDD Field `Leaf Reflectivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `leaf_reflectivity` or None if not set

        """
        return self["Leaf Reflectivity"]

    @leaf_reflectivity.setter
    def leaf_reflectivity(self, value=0.22):
        """Corresponds to IDD field `Leaf Reflectivity`"""
        self["Leaf Reflectivity"] = value

    @property
    def leaf_emissivity(self):
        """field `Leaf Emissivity`

        |  Default value: 0.95
        |  value >= 0.8
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Leaf Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `leaf_emissivity` or None if not set

        """
        return self["Leaf Emissivity"]

    @leaf_emissivity.setter
    def leaf_emissivity(self, value=0.95):
        """Corresponds to IDD field `Leaf Emissivity`"""
        self["Leaf Emissivity"] = value

    @property
    def minimum_stomatal_resistance(self):
        """field `Minimum Stomatal Resistance`

        |  This depends upon plant type
        |  Units: s/m
        |  Default value: 180.0
        |  value >= 50.0
        |  value <= 300.0

        Args:
            value (float): value for IDD Field `Minimum Stomatal Resistance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_stomatal_resistance` or None if not set

        """
        return self["Minimum Stomatal Resistance"]

    @minimum_stomatal_resistance.setter
    def minimum_stomatal_resistance(self, value=180.0):
        """Corresponds to IDD field `Minimum Stomatal Resistance`"""
        self["Minimum Stomatal Resistance"] = value

    @property
    def soil_layer_name(self):
        """field `Soil Layer Name`

        |  Default value: Green Roof Soil

        Args:
            value (str): value for IDD Field `Soil Layer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `soil_layer_name` or None if not set

        """
        return self["Soil Layer Name"]

    @soil_layer_name.setter
    def soil_layer_name(self, value="Green Roof Soil"):
        """Corresponds to IDD field `Soil Layer Name`"""
        self["Soil Layer Name"] = value

    @property
    def roughness(self):
        """field `Roughness`

        |  Default value: MediumRough

        Args:
            value (str): value for IDD Field `Roughness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `roughness` or None if not set

        """
        return self["Roughness"]

    @roughness.setter
    def roughness(self, value="MediumRough"):
        """Corresponds to IDD field `Roughness`"""
        self["Roughness"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  thickness of the soil layer of the EcoRoof
        |  Soil depths of 0.15m (6in) and 0.30m (12in) are common.
        |  Units: m
        |  IP-Units: in
        |  Default value: 0.1
        |  value > 0.05
        |  value <= 0.7

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=0.1):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def conductivity_of_dry_soil(self):
        """field `Conductivity of Dry Soil`

        |  Thermal conductivity of dry soil.
        |  Typical ecoroof soils range from 0.3 to 0.5
        |  Units: W/m-K
        |  Default value: 0.35
        |  value >= 0.2
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Conductivity of Dry Soil`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_of_dry_soil` or None if not set

        """
        return self["Conductivity of Dry Soil"]

    @conductivity_of_dry_soil.setter
    def conductivity_of_dry_soil(self, value=0.35):
        """Corresponds to IDD field `Conductivity of Dry Soil`"""
        self["Conductivity of Dry Soil"] = value

    @property
    def density_of_dry_soil(self):
        """field `Density of Dry Soil`

        |  Density of dry soil (the code modifies this as the soil becomes moist)
        |  Typical ecoroof soils range from 400 to 1000 (dry to wet)
        |  Units: kg/m3
        |  Default value: 1100.0
        |  value >= 300.0
        |  value <= 2000.0

        Args:
            value (float): value for IDD Field `Density of Dry Soil`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_of_dry_soil` or None if not set

        """
        return self["Density of Dry Soil"]

    @density_of_dry_soil.setter
    def density_of_dry_soil(self, value=1100.0):
        """Corresponds to IDD field `Density of Dry Soil`"""
        self["Density of Dry Soil"] = value

    @property
    def specific_heat_of_dry_soil(self):
        """field `Specific Heat of Dry Soil`

        |  Specific heat of dry soil
        |  Units: J/kg-K
        |  Default value: 1200.0
        |  value > 500.0
        |  value <= 2000.0

        Args:
            value (float): value for IDD Field `Specific Heat of Dry Soil`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_of_dry_soil` or None if not set

        """
        return self["Specific Heat of Dry Soil"]

    @specific_heat_of_dry_soil.setter
    def specific_heat_of_dry_soil(self, value=1200.0):
        """Corresponds to IDD field `Specific Heat of Dry Soil`"""
        self["Specific Heat of Dry Soil"] = value

    @property
    def thermal_absorptance(self):
        """field `Thermal Absorptance`

        |  Soil emissivity is typically in range of 0.90 to 0.98
        |  Default value: 0.9
        |  value > 0.8
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Thermal Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_absorptance` or None if not set

        """
        return self["Thermal Absorptance"]

    @thermal_absorptance.setter
    def thermal_absorptance(self, value=0.9):
        """Corresponds to IDD field `Thermal Absorptance`"""
        self["Thermal Absorptance"] = value

    @property
    def solar_absorptance(self):
        """field `Solar Absorptance`

        |  Solar absorptance of dry soil (1-albedo) is typically 0.60 to 0.85
        |  corresponding to a dry albedo of 0.15 to 0.40
        |  Default value: 0.7
        |  value >= 0.4
        |  value <= 0.9

        Args:
            value (float): value for IDD Field `Solar Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_absorptance` or None if not set

        """
        return self["Solar Absorptance"]

    @solar_absorptance.setter
    def solar_absorptance(self, value=0.7):
        """Corresponds to IDD field `Solar Absorptance`"""
        self["Solar Absorptance"] = value

    @property
    def visible_absorptance(self):
        """field `Visible Absorptance`

        |  Default value: 0.75
        |  value > 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Visible Absorptance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_absorptance` or None if not set

        """
        return self["Visible Absorptance"]

    @visible_absorptance.setter
    def visible_absorptance(self, value=0.75):
        """Corresponds to IDD field `Visible Absorptance`"""
        self["Visible Absorptance"] = value

    @property
    def saturation_volumetric_moisture_content_of_the_soil_layer(self):
        """field `Saturation Volumetric Moisture Content of the Soil Layer`

        |  Maximum moisture content is typically less than 0.5
        |  Default value: 0.3
        |  value > 0.1
        |  value <= 0.5

        Args:
            value (float): value for IDD Field `Saturation Volumetric Moisture Content of the Soil Layer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `saturation_volumetric_moisture_content_of_the_soil_layer` or None if not set

        """
        return self["Saturation Volumetric Moisture Content of the Soil Layer"]

    @saturation_volumetric_moisture_content_of_the_soil_layer.setter
    def saturation_volumetric_moisture_content_of_the_soil_layer(
            self,
            value=0.3):
        """Corresponds to IDD field `Saturation Volumetric Moisture Content of
        the Soil Layer`"""
        self[
            "Saturation Volumetric Moisture Content of the Soil Layer"] = value

    @property
    def residual_volumetric_moisture_content_of_the_soil_layer(self):
        """field `Residual Volumetric Moisture Content of the Soil Layer`

        |  Default value: 0.01
        |  value >= 0.01
        |  value <= 0.1

        Args:
            value (float): value for IDD Field `Residual Volumetric Moisture Content of the Soil Layer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `residual_volumetric_moisture_content_of_the_soil_layer` or None if not set

        """
        return self["Residual Volumetric Moisture Content of the Soil Layer"]

    @residual_volumetric_moisture_content_of_the_soil_layer.setter
    def residual_volumetric_moisture_content_of_the_soil_layer(
            self,
            value=0.01):
        """Corresponds to IDD field `Residual Volumetric Moisture Content of
        the Soil Layer`"""
        self["Residual Volumetric Moisture Content of the Soil Layer"] = value

    @property
    def initial_volumetric_moisture_content_of_the_soil_layer(self):
        """field `Initial Volumetric Moisture Content of the Soil Layer`

        |  Default value: 0.1
        |  value > 0.05
        |  value <= 0.5

        Args:
            value (float): value for IDD Field `Initial Volumetric Moisture Content of the Soil Layer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_volumetric_moisture_content_of_the_soil_layer` or None if not set

        """
        return self["Initial Volumetric Moisture Content of the Soil Layer"]

    @initial_volumetric_moisture_content_of_the_soil_layer.setter
    def initial_volumetric_moisture_content_of_the_soil_layer(self, value=0.1):
        """Corresponds to IDD field `Initial Volumetric Moisture Content of the
        Soil Layer`"""
        self["Initial Volumetric Moisture Content of the Soil Layer"] = value

    @property
    def moisture_diffusion_calculation_method(self):
        """field `Moisture Diffusion Calculation Method`

        |  Advanced calculation requires increased number of timesteps (recommended >20).
        |  Default value: Advanced

        Args:
            value (str): value for IDD Field `Moisture Diffusion Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `moisture_diffusion_calculation_method` or None if not set

        """
        return self["Moisture Diffusion Calculation Method"]

    @moisture_diffusion_calculation_method.setter
    def moisture_diffusion_calculation_method(self, value="Advanced"):
        """Corresponds to IDD field `Moisture Diffusion Calculation Method`"""
        self["Moisture Diffusion Calculation Method"] = value




class WindowMaterialSimpleGlazingSystem(DataObject):

    """ Corresponds to IDD object `WindowMaterial:SimpleGlazingSystem`
        Alternate method of describing windows
        This window material object is used to define an entire glazing system
        using simple performance parameters.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'u-factor',
                                       {'name': u'U-Factor',
                                        'pyname': u'ufactor',
                                        'minimum>': 0.0,
                                        'maximum': 7.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'solar heat gain coefficient',
                                       {'name': u'Solar Heat Gain Coefficient',
                                        'pyname': u'solar_heat_gain_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'maximum<': 1.0}),
                                      (u'visible transmittance',
                                       {'name': u'Visible Transmittance',
                                        'pyname': u'visible_transmittance',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'maximum<': 1.0})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 3,
               'name': u'WindowMaterial:SimpleGlazingSystem',
               'pyname': u'WindowMaterialSimpleGlazingSystem',
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
    def ufactor(self):
        """field `U-Factor`

        |  Enter U-Factor including film coefficients
        |  Note that the effective upper limit for U-factor is 5.8 W/m2-K
        |  Units: W/m2-K
        |  value <= 7.0

        Args:
            value (float): value for IDD Field `U-Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ufactor` or None if not set
        """
        return self["U-Factor"]

    @ufactor.setter
    def ufactor(self, value=None):
        """  Corresponds to IDD field `U-Factor`

        """
        self["U-Factor"] = value

    @property
    def solar_heat_gain_coefficient(self):
        """field `Solar Heat Gain Coefficient`

        |  SHGC at Normal Incidence
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Solar Heat Gain Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_heat_gain_coefficient` or None if not set

        """
        return self["Solar Heat Gain Coefficient"]

    @solar_heat_gain_coefficient.setter
    def solar_heat_gain_coefficient(self, value=None):
        """Corresponds to IDD field `Solar Heat Gain Coefficient`"""
        self["Solar Heat Gain Coefficient"] = value

    @property
    def visible_transmittance(self):
        """field `Visible Transmittance`

        |  VT at Normal Incidence
        |  optional
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_transmittance` or None if not set

        """
        return self["Visible Transmittance"]

    @visible_transmittance.setter
    def visible_transmittance(self, value=None):
        """Corresponds to IDD field `Visible Transmittance`"""
        self["Visible Transmittance"] = value




class WindowMaterialGlazing(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Glazing`
        Glass material properties for Windows or Glass Doors
        Transmittance/Reflectance input method.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'optical data type',
                                       {'name': u'Optical Data Type',
                                        'pyname': u'optical_data_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'SpectralAverage',
                                                            u'Spectral',
                                                            u'BSDF'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'window glass spectral data set name',
                                       {'name': u'Window Glass Spectral Data Set Name',
                                        'pyname': u'window_glass_spectral_data_set_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'solar transmittance at normal incidence',
                                       {'name': u'Solar Transmittance at Normal Incidence',
                                        'pyname': u'solar_transmittance_at_normal_incidence',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side solar reflectance at normal incidence',
                                       {'name': u'Front Side Solar Reflectance at Normal Incidence',
                                        'pyname': u'front_side_solar_reflectance_at_normal_incidence',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side solar reflectance at normal incidence',
                                       {'name': u'Back Side Solar Reflectance at Normal Incidence',
                                        'pyname': u'back_side_solar_reflectance_at_normal_incidence',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'visible transmittance at normal incidence',
                                       {'name': u'Visible Transmittance at Normal Incidence',
                                        'pyname': u'visible_transmittance_at_normal_incidence',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side visible reflectance at normal incidence',
                                       {'name': u'Front Side Visible Reflectance at Normal Incidence',
                                        'pyname': u'front_side_visible_reflectance_at_normal_incidence',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side visible reflectance at normal incidence',
                                       {'name': u'Back Side Visible Reflectance at Normal Incidence',
                                        'pyname': u'back_side_visible_reflectance_at_normal_incidence',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'infrared transmittance at normal incidence',
                                       {'name': u'Infrared Transmittance at Normal Incidence',
                                        'pyname': u'infrared_transmittance_at_normal_incidence',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side infrared hemispherical emissivity',
                                       {'name': u'Front Side Infrared Hemispherical Emissivity',
                                        'pyname': u'front_side_infrared_hemispherical_emissivity',
                                        'default': 0.84,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0}),
                                      (u'back side infrared hemispherical emissivity',
                                       {'name': u'Back Side Infrared Hemispherical Emissivity',
                                        'pyname': u'back_side_infrared_hemispherical_emissivity',
                                        'default': 0.84,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0}),
                                      (u'conductivity',
                                       {'name': u'Conductivity',
                                        'pyname': u'conductivity',
                                        'default': 0.9,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'dirt correction factor for solar and visible transmittance',
                                       {'name': u'Dirt Correction Factor for Solar and Visible Transmittance',
                                        'pyname': u'dirt_correction_factor_for_solar_and_visible_transmittance',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'solar diffusing',
                                       {'name': u'Solar Diffusing',
                                        'pyname': u'solar_diffusing',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'No',
                                                            u'Yes'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u"young's modulus",
                                       {'name': u"Young's modulus",
                                        'pyname': u'youngs_modulus',
                                        'default': 72000000000.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u"poisson's ratio",
                                       {'name': u"Poisson's ratio",
                                        'pyname': u'poissons_ratio',
                                        'default': 0.22,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 14,
               'name': u'WindowMaterial:Glazing',
               'pyname': u'WindowMaterialGlazing',
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
    def optical_data_type(self):
        """field `Optical Data Type`

        Args:
            value (str): value for IDD Field `Optical Data Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `optical_data_type` or None if not set

        """
        return self["Optical Data Type"]

    @optical_data_type.setter
    def optical_data_type(self, value=None):
        """Corresponds to IDD field `Optical Data Type`"""
        self["Optical Data Type"] = value

    @property
    def window_glass_spectral_data_set_name(self):
        """field `Window Glass Spectral Data Set Name`

        |  Used only when Optical Data Type = Spectral

        Args:
            value (str): value for IDD Field `Window Glass Spectral Data Set Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `window_glass_spectral_data_set_name` or None if not set

        """
        return self["Window Glass Spectral Data Set Name"]

    @window_glass_spectral_data_set_name.setter
    def window_glass_spectral_data_set_name(self, value=None):
        """Corresponds to IDD field `Window Glass Spectral Data Set Name`"""
        self["Window Glass Spectral Data Set Name"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def solar_transmittance_at_normal_incidence(self):
        """field `Solar Transmittance at Normal Incidence`

        |  Used only when Optical Data Type = SpectralAverage
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Solar Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_transmittance_at_normal_incidence` or None if not set

        """
        return self["Solar Transmittance at Normal Incidence"]

    @solar_transmittance_at_normal_incidence.setter
    def solar_transmittance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Solar Transmittance at Normal
        Incidence`"""
        self["Solar Transmittance at Normal Incidence"] = value

    @property
    def front_side_solar_reflectance_at_normal_incidence(self):
        """field `Front Side Solar Reflectance at Normal Incidence`

        |  Used only when Optical Data Type = SpectralAverage
        |  Front Side is side closest to outdoor air
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Solar Reflectance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_solar_reflectance_at_normal_incidence` or None if not set

        """
        return self["Front Side Solar Reflectance at Normal Incidence"]

    @front_side_solar_reflectance_at_normal_incidence.setter
    def front_side_solar_reflectance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Front Side Solar Reflectance at Normal
        Incidence`"""
        self["Front Side Solar Reflectance at Normal Incidence"] = value

    @property
    def back_side_solar_reflectance_at_normal_incidence(self):
        """field `Back Side Solar Reflectance at Normal Incidence`

        |  Used only when Optical Data Type = SpectralAverage
        |  Back Side is side closest to zone air
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Solar Reflectance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_solar_reflectance_at_normal_incidence` or None if not set

        """
        return self["Back Side Solar Reflectance at Normal Incidence"]

    @back_side_solar_reflectance_at_normal_incidence.setter
    def back_side_solar_reflectance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Back Side Solar Reflectance at Normal
        Incidence`"""
        self["Back Side Solar Reflectance at Normal Incidence"] = value

    @property
    def visible_transmittance_at_normal_incidence(self):
        """field `Visible Transmittance at Normal Incidence`

        |  Used only when Optical Data Type = SpectralAverage
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Visible Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_transmittance_at_normal_incidence` or None if not set

        """
        return self["Visible Transmittance at Normal Incidence"]

    @visible_transmittance_at_normal_incidence.setter
    def visible_transmittance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Visible Transmittance at Normal
        Incidence`"""
        self["Visible Transmittance at Normal Incidence"] = value

    @property
    def front_side_visible_reflectance_at_normal_incidence(self):
        """field `Front Side Visible Reflectance at Normal Incidence`

        |  Used only when Optical Data Type = SpectralAverage
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Visible Reflectance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_visible_reflectance_at_normal_incidence` or None if not set

        """
        return self["Front Side Visible Reflectance at Normal Incidence"]

    @front_side_visible_reflectance_at_normal_incidence.setter
    def front_side_visible_reflectance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Front Side Visible Reflectance at Normal
        Incidence`"""
        self["Front Side Visible Reflectance at Normal Incidence"] = value

    @property
    def back_side_visible_reflectance_at_normal_incidence(self):
        """field `Back Side Visible Reflectance at Normal Incidence`

        |  Used only when Optical Data Type = SpectralAverage
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Visible Reflectance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_visible_reflectance_at_normal_incidence` or None if not set

        """
        return self["Back Side Visible Reflectance at Normal Incidence"]

    @back_side_visible_reflectance_at_normal_incidence.setter
    def back_side_visible_reflectance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Back Side Visible Reflectance at Normal
        Incidence`"""
        self["Back Side Visible Reflectance at Normal Incidence"] = value

    @property
    def infrared_transmittance_at_normal_incidence(self):
        """field `Infrared Transmittance at Normal Incidence`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Infrared Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `infrared_transmittance_at_normal_incidence` or None if not set

        """
        return self["Infrared Transmittance at Normal Incidence"]

    @infrared_transmittance_at_normal_incidence.setter
    def infrared_transmittance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Infrared Transmittance at Normal
        Incidence`"""
        self["Infrared Transmittance at Normal Incidence"] = value

    @property
    def front_side_infrared_hemispherical_emissivity(self):
        """field `Front Side Infrared Hemispherical Emissivity`

        |  Default value: 0.84
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Infrared Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_infrared_hemispherical_emissivity` or None if not set

        """
        return self["Front Side Infrared Hemispherical Emissivity"]

    @front_side_infrared_hemispherical_emissivity.setter
    def front_side_infrared_hemispherical_emissivity(self, value=0.84):
        """Corresponds to IDD field `Front Side Infrared Hemispherical
        Emissivity`"""
        self["Front Side Infrared Hemispherical Emissivity"] = value

    @property
    def back_side_infrared_hemispherical_emissivity(self):
        """field `Back Side Infrared Hemispherical Emissivity`

        |  Default value: 0.84
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Infrared Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_infrared_hemispherical_emissivity` or None if not set

        """
        return self["Back Side Infrared Hemispherical Emissivity"]

    @back_side_infrared_hemispherical_emissivity.setter
    def back_side_infrared_hemispherical_emissivity(self, value=0.84):
        """Corresponds to IDD field `Back Side Infrared Hemispherical
        Emissivity`"""
        self["Back Side Infrared Hemispherical Emissivity"] = value

    @property
    def conductivity(self):
        """field `Conductivity`

        |  Units: W/m-K
        |  Default value: 0.9

        Args:
            value (float): value for IDD Field `Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity` or None if not set

        """
        return self["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=0.9):
        """Corresponds to IDD field `Conductivity`"""
        self["Conductivity"] = value

    @property
    def dirt_correction_factor_for_solar_and_visible_transmittance(self):
        """field `Dirt Correction Factor for Solar and Visible Transmittance`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Dirt Correction Factor for Solar and Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dirt_correction_factor_for_solar_and_visible_transmittance` or None if not set

        """
        return self[
            "Dirt Correction Factor for Solar and Visible Transmittance"]

    @dirt_correction_factor_for_solar_and_visible_transmittance.setter
    def dirt_correction_factor_for_solar_and_visible_transmittance(
            self,
            value=1.0):
        """Corresponds to IDD field `Dirt Correction Factor for Solar and
        Visible Transmittance`"""
        self[
            "Dirt Correction Factor for Solar and Visible Transmittance"] = value

    @property
    def solar_diffusing(self):
        """field `Solar Diffusing`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Solar Diffusing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_diffusing` or None if not set

        """
        return self["Solar Diffusing"]

    @solar_diffusing.setter
    def solar_diffusing(self, value="No"):
        """Corresponds to IDD field `Solar Diffusing`"""
        self["Solar Diffusing"] = value

    @property
    def youngs_modulus(self):
        """field `Young's modulus`

        |  coefficient used for deflection calculations. Used only with complex
        |  fenestration when deflection model is set to TemperatureAndPressureInput
        |  Units: Pa
        |  Default value: 72000000000.0

        Args:
            value (float): value for IDD Field `Young's modulus`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `youngs_modulus` or None if not set

        """
        return self["Young's modulus"]

    @youngs_modulus.setter
    def youngs_modulus(self, value=72000000000.0):
        """Corresponds to IDD field `Young's modulus`"""
        self["Young's modulus"] = value

    @property
    def poissons_ratio(self):
        """field `Poisson's ratio`

        |  coefficient used for deflection calculations. Used only with complex
        |  fenestration when deflection model is set to TemperatureAndPressureInput
        |  Default value: 0.22
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Poisson's ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `poissons_ratio` or None if not set

        """
        return self["Poisson's ratio"]

    @poissons_ratio.setter
    def poissons_ratio(self, value=0.22):
        """Corresponds to IDD field `Poisson's ratio`"""
        self["Poisson's ratio"] = value




class WindowMaterialGlazingGroupThermochromic(DataObject):

    """ Corresponds to IDD object `WindowMaterial:GlazingGroup:Thermochromic`
        thermochromic glass at different temperatures
    """
    _schema = {'extensible-fields': OrderedDict([(u'optical data temperature 1',
                                                  {'name': u'Optical Data Temperature 1',
                                                   'pyname': u'optical_data_temperature_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'C'}),
                                                 (u'window material glazing name 1',
                                                  {'name': u'Window Material Glazing Name 1',
                                                   'pyname': u'window_material_glazing_name_1',
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
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 3,
               'name': u'WindowMaterial:GlazingGroup:Thermochromic',
               'pyname': u'WindowMaterialGlazingGroupThermochromic',
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

    def add_extensible(self,
                       optical_data_temperature_1=None,
                       window_material_glazing_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            optical_data_temperature_1 (float): value for IDD Field `Optical Data Temperature 1`
                Units: C
                IP-Units: F
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            window_material_glazing_name_1 (str): value for IDD Field `Window Material Glazing Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        optical_data_temperature_1 = self.check_value(
            "Optical Data Temperature 1",
            optical_data_temperature_1)
        vals.append(optical_data_temperature_1)
        window_material_glazing_name_1 = self.check_value(
            "Window Material Glazing Name 1",
            window_material_glazing_name_1)
        vals.append(window_material_glazing_name_1)
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




class WindowMaterialGlazingRefractionExtinctionMethod(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Glazing:RefractionExtinctionMethod`
        Glass material properties for Windows or Glass Doors
        Index of Refraction/Extinction Coefficient input method
        Not to be used for coated glass
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'solar index of refraction',
                                       {'name': u'Solar Index of Refraction',
                                        'pyname': u'solar_index_of_refraction',
                                        'minimum>': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'solar extinction coefficient',
                                       {'name': u'Solar Extinction Coefficient',
                                        'pyname': u'solar_extinction_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/m'}),
                                      (u'visible index of refraction',
                                       {'name': u'Visible Index of Refraction',
                                        'pyname': u'visible_index_of_refraction',
                                        'minimum>': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'visible extinction coefficient',
                                       {'name': u'Visible Extinction Coefficient',
                                        'pyname': u'visible_extinction_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/m'}),
                                      (u'infrared transmittance at normal incidence',
                                       {'name': u'Infrared Transmittance at Normal Incidence',
                                        'pyname': u'infrared_transmittance_at_normal_incidence',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'infrared hemispherical emissivity',
                                       {'name': u'Infrared Hemispherical Emissivity',
                                        'pyname': u'infrared_hemispherical_emissivity',
                                        'default': 0.84,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0}),
                                      (u'conductivity',
                                       {'name': u'Conductivity',
                                        'pyname': u'conductivity',
                                        'default': 0.9,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'dirt correction factor for solar and visible transmittance',
                                       {'name': u'Dirt Correction Factor for Solar and Visible Transmittance',
                                        'pyname': u'dirt_correction_factor_for_solar_and_visible_transmittance',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'solar diffusing',
                                       {'name': u'Solar Diffusing',
                                        'pyname': u'solar_diffusing',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'No',
                                                            u'Yes'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'WindowMaterial:Glazing:RefractionExtinctionMethod',
               'pyname': u'WindowMaterialGlazingRefractionExtinctionMethod',
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
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def solar_index_of_refraction(self):
        """field `Solar Index of Refraction`

        |  value > 1.0

        Args:
            value (float): value for IDD Field `Solar Index of Refraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_index_of_refraction` or None if not set

        """
        return self["Solar Index of Refraction"]

    @solar_index_of_refraction.setter
    def solar_index_of_refraction(self, value=None):
        """Corresponds to IDD field `Solar Index of Refraction`"""
        self["Solar Index of Refraction"] = value

    @property
    def solar_extinction_coefficient(self):
        """field `Solar Extinction Coefficient`

        |  Units: 1/m

        Args:
            value (float): value for IDD Field `Solar Extinction Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_extinction_coefficient` or None if not set

        """
        return self["Solar Extinction Coefficient"]

    @solar_extinction_coefficient.setter
    def solar_extinction_coefficient(self, value=None):
        """Corresponds to IDD field `Solar Extinction Coefficient`"""
        self["Solar Extinction Coefficient"] = value

    @property
    def visible_index_of_refraction(self):
        """field `Visible Index of Refraction`

        |  value > 1.0

        Args:
            value (float): value for IDD Field `Visible Index of Refraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_index_of_refraction` or None if not set

        """
        return self["Visible Index of Refraction"]

    @visible_index_of_refraction.setter
    def visible_index_of_refraction(self, value=None):
        """Corresponds to IDD field `Visible Index of Refraction`"""
        self["Visible Index of Refraction"] = value

    @property
    def visible_extinction_coefficient(self):
        """field `Visible Extinction Coefficient`

        |  Units: 1/m

        Args:
            value (float): value for IDD Field `Visible Extinction Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_extinction_coefficient` or None if not set

        """
        return self["Visible Extinction Coefficient"]

    @visible_extinction_coefficient.setter
    def visible_extinction_coefficient(self, value=None):
        """Corresponds to IDD field `Visible Extinction Coefficient`"""
        self["Visible Extinction Coefficient"] = value

    @property
    def infrared_transmittance_at_normal_incidence(self):
        """field `Infrared Transmittance at Normal Incidence`

        |  value < 1.0

        Args:
            value (float): value for IDD Field `Infrared Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `infrared_transmittance_at_normal_incidence` or None if not set

        """
        return self["Infrared Transmittance at Normal Incidence"]

    @infrared_transmittance_at_normal_incidence.setter
    def infrared_transmittance_at_normal_incidence(self, value=None):
        """Corresponds to IDD field `Infrared Transmittance at Normal
        Incidence`"""
        self["Infrared Transmittance at Normal Incidence"] = value

    @property
    def infrared_hemispherical_emissivity(self):
        """field `Infrared Hemispherical Emissivity`

        |  Emissivity of front and back side assumed equal
        |  Default value: 0.84
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Infrared Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `infrared_hemispherical_emissivity` or None if not set

        """
        return self["Infrared Hemispherical Emissivity"]

    @infrared_hemispherical_emissivity.setter
    def infrared_hemispherical_emissivity(self, value=0.84):
        """Corresponds to IDD field `Infrared Hemispherical Emissivity`"""
        self["Infrared Hemispherical Emissivity"] = value

    @property
    def conductivity(self):
        """field `Conductivity`

        |  Units: W/m-K
        |  Default value: 0.9

        Args:
            value (float): value for IDD Field `Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity` or None if not set

        """
        return self["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=0.9):
        """Corresponds to IDD field `Conductivity`"""
        self["Conductivity"] = value

    @property
    def dirt_correction_factor_for_solar_and_visible_transmittance(self):
        """field `Dirt Correction Factor for Solar and Visible Transmittance`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Dirt Correction Factor for Solar and Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dirt_correction_factor_for_solar_and_visible_transmittance` or None if not set

        """
        return self[
            "Dirt Correction Factor for Solar and Visible Transmittance"]

    @dirt_correction_factor_for_solar_and_visible_transmittance.setter
    def dirt_correction_factor_for_solar_and_visible_transmittance(
            self,
            value=1.0):
        """Corresponds to IDD field `Dirt Correction Factor for Solar and
        Visible Transmittance`"""
        self[
            "Dirt Correction Factor for Solar and Visible Transmittance"] = value

    @property
    def solar_diffusing(self):
        """field `Solar Diffusing`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Solar Diffusing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_diffusing` or None if not set

        """
        return self["Solar Diffusing"]

    @solar_diffusing.setter
    def solar_diffusing(self, value="No"):
        """Corresponds to IDD field `Solar Diffusing`"""
        self["Solar Diffusing"] = value




class WindowMaterialGas(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Gas`
        Gas material properties that are used in Windows or Glass Doors
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'gas type',
                                       {'name': u'Gas Type',
                                        'pyname': u'gas_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Air',
                                                            u'Argon',
                                                            u'Krypton',
                                                            u'Xenon',
                                                            u'Custom'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'conductivity coefficient a',
                                       {'name': u'Conductivity Coefficient A',
                                        'pyname': u'conductivity_coefficient_a',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'conductivity coefficient b',
                                       {'name': u'Conductivity Coefficient B',
                                        'pyname': u'conductivity_coefficient_b',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K2'}),
                                      (u'conductivity coefficient c',
                                       {'name': u'Conductivity Coefficient C',
                                        'pyname': u'conductivity_coefficient_c',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K3'}),
                                      (u'viscosity coefficient a',
                                       {'name': u'Viscosity Coefficient A',
                                        'pyname': u'viscosity_coefficient_a',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m-s'}),
                                      (u'viscosity coefficient b',
                                       {'name': u'Viscosity Coefficient B',
                                        'pyname': u'viscosity_coefficient_b',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m-s-K'}),
                                      (u'viscosity coefficient c',
                                       {'name': u'Viscosity Coefficient C',
                                        'pyname': u'viscosity_coefficient_c',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m-s-K2'}),
                                      (u'specific heat coefficient a',
                                       {'name': u'Specific Heat Coefficient A',
                                        'pyname': u'specific_heat_coefficient_a',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat coefficient b',
                                       {'name': u'Specific Heat Coefficient B',
                                        'pyname': u'specific_heat_coefficient_b',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K2'}),
                                      (u'specific heat coefficient c',
                                       {'name': u'Specific Heat Coefficient C',
                                        'pyname': u'specific_heat_coefficient_c',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K3'}),
                                      (u'molecular weight',
                                       {'name': u'Molecular Weight',
                                        'pyname': u'molecular_weight',
                                        'maximum': 200.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 20.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'g/mol'}),
                                      (u'specific heat ratio',
                                       {'name': u'Specific Heat Ratio',
                                        'pyname': u'specific_heat_ratio',
                                        'minimum>': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 3,
               'name': u'WindowMaterial:Gas',
               'pyname': u'WindowMaterialGas',
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
    def gas_type(self):
        """field `Gas Type`

        Args:
            value (str): value for IDD Field `Gas Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_type` or None if not set

        """
        return self["Gas Type"]

    @gas_type.setter
    def gas_type(self, value=None):
        """Corresponds to IDD field `Gas Type`"""
        self["Gas Type"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def conductivity_coefficient_a(self):
        """field `Conductivity Coefficient A`

        |  Used only if Gas Type = Custom
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Conductivity Coefficient A`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_coefficient_a` or None if not set

        """
        return self["Conductivity Coefficient A"]

    @conductivity_coefficient_a.setter
    def conductivity_coefficient_a(self, value=None):
        """Corresponds to IDD field `Conductivity Coefficient A`"""
        self["Conductivity Coefficient A"] = value

    @property
    def conductivity_coefficient_b(self):
        """field `Conductivity Coefficient B`

        |  Used only if Gas Type = Custom
        |  Units: W/m-K2

        Args:
            value (float): value for IDD Field `Conductivity Coefficient B`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_coefficient_b` or None if not set

        """
        return self["Conductivity Coefficient B"]

    @conductivity_coefficient_b.setter
    def conductivity_coefficient_b(self, value=None):
        """Corresponds to IDD field `Conductivity Coefficient B`"""
        self["Conductivity Coefficient B"] = value

    @property
    def conductivity_coefficient_c(self):
        """field `Conductivity Coefficient C`

        |  Used only if Gas Type = Custom
        |  Units: W/m-K3

        Args:
            value (float): value for IDD Field `Conductivity Coefficient C`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_coefficient_c` or None if not set

        """
        return self["Conductivity Coefficient C"]

    @conductivity_coefficient_c.setter
    def conductivity_coefficient_c(self, value=None):
        """Corresponds to IDD field `Conductivity Coefficient C`"""
        self["Conductivity Coefficient C"] = value

    @property
    def viscosity_coefficient_a(self):
        """field `Viscosity Coefficient A`

        |  Used only if Gas Type = Custom
        |  Units: kg/m-s

        Args:
            value (float): value for IDD Field `Viscosity Coefficient A`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `viscosity_coefficient_a` or None if not set

        """
        return self["Viscosity Coefficient A"]

    @viscosity_coefficient_a.setter
    def viscosity_coefficient_a(self, value=None):
        """Corresponds to IDD field `Viscosity Coefficient A`"""
        self["Viscosity Coefficient A"] = value

    @property
    def viscosity_coefficient_b(self):
        """field `Viscosity Coefficient B`

        |  Used only if Gas Type = Custom
        |  Units: kg/m-s-K

        Args:
            value (float): value for IDD Field `Viscosity Coefficient B`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `viscosity_coefficient_b` or None if not set

        """
        return self["Viscosity Coefficient B"]

    @viscosity_coefficient_b.setter
    def viscosity_coefficient_b(self, value=None):
        """Corresponds to IDD field `Viscosity Coefficient B`"""
        self["Viscosity Coefficient B"] = value

    @property
    def viscosity_coefficient_c(self):
        """field `Viscosity Coefficient C`

        |  Used only if Gas Type = Custom
        |  Units: kg/m-s-K2

        Args:
            value (float): value for IDD Field `Viscosity Coefficient C`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `viscosity_coefficient_c` or None if not set

        """
        return self["Viscosity Coefficient C"]

    @viscosity_coefficient_c.setter
    def viscosity_coefficient_c(self, value=None):
        """Corresponds to IDD field `Viscosity Coefficient C`"""
        self["Viscosity Coefficient C"] = value

    @property
    def specific_heat_coefficient_a(self):
        """field `Specific Heat Coefficient A`

        |  Used only if Gas Type = Custom
        |  Units: J/kg-K

        Args:
            value (float): value for IDD Field `Specific Heat Coefficient A`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_coefficient_a` or None if not set

        """
        return self["Specific Heat Coefficient A"]

    @specific_heat_coefficient_a.setter
    def specific_heat_coefficient_a(self, value=None):
        """Corresponds to IDD field `Specific Heat Coefficient A`"""
        self["Specific Heat Coefficient A"] = value

    @property
    def specific_heat_coefficient_b(self):
        """field `Specific Heat Coefficient B`

        |  Used only if Gas Type = Custom
        |  Units: J/kg-K2

        Args:
            value (float): value for IDD Field `Specific Heat Coefficient B`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_coefficient_b` or None if not set

        """
        return self["Specific Heat Coefficient B"]

    @specific_heat_coefficient_b.setter
    def specific_heat_coefficient_b(self, value=None):
        """Corresponds to IDD field `Specific Heat Coefficient B`"""
        self["Specific Heat Coefficient B"] = value

    @property
    def specific_heat_coefficient_c(self):
        """field `Specific Heat Coefficient C`

        |  Used only if Gas Type = Custom
        |  Units: J/kg-K3

        Args:
            value (float): value for IDD Field `Specific Heat Coefficient C`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_coefficient_c` or None if not set

        """
        return self["Specific Heat Coefficient C"]

    @specific_heat_coefficient_c.setter
    def specific_heat_coefficient_c(self, value=None):
        """Corresponds to IDD field `Specific Heat Coefficient C`"""
        self["Specific Heat Coefficient C"] = value

    @property
    def molecular_weight(self):
        """field `Molecular Weight`

        |  Used only if Gas Type = Custom
        |  Units: g/mol
        |  value >= 20.0
        |  value <= 200.0

        Args:
            value (float): value for IDD Field `Molecular Weight`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `molecular_weight` or None if not set

        """
        return self["Molecular Weight"]

    @molecular_weight.setter
    def molecular_weight(self, value=None):
        """Corresponds to IDD field `Molecular Weight`"""
        self["Molecular Weight"] = value

    @property
    def specific_heat_ratio(self):
        """field `Specific Heat Ratio`

        |  Used only if Gas Type = Custom
        |  value > 1.0

        Args:
            value (float): value for IDD Field `Specific Heat Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_ratio` or None if not set

        """
        return self["Specific Heat Ratio"]

    @specific_heat_ratio.setter
    def specific_heat_ratio(self, value=None):
        """Corresponds to IDD field `Specific Heat Ratio`"""
        self["Specific Heat Ratio"] = value




class WindowGapSupportPillar(DataObject):

    """ Corresponds to IDD object `WindowGap:SupportPillar`
        used to define pillar geometry for support pillars
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'spacing',
                                       {'name': u'Spacing',
                                        'pyname': u'spacing',
                                        'default': 0.04,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'radius',
                                       {'name': u'Radius',
                                        'pyname': u'radius',
                                        'default': 0.0004,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'WindowGap:SupportPillar',
               'pyname': u'WindowGapSupportPillar',
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
    def spacing(self):
        """field `Spacing`

        |  Units: m
        |  Default value: 0.04

        Args:
            value (float): value for IDD Field `Spacing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spacing` or None if not set

        """
        return self["Spacing"]

    @spacing.setter
    def spacing(self, value=0.04):
        """Corresponds to IDD field `Spacing`"""
        self["Spacing"] = value

    @property
    def radius(self):
        """field `Radius`

        |  Units: m
        |  Default value: 0.0004

        Args:
            value (float): value for IDD Field `Radius`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `radius` or None if not set

        """
        return self["Radius"]

    @radius.setter
    def radius(self, value=0.0004):
        """Corresponds to IDD field `Radius`"""
        self["Radius"] = value




class WindowGapDeflectionState(DataObject):

    """ Corresponds to IDD object `WindowGap:DeflectionState`
        Used to enter data describing deflection state of the gap. It is referenced from
        WindowMaterial:Gap object only and it is used only when deflection model is set to
        MeasuredDeflection, otherwise it is ignored.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'deflected thickness',
                                       {'name': u'Deflected Thickness',
                                        'pyname': u'deflected_thickness',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'initial temperature',
                                       {'name': u'Initial Temperature',
                                        'pyname': u'initial_temperature',
                                        'default': 25.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'initial pressure',
                                       {'name': u'Initial Pressure',
                                        'pyname': u'initial_pressure',
                                        'default': 101325.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'WindowGap:DeflectionState',
               'pyname': u'WindowGapDeflectionState',
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
    def deflected_thickness(self):
        """field `Deflected Thickness`

        |  If left blank will be considered that gap has no deflection.
        |  Units: m

        Args:
            value (float): value for IDD Field `Deflected Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `deflected_thickness` or None if not set

        """
        return self["Deflected Thickness"]

    @deflected_thickness.setter
    def deflected_thickness(self, value=None):
        """Corresponds to IDD field `Deflected Thickness`"""
        self["Deflected Thickness"] = value

    @property
    def initial_temperature(self):
        """field `Initial Temperature`

        |  Units: C
        |  Default value: 25.0

        Args:
            value (float): value for IDD Field `Initial Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_temperature` or None if not set

        """
        return self["Initial Temperature"]

    @initial_temperature.setter
    def initial_temperature(self, value=25.0):
        """Corresponds to IDD field `Initial Temperature`"""
        self["Initial Temperature"] = value

    @property
    def initial_pressure(self):
        """field `Initial Pressure`

        |  Units: Pa
        |  Default value: 101325.0

        Args:
            value (float): value for IDD Field `Initial Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_pressure` or None if not set

        """
        return self["Initial Pressure"]

    @initial_pressure.setter
    def initial_pressure(self, value=101325.0):
        """Corresponds to IDD field `Initial Pressure`"""
        self["Initial Pressure"] = value




class WindowMaterialGasMixture(DataObject):

    """ Corresponds to IDD object `WindowMaterial:GasMixture`
        Gas mixtures that are used in Windows or Glass Doors
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'number of gases in mixture',
                                       {'name': u'Number of Gases in Mixture',
                                        'pyname': u'number_of_gases_in_mixture',
                                        'maximum': 4,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'gas 1 type',
                                       {'name': u'Gas 1 Type',
                                        'pyname': u'gas_1_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Air',
                                                            u'Argon',
                                                            u'Krypton',
                                                            u'Xenon'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'gas 1 fraction',
                                       {'name': u'Gas 1 Fraction',
                                        'pyname': u'gas_1_fraction',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'gas 2 type',
                                       {'name': u'Gas 2 Type',
                                        'pyname': u'gas_2_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Air',
                                                            u'Argon',
                                                            u'Krypton',
                                                            u'Xenon'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'gas 2 fraction',
                                       {'name': u'Gas 2 Fraction',
                                        'pyname': u'gas_2_fraction',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'gas 3 type',
                                       {'name': u'Gas 3 Type',
                                        'pyname': u'gas_3_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Air',
                                                            u'Argon',
                                                            u'Krypton',
                                                            u'Xenon'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'gas 3 fraction',
                                       {'name': u'Gas 3 Fraction',
                                        'pyname': u'gas_3_fraction',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'gas 4 type',
                                       {'name': u'Gas 4 Type',
                                        'pyname': u'gas_4_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Air',
                                                            u'Argon',
                                                            u'Krypton',
                                                            u'Xenon'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'gas 4 fraction',
                                       {'name': u'Gas 4 Fraction',
                                        'pyname': u'gas_4_fraction',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 7,
               'name': u'WindowMaterial:GasMixture',
               'pyname': u'WindowMaterialGasMixture',
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
    def thickness(self):
        """field `Thickness`

        |  Units: m

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def number_of_gases_in_mixture(self):
        """field `Number of Gases in Mixture`

        |  value >= 1
        |  value <= 4

        Args:
            value (int): value for IDD Field `Number of Gases in Mixture`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_gases_in_mixture` or None if not set

        """
        return self["Number of Gases in Mixture"]

    @number_of_gases_in_mixture.setter
    def number_of_gases_in_mixture(self, value=None):
        """Corresponds to IDD field `Number of Gases in Mixture`"""
        self["Number of Gases in Mixture"] = value

    @property
    def gas_1_type(self):
        """field `Gas 1 Type`

        Args:
            value (str): value for IDD Field `Gas 1 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_1_type` or None if not set

        """
        return self["Gas 1 Type"]

    @gas_1_type.setter
    def gas_1_type(self, value=None):
        """Corresponds to IDD field `Gas 1 Type`"""
        self["Gas 1 Type"] = value

    @property
    def gas_1_fraction(self):
        """field `Gas 1 Fraction`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Gas 1 Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_1_fraction` or None if not set

        """
        return self["Gas 1 Fraction"]

    @gas_1_fraction.setter
    def gas_1_fraction(self, value=None):
        """Corresponds to IDD field `Gas 1 Fraction`"""
        self["Gas 1 Fraction"] = value

    @property
    def gas_2_type(self):
        """field `Gas 2 Type`

        Args:
            value (str): value for IDD Field `Gas 2 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_2_type` or None if not set

        """
        return self["Gas 2 Type"]

    @gas_2_type.setter
    def gas_2_type(self, value=None):
        """Corresponds to IDD field `Gas 2 Type`"""
        self["Gas 2 Type"] = value

    @property
    def gas_2_fraction(self):
        """field `Gas 2 Fraction`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Gas 2 Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_2_fraction` or None if not set

        """
        return self["Gas 2 Fraction"]

    @gas_2_fraction.setter
    def gas_2_fraction(self, value=None):
        """Corresponds to IDD field `Gas 2 Fraction`"""
        self["Gas 2 Fraction"] = value

    @property
    def gas_3_type(self):
        """field `Gas 3 Type`

        Args:
            value (str): value for IDD Field `Gas 3 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_3_type` or None if not set

        """
        return self["Gas 3 Type"]

    @gas_3_type.setter
    def gas_3_type(self, value=None):
        """Corresponds to IDD field `Gas 3 Type`"""
        self["Gas 3 Type"] = value

    @property
    def gas_3_fraction(self):
        """field `Gas 3 Fraction`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Gas 3 Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_3_fraction` or None if not set

        """
        return self["Gas 3 Fraction"]

    @gas_3_fraction.setter
    def gas_3_fraction(self, value=None):
        """Corresponds to IDD field `Gas 3 Fraction`"""
        self["Gas 3 Fraction"] = value

    @property
    def gas_4_type(self):
        """field `Gas 4 Type`

        Args:
            value (str): value for IDD Field `Gas 4 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_4_type` or None if not set

        """
        return self["Gas 4 Type"]

    @gas_4_type.setter
    def gas_4_type(self, value=None):
        """Corresponds to IDD field `Gas 4 Type`"""
        self["Gas 4 Type"] = value

    @property
    def gas_4_fraction(self):
        """field `Gas 4 Fraction`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Gas 4 Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_4_fraction` or None if not set

        """
        return self["Gas 4 Fraction"]

    @gas_4_fraction.setter
    def gas_4_fraction(self, value=None):
        """Corresponds to IDD field `Gas 4 Fraction`"""
        self["Gas 4 Fraction"] = value




class WindowMaterialGap(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Gap`
        Used to define the gap between two layers in a complex fenestration system, where the
        Construction:ComplexFenestrationState object is used. It is referenced as a layer in the
        Construction:ComplexFenestrationState object. It cannot be referenced as a layer from the
        Construction object.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'gas (or gas mixture)',
                                       {'name': u'Gas (or Gas Mixture)',
                                        'pyname': u'gas_or_gas_mixture',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pressure',
                                       {'name': u'Pressure',
                                        'pyname': u'pressure',
                                        'default': 101325.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'deflection state',
                                       {'name': u'Deflection State',
                                        'pyname': u'deflection_state',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'support pillar',
                                       {'name': u'Support Pillar',
                                        'pyname': u'support_pillar',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'WindowMaterial:Gap',
               'pyname': u'WindowMaterialGap',
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
    def thickness(self):
        """field `Thickness`

        |  Units: m

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def gas_or_gas_mixture(self):
        """field `Gas (or Gas Mixture)`

        |  This field should reference only WindowMaterial:Gas
        |  or WindowMaterial:GasMixture objects

        Args:
            value (str): value for IDD Field `Gas (or Gas Mixture)`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_or_gas_mixture` or None if not set

        """
        return self["Gas (or Gas Mixture)"]

    @gas_or_gas_mixture.setter
    def gas_or_gas_mixture(self, value=None):
        """Corresponds to IDD field `Gas (or Gas Mixture)`"""
        self["Gas (or Gas Mixture)"] = value

    @property
    def pressure(self):
        """field `Pressure`

        |  Units: Pa
        |  Default value: 101325.0

        Args:
            value (float): value for IDD Field `Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pressure` or None if not set

        """
        return self["Pressure"]

    @pressure.setter
    def pressure(self, value=101325.0):
        """Corresponds to IDD field `Pressure`"""
        self["Pressure"] = value

    @property
    def deflection_state(self):
        """field `Deflection State`

        |  If left blank, it will be considered that gap is not deflected

        Args:
            value (str): value for IDD Field `Deflection State`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `deflection_state` or None if not set

        """
        return self["Deflection State"]

    @deflection_state.setter
    def deflection_state(self, value=None):
        """Corresponds to IDD field `Deflection State`"""
        self["Deflection State"] = value

    @property
    def support_pillar(self):
        """field `Support Pillar`

        |  If left blank, it will be considered that gap does not have
        |  support pillars

        Args:
            value (str): value for IDD Field `Support Pillar`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `support_pillar` or None if not set

        """
        return self["Support Pillar"]

    @support_pillar.setter
    def support_pillar(self, value=None):
        """Corresponds to IDD field `Support Pillar`"""
        self["Support Pillar"] = value




class WindowMaterialShade(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Shade`
        Specifies the properties of window shade materials. Reflectance and emissivity
        properties are assumed to be the same on both sides of the shade. Shades are considered
        to be perfect diffusers (all transmitted and reflected radiation is
        hemispherically-diffuse) independent of angle of incidence.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'solar transmittance',
                                       {'name': u'Solar Transmittance',
                                        'pyname': u'solar_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'solar reflectance',
                                       {'name': u'Solar Reflectance',
                                        'pyname': u'solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'visible transmittance',
                                       {'name': u'Visible Transmittance',
                                        'pyname': u'visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'visible reflectance',
                                       {'name': u'Visible Reflectance',
                                        'pyname': u'visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'infrared hemispherical emissivity',
                                       {'name': u'Infrared Hemispherical Emissivity',
                                        'pyname': u'infrared_hemispherical_emissivity',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'infrared transmittance',
                                       {'name': u'Infrared Transmittance',
                                        'pyname': u'infrared_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'conductivity',
                                       {'name': u'Conductivity',
                                        'pyname': u'conductivity',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'shade to glass distance',
                                       {'name': u'Shade to Glass Distance',
                                        'pyname': u'shade_to_glass_distance',
                                        'default': 0.05,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.001,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'top opening multiplier',
                                       {'name': u'Top Opening Multiplier',
                                        'pyname': u'top_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'bottom opening multiplier',
                                       {'name': u'Bottom Opening Multiplier',
                                        'pyname': u'bottom_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'left-side opening multiplier',
                                       {'name': u'Left-Side Opening Multiplier',
                                        'pyname': u'leftside_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'right-side opening multiplier',
                                       {'name': u'Right-Side Opening Multiplier',
                                        'pyname': u'rightside_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'airflow permeability',
                                       {'name': u'Airflow Permeability',
                                        'pyname': u'airflow_permeability',
                                        'default': 0.0,
                                        'maximum': 0.8,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 15,
               'name': u'WindowMaterial:Shade',
               'pyname': u'WindowMaterialShade',
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
    def solar_transmittance(self):
        """field `Solar Transmittance`

        |  Assumed independent of incidence angle
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_transmittance` or None if not set

        """
        return self["Solar Transmittance"]

    @solar_transmittance.setter
    def solar_transmittance(self, value=None):
        """Corresponds to IDD field `Solar Transmittance`"""
        self["Solar Transmittance"] = value

    @property
    def solar_reflectance(self):
        """field `Solar Reflectance`

        |  Assumed same for both sides
        |  Assumed independent of incidence angle
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_reflectance` or None if not set

        """
        return self["Solar Reflectance"]

    @solar_reflectance.setter
    def solar_reflectance(self, value=None):
        """Corresponds to IDD field `Solar Reflectance`"""
        self["Solar Reflectance"] = value

    @property
    def visible_transmittance(self):
        """field `Visible Transmittance`

        |  Assumed independent of incidence angle
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_transmittance` or None if not set

        """
        return self["Visible Transmittance"]

    @visible_transmittance.setter
    def visible_transmittance(self, value=None):
        """Corresponds to IDD field `Visible Transmittance`"""
        self["Visible Transmittance"] = value

    @property
    def visible_reflectance(self):
        """field `Visible Reflectance`

        |  Assumed same for both sides
        |  Assumed independent of incidence angle
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `visible_reflectance` or None if not set

        """
        return self["Visible Reflectance"]

    @visible_reflectance.setter
    def visible_reflectance(self, value=None):
        """Corresponds to IDD field `Visible Reflectance`"""
        self["Visible Reflectance"] = value

    @property
    def infrared_hemispherical_emissivity(self):
        """field `Infrared Hemispherical Emissivity`

        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Infrared Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `infrared_hemispherical_emissivity` or None if not set

        """
        return self["Infrared Hemispherical Emissivity"]

    @infrared_hemispherical_emissivity.setter
    def infrared_hemispherical_emissivity(self, value=None):
        """Corresponds to IDD field `Infrared Hemispherical Emissivity`"""
        self["Infrared Hemispherical Emissivity"] = value

    @property
    def infrared_transmittance(self):
        """field `Infrared Transmittance`

        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Infrared Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `infrared_transmittance` or None if not set

        """
        return self["Infrared Transmittance"]

    @infrared_transmittance.setter
    def infrared_transmittance(self, value=None):
        """Corresponds to IDD field `Infrared Transmittance`"""
        self["Infrared Transmittance"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def conductivity(self):
        """field `Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity` or None if not set

        """
        return self["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=None):
        """Corresponds to IDD field `Conductivity`"""
        self["Conductivity"] = value

    @property
    def shade_to_glass_distance(self):
        """field `Shade to Glass Distance`

        |  Units: m
        |  IP-Units: in
        |  Default value: 0.05
        |  value >= 0.001
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Shade to Glass Distance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shade_to_glass_distance` or None if not set

        """
        return self["Shade to Glass Distance"]

    @shade_to_glass_distance.setter
    def shade_to_glass_distance(self, value=0.05):
        """Corresponds to IDD field `Shade to Glass Distance`"""
        self["Shade to Glass Distance"] = value

    @property
    def top_opening_multiplier(self):
        """field `Top Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Top Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `top_opening_multiplier` or None if not set

        """
        return self["Top Opening Multiplier"]

    @top_opening_multiplier.setter
    def top_opening_multiplier(self, value=0.5):
        """Corresponds to IDD field `Top Opening Multiplier`"""
        self["Top Opening Multiplier"] = value

    @property
    def bottom_opening_multiplier(self):
        """field `Bottom Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Bottom Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `bottom_opening_multiplier` or None if not set

        """
        return self["Bottom Opening Multiplier"]

    @bottom_opening_multiplier.setter
    def bottom_opening_multiplier(self, value=0.5):
        """Corresponds to IDD field `Bottom Opening Multiplier`"""
        self["Bottom Opening Multiplier"] = value

    @property
    def leftside_opening_multiplier(self):
        """field `Left-Side Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Left-Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `leftside_opening_multiplier` or None if not set
        """
        return self["Left-Side Opening Multiplier"]

    @leftside_opening_multiplier.setter
    def leftside_opening_multiplier(self, value=0.5):
        """  Corresponds to IDD field `Left-Side Opening Multiplier`

        """
        self["Left-Side Opening Multiplier"] = value

    @property
    def rightside_opening_multiplier(self):
        """field `Right-Side Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Right-Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rightside_opening_multiplier` or None if not set
        """
        return self["Right-Side Opening Multiplier"]

    @rightside_opening_multiplier.setter
    def rightside_opening_multiplier(self, value=0.5):
        """  Corresponds to IDD field `Right-Side Opening Multiplier`

        """
        self["Right-Side Opening Multiplier"] = value

    @property
    def airflow_permeability(self):
        """field `Airflow Permeability`

        |  Units: dimensionless
        |  value <= 0.8

        Args:
            value (float): value for IDD Field `Airflow Permeability`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `airflow_permeability` or None if not set

        """
        return self["Airflow Permeability"]

    @airflow_permeability.setter
    def airflow_permeability(self, value=None):
        """Corresponds to IDD field `Airflow Permeability`"""
        self["Airflow Permeability"] = value




class WindowMaterialComplexShade(DataObject):

    """ Corresponds to IDD object `WindowMaterial:ComplexShade`
        Complex window shading layer thermal properties
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'layer type',
                                       {'name': u'Layer Type',
                                        'pyname': u'layer_type',
                                        'default': u'OtherShadingType',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Venetian',
                                                            u'Woven',
                                                            u'Perforated',
                                                            u'BSDF',
                                                            u'OtherShadingType'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'default': 0.002,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'conductivity',
                                       {'name': u'Conductivity',
                                        'pyname': u'conductivity',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'ir transmittance',
                                       {'name': u'IR Transmittance',
                                        'pyname': u'ir_transmittance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front emissivity',
                                       {'name': u'Front Emissivity',
                                        'pyname': u'front_emissivity',
                                        'default': 0.84,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back emissivity',
                                       {'name': u'Back Emissivity',
                                        'pyname': u'back_emissivity',
                                        'default': 0.84,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'top opening multiplier',
                                       {'name': u'Top Opening Multiplier',
                                        'pyname': u'top_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'bottom opening multiplier',
                                       {'name': u'Bottom Opening Multiplier',
                                        'pyname': u'bottom_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'left side opening multiplier',
                                       {'name': u'Left Side Opening Multiplier',
                                        'pyname': u'left_side_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'right side opening multiplier',
                                       {'name': u'Right Side Opening Multiplier',
                                        'pyname': u'right_side_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front opening multiplier',
                                       {'name': u'Front Opening Multiplier',
                                        'pyname': u'front_opening_multiplier',
                                        'default': 0.05,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'slat width',
                                       {'name': u'Slat Width',
                                        'pyname': u'slat_width',
                                        'default': 0.016,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat spacing',
                                       {'name': u'Slat Spacing',
                                        'pyname': u'slat_spacing',
                                        'default': 0.012,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat thickness',
                                       {'name': u'Slat Thickness',
                                        'pyname': u'slat_thickness',
                                        'default': 0.0006,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat angle',
                                       {'name': u'Slat Angle',
                                        'pyname': u'slat_angle',
                                        'default': 90.0,
                                        'maximum': 90.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -90.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'slat conductivity',
                                       {'name': u'Slat Conductivity',
                                        'pyname': u'slat_conductivity',
                                        'default': 160.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'slat curve',
                                       {'name': u'Slat Curve',
                                        'pyname': u'slat_curve',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 12,
               'name': u'WindowMaterial:ComplexShade',
               'pyname': u'WindowMaterialComplexShade',
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
    def layer_type(self):
        """field `Layer Type`

        |  Default value: OtherShadingType

        Args:
            value (str): value for IDD Field `Layer Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_type` or None if not set

        """
        return self["Layer Type"]

    @layer_type.setter
    def layer_type(self, value="OtherShadingType"):
        """Corresponds to IDD field `Layer Type`"""
        self["Layer Type"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  Default value: 0.002

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=0.002):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def conductivity(self):
        """field `Conductivity`

        |  Units: W/m-K
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity` or None if not set

        """
        return self["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=1.0):
        """Corresponds to IDD field `Conductivity`"""
        self["Conductivity"] = value

    @property
    def ir_transmittance(self):
        """field `IR Transmittance`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `IR Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ir_transmittance` or None if not set

        """
        return self["IR Transmittance"]

    @ir_transmittance.setter
    def ir_transmittance(self, value=None):
        """Corresponds to IDD field `IR Transmittance`"""
        self["IR Transmittance"] = value

    @property
    def front_emissivity(self):
        """field `Front Emissivity`

        |  Default value: 0.84
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_emissivity` or None if not set

        """
        return self["Front Emissivity"]

    @front_emissivity.setter
    def front_emissivity(self, value=0.84):
        """Corresponds to IDD field `Front Emissivity`"""
        self["Front Emissivity"] = value

    @property
    def back_emissivity(self):
        """field `Back Emissivity`

        |  Default value: 0.84
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_emissivity` or None if not set

        """
        return self["Back Emissivity"]

    @back_emissivity.setter
    def back_emissivity(self, value=0.84):
        """Corresponds to IDD field `Back Emissivity`"""
        self["Back Emissivity"] = value

    @property
    def top_opening_multiplier(self):
        """field `Top Opening Multiplier`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Top Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `top_opening_multiplier` or None if not set

        """
        return self["Top Opening Multiplier"]

    @top_opening_multiplier.setter
    def top_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Top Opening Multiplier`"""
        self["Top Opening Multiplier"] = value

    @property
    def bottom_opening_multiplier(self):
        """field `Bottom Opening Multiplier`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Bottom Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `bottom_opening_multiplier` or None if not set

        """
        return self["Bottom Opening Multiplier"]

    @bottom_opening_multiplier.setter
    def bottom_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Bottom Opening Multiplier`"""
        self["Bottom Opening Multiplier"] = value

    @property
    def left_side_opening_multiplier(self):
        """field `Left Side Opening Multiplier`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Left Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `left_side_opening_multiplier` or None if not set

        """
        return self["Left Side Opening Multiplier"]

    @left_side_opening_multiplier.setter
    def left_side_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Left Side Opening Multiplier`"""
        self["Left Side Opening Multiplier"] = value

    @property
    def right_side_opening_multiplier(self):
        """field `Right Side Opening Multiplier`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Right Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `right_side_opening_multiplier` or None if not set

        """
        return self["Right Side Opening Multiplier"]

    @right_side_opening_multiplier.setter
    def right_side_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Right Side Opening Multiplier`"""
        self["Right Side Opening Multiplier"] = value

    @property
    def front_opening_multiplier(self):
        """field `Front Opening Multiplier`

        |  Default value: 0.05
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_opening_multiplier` or None if not set

        """
        return self["Front Opening Multiplier"]

    @front_opening_multiplier.setter
    def front_opening_multiplier(self, value=0.05):
        """Corresponds to IDD field `Front Opening Multiplier`"""
        self["Front Opening Multiplier"] = value

    @property
    def slat_width(self):
        """field `Slat Width`

        |  Units: m
        |  Default value: 0.016

        Args:
            value (float): value for IDD Field `Slat Width`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_width` or None if not set

        """
        return self["Slat Width"]

    @slat_width.setter
    def slat_width(self, value=0.016):
        """Corresponds to IDD field `Slat Width`"""
        self["Slat Width"] = value

    @property
    def slat_spacing(self):
        """field `Slat Spacing`

        |  Distance between adjacent slat faces
        |  Units: m
        |  Default value: 0.012

        Args:
            value (float): value for IDD Field `Slat Spacing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_spacing` or None if not set

        """
        return self["Slat Spacing"]

    @slat_spacing.setter
    def slat_spacing(self, value=0.012):
        """Corresponds to IDD field `Slat Spacing`"""
        self["Slat Spacing"] = value

    @property
    def slat_thickness(self):
        """field `Slat Thickness`

        |  Distance between top and bottom surfaces of slat
        |  Slat is assumed to be rectangular in cross section and flat
        |  Units: m
        |  Default value: 0.0006

        Args:
            value (float): value for IDD Field `Slat Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_thickness` or None if not set

        """
        return self["Slat Thickness"]

    @slat_thickness.setter
    def slat_thickness(self, value=0.0006):
        """Corresponds to IDD field `Slat Thickness`"""
        self["Slat Thickness"] = value

    @property
    def slat_angle(self):
        """field `Slat Angle`

        |  Units: deg
        |  Default value: 90.0
        |  value >= -90.0
        |  value <= 90.0

        Args:
            value (float): value for IDD Field `Slat Angle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_angle` or None if not set

        """
        return self["Slat Angle"]

    @slat_angle.setter
    def slat_angle(self, value=90.0):
        """Corresponds to IDD field `Slat Angle`"""
        self["Slat Angle"] = value

    @property
    def slat_conductivity(self):
        """field `Slat Conductivity`

        |  Units: W/m-K
        |  Default value: 160.0

        Args:
            value (float): value for IDD Field `Slat Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_conductivity` or None if not set

        """
        return self["Slat Conductivity"]

    @slat_conductivity.setter
    def slat_conductivity(self, value=160.0):
        """Corresponds to IDD field `Slat Conductivity`"""
        self["Slat Conductivity"] = value

    @property
    def slat_curve(self):
        """field `Slat Curve`

        |  this value represents curvature radius of the slat.
        |  if the slat is flat use zero.
        |  if this value is not zero, then it must be > SlatWidth/2.
        |  Units: m

        Args:
            value (float): value for IDD Field `Slat Curve`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_curve` or None if not set

        """
        return self["Slat Curve"]

    @slat_curve.setter
    def slat_curve(self, value=None):
        """Corresponds to IDD field `Slat Curve`"""
        self["Slat Curve"] = value




class WindowMaterialBlind(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Blind`
        Window blind thermal properties
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'slat orientation',
                                       {'name': u'Slat Orientation',
                                        'pyname': u'slat_orientation',
                                        'default': u'Horizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Horizontal',
                                                            u'Vertical'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'slat width',
                                       {'name': u'Slat Width',
                                        'pyname': u'slat_width',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat separation',
                                       {'name': u'Slat Separation',
                                        'pyname': u'slat_separation',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat thickness',
                                       {'name': u'Slat Thickness',
                                        'pyname': u'slat_thickness',
                                        'default': 0.00025,
                                        'minimum>': 0.0,
                                        'maximum': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat angle',
                                       {'name': u'Slat Angle',
                                        'pyname': u'slat_angle',
                                        'default': 45.0,
                                        'maximum': 180.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'slat conductivity',
                                       {'name': u'Slat Conductivity',
                                        'pyname': u'slat_conductivity',
                                        'default': 221.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'slat beam solar transmittance',
                                       {'name': u'Slat Beam Solar Transmittance',
                                        'pyname': u'slat_beam_solar_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat beam solar reflectance',
                                       {'name': u'Front Side Slat Beam Solar Reflectance',
                                        'pyname': u'front_side_slat_beam_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side slat beam solar reflectance',
                                       {'name': u'Back Side Slat Beam Solar Reflectance',
                                        'pyname': u'back_side_slat_beam_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'slat diffuse solar transmittance',
                                       {'name': u'Slat Diffuse Solar Transmittance',
                                        'pyname': u'slat_diffuse_solar_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat diffuse solar reflectance',
                                       {'name': u'Front Side Slat Diffuse Solar Reflectance',
                                        'pyname': u'front_side_slat_diffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side slat diffuse solar reflectance',
                                       {'name': u'Back Side Slat Diffuse Solar Reflectance',
                                        'pyname': u'back_side_slat_diffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'slat beam visible transmittance',
                                       {'name': u'Slat Beam Visible Transmittance',
                                        'pyname': u'slat_beam_visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat beam visible reflectance',
                                       {'name': u'Front Side Slat Beam Visible Reflectance',
                                        'pyname': u'front_side_slat_beam_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side slat beam visible reflectance',
                                       {'name': u'Back Side Slat Beam Visible Reflectance',
                                        'pyname': u'back_side_slat_beam_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'slat diffuse visible transmittance',
                                       {'name': u'Slat Diffuse Visible Transmittance',
                                        'pyname': u'slat_diffuse_visible_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat diffuse visible reflectance',
                                       {'name': u'Front Side Slat Diffuse Visible Reflectance',
                                        'pyname': u'front_side_slat_diffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side slat diffuse visible reflectance',
                                       {'name': u'Back Side Slat Diffuse Visible Reflectance',
                                        'pyname': u'back_side_slat_diffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'slat infrared hemispherical transmittance',
                                       {'name': u'Slat Infrared Hemispherical Transmittance',
                                        'pyname': u'slat_infrared_hemispherical_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat infrared hemispherical emissivity',
                                       {'name': u'Front Side Slat Infrared Hemispherical Emissivity',
                                        'pyname': u'front_side_slat_infrared_hemispherical_emissivity',
                                        'default': 0.9,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side slat infrared hemispherical emissivity',
                                       {'name': u'Back Side Slat Infrared Hemispherical Emissivity',
                                        'pyname': u'back_side_slat_infrared_hemispherical_emissivity',
                                        'default': 0.9,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'blind to glass distance',
                                       {'name': u'Blind to Glass Distance',
                                        'pyname': u'blind_to_glass_distance',
                                        'default': 0.05,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.01,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'blind top opening multiplier',
                                       {'name': u'Blind Top Opening Multiplier',
                                        'pyname': u'blind_top_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'blind bottom opening multiplier',
                                       {'name': u'Blind Bottom Opening Multiplier',
                                        'pyname': u'blind_bottom_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'blind left side opening multiplier',
                                       {'name': u'Blind Left Side Opening Multiplier',
                                        'pyname': u'blind_left_side_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'blind right side opening multiplier',
                                       {'name': u'Blind Right Side Opening Multiplier',
                                        'pyname': u'blind_right_side_opening_multiplier',
                                        'default': 0.5,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum slat angle',
                                       {'name': u'Minimum Slat Angle',
                                        'pyname': u'minimum_slat_angle',
                                        'default': 0.0,
                                        'maximum': 180.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'maximum slat angle',
                                       {'name': u'Maximum Slat Angle',
                                        'pyname': u'maximum_slat_angle',
                                        'default': 180.0,
                                        'maximum': 180.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 29,
               'name': u'WindowMaterial:Blind',
               'pyname': u'WindowMaterialBlind',
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
    def slat_orientation(self):
        """field `Slat Orientation`

        |  Default value: Horizontal

        Args:
            value (str): value for IDD Field `Slat Orientation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slat_orientation` or None if not set

        """
        return self["Slat Orientation"]

    @slat_orientation.setter
    def slat_orientation(self, value="Horizontal"):
        """Corresponds to IDD field `Slat Orientation`"""
        self["Slat Orientation"] = value

    @property
    def slat_width(self):
        """field `Slat Width`

        |  Units: m
        |  IP-Units: in
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Slat Width`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_width` or None if not set

        """
        return self["Slat Width"]

    @slat_width.setter
    def slat_width(self, value=None):
        """Corresponds to IDD field `Slat Width`"""
        self["Slat Width"] = value

    @property
    def slat_separation(self):
        """field `Slat Separation`

        |  Distance between adjacent slat faces
        |  Units: m
        |  IP-Units: in
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Slat Separation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_separation` or None if not set

        """
        return self["Slat Separation"]

    @slat_separation.setter
    def slat_separation(self, value=None):
        """Corresponds to IDD field `Slat Separation`"""
        self["Slat Separation"] = value

    @property
    def slat_thickness(self):
        """field `Slat Thickness`

        |  Distance between top and bottom surfaces of slat
        |  Slat is assumed to be rectangular in cross section and flat
        |  Units: m
        |  IP-Units: in
        |  Default value: 0.00025
        |  value <= 0.1

        Args:
            value (float): value for IDD Field `Slat Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_thickness` or None if not set

        """
        return self["Slat Thickness"]

    @slat_thickness.setter
    def slat_thickness(self, value=0.00025):
        """Corresponds to IDD field `Slat Thickness`"""
        self["Slat Thickness"] = value

    @property
    def slat_angle(self):
        """field `Slat Angle`

        |  If WindowProperty:ShadingControl for the window that incorporates this blind
        |  has Type of Slat Angle Control for Blinds = FixedSlatAngle,
        |  then this is the fixed value of the slat angle;
        |  If WindowProperty:ShadingControl for the window that incorporates this blind
        |  has Type of Slat Angle Control for Blinds = BlockBeamSolar,
        |  then this is the slat angle when slat angle control
        |  is not in effect (e.g., when there is no beam solar on the blind);
        |  Not used if WindowProperty:ShadingControl for the window that incorporates this blind
        |  has Type of Slat Angle Control for Blinds = ScheduledSlatAngle.
        |  Units: deg
        |  Default value: 45.0
        |  value <= 180.0

        Args:
            value (float): value for IDD Field `Slat Angle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_angle` or None if not set

        """
        return self["Slat Angle"]

    @slat_angle.setter
    def slat_angle(self, value=45.0):
        """Corresponds to IDD field `Slat Angle`"""
        self["Slat Angle"] = value

    @property
    def slat_conductivity(self):
        """field `Slat Conductivity`

        |  default is for aluminum
        |  Units: W/m-K
        |  Default value: 221.0

        Args:
            value (float): value for IDD Field `Slat Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_conductivity` or None if not set

        """
        return self["Slat Conductivity"]

    @slat_conductivity.setter
    def slat_conductivity(self, value=221.0):
        """Corresponds to IDD field `Slat Conductivity`"""
        self["Slat Conductivity"] = value

    @property
    def slat_beam_solar_transmittance(self):
        """field `Slat Beam Solar Transmittance`

        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Beam Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_beam_solar_transmittance` or None if not set

        """
        return self["Slat Beam Solar Transmittance"]

    @slat_beam_solar_transmittance.setter
    def slat_beam_solar_transmittance(self, value=None):
        """Corresponds to IDD field `Slat Beam Solar Transmittance`"""
        self["Slat Beam Solar Transmittance"] = value

    @property
    def front_side_slat_beam_solar_reflectance(self):
        """field `Front Side Slat Beam Solar Reflectance`

        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Beam Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_beam_solar_reflectance` or None if not set

        """
        return self["Front Side Slat Beam Solar Reflectance"]

    @front_side_slat_beam_solar_reflectance.setter
    def front_side_slat_beam_solar_reflectance(self, value=None):
        """Corresponds to IDD field `Front Side Slat Beam Solar Reflectance`"""
        self["Front Side Slat Beam Solar Reflectance"] = value

    @property
    def back_side_slat_beam_solar_reflectance(self):
        """field `Back Side Slat Beam Solar Reflectance`

        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Beam Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_beam_solar_reflectance` or None if not set

        """
        return self["Back Side Slat Beam Solar Reflectance"]

    @back_side_slat_beam_solar_reflectance.setter
    def back_side_slat_beam_solar_reflectance(self, value=None):
        """Corresponds to IDD field `Back Side Slat Beam Solar Reflectance`"""
        self["Back Side Slat Beam Solar Reflectance"] = value

    @property
    def slat_diffuse_solar_transmittance(self):
        """field `Slat Diffuse Solar Transmittance`

        |  Must equal "Slat beam solar transmittance"
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_diffuse_solar_transmittance` or None if not set

        """
        return self["Slat Diffuse Solar Transmittance"]

    @slat_diffuse_solar_transmittance.setter
    def slat_diffuse_solar_transmittance(self, value=None):
        """Corresponds to IDD field `Slat Diffuse Solar Transmittance`"""
        self["Slat Diffuse Solar Transmittance"] = value

    @property
    def front_side_slat_diffuse_solar_reflectance(self):
        """field `Front Side Slat Diffuse Solar Reflectance`

        |  Must equal "Front Side Slat Beam Solar Reflectance"
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_diffuse_solar_reflectance` or None if not set

        """
        return self["Front Side Slat Diffuse Solar Reflectance"]

    @front_side_slat_diffuse_solar_reflectance.setter
    def front_side_slat_diffuse_solar_reflectance(self, value=None):
        """Corresponds to IDD field `Front Side Slat Diffuse Solar
        Reflectance`"""
        self["Front Side Slat Diffuse Solar Reflectance"] = value

    @property
    def back_side_slat_diffuse_solar_reflectance(self):
        """field `Back Side Slat Diffuse Solar Reflectance`

        |  Must equal "Back Side Slat Beam Solar Reflectance"
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_diffuse_solar_reflectance` or None if not set

        """
        return self["Back Side Slat Diffuse Solar Reflectance"]

    @back_side_slat_diffuse_solar_reflectance.setter
    def back_side_slat_diffuse_solar_reflectance(self, value=None):
        """Corresponds to IDD field `Back Side Slat Diffuse Solar
        Reflectance`"""
        self["Back Side Slat Diffuse Solar Reflectance"] = value

    @property
    def slat_beam_visible_transmittance(self):
        """field `Slat Beam Visible Transmittance`

        |  Required for detailed daylighting calculation
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Beam Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_beam_visible_transmittance` or None if not set

        """
        return self["Slat Beam Visible Transmittance"]

    @slat_beam_visible_transmittance.setter
    def slat_beam_visible_transmittance(self, value=None):
        """Corresponds to IDD field `Slat Beam Visible Transmittance`"""
        self["Slat Beam Visible Transmittance"] = value

    @property
    def front_side_slat_beam_visible_reflectance(self):
        """field `Front Side Slat Beam Visible Reflectance`

        |  Required for detailed daylighting calculation
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Beam Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_beam_visible_reflectance` or None if not set

        """
        return self["Front Side Slat Beam Visible Reflectance"]

    @front_side_slat_beam_visible_reflectance.setter
    def front_side_slat_beam_visible_reflectance(self, value=None):
        """Corresponds to IDD field `Front Side Slat Beam Visible
        Reflectance`"""
        self["Front Side Slat Beam Visible Reflectance"] = value

    @property
    def back_side_slat_beam_visible_reflectance(self):
        """field `Back Side Slat Beam Visible Reflectance`

        |  Required for detailed daylighting calculation
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Beam Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_beam_visible_reflectance` or None if not set

        """
        return self["Back Side Slat Beam Visible Reflectance"]

    @back_side_slat_beam_visible_reflectance.setter
    def back_side_slat_beam_visible_reflectance(self, value=None):
        """Corresponds to IDD field `Back Side Slat Beam Visible
        Reflectance`"""
        self["Back Side Slat Beam Visible Reflectance"] = value

    @property
    def slat_diffuse_visible_transmittance(self):
        """field `Slat Diffuse Visible Transmittance`

        |  Used only for detailed daylighting calculation
        |  Must equal "Slat Beam Visible Transmittance"
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Diffuse Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_diffuse_visible_transmittance` or None if not set

        """
        return self["Slat Diffuse Visible Transmittance"]

    @slat_diffuse_visible_transmittance.setter
    def slat_diffuse_visible_transmittance(self, value=None):
        """Corresponds to IDD field `Slat Diffuse Visible Transmittance`"""
        self["Slat Diffuse Visible Transmittance"] = value

    @property
    def front_side_slat_diffuse_visible_reflectance(self):
        """field `Front Side Slat Diffuse Visible Reflectance`

        |  Required for detailed daylighting calculation
        |  Must equal "Front Side Slat Beam Visible Reflectance"
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_diffuse_visible_reflectance` or None if not set

        """
        return self["Front Side Slat Diffuse Visible Reflectance"]

    @front_side_slat_diffuse_visible_reflectance.setter
    def front_side_slat_diffuse_visible_reflectance(self, value=None):
        """Corresponds to IDD field `Front Side Slat Diffuse Visible
        Reflectance`"""
        self["Front Side Slat Diffuse Visible Reflectance"] = value

    @property
    def back_side_slat_diffuse_visible_reflectance(self):
        """field `Back Side Slat Diffuse Visible Reflectance`

        |  Required for detailed daylighting calculation
        |  Must equal "Back Side Slat Beam Visible Reflectance"
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_diffuse_visible_reflectance` or None if not set

        """
        return self["Back Side Slat Diffuse Visible Reflectance"]

    @back_side_slat_diffuse_visible_reflectance.setter
    def back_side_slat_diffuse_visible_reflectance(self, value=None):
        """Corresponds to IDD field `Back Side Slat Diffuse Visible
        Reflectance`"""
        self["Back Side Slat Diffuse Visible Reflectance"] = value

    @property
    def slat_infrared_hemispherical_transmittance(self):
        """field `Slat Infrared Hemispherical Transmittance`

        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Infrared Hemispherical Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_infrared_hemispherical_transmittance` or None if not set

        """
        return self["Slat Infrared Hemispherical Transmittance"]

    @slat_infrared_hemispherical_transmittance.setter
    def slat_infrared_hemispherical_transmittance(self, value=None):
        """Corresponds to IDD field `Slat Infrared Hemispherical
        Transmittance`"""
        self["Slat Infrared Hemispherical Transmittance"] = value

    @property
    def front_side_slat_infrared_hemispherical_emissivity(self):
        """field `Front Side Slat Infrared Hemispherical Emissivity`

        |  Default value: 0.9
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Infrared Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_infrared_hemispherical_emissivity` or None if not set

        """
        return self["Front Side Slat Infrared Hemispherical Emissivity"]

    @front_side_slat_infrared_hemispherical_emissivity.setter
    def front_side_slat_infrared_hemispherical_emissivity(self, value=0.9):
        """Corresponds to IDD field `Front Side Slat Infrared Hemispherical
        Emissivity`"""
        self["Front Side Slat Infrared Hemispherical Emissivity"] = value

    @property
    def back_side_slat_infrared_hemispherical_emissivity(self):
        """field `Back Side Slat Infrared Hemispherical Emissivity`

        |  Default value: 0.9
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Infrared Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_infrared_hemispherical_emissivity` or None if not set

        """
        return self["Back Side Slat Infrared Hemispherical Emissivity"]

    @back_side_slat_infrared_hemispherical_emissivity.setter
    def back_side_slat_infrared_hemispherical_emissivity(self, value=0.9):
        """Corresponds to IDD field `Back Side Slat Infrared Hemispherical
        Emissivity`"""
        self["Back Side Slat Infrared Hemispherical Emissivity"] = value

    @property
    def blind_to_glass_distance(self):
        """field `Blind to Glass Distance`

        |  Units: m
        |  IP-Units: in
        |  Default value: 0.05
        |  value >= 0.01
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Blind to Glass Distance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blind_to_glass_distance` or None if not set

        """
        return self["Blind to Glass Distance"]

    @blind_to_glass_distance.setter
    def blind_to_glass_distance(self, value=0.05):
        """Corresponds to IDD field `Blind to Glass Distance`"""
        self["Blind to Glass Distance"] = value

    @property
    def blind_top_opening_multiplier(self):
        """field `Blind Top Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Blind Top Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blind_top_opening_multiplier` or None if not set

        """
        return self["Blind Top Opening Multiplier"]

    @blind_top_opening_multiplier.setter
    def blind_top_opening_multiplier(self, value=0.5):
        """Corresponds to IDD field `Blind Top Opening Multiplier`"""
        self["Blind Top Opening Multiplier"] = value

    @property
    def blind_bottom_opening_multiplier(self):
        """field `Blind Bottom Opening Multiplier`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Blind Bottom Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blind_bottom_opening_multiplier` or None if not set

        """
        return self["Blind Bottom Opening Multiplier"]

    @blind_bottom_opening_multiplier.setter
    def blind_bottom_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Blind Bottom Opening Multiplier`"""
        self["Blind Bottom Opening Multiplier"] = value

    @property
    def blind_left_side_opening_multiplier(self):
        """field `Blind Left Side Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Blind Left Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blind_left_side_opening_multiplier` or None if not set

        """
        return self["Blind Left Side Opening Multiplier"]

    @blind_left_side_opening_multiplier.setter
    def blind_left_side_opening_multiplier(self, value=0.5):
        """Corresponds to IDD field `Blind Left Side Opening Multiplier`"""
        self["Blind Left Side Opening Multiplier"] = value

    @property
    def blind_right_side_opening_multiplier(self):
        """field `Blind Right Side Opening Multiplier`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Blind Right Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blind_right_side_opening_multiplier` or None if not set

        """
        return self["Blind Right Side Opening Multiplier"]

    @blind_right_side_opening_multiplier.setter
    def blind_right_side_opening_multiplier(self, value=0.5):
        """Corresponds to IDD field `Blind Right Side Opening Multiplier`"""
        self["Blind Right Side Opening Multiplier"] = value

    @property
    def minimum_slat_angle(self):
        """field `Minimum Slat Angle`

        |  Used only if WindowProperty:ShadingControl for the window that incorporates
        |  this blind varies the slat angle (i.e., WindowProperty:ShadingControl with
        |  Type of Slat Angle Control for Blinds = ScheduledSlatAngle
        |  or BlockBeamSolar)
        |  Units: deg
        |  value <= 180.0

        Args:
            value (float): value for IDD Field `Minimum Slat Angle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_slat_angle` or None if not set

        """
        return self["Minimum Slat Angle"]

    @minimum_slat_angle.setter
    def minimum_slat_angle(self, value=None):
        """Corresponds to IDD field `Minimum Slat Angle`"""
        self["Minimum Slat Angle"] = value

    @property
    def maximum_slat_angle(self):
        """field `Maximum Slat Angle`

        |  Used only if WindowProperty:ShadingControl for the window that incorporates
        |  this blind varies the slat angle (i.e., WindowProperty:ShadingControl with
        |  Type of Slat Angle Control for Blinds = ScheduledSlatAngle
        |  or BlockBeamSolar)
        |  Units: deg
        |  Default value: 180.0
        |  value <= 180.0

        Args:
            value (float): value for IDD Field `Maximum Slat Angle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_slat_angle` or None if not set

        """
        return self["Maximum Slat Angle"]

    @maximum_slat_angle.setter
    def maximum_slat_angle(self, value=180.0):
        """Corresponds to IDD field `Maximum Slat Angle`"""
        self["Maximum Slat Angle"] = value




class WindowMaterialScreen(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Screen`
        Window screen physical properties. Can only be located on the exterior side of a window construction.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'reflected beam transmittance accounting method',
                                       {'name': u'Reflected Beam Transmittance Accounting Method',
                                        'pyname': u'reflected_beam_transmittance_accounting_method',
                                        'default': u'ModelAsDiffuse',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DoNotModel',
                                                            u'ModelAsDirectBeam',
                                                            u'ModelAsDiffuse'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'diffuse solar reflectance',
                                       {'name': u'Diffuse Solar Reflectance',
                                        'pyname': u'diffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'diffuse visible reflectance',
                                       {'name': u'Diffuse Visible Reflectance',
                                        'pyname': u'diffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'thermal hemispherical emissivity',
                                       {'name': u'Thermal Hemispherical Emissivity',
                                        'pyname': u'thermal_hemispherical_emissivity',
                                        'default': 0.9,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'conductivity',
                                       {'name': u'Conductivity',
                                        'pyname': u'conductivity',
                                        'default': 221.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'screen material spacing',
                                       {'name': u'Screen Material Spacing',
                                        'pyname': u'screen_material_spacing',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'screen material diameter',
                                       {'name': u'Screen Material Diameter',
                                        'pyname': u'screen_material_diameter',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'screen to glass distance',
                                       {'name': u'Screen to Glass Distance',
                                        'pyname': u'screen_to_glass_distance',
                                        'default': 0.025,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.001,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'top opening multiplier',
                                       {'name': u'Top Opening Multiplier',
                                        'pyname': u'top_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'bottom opening multiplier',
                                       {'name': u'Bottom Opening Multiplier',
                                        'pyname': u'bottom_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'left side opening multiplier',
                                       {'name': u'Left Side Opening Multiplier',
                                        'pyname': u'left_side_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'right side opening multiplier',
                                       {'name': u'Right Side Opening Multiplier',
                                        'pyname': u'right_side_opening_multiplier',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'angle of resolution for screen transmittance output map',
                                       {'name': u'Angle of Resolution for Screen Transmittance Output Map',
                                        'pyname': u'angle_of_resolution_for_screen_transmittance_output_map',
                                        'default': 0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [0,
                                                            1,
                                                            2,
                                                            3,
                                                            5],
                                        'autocalculatable': False,
                                        'type': 'integer',
                                        'unit': u'deg'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 9,
               'name': u'WindowMaterial:Screen',
               'pyname': u'WindowMaterialScreen',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Enter a unique name for this window screen material.

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
    def reflected_beam_transmittance_accounting_method(self):
        """field `Reflected Beam Transmittance Accounting Method`

        |  Select the method used to account for the beam solar reflected off the material surface.
        |  Default value: ModelAsDiffuse

        Args:
            value (str): value for IDD Field `Reflected Beam Transmittance Accounting Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reflected_beam_transmittance_accounting_method` or None if not set

        """
        return self["Reflected Beam Transmittance Accounting Method"]

    @reflected_beam_transmittance_accounting_method.setter
    def reflected_beam_transmittance_accounting_method(
            self,
            value="ModelAsDiffuse"):
        """Corresponds to IDD field `Reflected Beam Transmittance Accounting
        Method`"""
        self["Reflected Beam Transmittance Accounting Method"] = value

    @property
    def diffuse_solar_reflectance(self):
        """field `Diffuse Solar Reflectance`

        |  Diffuse reflectance of the screen material over the entire solar radiation spectrum.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `diffuse_solar_reflectance` or None if not set

        """
        return self["Diffuse Solar Reflectance"]

    @diffuse_solar_reflectance.setter
    def diffuse_solar_reflectance(self, value=None):
        """Corresponds to IDD field `Diffuse Solar Reflectance`"""
        self["Diffuse Solar Reflectance"] = value

    @property
    def diffuse_visible_reflectance(self):
        """field `Diffuse Visible Reflectance`

        |  Diffuse visible reflectance of the screen material averaged over the solar spectrum
        |  and weighted by the response of the human eye.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `diffuse_visible_reflectance` or None if not set

        """
        return self["Diffuse Visible Reflectance"]

    @diffuse_visible_reflectance.setter
    def diffuse_visible_reflectance(self, value=None):
        """Corresponds to IDD field `Diffuse Visible Reflectance`"""
        self["Diffuse Visible Reflectance"] = value

    @property
    def thermal_hemispherical_emissivity(self):
        """field `Thermal Hemispherical Emissivity`

        |  Long-wave emissivity of the screen material.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  Default value: 0.9
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Thermal Hemispherical Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_hemispherical_emissivity` or None if not set

        """
        return self["Thermal Hemispherical Emissivity"]

    @thermal_hemispherical_emissivity.setter
    def thermal_hemispherical_emissivity(self, value=0.9):
        """Corresponds to IDD field `Thermal Hemispherical Emissivity`"""
        self["Thermal Hemispherical Emissivity"] = value

    @property
    def conductivity(self):
        """field `Conductivity`

        |  Thermal conductivity of the screen material.
        |  Default is for aluminum.
        |  Units: W/m-K
        |  Default value: 221.0

        Args:
            value (float): value for IDD Field `Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity` or None if not set

        """
        return self["Conductivity"]

    @conductivity.setter
    def conductivity(self, value=221.0):
        """Corresponds to IDD field `Conductivity`"""
        self["Conductivity"] = value

    @property
    def screen_material_spacing(self):
        """field `Screen Material Spacing`

        |  Spacing assumed to be the same in both directions.
        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Screen Material Spacing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_material_spacing` or None if not set

        """
        return self["Screen Material Spacing"]

    @screen_material_spacing.setter
    def screen_material_spacing(self, value=None):
        """Corresponds to IDD field `Screen Material Spacing`"""
        self["Screen Material Spacing"] = value

    @property
    def screen_material_diameter(self):
        """field `Screen Material Diameter`

        |  Diameter assumed to be the same in both directions.
        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Screen Material Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_material_diameter` or None if not set

        """
        return self["Screen Material Diameter"]

    @screen_material_diameter.setter
    def screen_material_diameter(self, value=None):
        """Corresponds to IDD field `Screen Material Diameter`"""
        self["Screen Material Diameter"] = value

    @property
    def screen_to_glass_distance(self):
        """field `Screen to Glass Distance`

        |  Distance from the window screen to the adjacent glass surface.
        |  Units: m
        |  IP-Units: in
        |  Default value: 0.025
        |  value >= 0.001
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Screen to Glass Distance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_to_glass_distance` or None if not set

        """
        return self["Screen to Glass Distance"]

    @screen_to_glass_distance.setter
    def screen_to_glass_distance(self, value=0.025):
        """Corresponds to IDD field `Screen to Glass Distance`"""
        self["Screen to Glass Distance"] = value

    @property
    def top_opening_multiplier(self):
        """field `Top Opening Multiplier`

        |  Effective area for air flow at the top of the screen divided by the perpendicular
        |  area between the glass and the top of the screen.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Top Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `top_opening_multiplier` or None if not set

        """
        return self["Top Opening Multiplier"]

    @top_opening_multiplier.setter
    def top_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Top Opening Multiplier`"""
        self["Top Opening Multiplier"] = value

    @property
    def bottom_opening_multiplier(self):
        """field `Bottom Opening Multiplier`

        |  Effective area for air flow at the bottom of the screen divided by the perpendicular
        |  area between the glass and the bottom of the screen.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Bottom Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `bottom_opening_multiplier` or None if not set

        """
        return self["Bottom Opening Multiplier"]

    @bottom_opening_multiplier.setter
    def bottom_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Bottom Opening Multiplier`"""
        self["Bottom Opening Multiplier"] = value

    @property
    def left_side_opening_multiplier(self):
        """field `Left Side Opening Multiplier`

        |  Effective area for air flow at the left side of the screen divided by the perpendicular
        |  area between the glass and the left side of the screen.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Left Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `left_side_opening_multiplier` or None if not set

        """
        return self["Left Side Opening Multiplier"]

    @left_side_opening_multiplier.setter
    def left_side_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Left Side Opening Multiplier`"""
        self["Left Side Opening Multiplier"] = value

    @property
    def right_side_opening_multiplier(self):
        """field `Right Side Opening Multiplier`

        |  Effective area for air flow at the right side of the screen divided by the perpendicular
        |  area between the glass and the right side of the screen.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Right Side Opening Multiplier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `right_side_opening_multiplier` or None if not set

        """
        return self["Right Side Opening Multiplier"]

    @right_side_opening_multiplier.setter
    def right_side_opening_multiplier(self, value=None):
        """Corresponds to IDD field `Right Side Opening Multiplier`"""
        self["Right Side Opening Multiplier"] = value

    @property
    def angle_of_resolution_for_screen_transmittance_output_map(self):
        """field `Angle of Resolution for Screen Transmittance Output Map`

        |  Select the resolution of azimuth and altitude angles for the screen transmittance map.
        |  A value of 0 means no transmittance map will be generated.
        |  Valid values for this field are 0, 1, 2, 3 and 5.
        |  Units: deg

        Args:
            value (int): value for IDD Field `Angle of Resolution for Screen Transmittance Output Map`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `angle_of_resolution_for_screen_transmittance_output_map` or None if not set

        """
        return self["Angle of Resolution for Screen Transmittance Output Map"]

    @angle_of_resolution_for_screen_transmittance_output_map.setter
    def angle_of_resolution_for_screen_transmittance_output_map(
            self,
            value=None):
        """Corresponds to IDD field `Angle of Resolution for Screen
        Transmittance Output Map`"""
        self["Angle of Resolution for Screen Transmittance Output Map"] = value




class WindowMaterialShadeEquivalentLayer(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Shade:EquivalentLayer`
        Specifies the properties of equivalent layer window shade material
        Shades are considered to be perfect diffusers (all transmitted and
        reflected radiation is hemispherically-diffuse) independent of angle
        of incidence.  Shade represents roller blinds.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'shade beam-beam solar transmittance',
                                       {'name': u'Shade Beam-Beam Solar Transmittance',
                                        'pyname': u'shade_beambeam_solar_transmittance',
                                        'default': 0.0,
                                        'maximum': 0.8,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side shade beam-diffuse solar transmittance',
                                       {'name': u'Front Side Shade Beam-Diffuse Solar Transmittance',
                                        'pyname': u'front_side_shade_beamdiffuse_solar_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side shade beam-diffuse solar transmittance',
                                       {'name': u'Back Side Shade Beam-Diffuse Solar Transmittance',
                                        'pyname': u'back_side_shade_beamdiffuse_solar_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side shade beam-diffuse solar reflectance',
                                       {'name': u'Front Side Shade Beam-Diffuse Solar Reflectance',
                                        'pyname': u'front_side_shade_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side shade beam-diffuse solar reflectance',
                                       {'name': u'Back Side Shade Beam-Diffuse Solar Reflectance',
                                        'pyname': u'back_side_shade_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'shade beam-beam visible transmittance at normal incidence',
                                       {'name': u'Shade Beam-Beam Visible Transmittance at Normal Incidence',
                                        'pyname': u'shade_beambeam_visible_transmittance_at_normal_incidence',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'shade beam-diffuse visible transmittance at normal incidence',
                                       {'name': u'Shade Beam-Diffuse Visible Transmittance at Normal Incidence',
                                        'pyname': u'shade_beamdiffuse_visible_transmittance_at_normal_incidence',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'shade beam-diffuse visible reflectance at normal incidence',
                                       {'name': u'Shade Beam-Diffuse Visible Reflectance at Normal Incidence',
                                        'pyname': u'shade_beamdiffuse_visible_reflectance_at_normal_incidence',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'shade material infrared transmittance',
                                       {'name': u'Shade Material Infrared Transmittance',
                                        'pyname': u'shade_material_infrared_transmittance',
                                        'default': 0.05,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side shade material infrared emissivity',
                                       {'name': u'Front Side Shade Material Infrared Emissivity',
                                        'pyname': u'front_side_shade_material_infrared_emissivity',
                                        'default': 0.91,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'back side shade material infrared emissivity',
                                       {'name': u'Back Side Shade Material Infrared Emissivity',
                                        'pyname': u'back_side_shade_material_infrared_emissivity',
                                        'default': 0.91,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 6,
               'name': u'WindowMaterial:Shade:EquivalentLayer',
               'pyname': u'WindowMaterialShadeEquivalentLayer',
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
    def shade_beambeam_solar_transmittance(self):
        """field `Shade Beam-Beam Solar Transmittance`

        |  The beam-beam solar transmittance at normal incidence.  This value is
        |  the same as the openness area fraction of the shade material. Assumed
        |  to be the same for front and back sides.
        |  Units: dimensionless
        |  value <= 0.8

        Args:
            value (float): value for IDD Field `Shade Beam-Beam Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shade_beambeam_solar_transmittance` or None if not set
        """
        return self["Shade Beam-Beam Solar Transmittance"]

    @shade_beambeam_solar_transmittance.setter
    def shade_beambeam_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Shade Beam-Beam Solar Transmittance`

        """
        self["Shade Beam-Beam Solar Transmittance"] = value

    @property
    def front_side_shade_beamdiffuse_solar_transmittance(self):
        """field `Front Side Shade Beam-Diffuse Solar Transmittance`

        |  The front side beam-diffuse solar transmittance at normal incidence averaged
        |  over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Shade Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_shade_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Front Side Shade Beam-Diffuse Solar Transmittance"]

    @front_side_shade_beamdiffuse_solar_transmittance.setter
    def front_side_shade_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Shade Beam-Diffuse Solar Transmittance`

        """
        self["Front Side Shade Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_shade_beamdiffuse_solar_transmittance(self):
        """field `Back Side Shade Beam-Diffuse Solar Transmittance`

        |  The back side beam-diffuse solar transmittance at normal incidence averaged
        |  over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Shade Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_shade_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Back Side Shade Beam-Diffuse Solar Transmittance"]

    @back_side_shade_beamdiffuse_solar_transmittance.setter
    def back_side_shade_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Shade Beam-Diffuse Solar Transmittance`

        """
        self["Back Side Shade Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_shade_beamdiffuse_solar_reflectance(self):
        """field `Front Side Shade Beam-Diffuse Solar Reflectance`

        |  The front side beam-diffuse solar reflectance at normal incidence averaged
        |  over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Shade Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_shade_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Front Side Shade Beam-Diffuse Solar Reflectance"]

    @front_side_shade_beamdiffuse_solar_reflectance.setter
    def front_side_shade_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Shade Beam-Diffuse Solar Reflectance`

        """
        self["Front Side Shade Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_shade_beamdiffuse_solar_reflectance(self):
        """field `Back Side Shade Beam-Diffuse Solar Reflectance`

        |  The back side beam-diffuse solar reflectance at normal incidence averaged
        |  over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Shade Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_shade_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Back Side Shade Beam-Diffuse Solar Reflectance"]

    @back_side_shade_beamdiffuse_solar_reflectance.setter
    def back_side_shade_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Shade Beam-Diffuse Solar Reflectance`

        """
        self["Back Side Shade Beam-Diffuse Solar Reflectance"] = value

    @property
    def shade_beambeam_visible_transmittance_at_normal_incidence(self):
        """field `Shade Beam-Beam Visible Transmittance at Normal Incidence`

        |  The beam-beam visible transmittance at normal incidence averaged over the
        |  visible spectrum range of solar radiation. Assumed to be the same for
        |  front and back sides of the shade.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Shade Beam-Beam Visible Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shade_beambeam_visible_transmittance_at_normal_incidence` or None if not set
        """
        return self[
            "Shade Beam-Beam Visible Transmittance at Normal Incidence"]

    @shade_beambeam_visible_transmittance_at_normal_incidence.setter
    def shade_beambeam_visible_transmittance_at_normal_incidence(
            self,
            value=None):
        """  Corresponds to IDD field `Shade Beam-Beam Visible Transmittance at Normal Incidence`

        """
        self[
            "Shade Beam-Beam Visible Transmittance at Normal Incidence"] = value

    @property
    def shade_beamdiffuse_visible_transmittance_at_normal_incidence(self):
        """field `Shade Beam-Diffuse Visible Transmittance at Normal Incidence`

        |  The beam-diffuse visible transmittance at normal incidence averaged over the
        |  visible spectrum range of solar radiation. Assumed to be the same for
        |  front and back sides of the shade.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Shade Beam-Diffuse Visible Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shade_beamdiffuse_visible_transmittance_at_normal_incidence` or None if not set
        """
        return self[
            "Shade Beam-Diffuse Visible Transmittance at Normal Incidence"]

    @shade_beamdiffuse_visible_transmittance_at_normal_incidence.setter
    def shade_beamdiffuse_visible_transmittance_at_normal_incidence(
            self,
            value=None):
        """  Corresponds to IDD field `Shade Beam-Diffuse Visible Transmittance at Normal Incidence`

        """
        self[
            "Shade Beam-Diffuse Visible Transmittance at Normal Incidence"] = value

    @property
    def shade_beamdiffuse_visible_reflectance_at_normal_incidence(self):
        """field `Shade Beam-Diffuse Visible Reflectance at Normal Incidence`

        |  The beam-diffuse visible reflectance at normal incidence averaged over the
        |  visible spectrum range of solar radiation. Assumed to be the same for
        |  front and back sides of the shade.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Shade Beam-Diffuse Visible Reflectance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shade_beamdiffuse_visible_reflectance_at_normal_incidence` or None if not set
        """
        return self[
            "Shade Beam-Diffuse Visible Reflectance at Normal Incidence"]

    @shade_beamdiffuse_visible_reflectance_at_normal_incidence.setter
    def shade_beamdiffuse_visible_reflectance_at_normal_incidence(
            self,
            value=None):
        """  Corresponds to IDD field `Shade Beam-Diffuse Visible Reflectance at Normal Incidence`

        """
        self[
            "Shade Beam-Diffuse Visible Reflectance at Normal Incidence"] = value

    @property
    def shade_material_infrared_transmittance(self):
        """field `Shade Material Infrared Transmittance`

        |  The long-wave transmittance of the shade material at zero shade openness.
        |  Assumed to be the same for front and back sides of the shade.
        |  Units: dimensionless
        |  Default value: 0.05
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Shade Material Infrared Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shade_material_infrared_transmittance` or None if not set

        """
        return self["Shade Material Infrared Transmittance"]

    @shade_material_infrared_transmittance.setter
    def shade_material_infrared_transmittance(self, value=0.05):
        """Corresponds to IDD field `Shade Material Infrared Transmittance`"""
        self["Shade Material Infrared Transmittance"] = value

    @property
    def front_side_shade_material_infrared_emissivity(self):
        """field `Front Side Shade Material Infrared Emissivity`

        |  The front side long-wave emissivity of the shade material at zero shade
        |  openness. Openness fraction is used to calculate the effective emissivity
        |  value.
        |  Units: dimensionless
        |  Default value: 0.91
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Shade Material Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_shade_material_infrared_emissivity` or None if not set

        """
        return self["Front Side Shade Material Infrared Emissivity"]

    @front_side_shade_material_infrared_emissivity.setter
    def front_side_shade_material_infrared_emissivity(self, value=0.91):
        """Corresponds to IDD field `Front Side Shade Material Infrared
        Emissivity`"""
        self["Front Side Shade Material Infrared Emissivity"] = value

    @property
    def back_side_shade_material_infrared_emissivity(self):
        """field `Back Side Shade Material Infrared Emissivity`

        |  The back side long-wave emissivity of the shade material at zero shade
        |  openness. Openness fraction is used to calculate the effective emissivity
        |  value.
        |  Units: dimensionless
        |  Default value: 0.91
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Shade Material Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_shade_material_infrared_emissivity` or None if not set

        """
        return self["Back Side Shade Material Infrared Emissivity"]

    @back_side_shade_material_infrared_emissivity.setter
    def back_side_shade_material_infrared_emissivity(self, value=0.91):
        """Corresponds to IDD field `Back Side Shade Material Infrared
        Emissivity`"""
        self["Back Side Shade Material Infrared Emissivity"] = value




class WindowMaterialDrapeEquivalentLayer(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Drape:EquivalentLayer`
        Specifies the properties of equivalent layer drape fabric materials.
        Shades are considered to be perfect diffusers (all transmitted and reflected
        radiation is hemispherically-diffuse) independent of angle of incidence.
        unpleated drape fabric is treated as thin and flat layer.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'drape beam-beam solar transmittance at normal incidence',
                                       {'name': u'Drape Beam-Beam Solar Transmittance at Normal Incidence',
                                        'pyname': u'drape_beambeam_solar_transmittance_at_normal_incidence',
                                        'default': 0.0,
                                        'maximum': 0.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side drape beam-diffuse solar transmittance',
                                       {'name': u'Front Side Drape Beam-Diffuse Solar Transmittance',
                                        'pyname': u'front_side_drape_beamdiffuse_solar_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side drape beam-diffuse solar transmittance',
                                       {'name': u'Back Side Drape Beam-Diffuse Solar Transmittance',
                                        'pyname': u'back_side_drape_beamdiffuse_solar_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side drape beam-diffuse solar reflectance',
                                       {'name': u'Front Side Drape Beam-Diffuse Solar Reflectance',
                                        'pyname': u'front_side_drape_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side drape beam-diffuse solar reflectance',
                                       {'name': u'Back Side Drape Beam-Diffuse Solar Reflectance',
                                        'pyname': u'back_side_drape_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'drape beam-beam visible transmittance',
                                       {'name': u'Drape Beam-Beam Visible Transmittance',
                                        'pyname': u'drape_beambeam_visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'drape beam-diffuse visible transmittance',
                                       {'name': u'Drape Beam-Diffuse Visible Transmittance',
                                        'pyname': u'drape_beamdiffuse_visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'drape beam-diffuse visible reflectance',
                                       {'name': u'Drape Beam-Diffuse Visible Reflectance',
                                        'pyname': u'drape_beamdiffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'drape material infrared transmittance',
                                       {'name': u'Drape Material Infrared Transmittance',
                                        'pyname': u'drape_material_infrared_transmittance',
                                        'default': 0.05,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side drape material infrared emissivity',
                                       {'name': u'Front Side Drape Material Infrared Emissivity',
                                        'pyname': u'front_side_drape_material_infrared_emissivity',
                                        'default': 0.87,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'back side drape material infrared emissivity',
                                       {'name': u'Back Side Drape Material Infrared Emissivity',
                                        'pyname': u'back_side_drape_material_infrared_emissivity',
                                        'default': 0.87,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'width of pleated fabric',
                                       {'name': u'Width of Pleated Fabric',
                                        'pyname': u'width_of_pleated_fabric',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'length of pleated fabric',
                                       {'name': u'Length of Pleated Fabric',
                                        'pyname': u'length_of_pleated_fabric',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 4,
               'name': u'WindowMaterial:Drape:EquivalentLayer',
               'pyname': u'WindowMaterialDrapeEquivalentLayer',
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
    def drape_beambeam_solar_transmittance_at_normal_incidence(self):
        """field `Drape Beam-Beam Solar Transmittance at Normal Incidence`

        |  The beam-beam solar transmittance at normal incidence. This value is the
        |  same as the openness area fraction of the drape fabric. Assumed to be
        |  same for front and back sides.
        |  Units: dimensionless
        |  value <= 0.2

        Args:
            value (float): value for IDD Field `Drape Beam-Beam Solar Transmittance at Normal Incidence`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drape_beambeam_solar_transmittance_at_normal_incidence` or None if not set
        """
        return self["Drape Beam-Beam Solar Transmittance at Normal Incidence"]

    @drape_beambeam_solar_transmittance_at_normal_incidence.setter
    def drape_beambeam_solar_transmittance_at_normal_incidence(
            self,
            value=None):
        """  Corresponds to IDD field `Drape Beam-Beam Solar Transmittance at Normal Incidence`

        """
        self["Drape Beam-Beam Solar Transmittance at Normal Incidence"] = value

    @property
    def front_side_drape_beamdiffuse_solar_transmittance(self):
        """field `Front Side Drape Beam-Diffuse Solar Transmittance`

        |  The front side beam-diffuse solar transmittance at normal incidence averaged
        |  over the entire spectrum of solar radiation. Assumed to be the same for front
        |  and back sides.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Drape Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_drape_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Front Side Drape Beam-Diffuse Solar Transmittance"]

    @front_side_drape_beamdiffuse_solar_transmittance.setter
    def front_side_drape_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Drape Beam-Diffuse Solar Transmittance`

        """
        self["Front Side Drape Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_drape_beamdiffuse_solar_transmittance(self):
        """field `Back Side Drape Beam-Diffuse Solar Transmittance`

        |  The back side beam-diffuse solar transmittance at normal incidence averaged
        |  over the entire spectrum of solar radiation. Assumed to be the same for front
        |  and back sides.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Drape Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_drape_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Back Side Drape Beam-Diffuse Solar Transmittance"]

    @back_side_drape_beamdiffuse_solar_transmittance.setter
    def back_side_drape_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Drape Beam-Diffuse Solar Transmittance`

        """
        self["Back Side Drape Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_drape_beamdiffuse_solar_reflectance(self):
        """field `Front Side Drape Beam-Diffuse Solar Reflectance`

        |  The front side beam-diffuse solar reflectance at normal incidence averaged
        |  over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Drape Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_drape_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Front Side Drape Beam-Diffuse Solar Reflectance"]

    @front_side_drape_beamdiffuse_solar_reflectance.setter
    def front_side_drape_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Drape Beam-Diffuse Solar Reflectance`

        """
        self["Front Side Drape Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_drape_beamdiffuse_solar_reflectance(self):
        """field `Back Side Drape Beam-Diffuse Solar Reflectance`

        |  The back side beam-diffuse solar reflectance at normal incidence averaged
        |  over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Drape Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_drape_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Back Side Drape Beam-Diffuse Solar Reflectance"]

    @back_side_drape_beamdiffuse_solar_reflectance.setter
    def back_side_drape_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Drape Beam-Diffuse Solar Reflectance`

        """
        self["Back Side Drape Beam-Diffuse Solar Reflectance"] = value

    @property
    def drape_beambeam_visible_transmittance(self):
        """field `Drape Beam-Beam Visible Transmittance`

        |  The beam-beam visible transmittance at normal incidence averaged over the
        |  visible spectrum of solar radiation. Assumed same for front and back sides.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Drape Beam-Beam Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drape_beambeam_visible_transmittance` or None if not set
        """
        return self["Drape Beam-Beam Visible Transmittance"]

    @drape_beambeam_visible_transmittance.setter
    def drape_beambeam_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Drape Beam-Beam Visible Transmittance`

        """
        self["Drape Beam-Beam Visible Transmittance"] = value

    @property
    def drape_beamdiffuse_visible_transmittance(self):
        """field `Drape Beam-Diffuse Visible Transmittance`

        |  The beam-diffuse visible transmittance at normal incidence averaged over the
        |  visible spectrum range of solar radiation. Assumed to be the same for front
        |  and back sides.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Drape Beam-Diffuse Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drape_beamdiffuse_visible_transmittance` or None if not set
        """
        return self["Drape Beam-Diffuse Visible Transmittance"]

    @drape_beamdiffuse_visible_transmittance.setter
    def drape_beamdiffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Drape Beam-Diffuse Visible Transmittance`

        """
        self["Drape Beam-Diffuse Visible Transmittance"] = value

    @property
    def drape_beamdiffuse_visible_reflectance(self):
        """field `Drape Beam-Diffuse Visible Reflectance`

        |  The beam-diffuse visible reflectance at normal incidence average over the
        |  visible spectrum range of solar radiation. Assumed to be the same for front
        |  and back sides.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Drape Beam-Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drape_beamdiffuse_visible_reflectance` or None if not set
        """
        return self["Drape Beam-Diffuse Visible Reflectance"]

    @drape_beamdiffuse_visible_reflectance.setter
    def drape_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD field `Drape Beam-Diffuse Visible Reflectance`

        """
        self["Drape Beam-Diffuse Visible Reflectance"] = value

    @property
    def drape_material_infrared_transmittance(self):
        """field `Drape Material Infrared Transmittance`

        |  Long-wave transmittance of the drape fabric at zero openness fraction.
        |  Assumed same for front and back sides.
        |  Units: dimensionless
        |  Default value: 0.05
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Drape Material Infrared Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drape_material_infrared_transmittance` or None if not set

        """
        return self["Drape Material Infrared Transmittance"]

    @drape_material_infrared_transmittance.setter
    def drape_material_infrared_transmittance(self, value=0.05):
        """Corresponds to IDD field `Drape Material Infrared Transmittance`"""
        self["Drape Material Infrared Transmittance"] = value

    @property
    def front_side_drape_material_infrared_emissivity(self):
        """field `Front Side Drape Material Infrared Emissivity`

        |  Front side long-wave emissivity of the drape fabric at zero shade openness.
        |  Openness fraction specified above is used to calculate the effective
        |  emissivity value.
        |  Units: dimensionless
        |  Default value: 0.87
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Drape Material Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_drape_material_infrared_emissivity` or None if not set

        """
        return self["Front Side Drape Material Infrared Emissivity"]

    @front_side_drape_material_infrared_emissivity.setter
    def front_side_drape_material_infrared_emissivity(self, value=0.87):
        """Corresponds to IDD field `Front Side Drape Material Infrared
        Emissivity`"""
        self["Front Side Drape Material Infrared Emissivity"] = value

    @property
    def back_side_drape_material_infrared_emissivity(self):
        """field `Back Side Drape Material Infrared Emissivity`

        |  Back side long-wave emissivity of the drape fabric at zero shade openness.
        |  Openness fraction specified above is used to calculate the effective
        |  emissivity value.
        |  Units: dimensionless
        |  Default value: 0.87
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Drape Material Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_drape_material_infrared_emissivity` or None if not set

        """
        return self["Back Side Drape Material Infrared Emissivity"]

    @back_side_drape_material_infrared_emissivity.setter
    def back_side_drape_material_infrared_emissivity(self, value=0.87):
        """Corresponds to IDD field `Back Side Drape Material Infrared
        Emissivity`"""
        self["Back Side Drape Material Infrared Emissivity"] = value

    @property
    def width_of_pleated_fabric(self):
        """field `Width of Pleated Fabric`

        |  Width of the pleated section of the draped fabric. If the drape fabric is
        |  unpleated or is flat, then the pleated section width is set to zero.
        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Width of Pleated Fabric`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `width_of_pleated_fabric` or None if not set

        """
        return self["Width of Pleated Fabric"]

    @width_of_pleated_fabric.setter
    def width_of_pleated_fabric(self, value=None):
        """Corresponds to IDD field `Width of Pleated Fabric`"""
        self["Width of Pleated Fabric"] = value

    @property
    def length_of_pleated_fabric(self):
        """field `Length of Pleated Fabric`

        |  Length of the pleated section of the draped fabric. If the drape fabric is
        |  unpleated or is flat, then the pleated section length is set to zero.
        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Length of Pleated Fabric`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `length_of_pleated_fabric` or None if not set

        """
        return self["Length of Pleated Fabric"]

    @length_of_pleated_fabric.setter
    def length_of_pleated_fabric(self, value=None):
        """Corresponds to IDD field `Length of Pleated Fabric`"""
        self["Length of Pleated Fabric"] = value




class WindowMaterialBlindEquivalentLayer(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Blind:EquivalentLayer`
        Window equivalent layer blind slat optical and thermal properties.
        The model assumes that slats are thin and flat, applies correction
        empirical correlation to account for curvature effect. Slats are
        assumed to transmit and reflect diffusely.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'slat orientation',
                                       {'name': u'Slat Orientation',
                                        'pyname': u'slat_orientation',
                                        'default': u'Horizontal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Horizontal',
                                                            u'Vertical'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'slat width',
                                       {'name': u'Slat Width',
                                        'pyname': u'slat_width',
                                        'minimum>': 0.0,
                                        'maximum': 0.025,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat separation',
                                       {'name': u'Slat Separation',
                                        'pyname': u'slat_separation',
                                        'minimum>': 0.0,
                                        'maximum': 0.025,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat crown',
                                       {'name': u'Slat Crown',
                                        'pyname': u'slat_crown',
                                        'default': 0.0015,
                                        'maximum': 0.00156,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'slat angle',
                                       {'name': u'Slat Angle',
                                        'pyname': u'slat_angle',
                                        'default': 45.0,
                                        'maximum': 180.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'front side slat beam-diffuse solar transmittance',
                                       {'name': u'Front Side Slat Beam-Diffuse Solar Transmittance',
                                        'pyname': u'front_side_slat_beamdiffuse_solar_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'back side slat beam-diffuse solar transmittance',
                                       {'name': u'Back Side Slat Beam-Diffuse Solar Transmittance',
                                        'pyname': u'back_side_slat_beamdiffuse_solar_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side slat beam-diffuse solar reflectance',
                                       {'name': u'Front Side Slat Beam-Diffuse Solar Reflectance',
                                        'pyname': u'front_side_slat_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side slat beam-diffuse solar reflectance',
                                       {'name': u'Back Side Slat Beam-Diffuse Solar Reflectance',
                                        'pyname': u'back_side_slat_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side slat beam-diffuse visible transmittance',
                                       {'name': u'Front Side Slat Beam-Diffuse Visible Transmittance',
                                        'pyname': u'front_side_slat_beamdiffuse_visible_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side slat beam-diffuse visible transmittance',
                                       {'name': u'Back Side Slat Beam-Diffuse Visible Transmittance',
                                        'pyname': u'back_side_slat_beamdiffuse_visible_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side slat beam-diffuse visible reflectance',
                                       {'name': u'Front Side Slat Beam-Diffuse Visible Reflectance',
                                        'pyname': u'front_side_slat_beamdiffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side slat beam-diffuse visible reflectance',
                                       {'name': u'Back Side Slat Beam-Diffuse Visible Reflectance',
                                        'pyname': u'back_side_slat_beamdiffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'slat diffuse-diffuse solar transmittance',
                                       {'name': u'Slat Diffuse-Diffuse Solar Transmittance',
                                        'pyname': u'slat_diffusediffuse_solar_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side slat diffuse-diffuse solar reflectance',
                                       {'name': u'Front Side Slat Diffuse-Diffuse Solar Reflectance',
                                        'pyname': u'front_side_slat_diffusediffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side slat diffuse-diffuse solar reflectance',
                                       {'name': u'Back Side Slat Diffuse-Diffuse Solar Reflectance',
                                        'pyname': u'back_side_slat_diffusediffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'slat diffuse-diffuse visible transmittance',
                                       {'name': u'Slat Diffuse-Diffuse Visible Transmittance',
                                        'pyname': u'slat_diffusediffuse_visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat diffuse-diffuse visible reflectance',
                                       {'name': u'Front Side Slat Diffuse-Diffuse Visible Reflectance',
                                        'pyname': u'front_side_slat_diffusediffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side slat diffuse-diffuse visible reflectance',
                                       {'name': u'Back Side Slat Diffuse-Diffuse Visible Reflectance',
                                        'pyname': u'back_side_slat_diffusediffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'slat infrared transmittance',
                                       {'name': u'Slat Infrared Transmittance',
                                        'pyname': u'slat_infrared_transmittance',
                                        'default': 0.0,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'front side slat infrared emissivity',
                                       {'name': u'Front Side Slat Infrared Emissivity',
                                        'pyname': u'front_side_slat_infrared_emissivity',
                                        'default': 0.9,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side slat infrared emissivity',
                                       {'name': u'Back Side Slat Infrared Emissivity',
                                        'pyname': u'back_side_slat_infrared_emissivity',
                                        'default': 0.9,
                                        'maximum<': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'slat angle control',
                                       {'name': u'Slat Angle Control',
                                        'pyname': u'slat_angle_control',
                                        'default': u'FixedSlatAngle',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FixedSlatAngle',
                                                            u'MaximizeSolar',
                                                            u'BlockBeamSolar'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 10,
               'name': u'WindowMaterial:Blind:EquivalentLayer',
               'pyname': u'WindowMaterialBlindEquivalentLayer',
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
    def slat_orientation(self):
        """field `Slat Orientation`

        |  Default value: Horizontal

        Args:
            value (str): value for IDD Field `Slat Orientation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slat_orientation` or None if not set

        """
        return self["Slat Orientation"]

    @slat_orientation.setter
    def slat_orientation(self, value="Horizontal"):
        """Corresponds to IDD field `Slat Orientation`"""
        self["Slat Orientation"] = value

    @property
    def slat_width(self):
        """field `Slat Width`

        |  Units: m
        |  IP-Units: in
        |  value <= 0.025

        Args:
            value (float): value for IDD Field `Slat Width`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_width` or None if not set

        """
        return self["Slat Width"]

    @slat_width.setter
    def slat_width(self, value=None):
        """Corresponds to IDD field `Slat Width`"""
        self["Slat Width"] = value

    @property
    def slat_separation(self):
        """field `Slat Separation`

        |  Distance between adjacent slat faces
        |  Units: m
        |  IP-Units: in
        |  value <= 0.025

        Args:
            value (float): value for IDD Field `Slat Separation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_separation` or None if not set

        """
        return self["Slat Separation"]

    @slat_separation.setter
    def slat_separation(self, value=None):
        """Corresponds to IDD field `Slat Separation`"""
        self["Slat Separation"] = value

    @property
    def slat_crown(self):
        """field `Slat Crown`

        |  Perpendicular length between the cord and the curve.
        |  Slat is assumed to be rectangular in cross section
        |  and flat. Crown=0.0625x"Slat width"
        |  Units: m
        |  IP-Units: in
        |  Default value: 0.0015
        |  value <= 0.00156

        Args:
            value (float): value for IDD Field `Slat Crown`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_crown` or None if not set

        """
        return self["Slat Crown"]

    @slat_crown.setter
    def slat_crown(self, value=0.0015):
        """Corresponds to IDD field `Slat Crown`"""
        self["Slat Crown"] = value

    @property
    def slat_angle(self):
        """field `Slat Angle`

        |  Units: deg
        |  Default value: 45.0
        |  value <= 180.0

        Args:
            value (float): value for IDD Field `Slat Angle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_angle` or None if not set

        """
        return self["Slat Angle"]

    @slat_angle.setter
    def slat_angle(self, value=45.0):
        """Corresponds to IDD field `Slat Angle`"""
        self["Slat Angle"] = value

    @property
    def front_side_slat_beamdiffuse_solar_transmittance(self):
        """field `Front Side Slat Beam-Diffuse Solar Transmittance`

        |  The front side beam-diffuse solar transmittance of the slat at normal
        |  incidence averaged over the entire spectrum of solar radiation.
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Front Side Slat Beam-Diffuse Solar Transmittance"]

    @front_side_slat_beamdiffuse_solar_transmittance.setter
    def front_side_slat_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Slat Beam-Diffuse Solar Transmittance`

        """
        self["Front Side Slat Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_slat_beamdiffuse_solar_transmittance(self):
        """field `Back Side Slat Beam-Diffuse Solar Transmittance`

        |  The back side beam-diffuse solar transmittance of the slat at normal
        |  incidence averaged over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Back Side Slat Beam-Diffuse Solar Transmittance"]

    @back_side_slat_beamdiffuse_solar_transmittance.setter
    def back_side_slat_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Slat Beam-Diffuse Solar Transmittance`

        """
        self["Back Side Slat Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_slat_beamdiffuse_solar_reflectance(self):
        """field `Front Side Slat Beam-Diffuse Solar Reflectance`

        |  The front side beam-diffuse solar reflectance of the slat at normal
        |  incidence averaged over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Front Side Slat Beam-Diffuse Solar Reflectance"]

    @front_side_slat_beamdiffuse_solar_reflectance.setter
    def front_side_slat_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Slat Beam-Diffuse Solar Reflectance`

        """
        self["Front Side Slat Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_slat_beamdiffuse_solar_reflectance(self):
        """field `Back Side Slat Beam-Diffuse Solar Reflectance`

        |  The back side beam-diffuse solar reflectance of the slat at normal
        |  incidence averaged over the entire spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Back Side Slat Beam-Diffuse Solar Reflectance"]

    @back_side_slat_beamdiffuse_solar_reflectance.setter
    def back_side_slat_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Slat Beam-Diffuse Solar Reflectance`

        """
        self["Back Side Slat Beam-Diffuse Solar Reflectance"] = value

    @property
    def front_side_slat_beamdiffuse_visible_transmittance(self):
        """field `Front Side Slat Beam-Diffuse Visible Transmittance`

        |  The front side beam-diffuse visible transmittance of the slat
        |  at normal incidence averaged over the visible spectrum range
        |  of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Beam-Diffuse Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_beamdiffuse_visible_transmittance` or None if not set
        """
        return self["Front Side Slat Beam-Diffuse Visible Transmittance"]

    @front_side_slat_beamdiffuse_visible_transmittance.setter
    def front_side_slat_beamdiffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Slat Beam-Diffuse Visible Transmittance`

        """
        self["Front Side Slat Beam-Diffuse Visible Transmittance"] = value

    @property
    def back_side_slat_beamdiffuse_visible_transmittance(self):
        """field `Back Side Slat Beam-Diffuse Visible Transmittance`

        |  The back side beam-diffuse visible transmittance of the slat
        |  at normal incidence averaged over the visible spectrum range
        |  of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Beam-Diffuse Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_beamdiffuse_visible_transmittance` or None if not set
        """
        return self["Back Side Slat Beam-Diffuse Visible Transmittance"]

    @back_side_slat_beamdiffuse_visible_transmittance.setter
    def back_side_slat_beamdiffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Slat Beam-Diffuse Visible Transmittance`

        """
        self["Back Side Slat Beam-Diffuse Visible Transmittance"] = value

    @property
    def front_side_slat_beamdiffuse_visible_reflectance(self):
        """field `Front Side Slat Beam-Diffuse Visible Reflectance`

        |  The front side beam-diffuse visible reflectance of the slat
        |  at normal incidence averaged over the visible spectrum range
        |  of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Beam-Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_beamdiffuse_visible_reflectance` or None if not set
        """
        return self["Front Side Slat Beam-Diffuse Visible Reflectance"]

    @front_side_slat_beamdiffuse_visible_reflectance.setter
    def front_side_slat_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Slat Beam-Diffuse Visible Reflectance`

        """
        self["Front Side Slat Beam-Diffuse Visible Reflectance"] = value

    @property
    def back_side_slat_beamdiffuse_visible_reflectance(self):
        """field `Back Side Slat Beam-Diffuse Visible Reflectance`

        |  The back side beam-diffuse visible reflectance of the slat
        |  at normal incidence averaged over the visible spectrum range
        |  of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Beam-Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_beamdiffuse_visible_reflectance` or None if not set
        """
        return self["Back Side Slat Beam-Diffuse Visible Reflectance"]

    @back_side_slat_beamdiffuse_visible_reflectance.setter
    def back_side_slat_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Slat Beam-Diffuse Visible Reflectance`

        """
        self["Back Side Slat Beam-Diffuse Visible Reflectance"] = value

    @property
    def slat_diffusediffuse_solar_transmittance(self):
        """field `Slat Diffuse-Diffuse Solar Transmittance`

        |  The beam-diffuse solar transmittance of the slat averaged
        |  over the entire solar spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Diffuse-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_diffusediffuse_solar_transmittance` or None if not set
        """
        return self["Slat Diffuse-Diffuse Solar Transmittance"]

    @slat_diffusediffuse_solar_transmittance.setter
    def slat_diffusediffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Slat Diffuse-Diffuse Solar Transmittance`

        """
        self["Slat Diffuse-Diffuse Solar Transmittance"] = value

    @property
    def front_side_slat_diffusediffuse_solar_reflectance(self):
        """field `Front Side Slat Diffuse-Diffuse Solar Reflectance`

        |  The front side beam-diffuse solar reflectance of the slat
        |  averaged over the entire solar spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Diffuse-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_diffusediffuse_solar_reflectance` or None if not set
        """
        return self["Front Side Slat Diffuse-Diffuse Solar Reflectance"]

    @front_side_slat_diffusediffuse_solar_reflectance.setter
    def front_side_slat_diffusediffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Slat Diffuse-Diffuse Solar Reflectance`

        """
        self["Front Side Slat Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def back_side_slat_diffusediffuse_solar_reflectance(self):
        """field `Back Side Slat Diffuse-Diffuse Solar Reflectance`

        |  The back side beam-diffuse solar reflectance of the slat
        |  averaged over the entire solar spectrum of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Diffuse-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_diffusediffuse_solar_reflectance` or None if not set
        """
        return self["Back Side Slat Diffuse-Diffuse Solar Reflectance"]

    @back_side_slat_diffusediffuse_solar_reflectance.setter
    def back_side_slat_diffusediffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Slat Diffuse-Diffuse Solar Reflectance`

        """
        self["Back Side Slat Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def slat_diffusediffuse_visible_transmittance(self):
        """field `Slat Diffuse-Diffuse Visible Transmittance`

        |  The beam-diffuse visible transmittance of the slat averaged
        |  over the visible spectrum range of solar radiation.
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Diffuse-Diffuse Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_diffusediffuse_visible_transmittance` or None if not set
        """
        return self["Slat Diffuse-Diffuse Visible Transmittance"]

    @slat_diffusediffuse_visible_transmittance.setter
    def slat_diffusediffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Slat Diffuse-Diffuse Visible Transmittance`

        """
        self["Slat Diffuse-Diffuse Visible Transmittance"] = value

    @property
    def front_side_slat_diffusediffuse_visible_reflectance(self):
        """field `Front Side Slat Diffuse-Diffuse Visible Reflectance`

        |  The front side beam-diffuse visible reflectance of the slat
        |  averaged over the visible spectrum range of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Diffuse-Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_diffusediffuse_visible_reflectance` or None if not set
        """
        return self["Front Side Slat Diffuse-Diffuse Visible Reflectance"]

    @front_side_slat_diffusediffuse_visible_reflectance.setter
    def front_side_slat_diffusediffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Slat Diffuse-Diffuse Visible Reflectance`

        """
        self["Front Side Slat Diffuse-Diffuse Visible Reflectance"] = value

    @property
    def back_side_slat_diffusediffuse_visible_reflectance(self):
        """field `Back Side Slat Diffuse-Diffuse Visible Reflectance`

        |  The back side beam-diffuse visible reflectance of the slat
        |  averaged over the visible spectrum range of solar radiation.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Diffuse-Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_diffusediffuse_visible_reflectance` or None if not set
        """
        return self["Back Side Slat Diffuse-Diffuse Visible Reflectance"]

    @back_side_slat_diffusediffuse_visible_reflectance.setter
    def back_side_slat_diffusediffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Slat Diffuse-Diffuse Visible Reflectance`

        """
        self["Back Side Slat Diffuse-Diffuse Visible Reflectance"] = value

    @property
    def slat_infrared_transmittance(self):
        """field `Slat Infrared Transmittance`

        |  Long-wave hemispherical transmittance of the slat material.
        |  Assumed to be the same for both sides of the slat.
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Slat Infrared Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slat_infrared_transmittance` or None if not set

        """
        return self["Slat Infrared Transmittance"]

    @slat_infrared_transmittance.setter
    def slat_infrared_transmittance(self, value=None):
        """Corresponds to IDD field `Slat Infrared Transmittance`"""
        self["Slat Infrared Transmittance"] = value

    @property
    def front_side_slat_infrared_emissivity(self):
        """field `Front Side Slat Infrared Emissivity`

        |  Front side long-wave hemispherical emissivity of the slat material.
        |  Units: dimensionless
        |  Default value: 0.9
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Slat Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_slat_infrared_emissivity` or None if not set

        """
        return self["Front Side Slat Infrared Emissivity"]

    @front_side_slat_infrared_emissivity.setter
    def front_side_slat_infrared_emissivity(self, value=0.9):
        """Corresponds to IDD field `Front Side Slat Infrared Emissivity`"""
        self["Front Side Slat Infrared Emissivity"] = value

    @property
    def back_side_slat_infrared_emissivity(self):
        """field `Back Side Slat Infrared Emissivity`

        |  Back side long-wave hemispherical emissivity of the slat material.
        |  Units: dimensionless
        |  Default value: 0.9
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Slat Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_slat_infrared_emissivity` or None if not set

        """
        return self["Back Side Slat Infrared Emissivity"]

    @back_side_slat_infrared_emissivity.setter
    def back_side_slat_infrared_emissivity(self, value=0.9):
        """Corresponds to IDD field `Back Side Slat Infrared Emissivity`"""
        self["Back Side Slat Infrared Emissivity"] = value

    @property
    def slat_angle_control(self):
        """field `Slat Angle Control`

        |  Used only if slat angle control is desired to either maximize solar
        |  gain (MaximizeSolar), maximize visibility while eliminating beam solar
        |  radiation (BlockBeamSolar), or fixed slate angle (FixedSlatAngle).
        |  If FixedSlatAngle is selected, the slat angle entered above is used.
        |  Default value: FixedSlatAngle

        Args:
            value (str): value for IDD Field `Slat Angle Control`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slat_angle_control` or None if not set

        """
        return self["Slat Angle Control"]

    @slat_angle_control.setter
    def slat_angle_control(self, value="FixedSlatAngle"):
        """Corresponds to IDD field `Slat Angle Control`"""
        self["Slat Angle Control"] = value




class WindowMaterialScreenEquivalentLayer(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Screen:EquivalentLayer`
        Equivalent layer window screen physical properties. Can only be
        located on the exterior side of a window construction.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'screen beam-beam solar transmittance',
                                       {'name': u'Screen Beam-Beam Solar Transmittance',
                                        'pyname': u'screen_beambeam_solar_transmittance',
                                        'default': 'autocalculate',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen beam-diffuse solar transmittance',
                                       {'name': u'Screen Beam-Diffuse Solar Transmittance',
                                        'pyname': u'screen_beamdiffuse_solar_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen beam-diffuse solar reflectance',
                                       {'name': u'Screen Beam-Diffuse Solar Reflectance',
                                        'pyname': u'screen_beamdiffuse_solar_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen beam-beam visible transmittance',
                                       {'name': u'Screen Beam-Beam Visible Transmittance',
                                        'pyname': u'screen_beambeam_visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen beam-diffuse visible transmittance',
                                       {'name': u'Screen Beam-Diffuse Visible Transmittance',
                                        'pyname': u'screen_beamdiffuse_visible_transmittance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen beam-diffuse visible reflectance',
                                       {'name': u'Screen Beam-Diffuse Visible Reflectance',
                                        'pyname': u'screen_beamdiffuse_visible_reflectance',
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen infrared transmittance',
                                       {'name': u'Screen Infrared Transmittance',
                                        'pyname': u'screen_infrared_transmittance',
                                        'default': 0.02,
                                        'maximum<': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'screen infrared emissivity',
                                       {'name': u'Screen Infrared Emissivity',
                                        'pyname': u'screen_infrared_emissivity',
                                        'default': 0.93,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'screen wire spacing',
                                       {'name': u'Screen Wire Spacing',
                                        'pyname': u'screen_wire_spacing',
                                        'default': 0.025,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'screen wire diameter',
                                       {'name': u'Screen Wire Diameter',
                                        'pyname': u'screen_wire_diameter',
                                        'default': 0.005,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 4,
               'name': u'WindowMaterial:Screen:EquivalentLayer',
               'pyname': u'WindowMaterialScreenEquivalentLayer',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Enter a unique name for this window screen material.

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
    def screen_beambeam_solar_transmittance(self):
        """field `Screen Beam-Beam Solar Transmittance`

        |  The beam-beam transmittance of the screen material at normal incidence.
        |  This input field is the same as the material openness area fraction
        |  and can be autocalculated from the wire spacing and wire and diameter.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value < 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Screen Beam-Beam Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `screen_beambeam_solar_transmittance` or None if not set
        """
        return self["Screen Beam-Beam Solar Transmittance"]

    @screen_beambeam_solar_transmittance.setter
    def screen_beambeam_solar_transmittance(self, value="autocalculate"):
        """  Corresponds to IDD field `Screen Beam-Beam Solar Transmittance`

        """
        self["Screen Beam-Beam Solar Transmittance"] = value

    @property
    def screen_beamdiffuse_solar_transmittance(self):
        """field `Screen Beam-Diffuse Solar Transmittance`

        |  The beam-diffuse solar transmittance of the screen material at normal
        |  incidence averaged over the entire spectrum of solar radiation.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Screen Beam-Diffuse Solar Transmittance"]

    @screen_beamdiffuse_solar_transmittance.setter
    def screen_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Screen Beam-Diffuse Solar Transmittance`

        """
        self["Screen Beam-Diffuse Solar Transmittance"] = value

    @property
    def screen_beamdiffuse_solar_reflectance(self):
        """field `Screen Beam-Diffuse Solar Reflectance`

        |  The beam-diffuse solar reflectance of the screen material at normal
        |  incidence averaged over the entire spectrum of solar radiation.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Screen Beam-Diffuse Solar Reflectance"]

    @screen_beamdiffuse_solar_reflectance.setter
    def screen_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Screen Beam-Diffuse Solar Reflectance`

        """
        self["Screen Beam-Diffuse Solar Reflectance"] = value

    @property
    def screen_beambeam_visible_transmittance(self):
        """field `Screen Beam-Beam Visible Transmittance`

        |  The beam-beam visible transmittance of the screen material at normal
        |  incidence averaged over the visible spectrum range of solar radiation.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Beam-Beam Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_beambeam_visible_transmittance` or None if not set
        """
        return self["Screen Beam-Beam Visible Transmittance"]

    @screen_beambeam_visible_transmittance.setter
    def screen_beambeam_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Screen Beam-Beam Visible Transmittance`

        """
        self["Screen Beam-Beam Visible Transmittance"] = value

    @property
    def screen_beamdiffuse_visible_transmittance(self):
        """field `Screen Beam-Diffuse Visible Transmittance`

        |  The beam-diffuse visible transmittance of the screen material at normal
        |  incidence averaged over the visible spectrum range of solar radiation.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Beam-Diffuse Visible Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_beamdiffuse_visible_transmittance` or None if not set
        """
        return self["Screen Beam-Diffuse Visible Transmittance"]

    @screen_beamdiffuse_visible_transmittance.setter
    def screen_beamdiffuse_visible_transmittance(self, value=None):
        """  Corresponds to IDD field `Screen Beam-Diffuse Visible Transmittance`

        """
        self["Screen Beam-Diffuse Visible Transmittance"] = value

    @property
    def screen_beamdiffuse_visible_reflectance(self):
        """field `Screen Beam-Diffuse Visible Reflectance`

        |  Beam-diffuse visible reflectance of the screen material at normal
        |  incidence averaged over the visible spectrum range of solar radiation.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Beam-Diffuse Visible Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_beamdiffuse_visible_reflectance` or None if not set
        """
        return self["Screen Beam-Diffuse Visible Reflectance"]

    @screen_beamdiffuse_visible_reflectance.setter
    def screen_beamdiffuse_visible_reflectance(self, value=None):
        """  Corresponds to IDD field `Screen Beam-Diffuse Visible Reflectance`

        """
        self["Screen Beam-Diffuse Visible Reflectance"] = value

    @property
    def screen_infrared_transmittance(self):
        """field `Screen Infrared Transmittance`

        |  The long-wave hemispherical transmittance of the screen material.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  Default value: 0.02
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Infrared Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_infrared_transmittance` or None if not set

        """
        return self["Screen Infrared Transmittance"]

    @screen_infrared_transmittance.setter
    def screen_infrared_transmittance(self, value=0.02):
        """Corresponds to IDD field `Screen Infrared Transmittance`"""
        self["Screen Infrared Transmittance"] = value

    @property
    def screen_infrared_emissivity(self):
        """field `Screen Infrared Emissivity`

        |  The long-wave hemispherical emissivity of the screen material.
        |  Assumed to be the same for both sides of the screen.
        |  Units: dimensionless
        |  Default value: 0.93
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Screen Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_infrared_emissivity` or None if not set

        """
        return self["Screen Infrared Emissivity"]

    @screen_infrared_emissivity.setter
    def screen_infrared_emissivity(self, value=0.93):
        """Corresponds to IDD field `Screen Infrared Emissivity`"""
        self["Screen Infrared Emissivity"] = value

    @property
    def screen_wire_spacing(self):
        """field `Screen Wire Spacing`

        |  Spacing assumed to be the same in both directions.
        |  Units: m
        |  IP-Units: in
        |  Default value: 0.025

        Args:
            value (float): value for IDD Field `Screen Wire Spacing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_wire_spacing` or None if not set

        """
        return self["Screen Wire Spacing"]

    @screen_wire_spacing.setter
    def screen_wire_spacing(self, value=0.025):
        """Corresponds to IDD field `Screen Wire Spacing`"""
        self["Screen Wire Spacing"] = value

    @property
    def screen_wire_diameter(self):
        """field `Screen Wire Diameter`

        |  Diameter assumed to be the same in both directions.
        |  Units: m
        |  IP-Units: in
        |  Default value: 0.005

        Args:
            value (float): value for IDD Field `Screen Wire Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `screen_wire_diameter` or None if not set

        """
        return self["Screen Wire Diameter"]

    @screen_wire_diameter.setter
    def screen_wire_diameter(self, value=0.005):
        """Corresponds to IDD field `Screen Wire Diameter`"""
        self["Screen Wire Diameter"] = value




class WindowMaterialGlazingEquivalentLayer(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Glazing:EquivalentLayer`
        Glass material properties for Windows or Glass Doors
        Transmittance/Reflectance input method.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'optical data type',
                                       {'name': u'Optical Data Type',
                                        'pyname': u'optical_data_type',
                                        'default': u'SpectralAverage',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'window glass spectral data set name',
                                       {'name': u'Window Glass Spectral Data Set Name',
                                        'pyname': u'window_glass_spectral_data_set_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'front side beam-beam solar transmittance',
                                       {'name': u'Front Side Beam-Beam Solar Transmittance',
                                        'pyname': u'front_side_beambeam_solar_transmittance',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-beam solar transmittance',
                                       {'name': u'Back Side Beam-Beam Solar Transmittance',
                                        'pyname': u'back_side_beambeam_solar_transmittance',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-beam solar reflectance',
                                       {'name': u'Front Side Beam-Beam Solar Reflectance',
                                        'pyname': u'front_side_beambeam_solar_reflectance',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-beam solar reflectance',
                                       {'name': u'Back Side Beam-Beam Solar Reflectance',
                                        'pyname': u'back_side_beambeam_solar_reflectance',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-beam visible solar transmittance',
                                       {'name': u'Front Side Beam-Beam Visible Solar Transmittance',
                                        'pyname': u'front_side_beambeam_visible_solar_transmittance',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-beam visible solar transmittance',
                                       {'name': u'Back Side Beam-Beam Visible Solar Transmittance',
                                        'pyname': u'back_side_beambeam_visible_solar_transmittance',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-beam visible solar reflectance',
                                       {'name': u'Front Side Beam-Beam Visible Solar Reflectance',
                                        'pyname': u'front_side_beambeam_visible_solar_reflectance',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-beam visible solar reflectance',
                                       {'name': u'Back Side Beam-Beam Visible Solar Reflectance',
                                        'pyname': u'back_side_beambeam_visible_solar_reflectance',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-diffuse solar transmittance',
                                       {'name': u'Front Side Beam-Diffuse Solar Transmittance',
                                        'pyname': u'front_side_beamdiffuse_solar_transmittance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-diffuse solar transmittance',
                                       {'name': u'Back Side Beam-Diffuse Solar Transmittance',
                                        'pyname': u'back_side_beamdiffuse_solar_transmittance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-diffuse solar reflectance',
                                       {'name': u'Front Side Beam-Diffuse Solar Reflectance',
                                        'pyname': u'front_side_beamdiffuse_solar_reflectance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-diffuse solar reflectance',
                                       {'name': u'Back Side Beam-Diffuse Solar Reflectance',
                                        'pyname': u'back_side_beamdiffuse_solar_reflectance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-diffuse visible solar transmittance',
                                       {'name': u'Front Side Beam-Diffuse Visible Solar Transmittance',
                                        'pyname': u'front_side_beamdiffuse_visible_solar_transmittance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-diffuse visible solar transmittance',
                                       {'name': u'Back Side Beam-Diffuse Visible Solar Transmittance',
                                        'pyname': u'back_side_beamdiffuse_visible_solar_transmittance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side beam-diffuse visible solar reflectance',
                                       {'name': u'Front Side Beam-Diffuse Visible Solar Reflectance',
                                        'pyname': u'front_side_beamdiffuse_visible_solar_reflectance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side beam-diffuse visible solar reflectance',
                                       {'name': u'Back Side Beam-Diffuse Visible Solar Reflectance',
                                        'pyname': u'back_side_beamdiffuse_visible_solar_reflectance',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'diffuse-diffuse solar transmittance',
                                       {'name': u'Diffuse-Diffuse Solar Transmittance',
                                        'pyname': u'diffusediffuse_solar_transmittance',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side diffuse-diffuse solar reflectance',
                                       {'name': u'Front Side Diffuse-Diffuse Solar Reflectance',
                                        'pyname': u'front_side_diffusediffuse_solar_reflectance',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side diffuse-diffuse solar reflectance',
                                       {'name': u'Back Side Diffuse-Diffuse Solar Reflectance',
                                        'pyname': u'back_side_diffusediffuse_solar_reflectance',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'diffuse-diffuse visible solar transmittance',
                                       {'name': u'Diffuse-Diffuse Visible Solar Transmittance',
                                        'pyname': u'diffusediffuse_visible_solar_transmittance',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side diffuse-diffuse visible solar reflectance',
                                       {'name': u'Front Side Diffuse-Diffuse Visible Solar Reflectance',
                                        'pyname': u'front_side_diffusediffuse_visible_solar_reflectance',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'back side diffuse-diffuse visible solar reflectance',
                                       {'name': u'Back Side Diffuse-Diffuse Visible Solar Reflectance',
                                        'pyname': u'back_side_diffusediffuse_visible_solar_reflectance',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'infrared transmittance (applies to front and back)',
                                       {'name': u'Infrared Transmittance (applies to front and back)',
                                        'pyname': u'infrared_transmittance_applies_to_front_and_back',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'front side infrared emissivity',
                                       {'name': u'Front Side Infrared Emissivity',
                                        'pyname': u'front_side_infrared_emissivity',
                                        'default': 0.84,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'back side infrared emissivity',
                                       {'name': u'Back Side Infrared Emissivity',
                                        'pyname': u'back_side_infrared_emissivity',
                                        'default': 0.84,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 11,
               'name': u'WindowMaterial:Glazing:EquivalentLayer',
               'pyname': u'WindowMaterialGlazingEquivalentLayer',
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
    def optical_data_type(self):
        """field `Optical Data Type`

        |  Spectral is no longer supported and SpectralAverage is now the default.
        |  Default value: SpectralAverage

        Args:
            value (str): value for IDD Field `Optical Data Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `optical_data_type` or None if not set

        """
        return self["Optical Data Type"]

    @optical_data_type.setter
    def optical_data_type(self, value="SpectralAverage"):
        """Corresponds to IDD field `Optical Data Type`"""
        self["Optical Data Type"] = value

    @property
    def window_glass_spectral_data_set_name(self):
        """field `Window Glass Spectral Data Set Name`

        |  Used only when Optical Data Type = Spectral

        Args:
            value (str): value for IDD Field `Window Glass Spectral Data Set Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `window_glass_spectral_data_set_name` or None if not set

        """
        return self["Window Glass Spectral Data Set Name"]

    @window_glass_spectral_data_set_name.setter
    def window_glass_spectral_data_set_name(self, value=None):
        """Corresponds to IDD field `Window Glass Spectral Data Set Name`"""
        self["Window Glass Spectral Data Set Name"] = value

    @property
    def front_side_beambeam_solar_transmittance(self):
        """field `Front Side Beam-Beam Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Beam Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beambeam_solar_transmittance` or None if not set
        """
        return self["Front Side Beam-Beam Solar Transmittance"]

    @front_side_beambeam_solar_transmittance.setter
    def front_side_beambeam_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Beam Solar Transmittance`

        """
        self["Front Side Beam-Beam Solar Transmittance"] = value

    @property
    def back_side_beambeam_solar_transmittance(self):
        """field `Back Side Beam-Beam Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Beam Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beambeam_solar_transmittance` or None if not set
        """
        return self["Back Side Beam-Beam Solar Transmittance"]

    @back_side_beambeam_solar_transmittance.setter
    def back_side_beambeam_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Beam Solar Transmittance`

        """
        self["Back Side Beam-Beam Solar Transmittance"] = value

    @property
    def front_side_beambeam_solar_reflectance(self):
        """field `Front Side Beam-Beam Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Front Side is side closest to outdoor air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Beam Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beambeam_solar_reflectance` or None if not set
        """
        return self["Front Side Beam-Beam Solar Reflectance"]

    @front_side_beambeam_solar_reflectance.setter
    def front_side_beambeam_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Beam Solar Reflectance`

        """
        self["Front Side Beam-Beam Solar Reflectance"] = value

    @property
    def back_side_beambeam_solar_reflectance(self):
        """field `Back Side Beam-Beam Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Back Side is side closest to zone air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Beam Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beambeam_solar_reflectance` or None if not set
        """
        return self["Back Side Beam-Beam Solar Reflectance"]

    @back_side_beambeam_solar_reflectance.setter
    def back_side_beambeam_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Beam Solar Reflectance`

        """
        self["Back Side Beam-Beam Solar Reflectance"] = value

    @property
    def front_side_beambeam_visible_solar_transmittance(self):
        """field `Front Side Beam-Beam Visible Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Beam Visible Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beambeam_visible_solar_transmittance` or None if not set
        """
        return self["Front Side Beam-Beam Visible Solar Transmittance"]

    @front_side_beambeam_visible_solar_transmittance.setter
    def front_side_beambeam_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Beam Visible Solar Transmittance`

        """
        self["Front Side Beam-Beam Visible Solar Transmittance"] = value

    @property
    def back_side_beambeam_visible_solar_transmittance(self):
        """field `Back Side Beam-Beam Visible Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Beam Visible Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beambeam_visible_solar_transmittance` or None if not set
        """
        return self["Back Side Beam-Beam Visible Solar Transmittance"]

    @back_side_beambeam_visible_solar_transmittance.setter
    def back_side_beambeam_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Beam Visible Solar Transmittance`

        """
        self["Back Side Beam-Beam Visible Solar Transmittance"] = value

    @property
    def front_side_beambeam_visible_solar_reflectance(self):
        """field `Front Side Beam-Beam Visible Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Front Side is side closest to outdoor air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Beam Visible Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beambeam_visible_solar_reflectance` or None if not set
        """
        return self["Front Side Beam-Beam Visible Solar Reflectance"]

    @front_side_beambeam_visible_solar_reflectance.setter
    def front_side_beambeam_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Beam Visible Solar Reflectance`

        """
        self["Front Side Beam-Beam Visible Solar Reflectance"] = value

    @property
    def back_side_beambeam_visible_solar_reflectance(self):
        """field `Back Side Beam-Beam Visible Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Back Side is side closest to zone air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Beam Visible Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beambeam_visible_solar_reflectance` or None if not set
        """
        return self["Back Side Beam-Beam Visible Solar Reflectance"]

    @back_side_beambeam_visible_solar_reflectance.setter
    def back_side_beambeam_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Beam Visible Solar Reflectance`

        """
        self["Back Side Beam-Beam Visible Solar Reflectance"] = value

    @property
    def front_side_beamdiffuse_solar_transmittance(self):
        """field `Front Side Beam-Diffuse Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Front Side Beam-Diffuse Solar Transmittance"]

    @front_side_beamdiffuse_solar_transmittance.setter
    def front_side_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Diffuse Solar Transmittance`

        """
        self["Front Side Beam-Diffuse Solar Transmittance"] = value

    @property
    def back_side_beamdiffuse_solar_transmittance(self):
        """field `Back Side Beam-Diffuse Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beamdiffuse_solar_transmittance` or None if not set
        """
        return self["Back Side Beam-Diffuse Solar Transmittance"]

    @back_side_beamdiffuse_solar_transmittance.setter
    def back_side_beamdiffuse_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Diffuse Solar Transmittance`

        """
        self["Back Side Beam-Diffuse Solar Transmittance"] = value

    @property
    def front_side_beamdiffuse_solar_reflectance(self):
        """field `Front Side Beam-Diffuse Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Front Side is side closest to outdoor air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Front Side Beam-Diffuse Solar Reflectance"]

    @front_side_beamdiffuse_solar_reflectance.setter
    def front_side_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Diffuse Solar Reflectance`

        """
        self["Front Side Beam-Diffuse Solar Reflectance"] = value

    @property
    def back_side_beamdiffuse_solar_reflectance(self):
        """field `Back Side Beam-Diffuse Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Back Side is side closest to zone air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beamdiffuse_solar_reflectance` or None if not set
        """
        return self["Back Side Beam-Diffuse Solar Reflectance"]

    @back_side_beamdiffuse_solar_reflectance.setter
    def back_side_beamdiffuse_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Diffuse Solar Reflectance`

        """
        self["Back Side Beam-Diffuse Solar Reflectance"] = value

    @property
    def front_side_beamdiffuse_visible_solar_transmittance(self):
        """field `Front Side Beam-Diffuse Visible Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Diffuse Visible Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beamdiffuse_visible_solar_transmittance` or None if not set
        """
        return self["Front Side Beam-Diffuse Visible Solar Transmittance"]

    @front_side_beamdiffuse_visible_solar_transmittance.setter
    def front_side_beamdiffuse_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Diffuse Visible Solar Transmittance`

        """
        self["Front Side Beam-Diffuse Visible Solar Transmittance"] = value

    @property
    def back_side_beamdiffuse_visible_solar_transmittance(self):
        """field `Back Side Beam-Diffuse Visible Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Diffuse Visible Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beamdiffuse_visible_solar_transmittance` or None if not set
        """
        return self["Back Side Beam-Diffuse Visible Solar Transmittance"]

    @back_side_beamdiffuse_visible_solar_transmittance.setter
    def back_side_beamdiffuse_visible_solar_transmittance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Diffuse Visible Solar Transmittance`

        """
        self["Back Side Beam-Diffuse Visible Solar Transmittance"] = value

    @property
    def front_side_beamdiffuse_visible_solar_reflectance(self):
        """field `Front Side Beam-Diffuse Visible Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Front Side is side closest to outdoor air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Front Side Beam-Diffuse Visible Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_beamdiffuse_visible_solar_reflectance` or None if not set
        """
        return self["Front Side Beam-Diffuse Visible Solar Reflectance"]

    @front_side_beamdiffuse_visible_solar_reflectance.setter
    def front_side_beamdiffuse_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Front Side Beam-Diffuse Visible Solar Reflectance`

        """
        self["Front Side Beam-Diffuse Visible Solar Reflectance"] = value

    @property
    def back_side_beamdiffuse_visible_solar_reflectance(self):
        """field `Back Side Beam-Diffuse Visible Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  Back Side is side closest to zone air
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Back Side Beam-Diffuse Visible Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_beamdiffuse_visible_solar_reflectance` or None if not set
        """
        return self["Back Side Beam-Diffuse Visible Solar Reflectance"]

    @back_side_beamdiffuse_visible_solar_reflectance.setter
    def back_side_beamdiffuse_visible_solar_reflectance(self, value=None):
        """  Corresponds to IDD field `Back Side Beam-Diffuse Visible Solar Reflectance`

        """
        self["Back Side Beam-Diffuse Visible Solar Reflectance"] = value

    @property
    def diffusediffuse_solar_transmittance(self):
        """field `Diffuse-Diffuse Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  If this field is autocalculate, then the diffuse-diffuse solar
        |  transmittance is automatically estimated from other inputs and used
        |  in subsequent calculations. If this field is zero or positive, then
        |  the value entered here will be used.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Diffuse-Diffuse Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `diffusediffuse_solar_transmittance` or None if not set
        """
        return self["Diffuse-Diffuse Solar Transmittance"]

    @diffusediffuse_solar_transmittance.setter
    def diffusediffuse_solar_transmittance(self, value="autocalculate"):
        """  Corresponds to IDD field `Diffuse-Diffuse Solar Transmittance`

        """
        self["Diffuse-Diffuse Solar Transmittance"] = value

    @property
    def front_side_diffusediffuse_solar_reflectance(self):
        """field `Front Side Diffuse-Diffuse Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  If this field is autocalculate, then the front diffuse-diffuse solar
        |  reflectance is automatically estimated from other inputs and used in
        |  subsequent calculations. If this field is zero or positive, then the value
        |  entered here will be used.  Front Side is side closest to outdoor air.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Front Side Diffuse-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `front_side_diffusediffuse_solar_reflectance` or None if not set
        """
        return self["Front Side Diffuse-Diffuse Solar Reflectance"]

    @front_side_diffusediffuse_solar_reflectance.setter
    def front_side_diffusediffuse_solar_reflectance(
            self,
            value="autocalculate"):
        """  Corresponds to IDD field `Front Side Diffuse-Diffuse Solar Reflectance`

        """
        self["Front Side Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def back_side_diffusediffuse_solar_reflectance(self):
        """field `Back Side Diffuse-Diffuse Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  If this field is autocalculate, then the back diffuse-diffuse solar
        |  reflectance is automatically estimated from other inputs and used in
        |  subsequent calculations. If this field is zero or positive, then the value
        |  entered here will be used.  Back side is side closest to indoor air.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Back Side Diffuse-Diffuse Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `back_side_diffusediffuse_solar_reflectance` or None if not set
        """
        return self["Back Side Diffuse-Diffuse Solar Reflectance"]

    @back_side_diffusediffuse_solar_reflectance.setter
    def back_side_diffusediffuse_solar_reflectance(
            self,
            value="autocalculate"):
        """  Corresponds to IDD field `Back Side Diffuse-Diffuse Solar Reflectance`

        """
        self["Back Side Diffuse-Diffuse Solar Reflectance"] = value

    @property
    def diffusediffuse_visible_solar_transmittance(self):
        """field `Diffuse-Diffuse Visible Solar Transmittance`

        |  Used only when Optical Data Type = SpectralAverage
        |  This input field is not used currently.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Diffuse-Diffuse Visible Solar Transmittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `diffusediffuse_visible_solar_transmittance` or None if not set
        """
        return self["Diffuse-Diffuse Visible Solar Transmittance"]

    @diffusediffuse_visible_solar_transmittance.setter
    def diffusediffuse_visible_solar_transmittance(
            self,
            value="autocalculate"):
        """  Corresponds to IDD field `Diffuse-Diffuse Visible Solar Transmittance`

        """
        self["Diffuse-Diffuse Visible Solar Transmittance"] = value

    @property
    def front_side_diffusediffuse_visible_solar_reflectance(self):
        """field `Front Side Diffuse-Diffuse Visible Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  This input field is not used currently.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Front Side Diffuse-Diffuse Visible Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `front_side_diffusediffuse_visible_solar_reflectance` or None if not set
        """
        return self["Front Side Diffuse-Diffuse Visible Solar Reflectance"]

    @front_side_diffusediffuse_visible_solar_reflectance.setter
    def front_side_diffusediffuse_visible_solar_reflectance(
            self,
            value="autocalculate"):
        """  Corresponds to IDD field `Front Side Diffuse-Diffuse Visible Solar Reflectance`

        """
        self["Front Side Diffuse-Diffuse Visible Solar Reflectance"] = value

    @property
    def back_side_diffusediffuse_visible_solar_reflectance(self):
        """field `Back Side Diffuse-Diffuse Visible Solar Reflectance`

        |  Used only when Optical Data Type = SpectralAverage
        |  This input field is not used currently.
        |  Units: dimensionless
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Back Side Diffuse-Diffuse Visible Solar Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `back_side_diffusediffuse_visible_solar_reflectance` or None if not set
        """
        return self["Back Side Diffuse-Diffuse Visible Solar Reflectance"]

    @back_side_diffusediffuse_visible_solar_reflectance.setter
    def back_side_diffusediffuse_visible_solar_reflectance(
            self,
            value="autocalculate"):
        """  Corresponds to IDD field `Back Side Diffuse-Diffuse Visible Solar Reflectance`

        """
        self["Back Side Diffuse-Diffuse Visible Solar Reflectance"] = value

    @property
    def infrared_transmittance_applies_to_front_and_back(self):
        """field `Infrared Transmittance (applies to front and back)`

        |  The long-wave hemispherical transmittance of the glazing.
        |  Assumed to be the same for both sides of the glazing.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Infrared Transmittance (applies to front and back)`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `infrared_transmittance_applies_to_front_and_back` or None if not set

        """
        return self["Infrared Transmittance (applies to front and back)"]

    @infrared_transmittance_applies_to_front_and_back.setter
    def infrared_transmittance_applies_to_front_and_back(self, value=None):
        """Corresponds to IDD field `Infrared Transmittance (applies to front
        and back)`"""
        self["Infrared Transmittance (applies to front and back)"] = value

    @property
    def front_side_infrared_emissivity(self):
        """field `Front Side Infrared Emissivity`

        |  The front side long-wave hemispherical emissivity of the glazing.
        |  Units: dimensionless
        |  Default value: 0.84
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Side Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_side_infrared_emissivity` or None if not set

        """
        return self["Front Side Infrared Emissivity"]

    @front_side_infrared_emissivity.setter
    def front_side_infrared_emissivity(self, value=0.84):
        """Corresponds to IDD field `Front Side Infrared Emissivity`"""
        self["Front Side Infrared Emissivity"] = value

    @property
    def back_side_infrared_emissivity(self):
        """field `Back Side Infrared Emissivity`

        |  The back side long-wave hemispherical emissivity of the glazing.
        |  Units: dimensionless
        |  Default value: 0.84
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Back Side Infrared Emissivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `back_side_infrared_emissivity` or None if not set

        """
        return self["Back Side Infrared Emissivity"]

    @back_side_infrared_emissivity.setter
    def back_side_infrared_emissivity(self, value=0.84):
        """Corresponds to IDD field `Back Side Infrared Emissivity`"""
        self["Back Side Infrared Emissivity"] = value




class WindowMaterialGapEquivalentLayer(DataObject):

    """ Corresponds to IDD object `WindowMaterial:Gap:EquivalentLayer`
        Gas material properties that are used in Windows Equivalent Layer
        References only WindowMaterial:Gas properties
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'gas type',
                                       {'name': u'Gas Type',
                                        'pyname': u'gas_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'AIR',
                                                            u'ARGON',
                                                            u'KRYPTON',
                                                            u'XENON',
                                                            u'CUSTOM'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thickness',
                                       {'name': u'Thickness',
                                        'pyname': u'thickness',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'gap vent type',
                                       {'name': u'Gap Vent Type',
                                        'pyname': u'gap_vent_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Sealed',
                                                            u'VentedIndoor',
                                                            u'VentedOutdoor'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'conductivity coefficient a',
                                       {'name': u'Conductivity Coefficient A',
                                        'pyname': u'conductivity_coefficient_a',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'conductivity coefficient b',
                                       {'name': u'Conductivity Coefficient B',
                                        'pyname': u'conductivity_coefficient_b',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K2'}),
                                      (u'conductivity coefficient c',
                                       {'name': u'Conductivity Coefficient C',
                                        'pyname': u'conductivity_coefficient_c',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K3'}),
                                      (u'viscosity coefficient a',
                                       {'name': u'Viscosity Coefficient A',
                                        'pyname': u'viscosity_coefficient_a',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m-s'}),
                                      (u'viscosity coefficient b',
                                       {'name': u'Viscosity Coefficient B',
                                        'pyname': u'viscosity_coefficient_b',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m-s-K'}),
                                      (u'viscosity coefficient c',
                                       {'name': u'Viscosity Coefficient C',
                                        'pyname': u'viscosity_coefficient_c',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m-s-K2'}),
                                      (u'specific heat coefficient a',
                                       {'name': u'Specific Heat Coefficient A',
                                        'pyname': u'specific_heat_coefficient_a',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat coefficient b',
                                       {'name': u'Specific Heat Coefficient B',
                                        'pyname': u'specific_heat_coefficient_b',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K2'}),
                                      (u'specific heat coefficient c',
                                       {'name': u'Specific Heat Coefficient C',
                                        'pyname': u'specific_heat_coefficient_c',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K3'}),
                                      (u'molecular weight',
                                       {'name': u'Molecular Weight',
                                        'pyname': u'molecular_weight',
                                        'maximum': 200.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 20.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'g/mol'}),
                                      (u'specific heat ratio',
                                       {'name': u'Specific Heat Ratio',
                                        'pyname': u'specific_heat_ratio',
                                        'minimum>': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 3,
               'name': u'WindowMaterial:Gap:EquivalentLayer',
               'pyname': u'WindowMaterialGapEquivalentLayer',
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
    def gas_type(self):
        """field `Gas Type`

        Args:
            value (str): value for IDD Field `Gas Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_type` or None if not set

        """
        return self["Gas Type"]

    @gas_type.setter
    def gas_type(self, value=None):
        """Corresponds to IDD field `Gas Type`"""
        self["Gas Type"] = value

    @property
    def thickness(self):
        """field `Thickness`

        |  Units: m
        |  IP-Units: in

        Args:
            value (float): value for IDD Field `Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thickness` or None if not set

        """
        return self["Thickness"]

    @thickness.setter
    def thickness(self, value=None):
        """Corresponds to IDD field `Thickness`"""
        self["Thickness"] = value

    @property
    def gap_vent_type(self):
        """field `Gap Vent Type`

        |  Sealed means the gap is enclosed and gas tight, i.e., no venting to indoor or
        |  outdoor environment.  VentedIndoor means the gap is vented to indoor environment, and
        |  VentedOutdoor means the gap is vented to the outdoor environment. The gap types
        |  VentedIndoor and VentedOutdoor are used with gas type "Air" only.

        Args:
            value (str): value for IDD Field `Gap Vent Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_vent_type` or None if not set

        """
        return self["Gap Vent Type"]

    @gap_vent_type.setter
    def gap_vent_type(self, value=None):
        """Corresponds to IDD field `Gap Vent Type`"""
        self["Gap Vent Type"] = value

    @property
    def conductivity_coefficient_a(self):
        """field `Conductivity Coefficient A`

        |  Used only if Gas Type = Custom
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Conductivity Coefficient A`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_coefficient_a` or None if not set

        """
        return self["Conductivity Coefficient A"]

    @conductivity_coefficient_a.setter
    def conductivity_coefficient_a(self, value=None):
        """Corresponds to IDD field `Conductivity Coefficient A`"""
        self["Conductivity Coefficient A"] = value

    @property
    def conductivity_coefficient_b(self):
        """field `Conductivity Coefficient B`

        |  Used only if Gas Type = Custom
        |  Units: W/m-K2

        Args:
            value (float): value for IDD Field `Conductivity Coefficient B`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_coefficient_b` or None if not set

        """
        return self["Conductivity Coefficient B"]

    @conductivity_coefficient_b.setter
    def conductivity_coefficient_b(self, value=None):
        """Corresponds to IDD field `Conductivity Coefficient B`"""
        self["Conductivity Coefficient B"] = value

    @property
    def conductivity_coefficient_c(self):
        """field `Conductivity Coefficient C`

        |  Used only if Gas Type = Custom
        |  Units: W/m-K3

        Args:
            value (float): value for IDD Field `Conductivity Coefficient C`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `conductivity_coefficient_c` or None if not set

        """
        return self["Conductivity Coefficient C"]

    @conductivity_coefficient_c.setter
    def conductivity_coefficient_c(self, value=None):
        """Corresponds to IDD field `Conductivity Coefficient C`"""
        self["Conductivity Coefficient C"] = value

    @property
    def viscosity_coefficient_a(self):
        """field `Viscosity Coefficient A`

        |  Used only if Gas Type = Custom
        |  Units: kg/m-s

        Args:
            value (float): value for IDD Field `Viscosity Coefficient A`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `viscosity_coefficient_a` or None if not set

        """
        return self["Viscosity Coefficient A"]

    @viscosity_coefficient_a.setter
    def viscosity_coefficient_a(self, value=None):
        """Corresponds to IDD field `Viscosity Coefficient A`"""
        self["Viscosity Coefficient A"] = value

    @property
    def viscosity_coefficient_b(self):
        """field `Viscosity Coefficient B`

        |  Used only if Gas Type = Custom
        |  Units: kg/m-s-K

        Args:
            value (float): value for IDD Field `Viscosity Coefficient B`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `viscosity_coefficient_b` or None if not set

        """
        return self["Viscosity Coefficient B"]

    @viscosity_coefficient_b.setter
    def viscosity_coefficient_b(self, value=None):
        """Corresponds to IDD field `Viscosity Coefficient B`"""
        self["Viscosity Coefficient B"] = value

    @property
    def viscosity_coefficient_c(self):
        """field `Viscosity Coefficient C`

        |  Used only if Gas Type = Custom
        |  Units: kg/m-s-K2

        Args:
            value (float): value for IDD Field `Viscosity Coefficient C`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `viscosity_coefficient_c` or None if not set

        """
        return self["Viscosity Coefficient C"]

    @viscosity_coefficient_c.setter
    def viscosity_coefficient_c(self, value=None):
        """Corresponds to IDD field `Viscosity Coefficient C`"""
        self["Viscosity Coefficient C"] = value

    @property
    def specific_heat_coefficient_a(self):
        """field `Specific Heat Coefficient A`

        |  Used only if Gas Type = Custom
        |  Units: J/kg-K

        Args:
            value (float): value for IDD Field `Specific Heat Coefficient A`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_coefficient_a` or None if not set

        """
        return self["Specific Heat Coefficient A"]

    @specific_heat_coefficient_a.setter
    def specific_heat_coefficient_a(self, value=None):
        """Corresponds to IDD field `Specific Heat Coefficient A`"""
        self["Specific Heat Coefficient A"] = value

    @property
    def specific_heat_coefficient_b(self):
        """field `Specific Heat Coefficient B`

        |  Used only if Gas Type = Custom
        |  Units: J/kg-K2

        Args:
            value (float): value for IDD Field `Specific Heat Coefficient B`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_coefficient_b` or None if not set

        """
        return self["Specific Heat Coefficient B"]

    @specific_heat_coefficient_b.setter
    def specific_heat_coefficient_b(self, value=None):
        """Corresponds to IDD field `Specific Heat Coefficient B`"""
        self["Specific Heat Coefficient B"] = value

    @property
    def specific_heat_coefficient_c(self):
        """field `Specific Heat Coefficient C`

        |  Used only if Gas Type = Custom
        |  Units: J/kg-K3

        Args:
            value (float): value for IDD Field `Specific Heat Coefficient C`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_coefficient_c` or None if not set

        """
        return self["Specific Heat Coefficient C"]

    @specific_heat_coefficient_c.setter
    def specific_heat_coefficient_c(self, value=None):
        """Corresponds to IDD field `Specific Heat Coefficient C`"""
        self["Specific Heat Coefficient C"] = value

    @property
    def molecular_weight(self):
        """field `Molecular Weight`

        |  Used only if Gas Type = Custom
        |  Units: g/mol
        |  value >= 20.0
        |  value <= 200.0

        Args:
            value (float): value for IDD Field `Molecular Weight`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `molecular_weight` or None if not set

        """
        return self["Molecular Weight"]

    @molecular_weight.setter
    def molecular_weight(self, value=None):
        """Corresponds to IDD field `Molecular Weight`"""
        self["Molecular Weight"] = value

    @property
    def specific_heat_ratio(self):
        """field `Specific Heat Ratio`

        |  Used only if Gas Type = Custom
        |  value > 1.0

        Args:
            value (float): value for IDD Field `Specific Heat Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_ratio` or None if not set

        """
        return self["Specific Heat Ratio"]

    @specific_heat_ratio.setter
    def specific_heat_ratio(self, value=None):
        """Corresponds to IDD field `Specific Heat Ratio`"""
        self["Specific Heat Ratio"] = value




class MaterialPropertyMoisturePenetrationDepthSettings(DataObject):

    """ Corresponds to IDD object `MaterialProperty:MoisturePenetrationDepth:Settings`
        Additional properties for moisture using EMPD procedure
        HeatBalanceAlgorithm choice=MoisturePenetrationDepthConductionTransferFunction only
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'moisture penetration depth',
                                       {'name': u'Moisture Penetration Depth',
                                        'pyname': u'moisture_penetration_depth',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'moisture equation coefficient a',
                                       {'name': u'Moisture Equation Coefficient a',
                                        'pyname': u'moisture_equation_coefficient_a',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture equation coefficient b',
                                       {'name': u'Moisture Equation Coefficient b',
                                        'pyname': u'moisture_equation_coefficient_b',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture equation coefficient c',
                                       {'name': u'Moisture Equation Coefficient c',
                                        'pyname': u'moisture_equation_coefficient_c',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture equation coefficient d',
                                       {'name': u'Moisture Equation Coefficient d',
                                        'pyname': u'moisture_equation_coefficient_d',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:MoisturePenetrationDepth:Settings',
               'pyname': u'MaterialPropertyMoisturePenetrationDepthSettings',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Material Name that the moisture properties will be added to.
        |  Additional material properties required to perform the EMPD model.
        |  Effective Mean Penetration Depth (EMPD)

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
    def moisture_penetration_depth(self):
        """field `Moisture Penetration Depth`

        |  This is the penetration depth
        |  Units: m

        Args:
            value (float): value for IDD Field `Moisture Penetration Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_penetration_depth` or None if not set

        """
        return self["Moisture Penetration Depth"]

    @moisture_penetration_depth.setter
    def moisture_penetration_depth(self, value=None):
        """Corresponds to IDD field `Moisture Penetration Depth`"""
        self["Moisture Penetration Depth"] = value

    @property
    def moisture_equation_coefficient_a(self):
        """field `Moisture Equation Coefficient a`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Moisture Equation Coefficient a`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_equation_coefficient_a` or None if not set

        """
        return self["Moisture Equation Coefficient a"]

    @moisture_equation_coefficient_a.setter
    def moisture_equation_coefficient_a(self, value=None):
        """Corresponds to IDD field `Moisture Equation Coefficient a`"""
        self["Moisture Equation Coefficient a"] = value

    @property
    def moisture_equation_coefficient_b(self):
        """field `Moisture Equation Coefficient b`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Moisture Equation Coefficient b`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_equation_coefficient_b` or None if not set

        """
        return self["Moisture Equation Coefficient b"]

    @moisture_equation_coefficient_b.setter
    def moisture_equation_coefficient_b(self, value=None):
        """Corresponds to IDD field `Moisture Equation Coefficient b`"""
        self["Moisture Equation Coefficient b"] = value

    @property
    def moisture_equation_coefficient_c(self):
        """field `Moisture Equation Coefficient c`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Moisture Equation Coefficient c`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_equation_coefficient_c` or None if not set

        """
        return self["Moisture Equation Coefficient c"]

    @moisture_equation_coefficient_c.setter
    def moisture_equation_coefficient_c(self, value=None):
        """Corresponds to IDD field `Moisture Equation Coefficient c`"""
        self["Moisture Equation Coefficient c"] = value

    @property
    def moisture_equation_coefficient_d(self):
        """field `Moisture Equation Coefficient d`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Moisture Equation Coefficient d`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_equation_coefficient_d` or None if not set

        """
        return self["Moisture Equation Coefficient d"]

    @moisture_equation_coefficient_d.setter
    def moisture_equation_coefficient_d(self, value=None):
        """Corresponds to IDD field `Moisture Equation Coefficient d`"""
        self["Moisture Equation Coefficient d"] = value




class MaterialPropertyPhaseChange(DataObject):

    """ Corresponds to IDD object `MaterialProperty:PhaseChange`
        Additional properties for temperature dependent thermal conductivity
        and enthalpy for Phase Change Materials (PCM)
        HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm only.
        Constructions with this should use the detailed CondFD process.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'temperature coefficient for thermal conductivity',
                                       {'name': u'Temperature Coefficient for Thermal Conductivity',
                                        'pyname': u'temperature_coefficient_for_thermal_conductivity',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K2'}),
                                      (u'temperature 1',
                                       {'name': u'Temperature 1',
                                        'pyname': u'temperature_1',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 1',
                                       {'name': u'Enthalpy 1',
                                        'pyname': u'enthalpy_1',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 2',
                                       {'name': u'Temperature 2',
                                        'pyname': u'temperature_2',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 2',
                                       {'name': u'Enthalpy 2',
                                        'pyname': u'enthalpy_2',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 3',
                                       {'name': u'Temperature 3',
                                        'pyname': u'temperature_3',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 3',
                                       {'name': u'Enthalpy 3',
                                        'pyname': u'enthalpy_3',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 4',
                                       {'name': u'Temperature 4',
                                        'pyname': u'temperature_4',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 4',
                                       {'name': u'Enthalpy 4',
                                        'pyname': u'enthalpy_4',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 5',
                                       {'name': u'Temperature 5',
                                        'pyname': u'temperature_5',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 5',
                                       {'name': u'Enthalpy 5',
                                        'pyname': u'enthalpy_5',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 6',
                                       {'name': u'Temperature 6',
                                        'pyname': u'temperature_6',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 6',
                                       {'name': u'Enthalpy 6',
                                        'pyname': u'enthalpy_6',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 7',
                                       {'name': u'Temperature 7',
                                        'pyname': u'temperature_7',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 7',
                                       {'name': u'Enthalpy 7',
                                        'pyname': u'enthalpy_7',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 8',
                                       {'name': u'Temperature 8',
                                        'pyname': u'temperature_8',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 8',
                                       {'name': u'Enthalpy 8',
                                        'pyname': u'enthalpy_8',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 9',
                                       {'name': u'Temperature 9',
                                        'pyname': u'temperature_9',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 9',
                                       {'name': u'Enthalpy 9',
                                        'pyname': u'enthalpy_9',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 10',
                                       {'name': u'Temperature 10',
                                        'pyname': u'temperature_10',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 10',
                                       {'name': u'Enthalpy 10',
                                        'pyname': u'enthalpy_10',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 11',
                                       {'name': u'Temperature 11',
                                        'pyname': u'temperature_11',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 11',
                                       {'name': u'Enthalpy 11',
                                        'pyname': u'enthalpy_11',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 12',
                                       {'name': u'Temperature 12',
                                        'pyname': u'temperature_12',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 12',
                                       {'name': u'Enthalpy 12',
                                        'pyname': u'enthalpy_12',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 13',
                                       {'name': u'Temperature 13',
                                        'pyname': u'temperature_13',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 13',
                                       {'name': u'Enthalpy 13',
                                        'pyname': u'enthalpy_13',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 14',
                                       {'name': u'Temperature 14',
                                        'pyname': u'temperature_14',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 14',
                                       {'name': u'Enthalpy 14',
                                        'pyname': u'enthalpy_14',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 15',
                                       {'name': u'Temperature 15',
                                        'pyname': u'temperature_15',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 15',
                                       {'name': u'Enthalpy 15',
                                        'pyname': u'enthalpy_15',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'temperature 16',
                                       {'name': u'Temperature 16',
                                        'pyname': u'temperature_16',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy 16',
                                       {'name': u'Enthalpy 16',
                                        'pyname': u'enthalpy_16',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:PhaseChange',
               'pyname': u'MaterialPropertyPhaseChange',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Regular Material Name to which the additional properties will be added.
        |  this the material name for the basic material properties.

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
    def temperature_coefficient_for_thermal_conductivity(self):
        """field `Temperature Coefficient for Thermal Conductivity`

        |  The base temperature is 20C.
        |  This is the thermal conductivity change per degree excursion from 20C.
        |  This variable conductivity function is overridden by the VariableThermalConductivity object, if present.
        |  Units: W/m-K2

        Args:
            value (float): value for IDD Field `Temperature Coefficient for Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_coefficient_for_thermal_conductivity` or None if not set

        """
        return self["Temperature Coefficient for Thermal Conductivity"]

    @temperature_coefficient_for_thermal_conductivity.setter
    def temperature_coefficient_for_thermal_conductivity(self, value=None):
        """Corresponds to IDD field `Temperature Coefficient for Thermal
        Conductivity`"""
        self["Temperature Coefficient for Thermal Conductivity"] = value

    @property
    def temperature_1(self):
        """field `Temperature 1`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_1` or None if not set

        """
        return self["Temperature 1"]

    @temperature_1.setter
    def temperature_1(self, value=None):
        """Corresponds to IDD field `Temperature 1`"""
        self["Temperature 1"] = value

    @property
    def enthalpy_1(self):
        """field `Enthalpy 1`

        |  for Temperature-enthalpy function corresponding to temperature 1
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_1` or None if not set

        """
        return self["Enthalpy 1"]

    @enthalpy_1.setter
    def enthalpy_1(self, value=None):
        """Corresponds to IDD field `Enthalpy 1`"""
        self["Enthalpy 1"] = value

    @property
    def temperature_2(self):
        """field `Temperature 2`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_2` or None if not set

        """
        return self["Temperature 2"]

    @temperature_2.setter
    def temperature_2(self, value=None):
        """Corresponds to IDD field `Temperature 2`"""
        self["Temperature 2"] = value

    @property
    def enthalpy_2(self):
        """field `Enthalpy 2`

        |  for Temperature-enthalpy function corresponding to temperature 2
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_2` or None if not set

        """
        return self["Enthalpy 2"]

    @enthalpy_2.setter
    def enthalpy_2(self, value=None):
        """Corresponds to IDD field `Enthalpy 2`"""
        self["Enthalpy 2"] = value

    @property
    def temperature_3(self):
        """field `Temperature 3`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_3` or None if not set

        """
        return self["Temperature 3"]

    @temperature_3.setter
    def temperature_3(self, value=None):
        """Corresponds to IDD field `Temperature 3`"""
        self["Temperature 3"] = value

    @property
    def enthalpy_3(self):
        """field `Enthalpy 3`

        |  for Temperature-enthalpy function corresponding to temperature 3
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_3` or None if not set

        """
        return self["Enthalpy 3"]

    @enthalpy_3.setter
    def enthalpy_3(self, value=None):
        """Corresponds to IDD field `Enthalpy 3`"""
        self["Enthalpy 3"] = value

    @property
    def temperature_4(self):
        """field `Temperature 4`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_4` or None if not set

        """
        return self["Temperature 4"]

    @temperature_4.setter
    def temperature_4(self, value=None):
        """Corresponds to IDD field `Temperature 4`"""
        self["Temperature 4"] = value

    @property
    def enthalpy_4(self):
        """field `Enthalpy 4`

        |  for Temperature-enthalpy function corresponding to temperature 4
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_4` or None if not set

        """
        return self["Enthalpy 4"]

    @enthalpy_4.setter
    def enthalpy_4(self, value=None):
        """Corresponds to IDD field `Enthalpy 4`"""
        self["Enthalpy 4"] = value

    @property
    def temperature_5(self):
        """field `Temperature 5`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_5` or None if not set

        """
        return self["Temperature 5"]

    @temperature_5.setter
    def temperature_5(self, value=None):
        """Corresponds to IDD field `Temperature 5`"""
        self["Temperature 5"] = value

    @property
    def enthalpy_5(self):
        """field `Enthalpy 5`

        |  for Temperature-enthalpy function corresponding to temperature 5
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_5` or None if not set

        """
        return self["Enthalpy 5"]

    @enthalpy_5.setter
    def enthalpy_5(self, value=None):
        """Corresponds to IDD field `Enthalpy 5`"""
        self["Enthalpy 5"] = value

    @property
    def temperature_6(self):
        """field `Temperature 6`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_6` or None if not set

        """
        return self["Temperature 6"]

    @temperature_6.setter
    def temperature_6(self, value=None):
        """Corresponds to IDD field `Temperature 6`"""
        self["Temperature 6"] = value

    @property
    def enthalpy_6(self):
        """field `Enthalpy 6`

        |  for Temperature-enthalpy function corresponding to temperature 6
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_6` or None if not set

        """
        return self["Enthalpy 6"]

    @enthalpy_6.setter
    def enthalpy_6(self, value=None):
        """Corresponds to IDD field `Enthalpy 6`"""
        self["Enthalpy 6"] = value

    @property
    def temperature_7(self):
        """field `Temperature 7`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_7` or None if not set

        """
        return self["Temperature 7"]

    @temperature_7.setter
    def temperature_7(self, value=None):
        """Corresponds to IDD field `Temperature 7`"""
        self["Temperature 7"] = value

    @property
    def enthalpy_7(self):
        """field `Enthalpy 7`

        |  for Temperature-enthalpy function corresponding to temperature 7
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_7` or None if not set

        """
        return self["Enthalpy 7"]

    @enthalpy_7.setter
    def enthalpy_7(self, value=None):
        """Corresponds to IDD field `Enthalpy 7`"""
        self["Enthalpy 7"] = value

    @property
    def temperature_8(self):
        """field `Temperature 8`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_8` or None if not set

        """
        return self["Temperature 8"]

    @temperature_8.setter
    def temperature_8(self, value=None):
        """Corresponds to IDD field `Temperature 8`"""
        self["Temperature 8"] = value

    @property
    def enthalpy_8(self):
        """field `Enthalpy 8`

        |  for Temperature-enthalpy function corresponding to temperature 8
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_8` or None if not set

        """
        return self["Enthalpy 8"]

    @enthalpy_8.setter
    def enthalpy_8(self, value=None):
        """Corresponds to IDD field `Enthalpy 8`"""
        self["Enthalpy 8"] = value

    @property
    def temperature_9(self):
        """field `Temperature 9`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_9` or None if not set

        """
        return self["Temperature 9"]

    @temperature_9.setter
    def temperature_9(self, value=None):
        """Corresponds to IDD field `Temperature 9`"""
        self["Temperature 9"] = value

    @property
    def enthalpy_9(self):
        """field `Enthalpy 9`

        |  for Temperature-enthalpy function corresponding to temperature 1
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_9` or None if not set

        """
        return self["Enthalpy 9"]

    @enthalpy_9.setter
    def enthalpy_9(self, value=None):
        """Corresponds to IDD field `Enthalpy 9`"""
        self["Enthalpy 9"] = value

    @property
    def temperature_10(self):
        """field `Temperature 10`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_10` or None if not set

        """
        return self["Temperature 10"]

    @temperature_10.setter
    def temperature_10(self, value=None):
        """Corresponds to IDD field `Temperature 10`"""
        self["Temperature 10"] = value

    @property
    def enthalpy_10(self):
        """field `Enthalpy 10`

        |  for Temperature-enthalpy function corresponding to temperature 2
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_10` or None if not set

        """
        return self["Enthalpy 10"]

    @enthalpy_10.setter
    def enthalpy_10(self, value=None):
        """Corresponds to IDD field `Enthalpy 10`"""
        self["Enthalpy 10"] = value

    @property
    def temperature_11(self):
        """field `Temperature 11`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_11` or None if not set

        """
        return self["Temperature 11"]

    @temperature_11.setter
    def temperature_11(self, value=None):
        """Corresponds to IDD field `Temperature 11`"""
        self["Temperature 11"] = value

    @property
    def enthalpy_11(self):
        """field `Enthalpy 11`

        |  for Temperature-enthalpy function corresponding to temperature 3
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_11` or None if not set

        """
        return self["Enthalpy 11"]

    @enthalpy_11.setter
    def enthalpy_11(self, value=None):
        """Corresponds to IDD field `Enthalpy 11`"""
        self["Enthalpy 11"] = value

    @property
    def temperature_12(self):
        """field `Temperature 12`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_12` or None if not set

        """
        return self["Temperature 12"]

    @temperature_12.setter
    def temperature_12(self, value=None):
        """Corresponds to IDD field `Temperature 12`"""
        self["Temperature 12"] = value

    @property
    def enthalpy_12(self):
        """field `Enthalpy 12`

        |  for Temperature-enthalpy function corresponding to temperature 14
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_12` or None if not set

        """
        return self["Enthalpy 12"]

    @enthalpy_12.setter
    def enthalpy_12(self, value=None):
        """Corresponds to IDD field `Enthalpy 12`"""
        self["Enthalpy 12"] = value

    @property
    def temperature_13(self):
        """field `Temperature 13`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_13` or None if not set

        """
        return self["Temperature 13"]

    @temperature_13.setter
    def temperature_13(self, value=None):
        """Corresponds to IDD field `Temperature 13`"""
        self["Temperature 13"] = value

    @property
    def enthalpy_13(self):
        """field `Enthalpy 13`

        |  for Temperature-enthalpy function corresponding to temperature 15
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_13` or None if not set

        """
        return self["Enthalpy 13"]

    @enthalpy_13.setter
    def enthalpy_13(self, value=None):
        """Corresponds to IDD field `Enthalpy 13`"""
        self["Enthalpy 13"] = value

    @property
    def temperature_14(self):
        """field `Temperature 14`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_14` or None if not set

        """
        return self["Temperature 14"]

    @temperature_14.setter
    def temperature_14(self, value=None):
        """Corresponds to IDD field `Temperature 14`"""
        self["Temperature 14"] = value

    @property
    def enthalpy_14(self):
        """field `Enthalpy 14`

        |  for Temperature-enthalpy function corresponding to temperature 16
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_14` or None if not set

        """
        return self["Enthalpy 14"]

    @enthalpy_14.setter
    def enthalpy_14(self, value=None):
        """Corresponds to IDD field `Enthalpy 14`"""
        self["Enthalpy 14"] = value

    @property
    def temperature_15(self):
        """field `Temperature 15`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_15` or None if not set

        """
        return self["Temperature 15"]

    @temperature_15.setter
    def temperature_15(self, value=None):
        """Corresponds to IDD field `Temperature 15`"""
        self["Temperature 15"] = value

    @property
    def enthalpy_15(self):
        """field `Enthalpy 15`

        |  for Temperature-enthalpy function corresponding to temperature 17
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_15` or None if not set

        """
        return self["Enthalpy 15"]

    @enthalpy_15.setter
    def enthalpy_15(self, value=None):
        """Corresponds to IDD field `Enthalpy 15`"""
        self["Enthalpy 15"] = value

    @property
    def temperature_16(self):
        """field `Temperature 16`

        |  for Temperature-enthalpy function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_16` or None if not set

        """
        return self["Temperature 16"]

    @temperature_16.setter
    def temperature_16(self, value=None):
        """Corresponds to IDD field `Temperature 16`"""
        self["Temperature 16"] = value

    @property
    def enthalpy_16(self):
        """field `Enthalpy 16`

        |  for Temperature-enthalpy function corresponding to temperature 16
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_16` or None if not set

        """
        return self["Enthalpy 16"]

    @enthalpy_16.setter
    def enthalpy_16(self, value=None):
        """Corresponds to IDD field `Enthalpy 16`"""
        self["Enthalpy 16"] = value




class MaterialPropertyVariableThermalConductivity(DataObject):

    """ Corresponds to IDD object `MaterialProperty:VariableThermalConductivity`
        Additional properties for temperature dependent thermal conductivity
        using piecewise linear temperature-conductivity function.
        HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm only.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'temperature 1',
                                       {'name': u'Temperature 1',
                                        'pyname': u'temperature_1',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 1',
                                       {'name': u'Thermal Conductivity 1',
                                        'pyname': u'thermal_conductivity_1',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 2',
                                       {'name': u'Temperature 2',
                                        'pyname': u'temperature_2',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 2',
                                       {'name': u'Thermal Conductivity 2',
                                        'pyname': u'thermal_conductivity_2',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 3',
                                       {'name': u'Temperature 3',
                                        'pyname': u'temperature_3',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 3',
                                       {'name': u'Thermal Conductivity 3',
                                        'pyname': u'thermal_conductivity_3',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 4',
                                       {'name': u'Temperature 4',
                                        'pyname': u'temperature_4',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 4',
                                       {'name': u'Thermal Conductivity 4',
                                        'pyname': u'thermal_conductivity_4',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 5',
                                       {'name': u'Temperature 5',
                                        'pyname': u'temperature_5',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 5',
                                       {'name': u'Thermal Conductivity 5',
                                        'pyname': u'thermal_conductivity_5',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 6',
                                       {'name': u'Temperature 6',
                                        'pyname': u'temperature_6',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 6',
                                       {'name': u'Thermal Conductivity 6',
                                        'pyname': u'thermal_conductivity_6',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 7',
                                       {'name': u'Temperature 7',
                                        'pyname': u'temperature_7',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 7',
                                       {'name': u'Thermal Conductivity 7',
                                        'pyname': u'thermal_conductivity_7',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 8',
                                       {'name': u'Temperature 8',
                                        'pyname': u'temperature_8',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 8',
                                       {'name': u'Thermal Conductivity 8',
                                        'pyname': u'thermal_conductivity_8',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 9',
                                       {'name': u'Temperature 9',
                                        'pyname': u'temperature_9',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 9',
                                       {'name': u'Thermal Conductivity 9',
                                        'pyname': u'thermal_conductivity_9',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'temperature 10',
                                       {'name': u'Temperature 10',
                                        'pyname': u'temperature_10',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal conductivity 10',
                                       {'name': u'Thermal Conductivity 10',
                                        'pyname': u'thermal_conductivity_10',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:VariableThermalConductivity',
               'pyname': u'MaterialPropertyVariableThermalConductivity',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Regular Material Name to which the additional properties will be added.
        |  this the material name for the basic material properties.

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
    def temperature_1(self):
        """field `Temperature 1`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_1` or None if not set

        """
        return self["Temperature 1"]

    @temperature_1.setter
    def temperature_1(self, value=None):
        """Corresponds to IDD field `Temperature 1`"""
        self["Temperature 1"] = value

    @property
    def thermal_conductivity_1(self):
        """field `Thermal Conductivity 1`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 1
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_1` or None if not set

        """
        return self["Thermal Conductivity 1"]

    @thermal_conductivity_1.setter
    def thermal_conductivity_1(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 1`"""
        self["Thermal Conductivity 1"] = value

    @property
    def temperature_2(self):
        """field `Temperature 2`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_2` or None if not set

        """
        return self["Temperature 2"]

    @temperature_2.setter
    def temperature_2(self, value=None):
        """Corresponds to IDD field `Temperature 2`"""
        self["Temperature 2"] = value

    @property
    def thermal_conductivity_2(self):
        """field `Thermal Conductivity 2`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 2
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_2` or None if not set

        """
        return self["Thermal Conductivity 2"]

    @thermal_conductivity_2.setter
    def thermal_conductivity_2(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 2`"""
        self["Thermal Conductivity 2"] = value

    @property
    def temperature_3(self):
        """field `Temperature 3`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_3` or None if not set

        """
        return self["Temperature 3"]

    @temperature_3.setter
    def temperature_3(self, value=None):
        """Corresponds to IDD field `Temperature 3`"""
        self["Temperature 3"] = value

    @property
    def thermal_conductivity_3(self):
        """field `Thermal Conductivity 3`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 3
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_3` or None if not set

        """
        return self["Thermal Conductivity 3"]

    @thermal_conductivity_3.setter
    def thermal_conductivity_3(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 3`"""
        self["Thermal Conductivity 3"] = value

    @property
    def temperature_4(self):
        """field `Temperature 4`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_4` or None if not set

        """
        return self["Temperature 4"]

    @temperature_4.setter
    def temperature_4(self, value=None):
        """Corresponds to IDD field `Temperature 4`"""
        self["Temperature 4"] = value

    @property
    def thermal_conductivity_4(self):
        """field `Thermal Conductivity 4`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 4
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_4` or None if not set

        """
        return self["Thermal Conductivity 4"]

    @thermal_conductivity_4.setter
    def thermal_conductivity_4(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 4`"""
        self["Thermal Conductivity 4"] = value

    @property
    def temperature_5(self):
        """field `Temperature 5`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_5` or None if not set

        """
        return self["Temperature 5"]

    @temperature_5.setter
    def temperature_5(self, value=None):
        """Corresponds to IDD field `Temperature 5`"""
        self["Temperature 5"] = value

    @property
    def thermal_conductivity_5(self):
        """field `Thermal Conductivity 5`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 5
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_5` or None if not set

        """
        return self["Thermal Conductivity 5"]

    @thermal_conductivity_5.setter
    def thermal_conductivity_5(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 5`"""
        self["Thermal Conductivity 5"] = value

    @property
    def temperature_6(self):
        """field `Temperature 6`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_6` or None if not set

        """
        return self["Temperature 6"]

    @temperature_6.setter
    def temperature_6(self, value=None):
        """Corresponds to IDD field `Temperature 6`"""
        self["Temperature 6"] = value

    @property
    def thermal_conductivity_6(self):
        """field `Thermal Conductivity 6`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 6
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_6` or None if not set

        """
        return self["Thermal Conductivity 6"]

    @thermal_conductivity_6.setter
    def thermal_conductivity_6(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 6`"""
        self["Thermal Conductivity 6"] = value

    @property
    def temperature_7(self):
        """field `Temperature 7`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_7` or None if not set

        """
        return self["Temperature 7"]

    @temperature_7.setter
    def temperature_7(self, value=None):
        """Corresponds to IDD field `Temperature 7`"""
        self["Temperature 7"] = value

    @property
    def thermal_conductivity_7(self):
        """field `Thermal Conductivity 7`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 7
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_7` or None if not set

        """
        return self["Thermal Conductivity 7"]

    @thermal_conductivity_7.setter
    def thermal_conductivity_7(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 7`"""
        self["Thermal Conductivity 7"] = value

    @property
    def temperature_8(self):
        """field `Temperature 8`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_8` or None if not set

        """
        return self["Temperature 8"]

    @temperature_8.setter
    def temperature_8(self, value=None):
        """Corresponds to IDD field `Temperature 8`"""
        self["Temperature 8"] = value

    @property
    def thermal_conductivity_8(self):
        """field `Thermal Conductivity 8`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 8
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_8` or None if not set

        """
        return self["Thermal Conductivity 8"]

    @thermal_conductivity_8.setter
    def thermal_conductivity_8(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 8`"""
        self["Thermal Conductivity 8"] = value

    @property
    def temperature_9(self):
        """field `Temperature 9`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_9` or None if not set

        """
        return self["Temperature 9"]

    @temperature_9.setter
    def temperature_9(self, value=None):
        """Corresponds to IDD field `Temperature 9`"""
        self["Temperature 9"] = value

    @property
    def thermal_conductivity_9(self):
        """field `Thermal Conductivity 9`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 9
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_9` or None if not set

        """
        return self["Thermal Conductivity 9"]

    @thermal_conductivity_9.setter
    def thermal_conductivity_9(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 9`"""
        self["Thermal Conductivity 9"] = value

    @property
    def temperature_10(self):
        """field `Temperature 10`

        |  for Temperature-Thermal Conductivity function
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_10` or None if not set

        """
        return self["Temperature 10"]

    @temperature_10.setter
    def temperature_10(self, value=None):
        """Corresponds to IDD field `Temperature 10`"""
        self["Temperature 10"] = value

    @property
    def thermal_conductivity_10(self):
        """field `Thermal Conductivity 10`

        |  for Temperature-Thermal Conductivity function corresponding to temperature 10
        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_10` or None if not set

        """
        return self["Thermal Conductivity 10"]

    @thermal_conductivity_10.setter
    def thermal_conductivity_10(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 10`"""
        self["Thermal Conductivity 10"] = value




class MaterialPropertyHeatAndMoistureTransferSettings(DataObject):

    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Settings`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Additional material properties for surfaces.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'porosity',
                                       {'name': u'Porosity',
                                        'pyname': u'porosity',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/m3'}),
                                      (u'initial water content ratio',
                                       {'name': u'Initial Water Content Ratio',
                                        'pyname': u'initial_water_content_ratio',
                                        'default': 0.2,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/kg'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:HeatAndMoistureTransfer:Settings',
               'pyname': u'MaterialPropertyHeatAndMoistureTransferSettings',
               'required-object': False,
               'unique-object': False}

    @property
    def material_name(self):
        """field `Material Name`

        |  Material Name that the moisture properties will be added to.
        |  This augments material properties needed for combined heat and moisture transfer for surfaces.

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
    def porosity(self):
        """field `Porosity`

        |  Units: m3/m3
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Porosity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `porosity` or None if not set

        """
        return self["Porosity"]

    @porosity.setter
    def porosity(self, value=None):
        """Corresponds to IDD field `Porosity`"""
        self["Porosity"] = value

    @property
    def initial_water_content_ratio(self):
        """field `Initial Water Content Ratio`

        |  units are the water/material density ratio at the beginning of each run period.
        |  Units: kg/kg
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Initial Water Content Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_water_content_ratio` or None if not set

        """
        return self["Initial Water Content Ratio"]

    @initial_water_content_ratio.setter
    def initial_water_content_ratio(self, value=0.2):
        """Corresponds to IDD field `Initial Water Content Ratio`"""
        self["Initial Water Content Ratio"] = value




class MaterialPropertyHeatAndMoistureTransferSorptionIsotherm(DataObject):

    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between moisture content and relative humidity fraction.
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of isotherm coordinates',
                                       {'name': u'Number of Isotherm Coordinates',
                                        'pyname': u'number_of_isotherm_coordinates',
                                        'maximum': 25,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'relative humidity fraction 1',
                                       {'name': u'Relative Humidity Fraction 1',
                                        'pyname': u'relative_humidity_fraction_1',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 1',
                                       {'name': u'Moisture Content 1',
                                        'pyname': u'moisture_content_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 2',
                                       {'name': u'Relative Humidity Fraction 2',
                                        'pyname': u'relative_humidity_fraction_2',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 2',
                                       {'name': u'Moisture Content 2',
                                        'pyname': u'moisture_content_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 3',
                                       {'name': u'Relative Humidity Fraction 3',
                                        'pyname': u'relative_humidity_fraction_3',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 3',
                                       {'name': u'Moisture Content 3',
                                        'pyname': u'moisture_content_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 4',
                                       {'name': u'Relative Humidity Fraction 4',
                                        'pyname': u'relative_humidity_fraction_4',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 4',
                                       {'name': u'Moisture Content 4',
                                        'pyname': u'moisture_content_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 5',
                                       {'name': u'Relative Humidity Fraction 5',
                                        'pyname': u'relative_humidity_fraction_5',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 5',
                                       {'name': u'Moisture Content 5',
                                        'pyname': u'moisture_content_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 6',
                                       {'name': u'Relative Humidity Fraction 6',
                                        'pyname': u'relative_humidity_fraction_6',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 6',
                                       {'name': u'Moisture Content 6',
                                        'pyname': u'moisture_content_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 7',
                                       {'name': u'Relative Humidity Fraction 7',
                                        'pyname': u'relative_humidity_fraction_7',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 7',
                                       {'name': u'Moisture Content 7',
                                        'pyname': u'moisture_content_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 8',
                                       {'name': u'Relative Humidity Fraction 8',
                                        'pyname': u'relative_humidity_fraction_8',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 8',
                                       {'name': u'Moisture Content 8',
                                        'pyname': u'moisture_content_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 9',
                                       {'name': u'Relative Humidity Fraction 9',
                                        'pyname': u'relative_humidity_fraction_9',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 9',
                                       {'name': u'Moisture Content 9',
                                        'pyname': u'moisture_content_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 10',
                                       {'name': u'Relative Humidity Fraction 10',
                                        'pyname': u'relative_humidity_fraction_10',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 10',
                                       {'name': u'Moisture Content 10',
                                        'pyname': u'moisture_content_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 11',
                                       {'name': u'Relative Humidity Fraction 11',
                                        'pyname': u'relative_humidity_fraction_11',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 11',
                                       {'name': u'Moisture Content 11',
                                        'pyname': u'moisture_content_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 12',
                                       {'name': u'Relative Humidity Fraction 12',
                                        'pyname': u'relative_humidity_fraction_12',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 12',
                                       {'name': u'Moisture Content 12',
                                        'pyname': u'moisture_content_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 13',
                                       {'name': u'Relative Humidity Fraction 13',
                                        'pyname': u'relative_humidity_fraction_13',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 13',
                                       {'name': u'Moisture Content 13',
                                        'pyname': u'moisture_content_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 14',
                                       {'name': u'Relative Humidity Fraction 14',
                                        'pyname': u'relative_humidity_fraction_14',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 14',
                                       {'name': u'Moisture Content 14',
                                        'pyname': u'moisture_content_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 15',
                                       {'name': u'Relative Humidity Fraction 15',
                                        'pyname': u'relative_humidity_fraction_15',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 15',
                                       {'name': u'Moisture Content 15',
                                        'pyname': u'moisture_content_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 16',
                                       {'name': u'Relative Humidity Fraction 16',
                                        'pyname': u'relative_humidity_fraction_16',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 16',
                                       {'name': u'Moisture Content 16',
                                        'pyname': u'moisture_content_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 17',
                                       {'name': u'Relative Humidity Fraction 17',
                                        'pyname': u'relative_humidity_fraction_17',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 17',
                                       {'name': u'Moisture Content 17',
                                        'pyname': u'moisture_content_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 18',
                                       {'name': u'Relative Humidity Fraction 18',
                                        'pyname': u'relative_humidity_fraction_18',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 18',
                                       {'name': u'Moisture Content 18',
                                        'pyname': u'moisture_content_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 19',
                                       {'name': u'Relative Humidity Fraction 19',
                                        'pyname': u'relative_humidity_fraction_19',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 19',
                                       {'name': u'Moisture Content 19',
                                        'pyname': u'moisture_content_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 20',
                                       {'name': u'Relative Humidity Fraction 20',
                                        'pyname': u'relative_humidity_fraction_20',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 20',
                                       {'name': u'Moisture Content 20',
                                        'pyname': u'moisture_content_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 21',
                                       {'name': u'Relative Humidity Fraction 21',
                                        'pyname': u'relative_humidity_fraction_21',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 21',
                                       {'name': u'Moisture Content 21',
                                        'pyname': u'moisture_content_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 22',
                                       {'name': u'Relative Humidity Fraction 22',
                                        'pyname': u'relative_humidity_fraction_22',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 22',
                                       {'name': u'Moisture Content 22',
                                        'pyname': u'moisture_content_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 23',
                                       {'name': u'Relative Humidity Fraction 23',
                                        'pyname': u'relative_humidity_fraction_23',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 23',
                                       {'name': u'Moisture Content 23',
                                        'pyname': u'moisture_content_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 24',
                                       {'name': u'Relative Humidity Fraction 24',
                                        'pyname': u'relative_humidity_fraction_24',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 24',
                                       {'name': u'Moisture Content 24',
                                        'pyname': u'moisture_content_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'relative humidity fraction 25',
                                       {'name': u'Relative Humidity Fraction 25',
                                        'pyname': u'relative_humidity_fraction_25',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'moisture content 25',
                                       {'name': u'Moisture Content 25',
                                        'pyname': u'moisture_content_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm',
               'pyname': u'MaterialPropertyHeatAndMoistureTransferSorptionIsotherm',
               'required-object': False,
               'unique-object': False}

    @property
    def material_name(self):
        """field `Material Name`

        |  The Material Name that the moisture sorption isotherm will be added to.

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
    def number_of_isotherm_coordinates(self):
        """field `Number of Isotherm Coordinates`

        |  Number of data Coordinates
        |  value >= 1
        |  value <= 25

        Args:
            value (int): value for IDD Field `Number of Isotherm Coordinates`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_isotherm_coordinates` or None if not set

        """
        return self["Number of Isotherm Coordinates"]

    @number_of_isotherm_coordinates.setter
    def number_of_isotherm_coordinates(self, value=None):
        """Corresponds to IDD field `Number of Isotherm Coordinates`"""
        self["Number of Isotherm Coordinates"] = value

    @property
    def relative_humidity_fraction_1(self):
        """field `Relative Humidity Fraction 1`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_1` or None if not set

        """
        return self["Relative Humidity Fraction 1"]

    @relative_humidity_fraction_1.setter
    def relative_humidity_fraction_1(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 1`"""
        self["Relative Humidity Fraction 1"] = value

    @property
    def moisture_content_1(self):
        """field `Moisture Content 1`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_1` or None if not set

        """
        return self["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """Corresponds to IDD field `Moisture Content 1`"""
        self["Moisture Content 1"] = value

    @property
    def relative_humidity_fraction_2(self):
        """field `Relative Humidity Fraction 2`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_2` or None if not set

        """
        return self["Relative Humidity Fraction 2"]

    @relative_humidity_fraction_2.setter
    def relative_humidity_fraction_2(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 2`"""
        self["Relative Humidity Fraction 2"] = value

    @property
    def moisture_content_2(self):
        """field `Moisture Content 2`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_2` or None if not set

        """
        return self["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """Corresponds to IDD field `Moisture Content 2`"""
        self["Moisture Content 2"] = value

    @property
    def relative_humidity_fraction_3(self):
        """field `Relative Humidity Fraction 3`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_3` or None if not set

        """
        return self["Relative Humidity Fraction 3"]

    @relative_humidity_fraction_3.setter
    def relative_humidity_fraction_3(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 3`"""
        self["Relative Humidity Fraction 3"] = value

    @property
    def moisture_content_3(self):
        """field `Moisture Content 3`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_3` or None if not set

        """
        return self["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """Corresponds to IDD field `Moisture Content 3`"""
        self["Moisture Content 3"] = value

    @property
    def relative_humidity_fraction_4(self):
        """field `Relative Humidity Fraction 4`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_4` or None if not set

        """
        return self["Relative Humidity Fraction 4"]

    @relative_humidity_fraction_4.setter
    def relative_humidity_fraction_4(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 4`"""
        self["Relative Humidity Fraction 4"] = value

    @property
    def moisture_content_4(self):
        """field `Moisture Content 4`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_4` or None if not set

        """
        return self["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """Corresponds to IDD field `Moisture Content 4`"""
        self["Moisture Content 4"] = value

    @property
    def relative_humidity_fraction_5(self):
        """field `Relative Humidity Fraction 5`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_5` or None if not set

        """
        return self["Relative Humidity Fraction 5"]

    @relative_humidity_fraction_5.setter
    def relative_humidity_fraction_5(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 5`"""
        self["Relative Humidity Fraction 5"] = value

    @property
    def moisture_content_5(self):
        """field `Moisture Content 5`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_5` or None if not set

        """
        return self["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """Corresponds to IDD field `Moisture Content 5`"""
        self["Moisture Content 5"] = value

    @property
    def relative_humidity_fraction_6(self):
        """field `Relative Humidity Fraction 6`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_6` or None if not set

        """
        return self["Relative Humidity Fraction 6"]

    @relative_humidity_fraction_6.setter
    def relative_humidity_fraction_6(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 6`"""
        self["Relative Humidity Fraction 6"] = value

    @property
    def moisture_content_6(self):
        """field `Moisture Content 6`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_6` or None if not set

        """
        return self["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """Corresponds to IDD field `Moisture Content 6`"""
        self["Moisture Content 6"] = value

    @property
    def relative_humidity_fraction_7(self):
        """field `Relative Humidity Fraction 7`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_7` or None if not set

        """
        return self["Relative Humidity Fraction 7"]

    @relative_humidity_fraction_7.setter
    def relative_humidity_fraction_7(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 7`"""
        self["Relative Humidity Fraction 7"] = value

    @property
    def moisture_content_7(self):
        """field `Moisture Content 7`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_7` or None if not set

        """
        return self["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """Corresponds to IDD field `Moisture Content 7`"""
        self["Moisture Content 7"] = value

    @property
    def relative_humidity_fraction_8(self):
        """field `Relative Humidity Fraction 8`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_8` or None if not set

        """
        return self["Relative Humidity Fraction 8"]

    @relative_humidity_fraction_8.setter
    def relative_humidity_fraction_8(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 8`"""
        self["Relative Humidity Fraction 8"] = value

    @property
    def moisture_content_8(self):
        """field `Moisture Content 8`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_8` or None if not set

        """
        return self["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """Corresponds to IDD field `Moisture Content 8`"""
        self["Moisture Content 8"] = value

    @property
    def relative_humidity_fraction_9(self):
        """field `Relative Humidity Fraction 9`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_9` or None if not set

        """
        return self["Relative Humidity Fraction 9"]

    @relative_humidity_fraction_9.setter
    def relative_humidity_fraction_9(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 9`"""
        self["Relative Humidity Fraction 9"] = value

    @property
    def moisture_content_9(self):
        """field `Moisture Content 9`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_9` or None if not set

        """
        return self["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """Corresponds to IDD field `Moisture Content 9`"""
        self["Moisture Content 9"] = value

    @property
    def relative_humidity_fraction_10(self):
        """field `Relative Humidity Fraction 10`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_10` or None if not set

        """
        return self["Relative Humidity Fraction 10"]

    @relative_humidity_fraction_10.setter
    def relative_humidity_fraction_10(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 10`"""
        self["Relative Humidity Fraction 10"] = value

    @property
    def moisture_content_10(self):
        """field `Moisture Content 10`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_10` or None if not set

        """
        return self["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """Corresponds to IDD field `Moisture Content 10`"""
        self["Moisture Content 10"] = value

    @property
    def relative_humidity_fraction_11(self):
        """field `Relative Humidity Fraction 11`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_11` or None if not set

        """
        return self["Relative Humidity Fraction 11"]

    @relative_humidity_fraction_11.setter
    def relative_humidity_fraction_11(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 11`"""
        self["Relative Humidity Fraction 11"] = value

    @property
    def moisture_content_11(self):
        """field `Moisture Content 11`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_11` or None if not set

        """
        return self["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """Corresponds to IDD field `Moisture Content 11`"""
        self["Moisture Content 11"] = value

    @property
    def relative_humidity_fraction_12(self):
        """field `Relative Humidity Fraction 12`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_12` or None if not set

        """
        return self["Relative Humidity Fraction 12"]

    @relative_humidity_fraction_12.setter
    def relative_humidity_fraction_12(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 12`"""
        self["Relative Humidity Fraction 12"] = value

    @property
    def moisture_content_12(self):
        """field `Moisture Content 12`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_12` or None if not set

        """
        return self["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """Corresponds to IDD field `Moisture Content 12`"""
        self["Moisture Content 12"] = value

    @property
    def relative_humidity_fraction_13(self):
        """field `Relative Humidity Fraction 13`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_13` or None if not set

        """
        return self["Relative Humidity Fraction 13"]

    @relative_humidity_fraction_13.setter
    def relative_humidity_fraction_13(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 13`"""
        self["Relative Humidity Fraction 13"] = value

    @property
    def moisture_content_13(self):
        """field `Moisture Content 13`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_13` or None if not set

        """
        return self["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """Corresponds to IDD field `Moisture Content 13`"""
        self["Moisture Content 13"] = value

    @property
    def relative_humidity_fraction_14(self):
        """field `Relative Humidity Fraction 14`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_14` or None if not set

        """
        return self["Relative Humidity Fraction 14"]

    @relative_humidity_fraction_14.setter
    def relative_humidity_fraction_14(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 14`"""
        self["Relative Humidity Fraction 14"] = value

    @property
    def moisture_content_14(self):
        """field `Moisture Content 14`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_14` or None if not set

        """
        return self["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """Corresponds to IDD field `Moisture Content 14`"""
        self["Moisture Content 14"] = value

    @property
    def relative_humidity_fraction_15(self):
        """field `Relative Humidity Fraction 15`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_15` or None if not set

        """
        return self["Relative Humidity Fraction 15"]

    @relative_humidity_fraction_15.setter
    def relative_humidity_fraction_15(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 15`"""
        self["Relative Humidity Fraction 15"] = value

    @property
    def moisture_content_15(self):
        """field `Moisture Content 15`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_15` or None if not set

        """
        return self["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """Corresponds to IDD field `Moisture Content 15`"""
        self["Moisture Content 15"] = value

    @property
    def relative_humidity_fraction_16(self):
        """field `Relative Humidity Fraction 16`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_16` or None if not set

        """
        return self["Relative Humidity Fraction 16"]

    @relative_humidity_fraction_16.setter
    def relative_humidity_fraction_16(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 16`"""
        self["Relative Humidity Fraction 16"] = value

    @property
    def moisture_content_16(self):
        """field `Moisture Content 16`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_16` or None if not set

        """
        return self["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """Corresponds to IDD field `Moisture Content 16`"""
        self["Moisture Content 16"] = value

    @property
    def relative_humidity_fraction_17(self):
        """field `Relative Humidity Fraction 17`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_17` or None if not set

        """
        return self["Relative Humidity Fraction 17"]

    @relative_humidity_fraction_17.setter
    def relative_humidity_fraction_17(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 17`"""
        self["Relative Humidity Fraction 17"] = value

    @property
    def moisture_content_17(self):
        """field `Moisture Content 17`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_17` or None if not set

        """
        return self["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """Corresponds to IDD field `Moisture Content 17`"""
        self["Moisture Content 17"] = value

    @property
    def relative_humidity_fraction_18(self):
        """field `Relative Humidity Fraction 18`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_18` or None if not set

        """
        return self["Relative Humidity Fraction 18"]

    @relative_humidity_fraction_18.setter
    def relative_humidity_fraction_18(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 18`"""
        self["Relative Humidity Fraction 18"] = value

    @property
    def moisture_content_18(self):
        """field `Moisture Content 18`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_18` or None if not set

        """
        return self["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """Corresponds to IDD field `Moisture Content 18`"""
        self["Moisture Content 18"] = value

    @property
    def relative_humidity_fraction_19(self):
        """field `Relative Humidity Fraction 19`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_19` or None if not set

        """
        return self["Relative Humidity Fraction 19"]

    @relative_humidity_fraction_19.setter
    def relative_humidity_fraction_19(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 19`"""
        self["Relative Humidity Fraction 19"] = value

    @property
    def moisture_content_19(self):
        """field `Moisture Content 19`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_19` or None if not set

        """
        return self["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """Corresponds to IDD field `Moisture Content 19`"""
        self["Moisture Content 19"] = value

    @property
    def relative_humidity_fraction_20(self):
        """field `Relative Humidity Fraction 20`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_20` or None if not set

        """
        return self["Relative Humidity Fraction 20"]

    @relative_humidity_fraction_20.setter
    def relative_humidity_fraction_20(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 20`"""
        self["Relative Humidity Fraction 20"] = value

    @property
    def moisture_content_20(self):
        """field `Moisture Content 20`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_20` or None if not set

        """
        return self["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """Corresponds to IDD field `Moisture Content 20`"""
        self["Moisture Content 20"] = value

    @property
    def relative_humidity_fraction_21(self):
        """field `Relative Humidity Fraction 21`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_21` or None if not set

        """
        return self["Relative Humidity Fraction 21"]

    @relative_humidity_fraction_21.setter
    def relative_humidity_fraction_21(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 21`"""
        self["Relative Humidity Fraction 21"] = value

    @property
    def moisture_content_21(self):
        """field `Moisture Content 21`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_21` or None if not set

        """
        return self["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """Corresponds to IDD field `Moisture Content 21`"""
        self["Moisture Content 21"] = value

    @property
    def relative_humidity_fraction_22(self):
        """field `Relative Humidity Fraction 22`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_22` or None if not set

        """
        return self["Relative Humidity Fraction 22"]

    @relative_humidity_fraction_22.setter
    def relative_humidity_fraction_22(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 22`"""
        self["Relative Humidity Fraction 22"] = value

    @property
    def moisture_content_22(self):
        """field `Moisture Content 22`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_22` or None if not set

        """
        return self["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """Corresponds to IDD field `Moisture Content 22`"""
        self["Moisture Content 22"] = value

    @property
    def relative_humidity_fraction_23(self):
        """field `Relative Humidity Fraction 23`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_23` or None if not set

        """
        return self["Relative Humidity Fraction 23"]

    @relative_humidity_fraction_23.setter
    def relative_humidity_fraction_23(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 23`"""
        self["Relative Humidity Fraction 23"] = value

    @property
    def moisture_content_23(self):
        """field `Moisture Content 23`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_23` or None if not set

        """
        return self["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """Corresponds to IDD field `Moisture Content 23`"""
        self["Moisture Content 23"] = value

    @property
    def relative_humidity_fraction_24(self):
        """field `Relative Humidity Fraction 24`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_24` or None if not set

        """
        return self["Relative Humidity Fraction 24"]

    @relative_humidity_fraction_24.setter
    def relative_humidity_fraction_24(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 24`"""
        self["Relative Humidity Fraction 24"] = value

    @property
    def moisture_content_24(self):
        """field `Moisture Content 24`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_24` or None if not set

        """
        return self["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """Corresponds to IDD field `Moisture Content 24`"""
        self["Moisture Content 24"] = value

    @property
    def relative_humidity_fraction_25(self):
        """field `Relative Humidity Fraction 25`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_25` or None if not set

        """
        return self["Relative Humidity Fraction 25"]

    @relative_humidity_fraction_25.setter
    def relative_humidity_fraction_25(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 25`"""
        self["Relative Humidity Fraction 25"] = value

    @property
    def moisture_content_25(self):
        """field `Moisture Content 25`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_25` or None if not set

        """
        return self["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """Corresponds to IDD field `Moisture Content 25`"""
        self["Moisture Content 25"] = value




class MaterialPropertyHeatAndMoistureTransferSuction(DataObject):

    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Suction`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between liquid suction transport coefficient and moisture content
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of suction points',
                                       {'name': u'Number of Suction points',
                                        'pyname': u'number_of_suction_points',
                                        'maximum': 25,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'moisture content 1',
                                       {'name': u'Moisture Content 1',
                                        'pyname': u'moisture_content_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 1',
                                       {'name': u'Liquid Transport Coefficient 1',
                                        'pyname': u'liquid_transport_coefficient_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 2',
                                       {'name': u'Moisture Content 2',
                                        'pyname': u'moisture_content_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 2',
                                       {'name': u'Liquid Transport Coefficient 2',
                                        'pyname': u'liquid_transport_coefficient_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 3',
                                       {'name': u'Moisture Content 3',
                                        'pyname': u'moisture_content_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 3',
                                       {'name': u'Liquid Transport Coefficient 3',
                                        'pyname': u'liquid_transport_coefficient_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 4',
                                       {'name': u'Moisture Content 4',
                                        'pyname': u'moisture_content_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 4',
                                       {'name': u'Liquid Transport Coefficient 4',
                                        'pyname': u'liquid_transport_coefficient_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 5',
                                       {'name': u'Moisture Content 5',
                                        'pyname': u'moisture_content_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 5',
                                       {'name': u'Liquid Transport Coefficient 5',
                                        'pyname': u'liquid_transport_coefficient_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 6',
                                       {'name': u'Moisture Content 6',
                                        'pyname': u'moisture_content_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 6',
                                       {'name': u'Liquid Transport Coefficient 6',
                                        'pyname': u'liquid_transport_coefficient_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 7',
                                       {'name': u'Moisture Content 7',
                                        'pyname': u'moisture_content_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 7',
                                       {'name': u'Liquid Transport Coefficient 7',
                                        'pyname': u'liquid_transport_coefficient_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 8',
                                       {'name': u'Moisture Content 8',
                                        'pyname': u'moisture_content_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 8',
                                       {'name': u'Liquid Transport Coefficient 8',
                                        'pyname': u'liquid_transport_coefficient_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 9',
                                       {'name': u'Moisture Content 9',
                                        'pyname': u'moisture_content_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 9',
                                       {'name': u'Liquid Transport Coefficient 9',
                                        'pyname': u'liquid_transport_coefficient_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 10',
                                       {'name': u'Moisture Content 10',
                                        'pyname': u'moisture_content_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 10',
                                       {'name': u'Liquid Transport Coefficient 10',
                                        'pyname': u'liquid_transport_coefficient_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 11',
                                       {'name': u'Moisture Content 11',
                                        'pyname': u'moisture_content_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 11',
                                       {'name': u'Liquid Transport Coefficient 11',
                                        'pyname': u'liquid_transport_coefficient_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 12',
                                       {'name': u'Moisture Content 12',
                                        'pyname': u'moisture_content_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 12',
                                       {'name': u'Liquid Transport Coefficient 12',
                                        'pyname': u'liquid_transport_coefficient_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 13',
                                       {'name': u'Moisture Content 13',
                                        'pyname': u'moisture_content_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 13',
                                       {'name': u'Liquid Transport Coefficient 13',
                                        'pyname': u'liquid_transport_coefficient_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 14',
                                       {'name': u'Moisture Content 14',
                                        'pyname': u'moisture_content_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 14',
                                       {'name': u'Liquid Transport Coefficient 14',
                                        'pyname': u'liquid_transport_coefficient_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 15',
                                       {'name': u'Moisture Content 15',
                                        'pyname': u'moisture_content_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 15',
                                       {'name': u'Liquid Transport Coefficient 15',
                                        'pyname': u'liquid_transport_coefficient_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 16',
                                       {'name': u'Moisture Content 16',
                                        'pyname': u'moisture_content_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 16',
                                       {'name': u'Liquid Transport Coefficient 16',
                                        'pyname': u'liquid_transport_coefficient_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 17',
                                       {'name': u'Moisture Content 17',
                                        'pyname': u'moisture_content_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 17',
                                       {'name': u'Liquid Transport Coefficient 17',
                                        'pyname': u'liquid_transport_coefficient_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 18',
                                       {'name': u'Moisture Content 18',
                                        'pyname': u'moisture_content_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 18',
                                       {'name': u'Liquid Transport Coefficient 18',
                                        'pyname': u'liquid_transport_coefficient_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 19',
                                       {'name': u'Moisture Content 19',
                                        'pyname': u'moisture_content_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 19',
                                       {'name': u'Liquid Transport Coefficient 19',
                                        'pyname': u'liquid_transport_coefficient_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 20',
                                       {'name': u'Moisture Content 20',
                                        'pyname': u'moisture_content_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 20',
                                       {'name': u'Liquid Transport Coefficient 20',
                                        'pyname': u'liquid_transport_coefficient_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 21',
                                       {'name': u'Moisture Content 21',
                                        'pyname': u'moisture_content_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 21',
                                       {'name': u'Liquid Transport Coefficient 21',
                                        'pyname': u'liquid_transport_coefficient_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 22',
                                       {'name': u'Moisture Content 22',
                                        'pyname': u'moisture_content_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 22',
                                       {'name': u'Liquid Transport Coefficient 22',
                                        'pyname': u'liquid_transport_coefficient_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 23',
                                       {'name': u'Moisture Content 23',
                                        'pyname': u'moisture_content_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 23',
                                       {'name': u'Liquid Transport Coefficient 23',
                                        'pyname': u'liquid_transport_coefficient_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 24',
                                       {'name': u'Moisture Content 24',
                                        'pyname': u'moisture_content_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 24',
                                       {'name': u'Liquid Transport Coefficient 24',
                                        'pyname': u'liquid_transport_coefficient_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 25',
                                       {'name': u'Moisture Content 25',
                                        'pyname': u'moisture_content_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 25',
                                       {'name': u'Liquid Transport Coefficient 25',
                                        'pyname': u'liquid_transport_coefficient_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:HeatAndMoistureTransfer:Suction',
               'pyname': u'MaterialPropertyHeatAndMoistureTransferSuction',
               'required-object': False,
               'unique-object': False}

    @property
    def material_name(self):
        """field `Material Name`

        |  Material Name that the moisture properties will be added to.

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
    def number_of_suction_points(self):
        """field `Number of Suction points`

        |  Number of Suction Liquid Transport Coefficient coordinates
        |  value >= 1
        |  value <= 25

        Args:
            value (int): value for IDD Field `Number of Suction points`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_suction_points` or None if not set

        """
        return self["Number of Suction points"]

    @number_of_suction_points.setter
    def number_of_suction_points(self, value=None):
        """Corresponds to IDD field `Number of Suction points`"""
        self["Number of Suction points"] = value

    @property
    def moisture_content_1(self):
        """field `Moisture Content 1`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_1` or None if not set

        """
        return self["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """Corresponds to IDD field `Moisture Content 1`"""
        self["Moisture Content 1"] = value

    @property
    def liquid_transport_coefficient_1(self):
        """field `Liquid Transport Coefficient 1`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_1` or None if not set

        """
        return self["Liquid Transport Coefficient 1"]

    @liquid_transport_coefficient_1.setter
    def liquid_transport_coefficient_1(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 1`"""
        self["Liquid Transport Coefficient 1"] = value

    @property
    def moisture_content_2(self):
        """field `Moisture Content 2`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_2` or None if not set

        """
        return self["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """Corresponds to IDD field `Moisture Content 2`"""
        self["Moisture Content 2"] = value

    @property
    def liquid_transport_coefficient_2(self):
        """field `Liquid Transport Coefficient 2`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_2` or None if not set

        """
        return self["Liquid Transport Coefficient 2"]

    @liquid_transport_coefficient_2.setter
    def liquid_transport_coefficient_2(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 2`"""
        self["Liquid Transport Coefficient 2"] = value

    @property
    def moisture_content_3(self):
        """field `Moisture Content 3`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_3` or None if not set

        """
        return self["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """Corresponds to IDD field `Moisture Content 3`"""
        self["Moisture Content 3"] = value

    @property
    def liquid_transport_coefficient_3(self):
        """field `Liquid Transport Coefficient 3`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_3` or None if not set

        """
        return self["Liquid Transport Coefficient 3"]

    @liquid_transport_coefficient_3.setter
    def liquid_transport_coefficient_3(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 3`"""
        self["Liquid Transport Coefficient 3"] = value

    @property
    def moisture_content_4(self):
        """field `Moisture Content 4`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_4` or None if not set

        """
        return self["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """Corresponds to IDD field `Moisture Content 4`"""
        self["Moisture Content 4"] = value

    @property
    def liquid_transport_coefficient_4(self):
        """field `Liquid Transport Coefficient 4`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_4` or None if not set

        """
        return self["Liquid Transport Coefficient 4"]

    @liquid_transport_coefficient_4.setter
    def liquid_transport_coefficient_4(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 4`"""
        self["Liquid Transport Coefficient 4"] = value

    @property
    def moisture_content_5(self):
        """field `Moisture Content 5`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_5` or None if not set

        """
        return self["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """Corresponds to IDD field `Moisture Content 5`"""
        self["Moisture Content 5"] = value

    @property
    def liquid_transport_coefficient_5(self):
        """field `Liquid Transport Coefficient 5`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_5` or None if not set

        """
        return self["Liquid Transport Coefficient 5"]

    @liquid_transport_coefficient_5.setter
    def liquid_transport_coefficient_5(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 5`"""
        self["Liquid Transport Coefficient 5"] = value

    @property
    def moisture_content_6(self):
        """field `Moisture Content 6`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_6` or None if not set

        """
        return self["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """Corresponds to IDD field `Moisture Content 6`"""
        self["Moisture Content 6"] = value

    @property
    def liquid_transport_coefficient_6(self):
        """field `Liquid Transport Coefficient 6`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_6` or None if not set

        """
        return self["Liquid Transport Coefficient 6"]

    @liquid_transport_coefficient_6.setter
    def liquid_transport_coefficient_6(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 6`"""
        self["Liquid Transport Coefficient 6"] = value

    @property
    def moisture_content_7(self):
        """field `Moisture Content 7`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_7` or None if not set

        """
        return self["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """Corresponds to IDD field `Moisture Content 7`"""
        self["Moisture Content 7"] = value

    @property
    def liquid_transport_coefficient_7(self):
        """field `Liquid Transport Coefficient 7`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_7` or None if not set

        """
        return self["Liquid Transport Coefficient 7"]

    @liquid_transport_coefficient_7.setter
    def liquid_transport_coefficient_7(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 7`"""
        self["Liquid Transport Coefficient 7"] = value

    @property
    def moisture_content_8(self):
        """field `Moisture Content 8`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_8` or None if not set

        """
        return self["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """Corresponds to IDD field `Moisture Content 8`"""
        self["Moisture Content 8"] = value

    @property
    def liquid_transport_coefficient_8(self):
        """field `Liquid Transport Coefficient 8`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_8` or None if not set

        """
        return self["Liquid Transport Coefficient 8"]

    @liquid_transport_coefficient_8.setter
    def liquid_transport_coefficient_8(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 8`"""
        self["Liquid Transport Coefficient 8"] = value

    @property
    def moisture_content_9(self):
        """field `Moisture Content 9`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_9` or None if not set

        """
        return self["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """Corresponds to IDD field `Moisture Content 9`"""
        self["Moisture Content 9"] = value

    @property
    def liquid_transport_coefficient_9(self):
        """field `Liquid Transport Coefficient 9`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_9` or None if not set

        """
        return self["Liquid Transport Coefficient 9"]

    @liquid_transport_coefficient_9.setter
    def liquid_transport_coefficient_9(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 9`"""
        self["Liquid Transport Coefficient 9"] = value

    @property
    def moisture_content_10(self):
        """field `Moisture Content 10`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_10` or None if not set

        """
        return self["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """Corresponds to IDD field `Moisture Content 10`"""
        self["Moisture Content 10"] = value

    @property
    def liquid_transport_coefficient_10(self):
        """field `Liquid Transport Coefficient 10`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_10` or None if not set

        """
        return self["Liquid Transport Coefficient 10"]

    @liquid_transport_coefficient_10.setter
    def liquid_transport_coefficient_10(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 10`"""
        self["Liquid Transport Coefficient 10"] = value

    @property
    def moisture_content_11(self):
        """field `Moisture Content 11`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_11` or None if not set

        """
        return self["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """Corresponds to IDD field `Moisture Content 11`"""
        self["Moisture Content 11"] = value

    @property
    def liquid_transport_coefficient_11(self):
        """field `Liquid Transport Coefficient 11`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_11` or None if not set

        """
        return self["Liquid Transport Coefficient 11"]

    @liquid_transport_coefficient_11.setter
    def liquid_transport_coefficient_11(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 11`"""
        self["Liquid Transport Coefficient 11"] = value

    @property
    def moisture_content_12(self):
        """field `Moisture Content 12`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_12` or None if not set

        """
        return self["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """Corresponds to IDD field `Moisture Content 12`"""
        self["Moisture Content 12"] = value

    @property
    def liquid_transport_coefficient_12(self):
        """field `Liquid Transport Coefficient 12`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_12` or None if not set

        """
        return self["Liquid Transport Coefficient 12"]

    @liquid_transport_coefficient_12.setter
    def liquid_transport_coefficient_12(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 12`"""
        self["Liquid Transport Coefficient 12"] = value

    @property
    def moisture_content_13(self):
        """field `Moisture Content 13`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_13` or None if not set

        """
        return self["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """Corresponds to IDD field `Moisture Content 13`"""
        self["Moisture Content 13"] = value

    @property
    def liquid_transport_coefficient_13(self):
        """field `Liquid Transport Coefficient 13`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_13` or None if not set

        """
        return self["Liquid Transport Coefficient 13"]

    @liquid_transport_coefficient_13.setter
    def liquid_transport_coefficient_13(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 13`"""
        self["Liquid Transport Coefficient 13"] = value

    @property
    def moisture_content_14(self):
        """field `Moisture Content 14`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_14` or None if not set

        """
        return self["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """Corresponds to IDD field `Moisture Content 14`"""
        self["Moisture Content 14"] = value

    @property
    def liquid_transport_coefficient_14(self):
        """field `Liquid Transport Coefficient 14`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_14` or None if not set

        """
        return self["Liquid Transport Coefficient 14"]

    @liquid_transport_coefficient_14.setter
    def liquid_transport_coefficient_14(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 14`"""
        self["Liquid Transport Coefficient 14"] = value

    @property
    def moisture_content_15(self):
        """field `Moisture Content 15`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_15` or None if not set

        """
        return self["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """Corresponds to IDD field `Moisture Content 15`"""
        self["Moisture Content 15"] = value

    @property
    def liquid_transport_coefficient_15(self):
        """field `Liquid Transport Coefficient 15`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_15` or None if not set

        """
        return self["Liquid Transport Coefficient 15"]

    @liquid_transport_coefficient_15.setter
    def liquid_transport_coefficient_15(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 15`"""
        self["Liquid Transport Coefficient 15"] = value

    @property
    def moisture_content_16(self):
        """field `Moisture Content 16`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_16` or None if not set

        """
        return self["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """Corresponds to IDD field `Moisture Content 16`"""
        self["Moisture Content 16"] = value

    @property
    def liquid_transport_coefficient_16(self):
        """field `Liquid Transport Coefficient 16`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_16` or None if not set

        """
        return self["Liquid Transport Coefficient 16"]

    @liquid_transport_coefficient_16.setter
    def liquid_transport_coefficient_16(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 16`"""
        self["Liquid Transport Coefficient 16"] = value

    @property
    def moisture_content_17(self):
        """field `Moisture Content 17`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_17` or None if not set

        """
        return self["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """Corresponds to IDD field `Moisture Content 17`"""
        self["Moisture Content 17"] = value

    @property
    def liquid_transport_coefficient_17(self):
        """field `Liquid Transport Coefficient 17`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_17` or None if not set

        """
        return self["Liquid Transport Coefficient 17"]

    @liquid_transport_coefficient_17.setter
    def liquid_transport_coefficient_17(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 17`"""
        self["Liquid Transport Coefficient 17"] = value

    @property
    def moisture_content_18(self):
        """field `Moisture Content 18`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_18` or None if not set

        """
        return self["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """Corresponds to IDD field `Moisture Content 18`"""
        self["Moisture Content 18"] = value

    @property
    def liquid_transport_coefficient_18(self):
        """field `Liquid Transport Coefficient 18`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_18` or None if not set

        """
        return self["Liquid Transport Coefficient 18"]

    @liquid_transport_coefficient_18.setter
    def liquid_transport_coefficient_18(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 18`"""
        self["Liquid Transport Coefficient 18"] = value

    @property
    def moisture_content_19(self):
        """field `Moisture Content 19`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_19` or None if not set

        """
        return self["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """Corresponds to IDD field `Moisture Content 19`"""
        self["Moisture Content 19"] = value

    @property
    def liquid_transport_coefficient_19(self):
        """field `Liquid Transport Coefficient 19`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_19` or None if not set

        """
        return self["Liquid Transport Coefficient 19"]

    @liquid_transport_coefficient_19.setter
    def liquid_transport_coefficient_19(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 19`"""
        self["Liquid Transport Coefficient 19"] = value

    @property
    def moisture_content_20(self):
        """field `Moisture Content 20`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_20` or None if not set

        """
        return self["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """Corresponds to IDD field `Moisture Content 20`"""
        self["Moisture Content 20"] = value

    @property
    def liquid_transport_coefficient_20(self):
        """field `Liquid Transport Coefficient 20`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_20` or None if not set

        """
        return self["Liquid Transport Coefficient 20"]

    @liquid_transport_coefficient_20.setter
    def liquid_transport_coefficient_20(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 20`"""
        self["Liquid Transport Coefficient 20"] = value

    @property
    def moisture_content_21(self):
        """field `Moisture Content 21`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_21` or None if not set

        """
        return self["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """Corresponds to IDD field `Moisture Content 21`"""
        self["Moisture Content 21"] = value

    @property
    def liquid_transport_coefficient_21(self):
        """field `Liquid Transport Coefficient 21`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_21` or None if not set

        """
        return self["Liquid Transport Coefficient 21"]

    @liquid_transport_coefficient_21.setter
    def liquid_transport_coefficient_21(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 21`"""
        self["Liquid Transport Coefficient 21"] = value

    @property
    def moisture_content_22(self):
        """field `Moisture Content 22`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_22` or None if not set

        """
        return self["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """Corresponds to IDD field `Moisture Content 22`"""
        self["Moisture Content 22"] = value

    @property
    def liquid_transport_coefficient_22(self):
        """field `Liquid Transport Coefficient 22`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_22` or None if not set

        """
        return self["Liquid Transport Coefficient 22"]

    @liquid_transport_coefficient_22.setter
    def liquid_transport_coefficient_22(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 22`"""
        self["Liquid Transport Coefficient 22"] = value

    @property
    def moisture_content_23(self):
        """field `Moisture Content 23`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_23` or None if not set

        """
        return self["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """Corresponds to IDD field `Moisture Content 23`"""
        self["Moisture Content 23"] = value

    @property
    def liquid_transport_coefficient_23(self):
        """field `Liquid Transport Coefficient 23`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_23` or None if not set

        """
        return self["Liquid Transport Coefficient 23"]

    @liquid_transport_coefficient_23.setter
    def liquid_transport_coefficient_23(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 23`"""
        self["Liquid Transport Coefficient 23"] = value

    @property
    def moisture_content_24(self):
        """field `Moisture Content 24`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_24` or None if not set

        """
        return self["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """Corresponds to IDD field `Moisture Content 24`"""
        self["Moisture Content 24"] = value

    @property
    def liquid_transport_coefficient_24(self):
        """field `Liquid Transport Coefficient 24`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_24` or None if not set

        """
        return self["Liquid Transport Coefficient 24"]

    @liquid_transport_coefficient_24.setter
    def liquid_transport_coefficient_24(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 24`"""
        self["Liquid Transport Coefficient 24"] = value

    @property
    def moisture_content_25(self):
        """field `Moisture Content 25`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_25` or None if not set

        """
        return self["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """Corresponds to IDD field `Moisture Content 25`"""
        self["Moisture Content 25"] = value

    @property
    def liquid_transport_coefficient_25(self):
        """field `Liquid Transport Coefficient 25`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_25` or None if not set

        """
        return self["Liquid Transport Coefficient 25"]

    @liquid_transport_coefficient_25.setter
    def liquid_transport_coefficient_25(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 25`"""
        self["Liquid Transport Coefficient 25"] = value




class MaterialPropertyHeatAndMoistureTransferRedistribution(DataObject):

    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Redistribution`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between liquid transport coefficient and moisture content
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of redistribution points',
                                       {'name': u'Number of Redistribution points',
                                        'pyname': u'number_of_redistribution_points',
                                        'maximum': 25,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'moisture content 1',
                                       {'name': u'Moisture Content 1',
                                        'pyname': u'moisture_content_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 1',
                                       {'name': u'Liquid Transport Coefficient 1',
                                        'pyname': u'liquid_transport_coefficient_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 2',
                                       {'name': u'Moisture Content 2',
                                        'pyname': u'moisture_content_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 2',
                                       {'name': u'Liquid Transport Coefficient 2',
                                        'pyname': u'liquid_transport_coefficient_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 3',
                                       {'name': u'Moisture Content 3',
                                        'pyname': u'moisture_content_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 3',
                                       {'name': u'Liquid Transport Coefficient 3',
                                        'pyname': u'liquid_transport_coefficient_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 4',
                                       {'name': u'Moisture Content 4',
                                        'pyname': u'moisture_content_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 4',
                                       {'name': u'Liquid Transport Coefficient 4',
                                        'pyname': u'liquid_transport_coefficient_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 5',
                                       {'name': u'Moisture Content 5',
                                        'pyname': u'moisture_content_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 5',
                                       {'name': u'Liquid Transport Coefficient 5',
                                        'pyname': u'liquid_transport_coefficient_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 6',
                                       {'name': u'Moisture Content 6',
                                        'pyname': u'moisture_content_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 6',
                                       {'name': u'Liquid Transport Coefficient 6',
                                        'pyname': u'liquid_transport_coefficient_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 7',
                                       {'name': u'Moisture Content 7',
                                        'pyname': u'moisture_content_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 7',
                                       {'name': u'Liquid Transport Coefficient 7',
                                        'pyname': u'liquid_transport_coefficient_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 8',
                                       {'name': u'Moisture Content 8',
                                        'pyname': u'moisture_content_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 8',
                                       {'name': u'Liquid Transport Coefficient 8',
                                        'pyname': u'liquid_transport_coefficient_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 9',
                                       {'name': u'Moisture Content 9',
                                        'pyname': u'moisture_content_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 9',
                                       {'name': u'Liquid Transport Coefficient 9',
                                        'pyname': u'liquid_transport_coefficient_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 10',
                                       {'name': u'Moisture Content 10',
                                        'pyname': u'moisture_content_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 10',
                                       {'name': u'Liquid Transport Coefficient 10',
                                        'pyname': u'liquid_transport_coefficient_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 11',
                                       {'name': u'Moisture Content 11',
                                        'pyname': u'moisture_content_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 11',
                                       {'name': u'Liquid Transport Coefficient 11',
                                        'pyname': u'liquid_transport_coefficient_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 12',
                                       {'name': u'Moisture Content 12',
                                        'pyname': u'moisture_content_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 12',
                                       {'name': u'Liquid Transport Coefficient 12',
                                        'pyname': u'liquid_transport_coefficient_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 13',
                                       {'name': u'Moisture Content 13',
                                        'pyname': u'moisture_content_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 13',
                                       {'name': u'Liquid Transport Coefficient 13',
                                        'pyname': u'liquid_transport_coefficient_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 14',
                                       {'name': u'Moisture Content 14',
                                        'pyname': u'moisture_content_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 14',
                                       {'name': u'Liquid Transport Coefficient 14',
                                        'pyname': u'liquid_transport_coefficient_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 15',
                                       {'name': u'Moisture Content 15',
                                        'pyname': u'moisture_content_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 15',
                                       {'name': u'Liquid Transport Coefficient 15',
                                        'pyname': u'liquid_transport_coefficient_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 16',
                                       {'name': u'Moisture Content 16',
                                        'pyname': u'moisture_content_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 16',
                                       {'name': u'Liquid Transport Coefficient 16',
                                        'pyname': u'liquid_transport_coefficient_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 17',
                                       {'name': u'Moisture Content 17',
                                        'pyname': u'moisture_content_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 17',
                                       {'name': u'Liquid Transport Coefficient 17',
                                        'pyname': u'liquid_transport_coefficient_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 18',
                                       {'name': u'Moisture Content 18',
                                        'pyname': u'moisture_content_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 18',
                                       {'name': u'Liquid Transport Coefficient 18',
                                        'pyname': u'liquid_transport_coefficient_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 19',
                                       {'name': u'Moisture Content 19',
                                        'pyname': u'moisture_content_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 19',
                                       {'name': u'Liquid Transport Coefficient 19',
                                        'pyname': u'liquid_transport_coefficient_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 20',
                                       {'name': u'Moisture Content 20',
                                        'pyname': u'moisture_content_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 20',
                                       {'name': u'Liquid Transport Coefficient 20',
                                        'pyname': u'liquid_transport_coefficient_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 21',
                                       {'name': u'Moisture Content 21',
                                        'pyname': u'moisture_content_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 21',
                                       {'name': u'Liquid Transport Coefficient 21',
                                        'pyname': u'liquid_transport_coefficient_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 22',
                                       {'name': u'Moisture Content 22',
                                        'pyname': u'moisture_content_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 22',
                                       {'name': u'Liquid Transport Coefficient 22',
                                        'pyname': u'liquid_transport_coefficient_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 23',
                                       {'name': u'Moisture Content 23',
                                        'pyname': u'moisture_content_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 23',
                                       {'name': u'Liquid Transport Coefficient 23',
                                        'pyname': u'liquid_transport_coefficient_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 24',
                                       {'name': u'Moisture Content 24',
                                        'pyname': u'moisture_content_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 24',
                                       {'name': u'Liquid Transport Coefficient 24',
                                        'pyname': u'liquid_transport_coefficient_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'}),
                                      (u'moisture content 25',
                                       {'name': u'Moisture Content 25',
                                        'pyname': u'moisture_content_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'liquid transport coefficient 25',
                                       {'name': u'Liquid Transport Coefficient 25',
                                        'pyname': u'liquid_transport_coefficient_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2/s'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:HeatAndMoistureTransfer:Redistribution',
               'pyname': u'MaterialPropertyHeatAndMoistureTransferRedistribution',
               'required-object': False,
               'unique-object': False}

    @property
    def material_name(self):
        """field `Material Name`

        |  Moisture Material Name that the moisture properties will be added to.

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
    def number_of_redistribution_points(self):
        """field `Number of Redistribution points`

        |  number of data points
        |  value >= 1
        |  value <= 25

        Args:
            value (int): value for IDD Field `Number of Redistribution points`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_redistribution_points` or None if not set

        """
        return self["Number of Redistribution points"]

    @number_of_redistribution_points.setter
    def number_of_redistribution_points(self, value=None):
        """Corresponds to IDD field `Number of Redistribution points`"""
        self["Number of Redistribution points"] = value

    @property
    def moisture_content_1(self):
        """field `Moisture Content 1`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_1` or None if not set

        """
        return self["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """Corresponds to IDD field `Moisture Content 1`"""
        self["Moisture Content 1"] = value

    @property
    def liquid_transport_coefficient_1(self):
        """field `Liquid Transport Coefficient 1`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_1` or None if not set

        """
        return self["Liquid Transport Coefficient 1"]

    @liquid_transport_coefficient_1.setter
    def liquid_transport_coefficient_1(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 1`"""
        self["Liquid Transport Coefficient 1"] = value

    @property
    def moisture_content_2(self):
        """field `Moisture Content 2`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_2` or None if not set

        """
        return self["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """Corresponds to IDD field `Moisture Content 2`"""
        self["Moisture Content 2"] = value

    @property
    def liquid_transport_coefficient_2(self):
        """field `Liquid Transport Coefficient 2`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_2` or None if not set

        """
        return self["Liquid Transport Coefficient 2"]

    @liquid_transport_coefficient_2.setter
    def liquid_transport_coefficient_2(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 2`"""
        self["Liquid Transport Coefficient 2"] = value

    @property
    def moisture_content_3(self):
        """field `Moisture Content 3`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_3` or None if not set

        """
        return self["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """Corresponds to IDD field `Moisture Content 3`"""
        self["Moisture Content 3"] = value

    @property
    def liquid_transport_coefficient_3(self):
        """field `Liquid Transport Coefficient 3`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_3` or None if not set

        """
        return self["Liquid Transport Coefficient 3"]

    @liquid_transport_coefficient_3.setter
    def liquid_transport_coefficient_3(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 3`"""
        self["Liquid Transport Coefficient 3"] = value

    @property
    def moisture_content_4(self):
        """field `Moisture Content 4`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_4` or None if not set

        """
        return self["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """Corresponds to IDD field `Moisture Content 4`"""
        self["Moisture Content 4"] = value

    @property
    def liquid_transport_coefficient_4(self):
        """field `Liquid Transport Coefficient 4`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_4` or None if not set

        """
        return self["Liquid Transport Coefficient 4"]

    @liquid_transport_coefficient_4.setter
    def liquid_transport_coefficient_4(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 4`"""
        self["Liquid Transport Coefficient 4"] = value

    @property
    def moisture_content_5(self):
        """field `Moisture Content 5`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_5` or None if not set

        """
        return self["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """Corresponds to IDD field `Moisture Content 5`"""
        self["Moisture Content 5"] = value

    @property
    def liquid_transport_coefficient_5(self):
        """field `Liquid Transport Coefficient 5`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_5` or None if not set

        """
        return self["Liquid Transport Coefficient 5"]

    @liquid_transport_coefficient_5.setter
    def liquid_transport_coefficient_5(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 5`"""
        self["Liquid Transport Coefficient 5"] = value

    @property
    def moisture_content_6(self):
        """field `Moisture Content 6`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_6` or None if not set

        """
        return self["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """Corresponds to IDD field `Moisture Content 6`"""
        self["Moisture Content 6"] = value

    @property
    def liquid_transport_coefficient_6(self):
        """field `Liquid Transport Coefficient 6`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_6` or None if not set

        """
        return self["Liquid Transport Coefficient 6"]

    @liquid_transport_coefficient_6.setter
    def liquid_transport_coefficient_6(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 6`"""
        self["Liquid Transport Coefficient 6"] = value

    @property
    def moisture_content_7(self):
        """field `Moisture Content 7`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_7` or None if not set

        """
        return self["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """Corresponds to IDD field `Moisture Content 7`"""
        self["Moisture Content 7"] = value

    @property
    def liquid_transport_coefficient_7(self):
        """field `Liquid Transport Coefficient 7`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_7` or None if not set

        """
        return self["Liquid Transport Coefficient 7"]

    @liquid_transport_coefficient_7.setter
    def liquid_transport_coefficient_7(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 7`"""
        self["Liquid Transport Coefficient 7"] = value

    @property
    def moisture_content_8(self):
        """field `Moisture Content 8`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_8` or None if not set

        """
        return self["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """Corresponds to IDD field `Moisture Content 8`"""
        self["Moisture Content 8"] = value

    @property
    def liquid_transport_coefficient_8(self):
        """field `Liquid Transport Coefficient 8`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_8` or None if not set

        """
        return self["Liquid Transport Coefficient 8"]

    @liquid_transport_coefficient_8.setter
    def liquid_transport_coefficient_8(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 8`"""
        self["Liquid Transport Coefficient 8"] = value

    @property
    def moisture_content_9(self):
        """field `Moisture Content 9`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_9` or None if not set

        """
        return self["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """Corresponds to IDD field `Moisture Content 9`"""
        self["Moisture Content 9"] = value

    @property
    def liquid_transport_coefficient_9(self):
        """field `Liquid Transport Coefficient 9`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_9` or None if not set

        """
        return self["Liquid Transport Coefficient 9"]

    @liquid_transport_coefficient_9.setter
    def liquid_transport_coefficient_9(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 9`"""
        self["Liquid Transport Coefficient 9"] = value

    @property
    def moisture_content_10(self):
        """field `Moisture Content 10`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_10` or None if not set

        """
        return self["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """Corresponds to IDD field `Moisture Content 10`"""
        self["Moisture Content 10"] = value

    @property
    def liquid_transport_coefficient_10(self):
        """field `Liquid Transport Coefficient 10`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_10` or None if not set

        """
        return self["Liquid Transport Coefficient 10"]

    @liquid_transport_coefficient_10.setter
    def liquid_transport_coefficient_10(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 10`"""
        self["Liquid Transport Coefficient 10"] = value

    @property
    def moisture_content_11(self):
        """field `Moisture Content 11`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_11` or None if not set

        """
        return self["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """Corresponds to IDD field `Moisture Content 11`"""
        self["Moisture Content 11"] = value

    @property
    def liquid_transport_coefficient_11(self):
        """field `Liquid Transport Coefficient 11`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_11` or None if not set

        """
        return self["Liquid Transport Coefficient 11"]

    @liquid_transport_coefficient_11.setter
    def liquid_transport_coefficient_11(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 11`"""
        self["Liquid Transport Coefficient 11"] = value

    @property
    def moisture_content_12(self):
        """field `Moisture Content 12`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_12` or None if not set

        """
        return self["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """Corresponds to IDD field `Moisture Content 12`"""
        self["Moisture Content 12"] = value

    @property
    def liquid_transport_coefficient_12(self):
        """field `Liquid Transport Coefficient 12`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_12` or None if not set

        """
        return self["Liquid Transport Coefficient 12"]

    @liquid_transport_coefficient_12.setter
    def liquid_transport_coefficient_12(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 12`"""
        self["Liquid Transport Coefficient 12"] = value

    @property
    def moisture_content_13(self):
        """field `Moisture Content 13`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_13` or None if not set

        """
        return self["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """Corresponds to IDD field `Moisture Content 13`"""
        self["Moisture Content 13"] = value

    @property
    def liquid_transport_coefficient_13(self):
        """field `Liquid Transport Coefficient 13`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_13` or None if not set

        """
        return self["Liquid Transport Coefficient 13"]

    @liquid_transport_coefficient_13.setter
    def liquid_transport_coefficient_13(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 13`"""
        self["Liquid Transport Coefficient 13"] = value

    @property
    def moisture_content_14(self):
        """field `Moisture Content 14`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_14` or None if not set

        """
        return self["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """Corresponds to IDD field `Moisture Content 14`"""
        self["Moisture Content 14"] = value

    @property
    def liquid_transport_coefficient_14(self):
        """field `Liquid Transport Coefficient 14`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_14` or None if not set

        """
        return self["Liquid Transport Coefficient 14"]

    @liquid_transport_coefficient_14.setter
    def liquid_transport_coefficient_14(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 14`"""
        self["Liquid Transport Coefficient 14"] = value

    @property
    def moisture_content_15(self):
        """field `Moisture Content 15`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_15` or None if not set

        """
        return self["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """Corresponds to IDD field `Moisture Content 15`"""
        self["Moisture Content 15"] = value

    @property
    def liquid_transport_coefficient_15(self):
        """field `Liquid Transport Coefficient 15`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_15` or None if not set

        """
        return self["Liquid Transport Coefficient 15"]

    @liquid_transport_coefficient_15.setter
    def liquid_transport_coefficient_15(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 15`"""
        self["Liquid Transport Coefficient 15"] = value

    @property
    def moisture_content_16(self):
        """field `Moisture Content 16`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_16` or None if not set

        """
        return self["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """Corresponds to IDD field `Moisture Content 16`"""
        self["Moisture Content 16"] = value

    @property
    def liquid_transport_coefficient_16(self):
        """field `Liquid Transport Coefficient 16`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_16` or None if not set

        """
        return self["Liquid Transport Coefficient 16"]

    @liquid_transport_coefficient_16.setter
    def liquid_transport_coefficient_16(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 16`"""
        self["Liquid Transport Coefficient 16"] = value

    @property
    def moisture_content_17(self):
        """field `Moisture Content 17`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_17` or None if not set

        """
        return self["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """Corresponds to IDD field `Moisture Content 17`"""
        self["Moisture Content 17"] = value

    @property
    def liquid_transport_coefficient_17(self):
        """field `Liquid Transport Coefficient 17`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_17` or None if not set

        """
        return self["Liquid Transport Coefficient 17"]

    @liquid_transport_coefficient_17.setter
    def liquid_transport_coefficient_17(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 17`"""
        self["Liquid Transport Coefficient 17"] = value

    @property
    def moisture_content_18(self):
        """field `Moisture Content 18`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_18` or None if not set

        """
        return self["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """Corresponds to IDD field `Moisture Content 18`"""
        self["Moisture Content 18"] = value

    @property
    def liquid_transport_coefficient_18(self):
        """field `Liquid Transport Coefficient 18`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_18` or None if not set

        """
        return self["Liquid Transport Coefficient 18"]

    @liquid_transport_coefficient_18.setter
    def liquid_transport_coefficient_18(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 18`"""
        self["Liquid Transport Coefficient 18"] = value

    @property
    def moisture_content_19(self):
        """field `Moisture Content 19`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_19` or None if not set

        """
        return self["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """Corresponds to IDD field `Moisture Content 19`"""
        self["Moisture Content 19"] = value

    @property
    def liquid_transport_coefficient_19(self):
        """field `Liquid Transport Coefficient 19`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_19` or None if not set

        """
        return self["Liquid Transport Coefficient 19"]

    @liquid_transport_coefficient_19.setter
    def liquid_transport_coefficient_19(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 19`"""
        self["Liquid Transport Coefficient 19"] = value

    @property
    def moisture_content_20(self):
        """field `Moisture Content 20`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_20` or None if not set

        """
        return self["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """Corresponds to IDD field `Moisture Content 20`"""
        self["Moisture Content 20"] = value

    @property
    def liquid_transport_coefficient_20(self):
        """field `Liquid Transport Coefficient 20`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_20` or None if not set

        """
        return self["Liquid Transport Coefficient 20"]

    @liquid_transport_coefficient_20.setter
    def liquid_transport_coefficient_20(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 20`"""
        self["Liquid Transport Coefficient 20"] = value

    @property
    def moisture_content_21(self):
        """field `Moisture Content 21`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_21` or None if not set

        """
        return self["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """Corresponds to IDD field `Moisture Content 21`"""
        self["Moisture Content 21"] = value

    @property
    def liquid_transport_coefficient_21(self):
        """field `Liquid Transport Coefficient 21`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_21` or None if not set

        """
        return self["Liquid Transport Coefficient 21"]

    @liquid_transport_coefficient_21.setter
    def liquid_transport_coefficient_21(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 21`"""
        self["Liquid Transport Coefficient 21"] = value

    @property
    def moisture_content_22(self):
        """field `Moisture Content 22`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_22` or None if not set

        """
        return self["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """Corresponds to IDD field `Moisture Content 22`"""
        self["Moisture Content 22"] = value

    @property
    def liquid_transport_coefficient_22(self):
        """field `Liquid Transport Coefficient 22`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_22` or None if not set

        """
        return self["Liquid Transport Coefficient 22"]

    @liquid_transport_coefficient_22.setter
    def liquid_transport_coefficient_22(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 22`"""
        self["Liquid Transport Coefficient 22"] = value

    @property
    def moisture_content_23(self):
        """field `Moisture Content 23`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_23` or None if not set

        """
        return self["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """Corresponds to IDD field `Moisture Content 23`"""
        self["Moisture Content 23"] = value

    @property
    def liquid_transport_coefficient_23(self):
        """field `Liquid Transport Coefficient 23`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_23` or None if not set

        """
        return self["Liquid Transport Coefficient 23"]

    @liquid_transport_coefficient_23.setter
    def liquid_transport_coefficient_23(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 23`"""
        self["Liquid Transport Coefficient 23"] = value

    @property
    def moisture_content_24(self):
        """field `Moisture Content 24`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_24` or None if not set

        """
        return self["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """Corresponds to IDD field `Moisture Content 24`"""
        self["Moisture Content 24"] = value

    @property
    def liquid_transport_coefficient_24(self):
        """field `Liquid Transport Coefficient 24`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_24` or None if not set

        """
        return self["Liquid Transport Coefficient 24"]

    @liquid_transport_coefficient_24.setter
    def liquid_transport_coefficient_24(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 24`"""
        self["Liquid Transport Coefficient 24"] = value

    @property
    def moisture_content_25(self):
        """field `Moisture Content 25`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_25` or None if not set

        """
        return self["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """Corresponds to IDD field `Moisture Content 25`"""
        self["Moisture Content 25"] = value

    @property
    def liquid_transport_coefficient_25(self):
        """field `Liquid Transport Coefficient 25`

        |  Units: m2/s

        Args:
            value (float): value for IDD Field `Liquid Transport Coefficient 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_transport_coefficient_25` or None if not set

        """
        return self["Liquid Transport Coefficient 25"]

    @liquid_transport_coefficient_25.setter
    def liquid_transport_coefficient_25(self, value=None):
        """Corresponds to IDD field `Liquid Transport Coefficient 25`"""
        self["Liquid Transport Coefficient 25"] = value




class MaterialPropertyHeatAndMoistureTransferDiffusion(DataObject):

    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:Diffusion`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between water vapor diffusion and relative humidity fraction
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of data pairs',
                                       {'name': u'Number of Data Pairs',
                                        'pyname': u'number_of_data_pairs',
                                        'maximum': 25,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'relative humidity fraction 1',
                                       {'name': u'Relative Humidity Fraction 1',
                                        'pyname': u'relative_humidity_fraction_1',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 1',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 1',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 2',
                                       {'name': u'Relative Humidity Fraction 2',
                                        'pyname': u'relative_humidity_fraction_2',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 2',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 2',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 3',
                                       {'name': u'Relative Humidity Fraction 3',
                                        'pyname': u'relative_humidity_fraction_3',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 3',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 3',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 4',
                                       {'name': u'Relative Humidity Fraction 4',
                                        'pyname': u'relative_humidity_fraction_4',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 4',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 4',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 5',
                                       {'name': u'Relative Humidity Fraction 5',
                                        'pyname': u'relative_humidity_fraction_5',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 5',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 5',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 6',
                                       {'name': u'Relative Humidity Fraction 6',
                                        'pyname': u'relative_humidity_fraction_6',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 6',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 6',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 7',
                                       {'name': u'Relative Humidity Fraction 7',
                                        'pyname': u'relative_humidity_fraction_7',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 7',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 7',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 8',
                                       {'name': u'Relative Humidity Fraction 8',
                                        'pyname': u'relative_humidity_fraction_8',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 8',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 8',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 9',
                                       {'name': u'Relative Humidity Fraction 9',
                                        'pyname': u'relative_humidity_fraction_9',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 9',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 9',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 10',
                                       {'name': u'Relative Humidity Fraction 10',
                                        'pyname': u'relative_humidity_fraction_10',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 10',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 10',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 11',
                                       {'name': u'Relative Humidity Fraction 11',
                                        'pyname': u'relative_humidity_fraction_11',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 11',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 11',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 12',
                                       {'name': u'Relative Humidity Fraction 12',
                                        'pyname': u'relative_humidity_fraction_12',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 12',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 12',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 13',
                                       {'name': u'Relative Humidity Fraction 13',
                                        'pyname': u'relative_humidity_fraction_13',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 13',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 13',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 14',
                                       {'name': u'Relative Humidity Fraction 14',
                                        'pyname': u'relative_humidity_fraction_14',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 14',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 14',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 15',
                                       {'name': u'Relative Humidity Fraction 15',
                                        'pyname': u'relative_humidity_fraction_15',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 15',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 15',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 16',
                                       {'name': u'Relative Humidity Fraction 16',
                                        'pyname': u'relative_humidity_fraction_16',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 16',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 16',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 17',
                                       {'name': u'Relative Humidity Fraction 17',
                                        'pyname': u'relative_humidity_fraction_17',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 17',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 17',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 18',
                                       {'name': u'Relative Humidity Fraction 18',
                                        'pyname': u'relative_humidity_fraction_18',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 18',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 18',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 19',
                                       {'name': u'Relative Humidity Fraction 19',
                                        'pyname': u'relative_humidity_fraction_19',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 19',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 19',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 20',
                                       {'name': u'Relative Humidity Fraction 20',
                                        'pyname': u'relative_humidity_fraction_20',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 20',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 20',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 21',
                                       {'name': u'Relative Humidity Fraction 21',
                                        'pyname': u'relative_humidity_fraction_21',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 21',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 21',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 22',
                                       {'name': u'Relative Humidity Fraction 22',
                                        'pyname': u'relative_humidity_fraction_22',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 22',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 22',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 23',
                                       {'name': u'Relative Humidity Fraction 23',
                                        'pyname': u'relative_humidity_fraction_23',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 23',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 23',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 24',
                                       {'name': u'Relative Humidity Fraction 24',
                                        'pyname': u'relative_humidity_fraction_24',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 24',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 24',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'relative humidity fraction 25',
                                       {'name': u'Relative Humidity Fraction 25',
                                        'pyname': u'relative_humidity_fraction_25',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'water vapor diffusion resistance factor 25',
                                       {'name': u'Water Vapor Diffusion Resistance Factor 25',
                                        'pyname': u'water_vapor_diffusion_resistance_factor_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:HeatAndMoistureTransfer:Diffusion',
               'pyname': u'MaterialPropertyHeatAndMoistureTransferDiffusion',
               'required-object': False,
               'unique-object': False}

    @property
    def material_name(self):
        """field `Material Name`

        |  Moisture Material Name that the moisture properties will be added to.

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
    def number_of_data_pairs(self):
        """field `Number of Data Pairs`

        |  Water Vapor Diffusion Resistance Factor
        |  value >= 1
        |  value <= 25

        Args:
            value (int): value for IDD Field `Number of Data Pairs`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_data_pairs` or None if not set

        """
        return self["Number of Data Pairs"]

    @number_of_data_pairs.setter
    def number_of_data_pairs(self, value=None):
        """Corresponds to IDD field `Number of Data Pairs`"""
        self["Number of Data Pairs"] = value

    @property
    def relative_humidity_fraction_1(self):
        """field `Relative Humidity Fraction 1`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_1` or None if not set

        """
        return self["Relative Humidity Fraction 1"]

    @relative_humidity_fraction_1.setter
    def relative_humidity_fraction_1(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 1`"""
        self["Relative Humidity Fraction 1"] = value

    @property
    def water_vapor_diffusion_resistance_factor_1(self):
        """field `Water Vapor Diffusion Resistance Factor 1`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_1` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 1"]

    @water_vapor_diffusion_resistance_factor_1.setter
    def water_vapor_diffusion_resistance_factor_1(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        1`"""
        self["Water Vapor Diffusion Resistance Factor 1"] = value

    @property
    def relative_humidity_fraction_2(self):
        """field `Relative Humidity Fraction 2`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_2` or None if not set

        """
        return self["Relative Humidity Fraction 2"]

    @relative_humidity_fraction_2.setter
    def relative_humidity_fraction_2(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 2`"""
        self["Relative Humidity Fraction 2"] = value

    @property
    def water_vapor_diffusion_resistance_factor_2(self):
        """field `Water Vapor Diffusion Resistance Factor 2`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_2` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 2"]

    @water_vapor_diffusion_resistance_factor_2.setter
    def water_vapor_diffusion_resistance_factor_2(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        2`"""
        self["Water Vapor Diffusion Resistance Factor 2"] = value

    @property
    def relative_humidity_fraction_3(self):
        """field `Relative Humidity Fraction 3`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_3` or None if not set

        """
        return self["Relative Humidity Fraction 3"]

    @relative_humidity_fraction_3.setter
    def relative_humidity_fraction_3(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 3`"""
        self["Relative Humidity Fraction 3"] = value

    @property
    def water_vapor_diffusion_resistance_factor_3(self):
        """field `Water Vapor Diffusion Resistance Factor 3`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_3` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 3"]

    @water_vapor_diffusion_resistance_factor_3.setter
    def water_vapor_diffusion_resistance_factor_3(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        3`"""
        self["Water Vapor Diffusion Resistance Factor 3"] = value

    @property
    def relative_humidity_fraction_4(self):
        """field `Relative Humidity Fraction 4`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_4` or None if not set

        """
        return self["Relative Humidity Fraction 4"]

    @relative_humidity_fraction_4.setter
    def relative_humidity_fraction_4(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 4`"""
        self["Relative Humidity Fraction 4"] = value

    @property
    def water_vapor_diffusion_resistance_factor_4(self):
        """field `Water Vapor Diffusion Resistance Factor 4`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_4` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 4"]

    @water_vapor_diffusion_resistance_factor_4.setter
    def water_vapor_diffusion_resistance_factor_4(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        4`"""
        self["Water Vapor Diffusion Resistance Factor 4"] = value

    @property
    def relative_humidity_fraction_5(self):
        """field `Relative Humidity Fraction 5`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_5` or None if not set

        """
        return self["Relative Humidity Fraction 5"]

    @relative_humidity_fraction_5.setter
    def relative_humidity_fraction_5(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 5`"""
        self["Relative Humidity Fraction 5"] = value

    @property
    def water_vapor_diffusion_resistance_factor_5(self):
        """field `Water Vapor Diffusion Resistance Factor 5`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_5` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 5"]

    @water_vapor_diffusion_resistance_factor_5.setter
    def water_vapor_diffusion_resistance_factor_5(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        5`"""
        self["Water Vapor Diffusion Resistance Factor 5"] = value

    @property
    def relative_humidity_fraction_6(self):
        """field `Relative Humidity Fraction 6`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_6` or None if not set

        """
        return self["Relative Humidity Fraction 6"]

    @relative_humidity_fraction_6.setter
    def relative_humidity_fraction_6(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 6`"""
        self["Relative Humidity Fraction 6"] = value

    @property
    def water_vapor_diffusion_resistance_factor_6(self):
        """field `Water Vapor Diffusion Resistance Factor 6`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_6` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 6"]

    @water_vapor_diffusion_resistance_factor_6.setter
    def water_vapor_diffusion_resistance_factor_6(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        6`"""
        self["Water Vapor Diffusion Resistance Factor 6"] = value

    @property
    def relative_humidity_fraction_7(self):
        """field `Relative Humidity Fraction 7`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_7` or None if not set

        """
        return self["Relative Humidity Fraction 7"]

    @relative_humidity_fraction_7.setter
    def relative_humidity_fraction_7(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 7`"""
        self["Relative Humidity Fraction 7"] = value

    @property
    def water_vapor_diffusion_resistance_factor_7(self):
        """field `Water Vapor Diffusion Resistance Factor 7`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_7` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 7"]

    @water_vapor_diffusion_resistance_factor_7.setter
    def water_vapor_diffusion_resistance_factor_7(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        7`"""
        self["Water Vapor Diffusion Resistance Factor 7"] = value

    @property
    def relative_humidity_fraction_8(self):
        """field `Relative Humidity Fraction 8`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_8` or None if not set

        """
        return self["Relative Humidity Fraction 8"]

    @relative_humidity_fraction_8.setter
    def relative_humidity_fraction_8(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 8`"""
        self["Relative Humidity Fraction 8"] = value

    @property
    def water_vapor_diffusion_resistance_factor_8(self):
        """field `Water Vapor Diffusion Resistance Factor 8`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_8` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 8"]

    @water_vapor_diffusion_resistance_factor_8.setter
    def water_vapor_diffusion_resistance_factor_8(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        8`"""
        self["Water Vapor Diffusion Resistance Factor 8"] = value

    @property
    def relative_humidity_fraction_9(self):
        """field `Relative Humidity Fraction 9`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_9` or None if not set

        """
        return self["Relative Humidity Fraction 9"]

    @relative_humidity_fraction_9.setter
    def relative_humidity_fraction_9(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 9`"""
        self["Relative Humidity Fraction 9"] = value

    @property
    def water_vapor_diffusion_resistance_factor_9(self):
        """field `Water Vapor Diffusion Resistance Factor 9`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_9` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 9"]

    @water_vapor_diffusion_resistance_factor_9.setter
    def water_vapor_diffusion_resistance_factor_9(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        9`"""
        self["Water Vapor Diffusion Resistance Factor 9"] = value

    @property
    def relative_humidity_fraction_10(self):
        """field `Relative Humidity Fraction 10`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_10` or None if not set

        """
        return self["Relative Humidity Fraction 10"]

    @relative_humidity_fraction_10.setter
    def relative_humidity_fraction_10(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 10`"""
        self["Relative Humidity Fraction 10"] = value

    @property
    def water_vapor_diffusion_resistance_factor_10(self):
        """field `Water Vapor Diffusion Resistance Factor 10`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_10` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 10"]

    @water_vapor_diffusion_resistance_factor_10.setter
    def water_vapor_diffusion_resistance_factor_10(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        10`"""
        self["Water Vapor Diffusion Resistance Factor 10"] = value

    @property
    def relative_humidity_fraction_11(self):
        """field `Relative Humidity Fraction 11`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_11` or None if not set

        """
        return self["Relative Humidity Fraction 11"]

    @relative_humidity_fraction_11.setter
    def relative_humidity_fraction_11(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 11`"""
        self["Relative Humidity Fraction 11"] = value

    @property
    def water_vapor_diffusion_resistance_factor_11(self):
        """field `Water Vapor Diffusion Resistance Factor 11`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_11` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 11"]

    @water_vapor_diffusion_resistance_factor_11.setter
    def water_vapor_diffusion_resistance_factor_11(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        11`"""
        self["Water Vapor Diffusion Resistance Factor 11"] = value

    @property
    def relative_humidity_fraction_12(self):
        """field `Relative Humidity Fraction 12`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_12` or None if not set

        """
        return self["Relative Humidity Fraction 12"]

    @relative_humidity_fraction_12.setter
    def relative_humidity_fraction_12(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 12`"""
        self["Relative Humidity Fraction 12"] = value

    @property
    def water_vapor_diffusion_resistance_factor_12(self):
        """field `Water Vapor Diffusion Resistance Factor 12`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_12` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 12"]

    @water_vapor_diffusion_resistance_factor_12.setter
    def water_vapor_diffusion_resistance_factor_12(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        12`"""
        self["Water Vapor Diffusion Resistance Factor 12"] = value

    @property
    def relative_humidity_fraction_13(self):
        """field `Relative Humidity Fraction 13`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_13` or None if not set

        """
        return self["Relative Humidity Fraction 13"]

    @relative_humidity_fraction_13.setter
    def relative_humidity_fraction_13(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 13`"""
        self["Relative Humidity Fraction 13"] = value

    @property
    def water_vapor_diffusion_resistance_factor_13(self):
        """field `Water Vapor Diffusion Resistance Factor 13`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_13` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 13"]

    @water_vapor_diffusion_resistance_factor_13.setter
    def water_vapor_diffusion_resistance_factor_13(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        13`"""
        self["Water Vapor Diffusion Resistance Factor 13"] = value

    @property
    def relative_humidity_fraction_14(self):
        """field `Relative Humidity Fraction 14`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_14` or None if not set

        """
        return self["Relative Humidity Fraction 14"]

    @relative_humidity_fraction_14.setter
    def relative_humidity_fraction_14(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 14`"""
        self["Relative Humidity Fraction 14"] = value

    @property
    def water_vapor_diffusion_resistance_factor_14(self):
        """field `Water Vapor Diffusion Resistance Factor 14`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_14` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 14"]

    @water_vapor_diffusion_resistance_factor_14.setter
    def water_vapor_diffusion_resistance_factor_14(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        14`"""
        self["Water Vapor Diffusion Resistance Factor 14"] = value

    @property
    def relative_humidity_fraction_15(self):
        """field `Relative Humidity Fraction 15`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_15` or None if not set

        """
        return self["Relative Humidity Fraction 15"]

    @relative_humidity_fraction_15.setter
    def relative_humidity_fraction_15(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 15`"""
        self["Relative Humidity Fraction 15"] = value

    @property
    def water_vapor_diffusion_resistance_factor_15(self):
        """field `Water Vapor Diffusion Resistance Factor 15`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_15` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 15"]

    @water_vapor_diffusion_resistance_factor_15.setter
    def water_vapor_diffusion_resistance_factor_15(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        15`"""
        self["Water Vapor Diffusion Resistance Factor 15"] = value

    @property
    def relative_humidity_fraction_16(self):
        """field `Relative Humidity Fraction 16`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_16` or None if not set

        """
        return self["Relative Humidity Fraction 16"]

    @relative_humidity_fraction_16.setter
    def relative_humidity_fraction_16(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 16`"""
        self["Relative Humidity Fraction 16"] = value

    @property
    def water_vapor_diffusion_resistance_factor_16(self):
        """field `Water Vapor Diffusion Resistance Factor 16`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_16` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 16"]

    @water_vapor_diffusion_resistance_factor_16.setter
    def water_vapor_diffusion_resistance_factor_16(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        16`"""
        self["Water Vapor Diffusion Resistance Factor 16"] = value

    @property
    def relative_humidity_fraction_17(self):
        """field `Relative Humidity Fraction 17`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_17` or None if not set

        """
        return self["Relative Humidity Fraction 17"]

    @relative_humidity_fraction_17.setter
    def relative_humidity_fraction_17(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 17`"""
        self["Relative Humidity Fraction 17"] = value

    @property
    def water_vapor_diffusion_resistance_factor_17(self):
        """field `Water Vapor Diffusion Resistance Factor 17`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_17` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 17"]

    @water_vapor_diffusion_resistance_factor_17.setter
    def water_vapor_diffusion_resistance_factor_17(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        17`"""
        self["Water Vapor Diffusion Resistance Factor 17"] = value

    @property
    def relative_humidity_fraction_18(self):
        """field `Relative Humidity Fraction 18`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_18` or None if not set

        """
        return self["Relative Humidity Fraction 18"]

    @relative_humidity_fraction_18.setter
    def relative_humidity_fraction_18(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 18`"""
        self["Relative Humidity Fraction 18"] = value

    @property
    def water_vapor_diffusion_resistance_factor_18(self):
        """field `Water Vapor Diffusion Resistance Factor 18`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_18` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 18"]

    @water_vapor_diffusion_resistance_factor_18.setter
    def water_vapor_diffusion_resistance_factor_18(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        18`"""
        self["Water Vapor Diffusion Resistance Factor 18"] = value

    @property
    def relative_humidity_fraction_19(self):
        """field `Relative Humidity Fraction 19`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_19` or None if not set

        """
        return self["Relative Humidity Fraction 19"]

    @relative_humidity_fraction_19.setter
    def relative_humidity_fraction_19(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 19`"""
        self["Relative Humidity Fraction 19"] = value

    @property
    def water_vapor_diffusion_resistance_factor_19(self):
        """field `Water Vapor Diffusion Resistance Factor 19`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_19` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 19"]

    @water_vapor_diffusion_resistance_factor_19.setter
    def water_vapor_diffusion_resistance_factor_19(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        19`"""
        self["Water Vapor Diffusion Resistance Factor 19"] = value

    @property
    def relative_humidity_fraction_20(self):
        """field `Relative Humidity Fraction 20`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_20` or None if not set

        """
        return self["Relative Humidity Fraction 20"]

    @relative_humidity_fraction_20.setter
    def relative_humidity_fraction_20(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 20`"""
        self["Relative Humidity Fraction 20"] = value

    @property
    def water_vapor_diffusion_resistance_factor_20(self):
        """field `Water Vapor Diffusion Resistance Factor 20`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_20` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 20"]

    @water_vapor_diffusion_resistance_factor_20.setter
    def water_vapor_diffusion_resistance_factor_20(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        20`"""
        self["Water Vapor Diffusion Resistance Factor 20"] = value

    @property
    def relative_humidity_fraction_21(self):
        """field `Relative Humidity Fraction 21`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_21` or None if not set

        """
        return self["Relative Humidity Fraction 21"]

    @relative_humidity_fraction_21.setter
    def relative_humidity_fraction_21(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 21`"""
        self["Relative Humidity Fraction 21"] = value

    @property
    def water_vapor_diffusion_resistance_factor_21(self):
        """field `Water Vapor Diffusion Resistance Factor 21`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_21` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 21"]

    @water_vapor_diffusion_resistance_factor_21.setter
    def water_vapor_diffusion_resistance_factor_21(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        21`"""
        self["Water Vapor Diffusion Resistance Factor 21"] = value

    @property
    def relative_humidity_fraction_22(self):
        """field `Relative Humidity Fraction 22`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_22` or None if not set

        """
        return self["Relative Humidity Fraction 22"]

    @relative_humidity_fraction_22.setter
    def relative_humidity_fraction_22(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 22`"""
        self["Relative Humidity Fraction 22"] = value

    @property
    def water_vapor_diffusion_resistance_factor_22(self):
        """field `Water Vapor Diffusion Resistance Factor 22`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_22` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 22"]

    @water_vapor_diffusion_resistance_factor_22.setter
    def water_vapor_diffusion_resistance_factor_22(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        22`"""
        self["Water Vapor Diffusion Resistance Factor 22"] = value

    @property
    def relative_humidity_fraction_23(self):
        """field `Relative Humidity Fraction 23`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_23` or None if not set

        """
        return self["Relative Humidity Fraction 23"]

    @relative_humidity_fraction_23.setter
    def relative_humidity_fraction_23(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 23`"""
        self["Relative Humidity Fraction 23"] = value

    @property
    def water_vapor_diffusion_resistance_factor_23(self):
        """field `Water Vapor Diffusion Resistance Factor 23`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_23` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 23"]

    @water_vapor_diffusion_resistance_factor_23.setter
    def water_vapor_diffusion_resistance_factor_23(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        23`"""
        self["Water Vapor Diffusion Resistance Factor 23"] = value

    @property
    def relative_humidity_fraction_24(self):
        """field `Relative Humidity Fraction 24`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_24` or None if not set

        """
        return self["Relative Humidity Fraction 24"]

    @relative_humidity_fraction_24.setter
    def relative_humidity_fraction_24(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 24`"""
        self["Relative Humidity Fraction 24"] = value

    @property
    def water_vapor_diffusion_resistance_factor_24(self):
        """field `Water Vapor Diffusion Resistance Factor 24`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_24` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 24"]

    @water_vapor_diffusion_resistance_factor_24.setter
    def water_vapor_diffusion_resistance_factor_24(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        24`"""
        self["Water Vapor Diffusion Resistance Factor 24"] = value

    @property
    def relative_humidity_fraction_25(self):
        """field `Relative Humidity Fraction 25`

        |  The relative humidity is entered as a fraction.
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Humidity Fraction 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_fraction_25` or None if not set

        """
        return self["Relative Humidity Fraction 25"]

    @relative_humidity_fraction_25.setter
    def relative_humidity_fraction_25(self, value=None):
        """Corresponds to IDD field `Relative Humidity Fraction 25`"""
        self["Relative Humidity Fraction 25"] = value

    @property
    def water_vapor_diffusion_resistance_factor_25(self):
        """field `Water Vapor Diffusion Resistance Factor 25`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Water Vapor Diffusion Resistance Factor 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_vapor_diffusion_resistance_factor_25` or None if not set

        """
        return self["Water Vapor Diffusion Resistance Factor 25"]

    @water_vapor_diffusion_resistance_factor_25.setter
    def water_vapor_diffusion_resistance_factor_25(self, value=None):
        """Corresponds to IDD field `Water Vapor Diffusion Resistance Factor
        25`"""
        self["Water Vapor Diffusion Resistance Factor 25"] = value




class MaterialPropertyHeatAndMoistureTransferThermalConductivity(DataObject):

    """ Corresponds to IDD object `MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity`
        HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only.
        Relationship between thermal conductivity and moisture content
        Has no effect with other HeatBalanceAlgorithm solution algorithms
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'material name',
                                       {'name': u'Material Name',
                                        'pyname': u'material_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of thermal coordinates',
                                       {'name': u'Number of Thermal Coordinates',
                                        'pyname': u'number_of_thermal_coordinates',
                                        'maximum': 25,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'moisture content 1',
                                       {'name': u'Moisture Content 1',
                                        'pyname': u'moisture_content_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 1',
                                       {'name': u'Thermal Conductivity 1',
                                        'pyname': u'thermal_conductivity_1',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 2',
                                       {'name': u'Moisture Content 2',
                                        'pyname': u'moisture_content_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 2',
                                       {'name': u'Thermal Conductivity 2',
                                        'pyname': u'thermal_conductivity_2',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 3',
                                       {'name': u'Moisture Content 3',
                                        'pyname': u'moisture_content_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 3',
                                       {'name': u'Thermal Conductivity 3',
                                        'pyname': u'thermal_conductivity_3',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 4',
                                       {'name': u'Moisture Content 4',
                                        'pyname': u'moisture_content_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 4',
                                       {'name': u'Thermal Conductivity 4',
                                        'pyname': u'thermal_conductivity_4',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 5',
                                       {'name': u'Moisture Content 5',
                                        'pyname': u'moisture_content_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 5',
                                       {'name': u'Thermal Conductivity 5',
                                        'pyname': u'thermal_conductivity_5',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 6',
                                       {'name': u'Moisture Content 6',
                                        'pyname': u'moisture_content_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 6',
                                       {'name': u'Thermal Conductivity 6',
                                        'pyname': u'thermal_conductivity_6',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 7',
                                       {'name': u'Moisture Content 7',
                                        'pyname': u'moisture_content_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 7',
                                       {'name': u'Thermal Conductivity 7',
                                        'pyname': u'thermal_conductivity_7',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 8',
                                       {'name': u'Moisture Content 8',
                                        'pyname': u'moisture_content_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 8',
                                       {'name': u'Thermal Conductivity 8',
                                        'pyname': u'thermal_conductivity_8',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 9',
                                       {'name': u'Moisture Content 9',
                                        'pyname': u'moisture_content_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 9',
                                       {'name': u'Thermal Conductivity 9',
                                        'pyname': u'thermal_conductivity_9',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 10',
                                       {'name': u'Moisture Content 10',
                                        'pyname': u'moisture_content_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 10',
                                       {'name': u'Thermal Conductivity 10',
                                        'pyname': u'thermal_conductivity_10',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 11',
                                       {'name': u'Moisture Content 11',
                                        'pyname': u'moisture_content_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 11',
                                       {'name': u'Thermal Conductivity 11',
                                        'pyname': u'thermal_conductivity_11',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 12',
                                       {'name': u'Moisture Content 12',
                                        'pyname': u'moisture_content_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 12',
                                       {'name': u'Thermal Conductivity 12',
                                        'pyname': u'thermal_conductivity_12',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 13',
                                       {'name': u'Moisture Content 13',
                                        'pyname': u'moisture_content_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 13',
                                       {'name': u'Thermal Conductivity 13',
                                        'pyname': u'thermal_conductivity_13',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 14',
                                       {'name': u'Moisture Content 14',
                                        'pyname': u'moisture_content_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 14',
                                       {'name': u'Thermal Conductivity 14',
                                        'pyname': u'thermal_conductivity_14',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 15',
                                       {'name': u'Moisture Content 15',
                                        'pyname': u'moisture_content_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 15',
                                       {'name': u'Thermal Conductivity 15',
                                        'pyname': u'thermal_conductivity_15',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 16',
                                       {'name': u'Moisture Content 16',
                                        'pyname': u'moisture_content_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 16',
                                       {'name': u'Thermal Conductivity 16',
                                        'pyname': u'thermal_conductivity_16',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 17',
                                       {'name': u'Moisture Content 17',
                                        'pyname': u'moisture_content_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 17',
                                       {'name': u'Thermal Conductivity 17',
                                        'pyname': u'thermal_conductivity_17',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 18',
                                       {'name': u'Moisture Content 18',
                                        'pyname': u'moisture_content_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 18',
                                       {'name': u'Thermal Conductivity 18',
                                        'pyname': u'thermal_conductivity_18',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 19',
                                       {'name': u'Moisture Content 19',
                                        'pyname': u'moisture_content_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 19',
                                       {'name': u'Thermal Conductivity 19',
                                        'pyname': u'thermal_conductivity_19',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 20',
                                       {'name': u'Moisture Content 20',
                                        'pyname': u'moisture_content_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 20',
                                       {'name': u'Thermal Conductivity 20',
                                        'pyname': u'thermal_conductivity_20',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 21',
                                       {'name': u'Moisture Content 21',
                                        'pyname': u'moisture_content_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 21',
                                       {'name': u'Thermal Conductivity 21',
                                        'pyname': u'thermal_conductivity_21',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 22',
                                       {'name': u'Moisture Content 22',
                                        'pyname': u'moisture_content_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 22',
                                       {'name': u'Thermal Conductivity 22',
                                        'pyname': u'thermal_conductivity_22',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 23',
                                       {'name': u'Moisture Content 23',
                                        'pyname': u'moisture_content_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 23',
                                       {'name': u'Thermal Conductivity 23',
                                        'pyname': u'thermal_conductivity_23',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 24',
                                       {'name': u'Moisture Content 24',
                                        'pyname': u'moisture_content_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 24',
                                       {'name': u'Thermal Conductivity 24',
                                        'pyname': u'thermal_conductivity_24',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'moisture content 25',
                                       {'name': u'Moisture Content 25',
                                        'pyname': u'moisture_content_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'thermal conductivity 25',
                                       {'name': u'Thermal Conductivity 25',
                                        'pyname': u'thermal_conductivity_25',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity',
               'pyname': u'MaterialPropertyHeatAndMoistureTransferThermalConductivity',
               'required-object': False,
               'unique-object': False}

    @property
    def material_name(self):
        """field `Material Name`

        |  Moisture Material Name that the Thermal Conductivity will be added to.

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
    def number_of_thermal_coordinates(self):
        """field `Number of Thermal Coordinates`

        |  number of data coordinates
        |  value >= 1
        |  value <= 25

        Args:
            value (int): value for IDD Field `Number of Thermal Coordinates`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_thermal_coordinates` or None if not set

        """
        return self["Number of Thermal Coordinates"]

    @number_of_thermal_coordinates.setter
    def number_of_thermal_coordinates(self, value=None):
        """Corresponds to IDD field `Number of Thermal Coordinates`"""
        self["Number of Thermal Coordinates"] = value

    @property
    def moisture_content_1(self):
        """field `Moisture Content 1`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_1` or None if not set

        """
        return self["Moisture Content 1"]

    @moisture_content_1.setter
    def moisture_content_1(self, value=None):
        """Corresponds to IDD field `Moisture Content 1`"""
        self["Moisture Content 1"] = value

    @property
    def thermal_conductivity_1(self):
        """field `Thermal Conductivity 1`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_1` or None if not set

        """
        return self["Thermal Conductivity 1"]

    @thermal_conductivity_1.setter
    def thermal_conductivity_1(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 1`"""
        self["Thermal Conductivity 1"] = value

    @property
    def moisture_content_2(self):
        """field `Moisture Content 2`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_2` or None if not set

        """
        return self["Moisture Content 2"]

    @moisture_content_2.setter
    def moisture_content_2(self, value=None):
        """Corresponds to IDD field `Moisture Content 2`"""
        self["Moisture Content 2"] = value

    @property
    def thermal_conductivity_2(self):
        """field `Thermal Conductivity 2`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_2` or None if not set

        """
        return self["Thermal Conductivity 2"]

    @thermal_conductivity_2.setter
    def thermal_conductivity_2(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 2`"""
        self["Thermal Conductivity 2"] = value

    @property
    def moisture_content_3(self):
        """field `Moisture Content 3`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_3` or None if not set

        """
        return self["Moisture Content 3"]

    @moisture_content_3.setter
    def moisture_content_3(self, value=None):
        """Corresponds to IDD field `Moisture Content 3`"""
        self["Moisture Content 3"] = value

    @property
    def thermal_conductivity_3(self):
        """field `Thermal Conductivity 3`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_3` or None if not set

        """
        return self["Thermal Conductivity 3"]

    @thermal_conductivity_3.setter
    def thermal_conductivity_3(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 3`"""
        self["Thermal Conductivity 3"] = value

    @property
    def moisture_content_4(self):
        """field `Moisture Content 4`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_4` or None if not set

        """
        return self["Moisture Content 4"]

    @moisture_content_4.setter
    def moisture_content_4(self, value=None):
        """Corresponds to IDD field `Moisture Content 4`"""
        self["Moisture Content 4"] = value

    @property
    def thermal_conductivity_4(self):
        """field `Thermal Conductivity 4`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_4` or None if not set

        """
        return self["Thermal Conductivity 4"]

    @thermal_conductivity_4.setter
    def thermal_conductivity_4(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 4`"""
        self["Thermal Conductivity 4"] = value

    @property
    def moisture_content_5(self):
        """field `Moisture Content 5`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_5` or None if not set

        """
        return self["Moisture Content 5"]

    @moisture_content_5.setter
    def moisture_content_5(self, value=None):
        """Corresponds to IDD field `Moisture Content 5`"""
        self["Moisture Content 5"] = value

    @property
    def thermal_conductivity_5(self):
        """field `Thermal Conductivity 5`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_5` or None if not set

        """
        return self["Thermal Conductivity 5"]

    @thermal_conductivity_5.setter
    def thermal_conductivity_5(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 5`"""
        self["Thermal Conductivity 5"] = value

    @property
    def moisture_content_6(self):
        """field `Moisture Content 6`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_6` or None if not set

        """
        return self["Moisture Content 6"]

    @moisture_content_6.setter
    def moisture_content_6(self, value=None):
        """Corresponds to IDD field `Moisture Content 6`"""
        self["Moisture Content 6"] = value

    @property
    def thermal_conductivity_6(self):
        """field `Thermal Conductivity 6`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_6` or None if not set

        """
        return self["Thermal Conductivity 6"]

    @thermal_conductivity_6.setter
    def thermal_conductivity_6(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 6`"""
        self["Thermal Conductivity 6"] = value

    @property
    def moisture_content_7(self):
        """field `Moisture Content 7`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_7` or None if not set

        """
        return self["Moisture Content 7"]

    @moisture_content_7.setter
    def moisture_content_7(self, value=None):
        """Corresponds to IDD field `Moisture Content 7`"""
        self["Moisture Content 7"] = value

    @property
    def thermal_conductivity_7(self):
        """field `Thermal Conductivity 7`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_7` or None if not set

        """
        return self["Thermal Conductivity 7"]

    @thermal_conductivity_7.setter
    def thermal_conductivity_7(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 7`"""
        self["Thermal Conductivity 7"] = value

    @property
    def moisture_content_8(self):
        """field `Moisture Content 8`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_8` or None if not set

        """
        return self["Moisture Content 8"]

    @moisture_content_8.setter
    def moisture_content_8(self, value=None):
        """Corresponds to IDD field `Moisture Content 8`"""
        self["Moisture Content 8"] = value

    @property
    def thermal_conductivity_8(self):
        """field `Thermal Conductivity 8`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_8` or None if not set

        """
        return self["Thermal Conductivity 8"]

    @thermal_conductivity_8.setter
    def thermal_conductivity_8(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 8`"""
        self["Thermal Conductivity 8"] = value

    @property
    def moisture_content_9(self):
        """field `Moisture Content 9`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_9` or None if not set

        """
        return self["Moisture Content 9"]

    @moisture_content_9.setter
    def moisture_content_9(self, value=None):
        """Corresponds to IDD field `Moisture Content 9`"""
        self["Moisture Content 9"] = value

    @property
    def thermal_conductivity_9(self):
        """field `Thermal Conductivity 9`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_9` or None if not set

        """
        return self["Thermal Conductivity 9"]

    @thermal_conductivity_9.setter
    def thermal_conductivity_9(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 9`"""
        self["Thermal Conductivity 9"] = value

    @property
    def moisture_content_10(self):
        """field `Moisture Content 10`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_10` or None if not set

        """
        return self["Moisture Content 10"]

    @moisture_content_10.setter
    def moisture_content_10(self, value=None):
        """Corresponds to IDD field `Moisture Content 10`"""
        self["Moisture Content 10"] = value

    @property
    def thermal_conductivity_10(self):
        """field `Thermal Conductivity 10`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_10` or None if not set

        """
        return self["Thermal Conductivity 10"]

    @thermal_conductivity_10.setter
    def thermal_conductivity_10(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 10`"""
        self["Thermal Conductivity 10"] = value

    @property
    def moisture_content_11(self):
        """field `Moisture Content 11`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_11` or None if not set

        """
        return self["Moisture Content 11"]

    @moisture_content_11.setter
    def moisture_content_11(self, value=None):
        """Corresponds to IDD field `Moisture Content 11`"""
        self["Moisture Content 11"] = value

    @property
    def thermal_conductivity_11(self):
        """field `Thermal Conductivity 11`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_11` or None if not set

        """
        return self["Thermal Conductivity 11"]

    @thermal_conductivity_11.setter
    def thermal_conductivity_11(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 11`"""
        self["Thermal Conductivity 11"] = value

    @property
    def moisture_content_12(self):
        """field `Moisture Content 12`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_12` or None if not set

        """
        return self["Moisture Content 12"]

    @moisture_content_12.setter
    def moisture_content_12(self, value=None):
        """Corresponds to IDD field `Moisture Content 12`"""
        self["Moisture Content 12"] = value

    @property
    def thermal_conductivity_12(self):
        """field `Thermal Conductivity 12`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_12` or None if not set

        """
        return self["Thermal Conductivity 12"]

    @thermal_conductivity_12.setter
    def thermal_conductivity_12(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 12`"""
        self["Thermal Conductivity 12"] = value

    @property
    def moisture_content_13(self):
        """field `Moisture Content 13`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_13` or None if not set

        """
        return self["Moisture Content 13"]

    @moisture_content_13.setter
    def moisture_content_13(self, value=None):
        """Corresponds to IDD field `Moisture Content 13`"""
        self["Moisture Content 13"] = value

    @property
    def thermal_conductivity_13(self):
        """field `Thermal Conductivity 13`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_13` or None if not set

        """
        return self["Thermal Conductivity 13"]

    @thermal_conductivity_13.setter
    def thermal_conductivity_13(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 13`"""
        self["Thermal Conductivity 13"] = value

    @property
    def moisture_content_14(self):
        """field `Moisture Content 14`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_14` or None if not set

        """
        return self["Moisture Content 14"]

    @moisture_content_14.setter
    def moisture_content_14(self, value=None):
        """Corresponds to IDD field `Moisture Content 14`"""
        self["Moisture Content 14"] = value

    @property
    def thermal_conductivity_14(self):
        """field `Thermal Conductivity 14`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_14` or None if not set

        """
        return self["Thermal Conductivity 14"]

    @thermal_conductivity_14.setter
    def thermal_conductivity_14(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 14`"""
        self["Thermal Conductivity 14"] = value

    @property
    def moisture_content_15(self):
        """field `Moisture Content 15`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_15` or None if not set

        """
        return self["Moisture Content 15"]

    @moisture_content_15.setter
    def moisture_content_15(self, value=None):
        """Corresponds to IDD field `Moisture Content 15`"""
        self["Moisture Content 15"] = value

    @property
    def thermal_conductivity_15(self):
        """field `Thermal Conductivity 15`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_15` or None if not set

        """
        return self["Thermal Conductivity 15"]

    @thermal_conductivity_15.setter
    def thermal_conductivity_15(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 15`"""
        self["Thermal Conductivity 15"] = value

    @property
    def moisture_content_16(self):
        """field `Moisture Content 16`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_16` or None if not set

        """
        return self["Moisture Content 16"]

    @moisture_content_16.setter
    def moisture_content_16(self, value=None):
        """Corresponds to IDD field `Moisture Content 16`"""
        self["Moisture Content 16"] = value

    @property
    def thermal_conductivity_16(self):
        """field `Thermal Conductivity 16`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_16` or None if not set

        """
        return self["Thermal Conductivity 16"]

    @thermal_conductivity_16.setter
    def thermal_conductivity_16(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 16`"""
        self["Thermal Conductivity 16"] = value

    @property
    def moisture_content_17(self):
        """field `Moisture Content 17`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_17` or None if not set

        """
        return self["Moisture Content 17"]

    @moisture_content_17.setter
    def moisture_content_17(self, value=None):
        """Corresponds to IDD field `Moisture Content 17`"""
        self["Moisture Content 17"] = value

    @property
    def thermal_conductivity_17(self):
        """field `Thermal Conductivity 17`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_17` or None if not set

        """
        return self["Thermal Conductivity 17"]

    @thermal_conductivity_17.setter
    def thermal_conductivity_17(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 17`"""
        self["Thermal Conductivity 17"] = value

    @property
    def moisture_content_18(self):
        """field `Moisture Content 18`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_18` or None if not set

        """
        return self["Moisture Content 18"]

    @moisture_content_18.setter
    def moisture_content_18(self, value=None):
        """Corresponds to IDD field `Moisture Content 18`"""
        self["Moisture Content 18"] = value

    @property
    def thermal_conductivity_18(self):
        """field `Thermal Conductivity 18`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_18` or None if not set

        """
        return self["Thermal Conductivity 18"]

    @thermal_conductivity_18.setter
    def thermal_conductivity_18(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 18`"""
        self["Thermal Conductivity 18"] = value

    @property
    def moisture_content_19(self):
        """field `Moisture Content 19`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_19` or None if not set

        """
        return self["Moisture Content 19"]

    @moisture_content_19.setter
    def moisture_content_19(self, value=None):
        """Corresponds to IDD field `Moisture Content 19`"""
        self["Moisture Content 19"] = value

    @property
    def thermal_conductivity_19(self):
        """field `Thermal Conductivity 19`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_19` or None if not set

        """
        return self["Thermal Conductivity 19"]

    @thermal_conductivity_19.setter
    def thermal_conductivity_19(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 19`"""
        self["Thermal Conductivity 19"] = value

    @property
    def moisture_content_20(self):
        """field `Moisture Content 20`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_20` or None if not set

        """
        return self["Moisture Content 20"]

    @moisture_content_20.setter
    def moisture_content_20(self, value=None):
        """Corresponds to IDD field `Moisture Content 20`"""
        self["Moisture Content 20"] = value

    @property
    def thermal_conductivity_20(self):
        """field `Thermal Conductivity 20`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_20` or None if not set

        """
        return self["Thermal Conductivity 20"]

    @thermal_conductivity_20.setter
    def thermal_conductivity_20(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 20`"""
        self["Thermal Conductivity 20"] = value

    @property
    def moisture_content_21(self):
        """field `Moisture Content 21`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_21` or None if not set

        """
        return self["Moisture Content 21"]

    @moisture_content_21.setter
    def moisture_content_21(self, value=None):
        """Corresponds to IDD field `Moisture Content 21`"""
        self["Moisture Content 21"] = value

    @property
    def thermal_conductivity_21(self):
        """field `Thermal Conductivity 21`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_21` or None if not set

        """
        return self["Thermal Conductivity 21"]

    @thermal_conductivity_21.setter
    def thermal_conductivity_21(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 21`"""
        self["Thermal Conductivity 21"] = value

    @property
    def moisture_content_22(self):
        """field `Moisture Content 22`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_22` or None if not set

        """
        return self["Moisture Content 22"]

    @moisture_content_22.setter
    def moisture_content_22(self, value=None):
        """Corresponds to IDD field `Moisture Content 22`"""
        self["Moisture Content 22"] = value

    @property
    def thermal_conductivity_22(self):
        """field `Thermal Conductivity 22`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_22` or None if not set

        """
        return self["Thermal Conductivity 22"]

    @thermal_conductivity_22.setter
    def thermal_conductivity_22(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 22`"""
        self["Thermal Conductivity 22"] = value

    @property
    def moisture_content_23(self):
        """field `Moisture Content 23`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_23` or None if not set

        """
        return self["Moisture Content 23"]

    @moisture_content_23.setter
    def moisture_content_23(self, value=None):
        """Corresponds to IDD field `Moisture Content 23`"""
        self["Moisture Content 23"] = value

    @property
    def thermal_conductivity_23(self):
        """field `Thermal Conductivity 23`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_23` or None if not set

        """
        return self["Thermal Conductivity 23"]

    @thermal_conductivity_23.setter
    def thermal_conductivity_23(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 23`"""
        self["Thermal Conductivity 23"] = value

    @property
    def moisture_content_24(self):
        """field `Moisture Content 24`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_24` or None if not set

        """
        return self["Moisture Content 24"]

    @moisture_content_24.setter
    def moisture_content_24(self, value=None):
        """Corresponds to IDD field `Moisture Content 24`"""
        self["Moisture Content 24"] = value

    @property
    def thermal_conductivity_24(self):
        """field `Thermal Conductivity 24`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_24` or None if not set

        """
        return self["Thermal Conductivity 24"]

    @thermal_conductivity_24.setter
    def thermal_conductivity_24(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 24`"""
        self["Thermal Conductivity 24"] = value

    @property
    def moisture_content_25(self):
        """field `Moisture Content 25`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Moisture Content 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `moisture_content_25` or None if not set

        """
        return self["Moisture Content 25"]

    @moisture_content_25.setter
    def moisture_content_25(self, value=None):
        """Corresponds to IDD field `Moisture Content 25`"""
        self["Moisture Content 25"] = value

    @property
    def thermal_conductivity_25(self):
        """field `Thermal Conductivity 25`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Thermal Conductivity 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_25` or None if not set

        """
        return self["Thermal Conductivity 25"]

    @thermal_conductivity_25.setter
    def thermal_conductivity_25(self, value=None):
        """Corresponds to IDD field `Thermal Conductivity 25`"""
        self["Thermal Conductivity 25"] = value




class Construction(DataObject):

    """Corresponds to IDD object `Construction` Start with outside layer and
    work your way to the inside layer Up to 10 layers total, 8 for windows
    Enter the material name for each layer."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'outside layer',
                                       {'name': u'Outside Layer',
                                        'pyname': u'outside_layer',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2',
                                       {'name': u'Layer 2',
                                        'pyname': u'layer_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3',
                                       {'name': u'Layer 3',
                                        'pyname': u'layer_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4',
                                       {'name': u'Layer 4',
                                        'pyname': u'layer_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5',
                                       {'name': u'Layer 5',
                                        'pyname': u'layer_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 6',
                                       {'name': u'Layer 6',
                                        'pyname': u'layer_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 7',
                                       {'name': u'Layer 7',
                                        'pyname': u'layer_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 8',
                                       {'name': u'Layer 8',
                                        'pyname': u'layer_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 9',
                                       {'name': u'Layer 9',
                                        'pyname': u'layer_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 10',
                                       {'name': u'Layer 10',
                                        'pyname': u'layer_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'Construction',
               'pyname': u'Construction',
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
    def outside_layer(self):
        """field `Outside Layer`

        Args:
            value (str): value for IDD Field `Outside Layer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_layer` or None if not set

        """
        return self["Outside Layer"]

    @outside_layer.setter
    def outside_layer(self, value=None):
        """Corresponds to IDD field `Outside Layer`"""
        self["Outside Layer"] = value

    @property
    def layer_2(self):
        """field `Layer 2`

        Args:
            value (str): value for IDD Field `Layer 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2` or None if not set

        """
        return self["Layer 2"]

    @layer_2.setter
    def layer_2(self, value=None):
        """Corresponds to IDD field `Layer 2`"""
        self["Layer 2"] = value

    @property
    def layer_3(self):
        """field `Layer 3`

        Args:
            value (str): value for IDD Field `Layer 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3` or None if not set

        """
        return self["Layer 3"]

    @layer_3.setter
    def layer_3(self, value=None):
        """Corresponds to IDD field `Layer 3`"""
        self["Layer 3"] = value

    @property
    def layer_4(self):
        """field `Layer 4`

        Args:
            value (str): value for IDD Field `Layer 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4` or None if not set

        """
        return self["Layer 4"]

    @layer_4.setter
    def layer_4(self, value=None):
        """Corresponds to IDD field `Layer 4`"""
        self["Layer 4"] = value

    @property
    def layer_5(self):
        """field `Layer 5`

        Args:
            value (str): value for IDD Field `Layer 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5` or None if not set

        """
        return self["Layer 5"]

    @layer_5.setter
    def layer_5(self, value=None):
        """Corresponds to IDD field `Layer 5`"""
        self["Layer 5"] = value

    @property
    def layer_6(self):
        """field `Layer 6`

        Args:
            value (str): value for IDD Field `Layer 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_6` or None if not set

        """
        return self["Layer 6"]

    @layer_6.setter
    def layer_6(self, value=None):
        """Corresponds to IDD field `Layer 6`"""
        self["Layer 6"] = value

    @property
    def layer_7(self):
        """field `Layer 7`

        Args:
            value (str): value for IDD Field `Layer 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_7` or None if not set

        """
        return self["Layer 7"]

    @layer_7.setter
    def layer_7(self, value=None):
        """Corresponds to IDD field `Layer 7`"""
        self["Layer 7"] = value

    @property
    def layer_8(self):
        """field `Layer 8`

        Args:
            value (str): value for IDD Field `Layer 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_8` or None if not set

        """
        return self["Layer 8"]

    @layer_8.setter
    def layer_8(self, value=None):
        """Corresponds to IDD field `Layer 8`"""
        self["Layer 8"] = value

    @property
    def layer_9(self):
        """field `Layer 9`

        Args:
            value (str): value for IDD Field `Layer 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_9` or None if not set

        """
        return self["Layer 9"]

    @layer_9.setter
    def layer_9(self, value=None):
        """Corresponds to IDD field `Layer 9`"""
        self["Layer 9"] = value

    @property
    def layer_10(self):
        """field `Layer 10`

        Args:
            value (str): value for IDD Field `Layer 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_10` or None if not set

        """
        return self["Layer 10"]

    @layer_10.setter
    def layer_10(self, value=None):
        """Corresponds to IDD field `Layer 10`"""
        self["Layer 10"] = value




class ConstructionCfactorUndergroundWall(DataObject):

    """ Corresponds to IDD object `Construction:CfactorUndergroundWall`
        Alternate method of describing underground wall constructions
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'c-factor',
                                       {'name': u'C-Factor',
                                        'pyname': u'cfactor',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'height',
                                       {'name': u'Height',
                                        'pyname': u'height',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'Construction:CfactorUndergroundWall',
               'pyname': u'ConstructionCfactorUndergroundWall',
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
    def cfactor(self):
        """field `C-Factor`

        |  Enter C-Factor without film coefficients or soil
        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `C-Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cfactor` or None if not set
        """
        return self["C-Factor"]

    @cfactor.setter
    def cfactor(self, value=None):
        """  Corresponds to IDD field `C-Factor`

        """
        self["C-Factor"] = value

    @property
    def height(self):
        """field `Height`

        |  Enter height of the underground wall
        |  Units: m

        Args:
            value (float): value for IDD Field `Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `height` or None if not set

        """
        return self["Height"]

    @height.setter
    def height(self, value=None):
        """Corresponds to IDD field `Height`"""
        self["Height"] = value




class ConstructionFfactorGroundFloor(DataObject):

    """ Corresponds to IDD object `Construction:FfactorGroundFloor`
        Alternate method of describing slab-on-grade or underground floor constructions
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'f-factor',
                                       {'name': u'F-Factor',
                                        'pyname': u'ffactor',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'area',
                                       {'name': u'Area',
                                        'pyname': u'area',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'perimeterexposed',
                                       {'name': u'PerimeterExposed',
                                        'pyname': u'perimeterexposed',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'Construction:FfactorGroundFloor',
               'pyname': u'ConstructionFfactorGroundFloor',
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
    def ffactor(self):
        """field `F-Factor`

        |  Units: W/m-K
        |  IP-Units: Btu/h-ft-F

        Args:
            value (float): value for IDD Field `F-Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ffactor` or None if not set
        """
        return self["F-Factor"]

    @ffactor.setter
    def ffactor(self, value=None):
        """  Corresponds to IDD field `F-Factor`

        """
        self["F-Factor"] = value

    @property
    def area(self):
        """field `Area`

        |  Enter area of the floor
        |  Units: m2

        Args:
            value (float): value for IDD Field `Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `area` or None if not set

        """
        return self["Area"]

    @area.setter
    def area(self, value=None):
        """Corresponds to IDD field `Area`"""
        self["Area"] = value

    @property
    def perimeterexposed(self):
        """field `PerimeterExposed`

        |  Enter exposed perimeter of the floor
        |  Units: m

        Args:
            value (float): value for IDD Field `PerimeterExposed`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `perimeterexposed` or None if not set

        """
        return self["PerimeterExposed"]

    @perimeterexposed.setter
    def perimeterexposed(self, value=None):
        """Corresponds to IDD field `PerimeterExposed`"""
        self["PerimeterExposed"] = value




class ConstructionInternalSource(DataObject):

    """ Corresponds to IDD object `Construction:InternalSource`
        Start with outside layer and work your way to the inside Layer
        Up to 10 layers total, 8 for windows
        Enter the material name for each layer
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'source present after layer number',
                                       {'name': u'Source Present After Layer Number',
                                        'pyname': u'source_present_after_layer_number',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'temperature calculation requested after layer number',
                                       {'name': u'Temperature Calculation Requested After Layer Number',
                                        'pyname': u'temperature_calculation_requested_after_layer_number',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'dimensions for the ctf calculation',
                                       {'name': u'Dimensions for the CTF Calculation',
                                        'pyname': u'dimensions_for_the_ctf_calculation',
                                        'maximum': 2,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'tube spacing',
                                       {'name': u'Tube Spacing',
                                        'pyname': u'tube_spacing',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'outside layer',
                                       {'name': u'Outside Layer',
                                        'pyname': u'outside_layer',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2',
                                       {'name': u'Layer 2',
                                        'pyname': u'layer_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3',
                                       {'name': u'Layer 3',
                                        'pyname': u'layer_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4',
                                       {'name': u'Layer 4',
                                        'pyname': u'layer_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5',
                                       {'name': u'Layer 5',
                                        'pyname': u'layer_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 6',
                                       {'name': u'Layer 6',
                                        'pyname': u'layer_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 7',
                                       {'name': u'Layer 7',
                                        'pyname': u'layer_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 8',
                                       {'name': u'Layer 8',
                                        'pyname': u'layer_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 9',
                                       {'name': u'Layer 9',
                                        'pyname': u'layer_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 10',
                                       {'name': u'Layer 10',
                                        'pyname': u'layer_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'Construction:InternalSource',
               'pyname': u'ConstructionInternalSource',
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
    def source_present_after_layer_number(self):
        """field `Source Present After Layer Number`

        |  refers to the list of materials which follows
        |  value >= 1

        Args:
            value (int): value for IDD Field `Source Present After Layer Number`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `source_present_after_layer_number` or None if not set

        """
        return self["Source Present After Layer Number"]

    @source_present_after_layer_number.setter
    def source_present_after_layer_number(self, value=None):
        """Corresponds to IDD field `Source Present After Layer Number`"""
        self["Source Present After Layer Number"] = value

    @property
    def temperature_calculation_requested_after_layer_number(self):
        """field `Temperature Calculation Requested After Layer Number`

        |  refers to the list of materials which follows

        Args:
            value (int): value for IDD Field `Temperature Calculation Requested After Layer Number`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `temperature_calculation_requested_after_layer_number` or None if not set

        """
        return self["Temperature Calculation Requested After Layer Number"]

    @temperature_calculation_requested_after_layer_number.setter
    def temperature_calculation_requested_after_layer_number(self, value=None):
        """Corresponds to IDD field `Temperature Calculation Requested After
        Layer Number`"""
        self["Temperature Calculation Requested After Layer Number"] = value

    @property
    def dimensions_for_the_ctf_calculation(self):
        """field `Dimensions for the CTF Calculation`

        |  1 = 1-dimensional calculation, 2 = 2-dimensional calculation
        |  value >= 1
        |  value <= 2

        Args:
            value (int): value for IDD Field `Dimensions for the CTF Calculation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `dimensions_for_the_ctf_calculation` or None if not set

        """
        return self["Dimensions for the CTF Calculation"]

    @dimensions_for_the_ctf_calculation.setter
    def dimensions_for_the_ctf_calculation(self, value=None):
        """Corresponds to IDD field `Dimensions for the CTF Calculation`"""
        self["Dimensions for the CTF Calculation"] = value

    @property
    def tube_spacing(self):
        """field `Tube Spacing`

        |  uniform spacing between tubes or resistance wires in direction
        |  perpendicular to main intended direction of heat transfer
        |  Units: m

        Args:
            value (float): value for IDD Field `Tube Spacing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tube_spacing` or None if not set

        """
        return self["Tube Spacing"]

    @tube_spacing.setter
    def tube_spacing(self, value=None):
        """Corresponds to IDD field `Tube Spacing`"""
        self["Tube Spacing"] = value

    @property
    def outside_layer(self):
        """field `Outside Layer`

        Args:
            value (str): value for IDD Field `Outside Layer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_layer` or None if not set

        """
        return self["Outside Layer"]

    @outside_layer.setter
    def outside_layer(self, value=None):
        """Corresponds to IDD field `Outside Layer`"""
        self["Outside Layer"] = value

    @property
    def layer_2(self):
        """field `Layer 2`

        Args:
            value (str): value for IDD Field `Layer 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2` or None if not set

        """
        return self["Layer 2"]

    @layer_2.setter
    def layer_2(self, value=None):
        """Corresponds to IDD field `Layer 2`"""
        self["Layer 2"] = value

    @property
    def layer_3(self):
        """field `Layer 3`

        Args:
            value (str): value for IDD Field `Layer 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3` or None if not set

        """
        return self["Layer 3"]

    @layer_3.setter
    def layer_3(self, value=None):
        """Corresponds to IDD field `Layer 3`"""
        self["Layer 3"] = value

    @property
    def layer_4(self):
        """field `Layer 4`

        Args:
            value (str): value for IDD Field `Layer 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4` or None if not set

        """
        return self["Layer 4"]

    @layer_4.setter
    def layer_4(self, value=None):
        """Corresponds to IDD field `Layer 4`"""
        self["Layer 4"] = value

    @property
    def layer_5(self):
        """field `Layer 5`

        Args:
            value (str): value for IDD Field `Layer 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5` or None if not set

        """
        return self["Layer 5"]

    @layer_5.setter
    def layer_5(self, value=None):
        """Corresponds to IDD field `Layer 5`"""
        self["Layer 5"] = value

    @property
    def layer_6(self):
        """field `Layer 6`

        Args:
            value (str): value for IDD Field `Layer 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_6` or None if not set

        """
        return self["Layer 6"]

    @layer_6.setter
    def layer_6(self, value=None):
        """Corresponds to IDD field `Layer 6`"""
        self["Layer 6"] = value

    @property
    def layer_7(self):
        """field `Layer 7`

        Args:
            value (str): value for IDD Field `Layer 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_7` or None if not set

        """
        return self["Layer 7"]

    @layer_7.setter
    def layer_7(self, value=None):
        """Corresponds to IDD field `Layer 7`"""
        self["Layer 7"] = value

    @property
    def layer_8(self):
        """field `Layer 8`

        Args:
            value (str): value for IDD Field `Layer 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_8` or None if not set

        """
        return self["Layer 8"]

    @layer_8.setter
    def layer_8(self, value=None):
        """Corresponds to IDD field `Layer 8`"""
        self["Layer 8"] = value

    @property
    def layer_9(self):
        """field `Layer 9`

        Args:
            value (str): value for IDD Field `Layer 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_9` or None if not set

        """
        return self["Layer 9"]

    @layer_9.setter
    def layer_9(self, value=None):
        """Corresponds to IDD field `Layer 9`"""
        self["Layer 9"] = value

    @property
    def layer_10(self):
        """field `Layer 10`

        Args:
            value (str): value for IDD Field `Layer 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_10` or None if not set

        """
        return self["Layer 10"]

    @layer_10.setter
    def layer_10(self, value=None):
        """Corresponds to IDD field `Layer 10`"""
        self["Layer 10"] = value




class WindowThermalModelParams(DataObject):

    """ Corresponds to IDD object `WindowThermalModel:Params`
        object is used to select which thermal model should be used in tarcog simulations
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'standard',
                                       {'name': u'standard',
                                        'pyname': u'standard',
                                        'default': u'ISO15099',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ISO15099',
                                                            u'EN673Declared',
                                                            u'EN673Design'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal model',
                                       {'name': u'Thermal Model',
                                        'pyname': u'thermal_model',
                                        'default': u'ISO15099',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ISO15099',
                                                            u'ScaledCavityWidth',
                                                            u'ConvectiveScalarModel_NoSDThickness',
                                                            u'ConvectiveScalarModel_withSDThickness'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'sdscalar',
                                       {'name': u'SDScalar',
                                        'pyname': u'sdscalar',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'deflection model',
                                       {'name': u'Deflection Model',
                                        'pyname': u'deflection_model',
                                        'default': u'NoDeflection',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NoDeflection',
                                                            u'TemperatureAndPressureInput',
                                                            u'MeasuredDeflection'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'vacuum pressure limit',
                                       {'name': u'Vacuum Pressure Limit',
                                        'pyname': u'vacuum_pressure_limit',
                                        'default': 13.238,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'initial temperature',
                                       {'name': u'Initial temperature',
                                        'pyname': u'initial_temperature',
                                        'default': 25.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'initial pressure',
                                       {'name': u'Initial pressure',
                                        'pyname': u'initial_pressure',
                                        'default': 101325.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'WindowThermalModel:Params',
               'pyname': u'WindowThermalModelParams',
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
    def standard(self):
        """field `standard`

        |  Default value: ISO15099

        Args:
            value (str): value for IDD Field `standard`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `standard` or None if not set

        """
        return self["standard"]

    @standard.setter
    def standard(self, value="ISO15099"):
        """Corresponds to IDD field `standard`"""
        self["standard"] = value

    @property
    def thermal_model(self):
        """field `Thermal Model`

        |  Default value: ISO15099

        Args:
            value (str): value for IDD Field `Thermal Model`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_model` or None if not set

        """
        return self["Thermal Model"]

    @thermal_model.setter
    def thermal_model(self, value="ISO15099"):
        """Corresponds to IDD field `Thermal Model`"""
        self["Thermal Model"] = value

    @property
    def sdscalar(self):
        """field `SDScalar`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `SDScalar`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sdscalar` or None if not set

        """
        return self["SDScalar"]

    @sdscalar.setter
    def sdscalar(self, value=1.0):
        """Corresponds to IDD field `SDScalar`"""
        self["SDScalar"] = value

    @property
    def deflection_model(self):
        """field `Deflection Model`

        |  Default value: NoDeflection

        Args:
            value (str): value for IDD Field `Deflection Model`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `deflection_model` or None if not set

        """
        return self["Deflection Model"]

    @deflection_model.setter
    def deflection_model(self, value="NoDeflection"):
        """Corresponds to IDD field `Deflection Model`"""
        self["Deflection Model"] = value

    @property
    def vacuum_pressure_limit(self):
        """field `Vacuum Pressure Limit`

        |  Units: Pa
        |  Default value: 13.238

        Args:
            value (float): value for IDD Field `Vacuum Pressure Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `vacuum_pressure_limit` or None if not set

        """
        return self["Vacuum Pressure Limit"]

    @vacuum_pressure_limit.setter
    def vacuum_pressure_limit(self, value=13.238):
        """Corresponds to IDD field `Vacuum Pressure Limit`"""
        self["Vacuum Pressure Limit"] = value

    @property
    def initial_temperature(self):
        """field `Initial temperature`

        |  This is temperature in time of window fabrication
        |  Units: C
        |  Default value: 25.0

        Args:
            value (float): value for IDD Field `Initial temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_temperature` or None if not set

        """
        return self["Initial temperature"]

    @initial_temperature.setter
    def initial_temperature(self, value=25.0):
        """Corresponds to IDD field `Initial temperature`"""
        self["Initial temperature"] = value

    @property
    def initial_pressure(self):
        """field `Initial pressure`

        |  This is pressure in time of window fabrication
        |  Units: Pa
        |  Default value: 101325.0

        Args:
            value (float): value for IDD Field `Initial pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_pressure` or None if not set

        """
        return self["Initial pressure"]

    @initial_pressure.setter
    def initial_pressure(self, value=101325.0):
        """Corresponds to IDD field `Initial pressure`"""
        self["Initial pressure"] = value




class ConstructionComplexFenestrationState(DataObject):

    """ Corresponds to IDD object `Construction:ComplexFenestrationState`
        Describes one state for a complex glazing system
        These input objects are typically generated by using WINDOW software and export to IDF syntax
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'basis type',
                                       {'name': u'Basis Type',
                                        'pyname': u'basis_type',
                                        'default': u'LBNLWINDOW',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LBNLWINDOW',
                                                            u'UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'basis symmetry type',
                                       {'name': u'Basis Symmetry Type',
                                        'pyname': u'basis_symmetry_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Axisymmetric',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'window thermal model',
                                       {'name': u'Window Thermal Model',
                                        'pyname': u'window_thermal_model',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'basis matrix name',
                                       {'name': u'Basis Matrix Name',
                                        'pyname': u'basis_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'solar optical complex front transmittance matrix name',
                                       {'name': u'Solar Optical Complex Front Transmittance Matrix Name',
                                        'pyname': u'solar_optical_complex_front_transmittance_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'solar optical complex back reflectance matrix name',
                                       {'name': u'Solar Optical Complex Back Reflectance Matrix Name',
                                        'pyname': u'solar_optical_complex_back_reflectance_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'visible optical complex front transmittance matrix name',
                                       {'name': u'Visible Optical Complex Front Transmittance Matrix Name',
                                        'pyname': u'visible_optical_complex_front_transmittance_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'visible optical complex back transmittance matrix name',
                                       {'name': u'Visible Optical Complex Back Transmittance Matrix Name',
                                        'pyname': u'visible_optical_complex_back_transmittance_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outside layer name',
                                       {'name': u'Outside Layer Name',
                                        'pyname': u'outside_layer_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outside layer directional front absoptance matrix name',
                                       {'name': u'Outside Layer Directional Front Absoptance Matrix Name',
                                        'pyname': u'outside_layer_directional_front_absoptance_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outside layer directional back absoptance matrix name',
                                       {'name': u'Outside Layer Directional Back Absoptance Matrix Name',
                                        'pyname': u'outside_layer_directional_back_absoptance_matrix_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 1 name',
                                       {'name': u'Gap 1 Name',
                                        'pyname': u'gap_1_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cfs gap 1 directional front absoptance matrix name',
                                       {'name': u'CFS Gap 1 Directional Front Absoptance Matrix Name',
                                        'pyname': u'cfs_gap_1_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cfs gap 1 directional back absoptance matrix name',
                                       {'name': u'CFS Gap 1 Directional Back Absoptance Matrix Name',
                                        'pyname': u'cfs_gap_1_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2 name',
                                       {'name': u'Layer 2 Name',
                                        'pyname': u'layer_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2 directional front absoptance matrix name',
                                       {'name': u'Layer 2 Directional Front Absoptance Matrix Name',
                                        'pyname': u'layer_2_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2 directional back absoptance matrix name',
                                       {'name': u'Layer 2 Directional Back Absoptance Matrix Name',
                                        'pyname': u'layer_2_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 2 name',
                                       {'name': u'Gap 2 Name',
                                        'pyname': u'gap_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 2 directional front absoptance matrix name',
                                       {'name': u'Gap 2 Directional Front Absoptance Matrix Name',
                                        'pyname': u'gap_2_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 2 directional back absoptance matrix name',
                                       {'name': u'Gap 2 Directional Back Absoptance Matrix Name',
                                        'pyname': u'gap_2_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3 material',
                                       {'name': u'Layer 3 Material',
                                        'pyname': u'layer_3_material',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3 directional front absoptance matrix name',
                                       {'name': u'Layer 3 Directional Front Absoptance Matrix Name',
                                        'pyname': u'layer_3_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3 directional back absoptance matrix name',
                                       {'name': u'Layer 3 Directional Back Absoptance Matrix Name',
                                        'pyname': u'layer_3_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 3 name',
                                       {'name': u'Gap 3 Name',
                                        'pyname': u'gap_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 3 directional front absoptance matrix name',
                                       {'name': u'Gap 3 Directional Front Absoptance Matrix Name',
                                        'pyname': u'gap_3_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 3 directional back absoptance matrix name',
                                       {'name': u'Gap 3 Directional Back Absoptance Matrix Name',
                                        'pyname': u'gap_3_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4 name',
                                       {'name': u'Layer 4 Name',
                                        'pyname': u'layer_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4 directional front absoptance matrix name',
                                       {'name': u'Layer 4 Directional Front Absoptance Matrix Name',
                                        'pyname': u'layer_4_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4 directional back absoptance matrix name',
                                       {'name': u'Layer 4 Directional Back Absoptance Matrix Name',
                                        'pyname': u'layer_4_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 4 name',
                                       {'name': u'Gap 4 Name',
                                        'pyname': u'gap_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 4 directional front absoptance matrix name',
                                       {'name': u'Gap 4 Directional Front Absoptance Matrix Name',
                                        'pyname': u'gap_4_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gap 4 directional back absoptance matrix name',
                                       {'name': u'Gap 4 Directional Back Absoptance Matrix Name',
                                        'pyname': u'gap_4_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5 name',
                                       {'name': u'Layer 5 Name',
                                        'pyname': u'layer_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5 directional front absoptance matrix name',
                                       {'name': u'Layer 5 Directional Front Absoptance Matrix Name',
                                        'pyname': u'layer_5_directional_front_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5 directional back absoptance matrix name',
                                       {'name': u'Layer 5 Directional Back Absoptance Matrix Name',
                                        'pyname': u'layer_5_directional_back_absoptance_matrix_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'Construction:ComplexFenestrationState',
               'pyname': u'ConstructionComplexFenestrationState',
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
    def basis_type(self):
        """field `Basis Type`

        |  Default value: LBNLWINDOW

        Args:
            value (str): value for IDD Field `Basis Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basis_type` or None if not set

        """
        return self["Basis Type"]

    @basis_type.setter
    def basis_type(self, value="LBNLWINDOW"):
        """Corresponds to IDD field `Basis Type`"""
        self["Basis Type"] = value

    @property
    def basis_symmetry_type(self):
        """field `Basis Symmetry Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Basis Symmetry Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basis_symmetry_type` or None if not set

        """
        return self["Basis Symmetry Type"]

    @basis_symmetry_type.setter
    def basis_symmetry_type(self, value="None"):
        """Corresponds to IDD field `Basis Symmetry Type`"""
        self["Basis Symmetry Type"] = value

    @property
    def window_thermal_model(self):
        """field `Window Thermal Model`

        Args:
            value (str): value for IDD Field `Window Thermal Model`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `window_thermal_model` or None if not set

        """
        return self["Window Thermal Model"]

    @window_thermal_model.setter
    def window_thermal_model(self, value=None):
        """Corresponds to IDD field `Window Thermal Model`"""
        self["Window Thermal Model"] = value

    @property
    def basis_matrix_name(self):
        """field `Basis Matrix Name`

        Args:
            value (str): value for IDD Field `Basis Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basis_matrix_name` or None if not set

        """
        return self["Basis Matrix Name"]

    @basis_matrix_name.setter
    def basis_matrix_name(self, value=None):
        """Corresponds to IDD field `Basis Matrix Name`"""
        self["Basis Matrix Name"] = value

    @property
    def solar_optical_complex_front_transmittance_matrix_name(self):
        """field `Solar Optical Complex Front Transmittance Matrix Name`

        Args:
            value (str): value for IDD Field `Solar Optical Complex Front Transmittance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_optical_complex_front_transmittance_matrix_name` or None if not set

        """
        return self["Solar Optical Complex Front Transmittance Matrix Name"]

    @solar_optical_complex_front_transmittance_matrix_name.setter
    def solar_optical_complex_front_transmittance_matrix_name(
            self,
            value=None):
        """Corresponds to IDD field `Solar Optical Complex Front Transmittance
        Matrix Name`"""
        self["Solar Optical Complex Front Transmittance Matrix Name"] = value

    @property
    def solar_optical_complex_back_reflectance_matrix_name(self):
        """field `Solar Optical Complex Back Reflectance Matrix Name`

        Args:
            value (str): value for IDD Field `Solar Optical Complex Back Reflectance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_optical_complex_back_reflectance_matrix_name` or None if not set

        """
        return self["Solar Optical Complex Back Reflectance Matrix Name"]

    @solar_optical_complex_back_reflectance_matrix_name.setter
    def solar_optical_complex_back_reflectance_matrix_name(self, value=None):
        """Corresponds to IDD field `Solar Optical Complex Back Reflectance
        Matrix Name`"""
        self["Solar Optical Complex Back Reflectance Matrix Name"] = value

    @property
    def visible_optical_complex_front_transmittance_matrix_name(self):
        """field `Visible Optical Complex Front Transmittance Matrix Name`

        Args:
            value (str): value for IDD Field `Visible Optical Complex Front Transmittance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `visible_optical_complex_front_transmittance_matrix_name` or None if not set

        """
        return self["Visible Optical Complex Front Transmittance Matrix Name"]

    @visible_optical_complex_front_transmittance_matrix_name.setter
    def visible_optical_complex_front_transmittance_matrix_name(
            self,
            value=None):
        """Corresponds to IDD field `Visible Optical Complex Front
        Transmittance Matrix Name`"""
        self["Visible Optical Complex Front Transmittance Matrix Name"] = value

    @property
    def visible_optical_complex_back_transmittance_matrix_name(self):
        """field `Visible Optical Complex Back Transmittance Matrix Name`

        Args:
            value (str): value for IDD Field `Visible Optical Complex Back Transmittance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `visible_optical_complex_back_transmittance_matrix_name` or None if not set

        """
        return self["Visible Optical Complex Back Transmittance Matrix Name"]

    @visible_optical_complex_back_transmittance_matrix_name.setter
    def visible_optical_complex_back_transmittance_matrix_name(
            self,
            value=None):
        """Corresponds to IDD field `Visible Optical Complex Back Transmittance
        Matrix Name`"""
        self["Visible Optical Complex Back Transmittance Matrix Name"] = value

    @property
    def outside_layer_name(self):
        """field `Outside Layer Name`

        Args:
            value (str): value for IDD Field `Outside Layer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_layer_name` or None if not set

        """
        return self["Outside Layer Name"]

    @outside_layer_name.setter
    def outside_layer_name(self, value=None):
        """Corresponds to IDD field `Outside Layer Name`"""
        self["Outside Layer Name"] = value

    @property
    def outside_layer_directional_front_absoptance_matrix_name(self):
        """field `Outside Layer Directional Front Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Outside Layer Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_layer_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Outside Layer Directional Front Absoptance Matrix Name"]

    @outside_layer_directional_front_absoptance_matrix_name.setter
    def outside_layer_directional_front_absoptance_matrix_name(
            self,
            value=None):
        """Corresponds to IDD field `Outside Layer Directional Front Absoptance
        Matrix Name`"""
        self["Outside Layer Directional Front Absoptance Matrix Name"] = value

    @property
    def outside_layer_directional_back_absoptance_matrix_name(self):
        """field `Outside Layer Directional Back Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Outside Layer Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_layer_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Outside Layer Directional Back Absoptance Matrix Name"]

    @outside_layer_directional_back_absoptance_matrix_name.setter
    def outside_layer_directional_back_absoptance_matrix_name(
            self,
            value=None):
        """Corresponds to IDD field `Outside Layer Directional Back Absoptance
        Matrix Name`"""
        self["Outside Layer Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_1_name(self):
        """field `Gap 1 Name`

        Args:
            value (str): value for IDD Field `Gap 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_1_name` or None if not set

        """
        return self["Gap 1 Name"]

    @gap_1_name.setter
    def gap_1_name(self, value=None):
        """Corresponds to IDD field `Gap 1 Name`"""
        self["Gap 1 Name"] = value

    @property
    def cfs_gap_1_directional_front_absoptance_matrix_name(self):
        """field `CFS Gap 1 Directional Front Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `CFS Gap 1 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cfs_gap_1_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["CFS Gap 1 Directional Front Absoptance Matrix Name"]

    @cfs_gap_1_directional_front_absoptance_matrix_name.setter
    def cfs_gap_1_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `CFS Gap 1 Directional Front Absoptance
        Matrix Name`"""
        self["CFS Gap 1 Directional Front Absoptance Matrix Name"] = value

    @property
    def cfs_gap_1_directional_back_absoptance_matrix_name(self):
        """field `CFS Gap 1 Directional Back Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `CFS Gap 1 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cfs_gap_1_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["CFS Gap 1 Directional Back Absoptance Matrix Name"]

    @cfs_gap_1_directional_back_absoptance_matrix_name.setter
    def cfs_gap_1_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `CFS Gap 1 Directional Back Absoptance
        Matrix Name`"""
        self["CFS Gap 1 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_2_name(self):
        """field `Layer 2 Name`

        Args:
            value (str): value for IDD Field `Layer 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2_name` or None if not set

        """
        return self["Layer 2 Name"]

    @layer_2_name.setter
    def layer_2_name(self, value=None):
        """Corresponds to IDD field `Layer 2 Name`"""
        self["Layer 2 Name"] = value

    @property
    def layer_2_directional_front_absoptance_matrix_name(self):
        """field `Layer 2 Directional Front Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 2 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Layer 2 Directional Front Absoptance Matrix Name"]

    @layer_2_directional_front_absoptance_matrix_name.setter
    def layer_2_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 2 Directional Front Absoptance
        Matrix Name`"""
        self["Layer 2 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_2_directional_back_absoptance_matrix_name(self):
        """field `Layer 2 Directional Back Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 2 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Layer 2 Directional Back Absoptance Matrix Name"]

    @layer_2_directional_back_absoptance_matrix_name.setter
    def layer_2_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 2 Directional Back Absoptance Matrix
        Name`"""
        self["Layer 2 Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_2_name(self):
        """field `Gap 2 Name`

        Args:
            value (str): value for IDD Field `Gap 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_2_name` or None if not set

        """
        return self["Gap 2 Name"]

    @gap_2_name.setter
    def gap_2_name(self, value=None):
        """Corresponds to IDD field `Gap 2 Name`"""
        self["Gap 2 Name"] = value

    @property
    def gap_2_directional_front_absoptance_matrix_name(self):
        """field `Gap 2 Directional Front Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `Gap 2 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_2_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Gap 2 Directional Front Absoptance Matrix Name"]

    @gap_2_directional_front_absoptance_matrix_name.setter
    def gap_2_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Gap 2 Directional Front Absoptance Matrix
        Name`"""
        self["Gap 2 Directional Front Absoptance Matrix Name"] = value

    @property
    def gap_2_directional_back_absoptance_matrix_name(self):
        """field `Gap 2 Directional Back Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `Gap 2 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_2_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Gap 2 Directional Back Absoptance Matrix Name"]

    @gap_2_directional_back_absoptance_matrix_name.setter
    def gap_2_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Gap 2 Directional Back Absoptance Matrix
        Name`"""
        self["Gap 2 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_3_material(self):
        """field `Layer 3 Material`

        Args:
            value (str): value for IDD Field `Layer 3 Material`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3_material` or None if not set

        """
        return self["Layer 3 Material"]

    @layer_3_material.setter
    def layer_3_material(self, value=None):
        """Corresponds to IDD field `Layer 3 Material`"""
        self["Layer 3 Material"] = value

    @property
    def layer_3_directional_front_absoptance_matrix_name(self):
        """field `Layer 3 Directional Front Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 3 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Layer 3 Directional Front Absoptance Matrix Name"]

    @layer_3_directional_front_absoptance_matrix_name.setter
    def layer_3_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 3 Directional Front Absoptance
        Matrix Name`"""
        self["Layer 3 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_3_directional_back_absoptance_matrix_name(self):
        """field `Layer 3 Directional Back Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 3 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Layer 3 Directional Back Absoptance Matrix Name"]

    @layer_3_directional_back_absoptance_matrix_name.setter
    def layer_3_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 3 Directional Back Absoptance Matrix
        Name`"""
        self["Layer 3 Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_3_name(self):
        """field `Gap 3 Name`

        Args:
            value (str): value for IDD Field `Gap 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_3_name` or None if not set

        """
        return self["Gap 3 Name"]

    @gap_3_name.setter
    def gap_3_name(self, value=None):
        """Corresponds to IDD field `Gap 3 Name`"""
        self["Gap 3 Name"] = value

    @property
    def gap_3_directional_front_absoptance_matrix_name(self):
        """field `Gap 3 Directional Front Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `Gap 3 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_3_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Gap 3 Directional Front Absoptance Matrix Name"]

    @gap_3_directional_front_absoptance_matrix_name.setter
    def gap_3_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Gap 3 Directional Front Absoptance Matrix
        Name`"""
        self["Gap 3 Directional Front Absoptance Matrix Name"] = value

    @property
    def gap_3_directional_back_absoptance_matrix_name(self):
        """field `Gap 3 Directional Back Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `Gap 3 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_3_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Gap 3 Directional Back Absoptance Matrix Name"]

    @gap_3_directional_back_absoptance_matrix_name.setter
    def gap_3_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Gap 3 Directional Back Absoptance Matrix
        Name`"""
        self["Gap 3 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_4_name(self):
        """field `Layer 4 Name`

        Args:
            value (str): value for IDD Field `Layer 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4_name` or None if not set

        """
        return self["Layer 4 Name"]

    @layer_4_name.setter
    def layer_4_name(self, value=None):
        """Corresponds to IDD field `Layer 4 Name`"""
        self["Layer 4 Name"] = value

    @property
    def layer_4_directional_front_absoptance_matrix_name(self):
        """field `Layer 4 Directional Front Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 4 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Layer 4 Directional Front Absoptance Matrix Name"]

    @layer_4_directional_front_absoptance_matrix_name.setter
    def layer_4_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 4 Directional Front Absoptance
        Matrix Name`"""
        self["Layer 4 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_4_directional_back_absoptance_matrix_name(self):
        """field `Layer 4 Directional Back Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 4 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Layer 4 Directional Back Absoptance Matrix Name"]

    @layer_4_directional_back_absoptance_matrix_name.setter
    def layer_4_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 4 Directional Back Absoptance Matrix
        Name`"""
        self["Layer 4 Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_4_name(self):
        """field `Gap 4 Name`

        Args:
            value (str): value for IDD Field `Gap 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_4_name` or None if not set

        """
        return self["Gap 4 Name"]

    @gap_4_name.setter
    def gap_4_name(self, value=None):
        """Corresponds to IDD field `Gap 4 Name`"""
        self["Gap 4 Name"] = value

    @property
    def gap_4_directional_front_absoptance_matrix_name(self):
        """field `Gap 4 Directional Front Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `Gap 4 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_4_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Gap 4 Directional Front Absoptance Matrix Name"]

    @gap_4_directional_front_absoptance_matrix_name.setter
    def gap_4_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Gap 4 Directional Front Absoptance Matrix
        Name`"""
        self["Gap 4 Directional Front Absoptance Matrix Name"] = value

    @property
    def gap_4_directional_back_absoptance_matrix_name(self):
        """field `Gap 4 Directional Back Absoptance Matrix Name`

        |  Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `Gap 4 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gap_4_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Gap 4 Directional Back Absoptance Matrix Name"]

    @gap_4_directional_back_absoptance_matrix_name.setter
    def gap_4_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Gap 4 Directional Back Absoptance Matrix
        Name`"""
        self["Gap 4 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_5_name(self):
        """field `Layer 5 Name`

        Args:
            value (str): value for IDD Field `Layer 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5_name` or None if not set

        """
        return self["Layer 5 Name"]

    @layer_5_name.setter
    def layer_5_name(self, value=None):
        """Corresponds to IDD field `Layer 5 Name`"""
        self["Layer 5 Name"] = value

    @property
    def layer_5_directional_front_absoptance_matrix_name(self):
        """field `Layer 5 Directional Front Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 5 Directional Front Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5_directional_front_absoptance_matrix_name` or None if not set

        """
        return self["Layer 5 Directional Front Absoptance Matrix Name"]

    @layer_5_directional_front_absoptance_matrix_name.setter
    def layer_5_directional_front_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 5 Directional Front Absoptance
        Matrix Name`"""
        self["Layer 5 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_5_directional_back_absoptance_matrix_name(self):
        """field `Layer 5 Directional Back Absoptance Matrix Name`

        Args:
            value (str): value for IDD Field `Layer 5 Directional Back Absoptance Matrix Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5_directional_back_absoptance_matrix_name` or None if not set

        """
        return self["Layer 5 Directional Back Absoptance Matrix Name"]

    @layer_5_directional_back_absoptance_matrix_name.setter
    def layer_5_directional_back_absoptance_matrix_name(self, value=None):
        """Corresponds to IDD field `Layer 5 Directional Back Absoptance Matrix
        Name`"""
        self["Layer 5 Directional Back Absoptance Matrix Name"] = value




class ConstructionWindowEquivalentLayer(DataObject):

    """ Corresponds to IDD object `Construction:WindowEquivalentLayer`
        Start with outside layer and work your way to the inside Layer
        Up to 11 layers total. Up to six solid layers and up to five gaps.
        Enter the material name for each layer
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'outside layer',
                                       {'name': u'Outside Layer',
                                        'pyname': u'outside_layer',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 2',
                                       {'name': u'Layer 2',
                                        'pyname': u'layer_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 3',
                                       {'name': u'Layer 3',
                                        'pyname': u'layer_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 4',
                                       {'name': u'Layer 4',
                                        'pyname': u'layer_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 5',
                                       {'name': u'Layer 5',
                                        'pyname': u'layer_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 6',
                                       {'name': u'Layer 6',
                                        'pyname': u'layer_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 7',
                                       {'name': u'Layer 7',
                                        'pyname': u'layer_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 8',
                                       {'name': u'Layer 8',
                                        'pyname': u'layer_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 9',
                                       {'name': u'Layer 9',
                                        'pyname': u'layer_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 10',
                                       {'name': u'Layer 10',
                                        'pyname': u'layer_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'layer 11',
                                       {'name': u'Layer 11',
                                        'pyname': u'layer_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 2,
               'name': u'Construction:WindowEquivalentLayer',
               'pyname': u'ConstructionWindowEquivalentLayer',
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
    def outside_layer(self):
        """field `Outside Layer`

        Args:
            value (str): value for IDD Field `Outside Layer`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_layer` or None if not set

        """
        return self["Outside Layer"]

    @outside_layer.setter
    def outside_layer(self, value=None):
        """Corresponds to IDD field `Outside Layer`"""
        self["Outside Layer"] = value

    @property
    def layer_2(self):
        """field `Layer 2`

        Args:
            value (str): value for IDD Field `Layer 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_2` or None if not set

        """
        return self["Layer 2"]

    @layer_2.setter
    def layer_2(self, value=None):
        """Corresponds to IDD field `Layer 2`"""
        self["Layer 2"] = value

    @property
    def layer_3(self):
        """field `Layer 3`

        Args:
            value (str): value for IDD Field `Layer 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_3` or None if not set

        """
        return self["Layer 3"]

    @layer_3.setter
    def layer_3(self, value=None):
        """Corresponds to IDD field `Layer 3`"""
        self["Layer 3"] = value

    @property
    def layer_4(self):
        """field `Layer 4`

        Args:
            value (str): value for IDD Field `Layer 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_4` or None if not set

        """
        return self["Layer 4"]

    @layer_4.setter
    def layer_4(self, value=None):
        """Corresponds to IDD field `Layer 4`"""
        self["Layer 4"] = value

    @property
    def layer_5(self):
        """field `Layer 5`

        Args:
            value (str): value for IDD Field `Layer 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_5` or None if not set

        """
        return self["Layer 5"]

    @layer_5.setter
    def layer_5(self, value=None):
        """Corresponds to IDD field `Layer 5`"""
        self["Layer 5"] = value

    @property
    def layer_6(self):
        """field `Layer 6`

        Args:
            value (str): value for IDD Field `Layer 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_6` or None if not set

        """
        return self["Layer 6"]

    @layer_6.setter
    def layer_6(self, value=None):
        """Corresponds to IDD field `Layer 6`"""
        self["Layer 6"] = value

    @property
    def layer_7(self):
        """field `Layer 7`

        Args:
            value (str): value for IDD Field `Layer 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_7` or None if not set

        """
        return self["Layer 7"]

    @layer_7.setter
    def layer_7(self, value=None):
        """Corresponds to IDD field `Layer 7`"""
        self["Layer 7"] = value

    @property
    def layer_8(self):
        """field `Layer 8`

        Args:
            value (str): value for IDD Field `Layer 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_8` or None if not set

        """
        return self["Layer 8"]

    @layer_8.setter
    def layer_8(self, value=None):
        """Corresponds to IDD field `Layer 8`"""
        self["Layer 8"] = value

    @property
    def layer_9(self):
        """field `Layer 9`

        Args:
            value (str): value for IDD Field `Layer 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_9` or None if not set

        """
        return self["Layer 9"]

    @layer_9.setter
    def layer_9(self, value=None):
        """Corresponds to IDD field `Layer 9`"""
        self["Layer 9"] = value

    @property
    def layer_10(self):
        """field `Layer 10`

        Args:
            value (str): value for IDD Field `Layer 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_10` or None if not set

        """
        return self["Layer 10"]

    @layer_10.setter
    def layer_10(self, value=None):
        """Corresponds to IDD field `Layer 10`"""
        self["Layer 10"] = value

    @property
    def layer_11(self):
        """field `Layer 11`

        Args:
            value (str): value for IDD Field `Layer 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `layer_11` or None if not set

        """
        return self["Layer 11"]

    @layer_11.setter
    def layer_11(self, value=None):
        """Corresponds to IDD field `Layer 11`"""
        self["Layer 11"] = value




class ConstructionWindowDataFile(DataObject):

    """ Corresponds to IDD object `Construction:WindowDataFile`
        Initiates search of the Window data file for a window called Name.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'file name',
                                       {'name': u'File Name',
                                        'pyname': u'file_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'Construction:WindowDataFile',
               'pyname': u'ConstructionWindowDataFile',
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
    def file_name(self):
        """field `File Name`

        |  default file name is "Window5DataFile.dat"
        |  limit on this field is 100 characters.

        Args:
            value (str): value for IDD Field `File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `file_name` or None if not set

        """
        return self["File Name"]

    @file_name.setter
    def file_name(self, value=None):
        """Corresponds to IDD field `File Name`"""
        self["File Name"] = value




class MaterialPropertyGlazingSpectralData(DataObject):

    """ Corresponds to IDD object `MaterialProperty:GlazingSpectralData`
        Name is followed by up to 800 sets of normal-incidence measured values of
        [wavelength, transmittance, front reflectance, back reflectance] for wavelengths
        covering the solar spectrum (from about 0.25 to 2.5 microns)
    """
    _schema = {'extensible-fields': OrderedDict([(u'wavelength',
                                                  {'name': u'Wavelength',
                                                   'pyname': u'wavelength',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'micron'}),
                                                 (u'transmittance',
                                                  {'name': u'Transmittance',
                                                   'pyname': u'transmittance',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'real'}),
                                                 (u'front reflectance',
                                                  {'name': u'Front Reflectance',
                                                   'pyname': u'front_reflectance',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'real'}),
                                                 (u'back reflectance',
                                                  {'name': u'Back Reflectance',
                                                   'pyname': u'back_reflectance',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'real'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'spectral',
               'group': u'Surface Construction Elements',
               'min-fields': 0,
               'name': u'MaterialProperty:GlazingSpectralData',
               'pyname': u'MaterialPropertyGlazingSpectralData',
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

    def add_extensible(self,
                       wavelength=None,
                       transmittance=None,
                       front_reflectance=None,
                       back_reflectance=None,
                       ):
        """Add values for extensible fields.

        Args:

            wavelength (float): value for IDD Field `Wavelength`
                Units: micron
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            transmittance (float): value for IDD Field `Transmittance`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            front_reflectance (float): value for IDD Field `Front Reflectance`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            back_reflectance (float): value for IDD Field `Back Reflectance`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        wavelength = self.check_value("Wavelength", wavelength)
        vals.append(wavelength)
        transmittance = self.check_value("Transmittance", transmittance)
        vals.append(transmittance)
        front_reflectance = self.check_value(
            "Front Reflectance",
            front_reflectance)
        vals.append(front_reflectance)
        back_reflectance = self.check_value(
            "Back Reflectance",
            back_reflectance)
        vals.append(back_reflectance)
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


