""" Data objects in group "Detailed Ground Heat Transfer"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class GroundHeatTransferControl(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Control`
        Object determines if the Slab and Basement preprocessors
        are going to be executed.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'run basement preprocessor',
                                       {'name': u'Run Basement Preprocessor',
                                        'pyname': u'run_basement_preprocessor',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'run slab preprocessor',
                                       {'name': u'Run Slab Preprocessor',
                                        'pyname': u'run_slab_preprocessor',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Control',
               'pyname': u'GroundHeatTransferControl',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This field is included for consistency.11

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
    def run_basement_preprocessor(self):
        """field `Run Basement Preprocessor`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Run Basement Preprocessor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `run_basement_preprocessor` or None if not set

        """
        return self["Run Basement Preprocessor"]

    @run_basement_preprocessor.setter
    def run_basement_preprocessor(self, value="No"):
        """Corresponds to IDD field `Run Basement Preprocessor`"""
        self["Run Basement Preprocessor"] = value

    @property
    def run_slab_preprocessor(self):
        """field `Run Slab Preprocessor`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Run Slab Preprocessor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `run_slab_preprocessor` or None if not set

        """
        return self["Run Slab Preprocessor"]

    @run_slab_preprocessor.setter
    def run_slab_preprocessor(self, value="No"):
        """Corresponds to IDD field `Run Slab Preprocessor`"""
        self["Run Slab Preprocessor"] = value




class GroundHeatTransferSlabMaterials(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:Materials`
        Object gives an overall description of the slab ground heat transfer model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'nmat: number of materials',
                                       {'name': u'NMAT: Number of materials',
                                        'pyname': u'nmat_number_of_materials',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'albedo: surface albedo: no snow',
                                       {'name': u'ALBEDO: Surface Albedo: No Snow',
                                        'pyname': u'albedo_surface_albedo_no_snow',
                                        'default': 0.16,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'albedo: surface albedo: snow',
                                       {'name': u'ALBEDO: Surface Albedo: Snow',
                                        'pyname': u'albedo_surface_albedo_snow',
                                        'default': 0.4,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'epslw: surface emissivity: no snow',
                                       {'name': u'EPSLW: Surface Emissivity: No Snow',
                                        'pyname': u'epslw_surface_emissivity_no_snow',
                                        'default': 0.94,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'epslw: surface emissivity: snow',
                                       {'name': u'EPSLW: Surface Emissivity: Snow',
                                        'pyname': u'epslw_surface_emissivity_snow',
                                        'default': 0.86,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'z0: surface roughness: no snow',
                                       {'name': u'Z0: Surface Roughness: No Snow',
                                        'pyname': u'z0_surface_roughness_no_snow',
                                        'default': 0.75,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'cm'}),
                                      (u'z0: surface roughness: snow',
                                       {'name': u'Z0: Surface Roughness: Snow',
                                        'pyname': u'z0_surface_roughness_snow',
                                        'default': 0.25,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'cm'}),
                                      (u'hin: indoor hconv: downward flow',
                                       {'name': u'HIN: Indoor HConv: Downward Flow',
                                        'pyname': u'hin_indoor_hconv_downward_flow',
                                        'default': 6.13,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'hin: indoor hconv: upward',
                                       {'name': u'HIN: Indoor HConv: Upward',
                                        'pyname': u'hin_indoor_hconv_upward',
                                        'default': 9.26,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:Materials',
               'pyname': u'GroundHeatTransferSlabMaterials',
               'required-object': False,
               'unique-object': False}

    @property
    def nmat_number_of_materials(self):
        """field `NMAT: Number of materials`

        |  This field specifies the number of different materials that will be used in the model.
        |  Typically only a ground material and a slab material are used. (2 materials)

        Args:
            value (float): value for IDD Field `NMAT: Number of materials`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nmat_number_of_materials` or None if not set
        """
        return self["NMAT: Number of materials"]

    @nmat_number_of_materials.setter
    def nmat_number_of_materials(self, value=None):
        """  Corresponds to IDD field `NMAT: Number of materials`

        """
        self["NMAT: Number of materials"] = value

    @property
    def albedo_surface_albedo_no_snow(self):
        """field `ALBEDO: Surface Albedo: No Snow`

        |  Two fields specify the albedo value of the surface: first for no snow coverage days;
        |  second for days with snow coverage. The albedo is the solar reflectivity of the surface,
        |  and can vary from 0.05 for blacktop to 0.95 for fresh snow.
        |  Typical values for North America reported by Bahnfleth range from 0.16 to 0.4.
        |  Default value: 0.16
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `ALBEDO: Surface Albedo: No Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `albedo_surface_albedo_no_snow` or None if not set
        """
        return self["ALBEDO: Surface Albedo: No Snow"]

    @albedo_surface_albedo_no_snow.setter
    def albedo_surface_albedo_no_snow(self, value=0.16):
        """  Corresponds to IDD field `ALBEDO: Surface Albedo: No Snow`

        """
        self["ALBEDO: Surface Albedo: No Snow"] = value

    @property
    def albedo_surface_albedo_snow(self):
        """field `ALBEDO: Surface Albedo: Snow`

        |  Default value: 0.4
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `ALBEDO: Surface Albedo: Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `albedo_surface_albedo_snow` or None if not set
        """
        return self["ALBEDO: Surface Albedo: Snow"]

    @albedo_surface_albedo_snow.setter
    def albedo_surface_albedo_snow(self, value=0.4):
        """  Corresponds to IDD field `ALBEDO: Surface Albedo: Snow`

        """
        self["ALBEDO: Surface Albedo: Snow"] = value

    @property
    def epslw_surface_emissivity_no_snow(self):
        """field `EPSLW: Surface Emissivity: No Snow`

        |  EPSLW (No Snow and Snow) specifies the long wavelength (thermal) emissivity of the ground surface.
        |  primarily important for nighttime radiation to sky.
        |  typical value .95
        |  Default value: 0.94

        Args:
            value (float): value for IDD Field `EPSLW: Surface Emissivity: No Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `epslw_surface_emissivity_no_snow` or None if not set
        """
        return self["EPSLW: Surface Emissivity: No Snow"]

    @epslw_surface_emissivity_no_snow.setter
    def epslw_surface_emissivity_no_snow(self, value=0.94):
        """  Corresponds to IDD field `EPSLW: Surface Emissivity: No Snow`

        """
        self["EPSLW: Surface Emissivity: No Snow"] = value

    @property
    def epslw_surface_emissivity_snow(self):
        """field `EPSLW: Surface Emissivity: Snow`

        |  Default value: 0.86

        Args:
            value (float): value for IDD Field `EPSLW: Surface Emissivity: Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `epslw_surface_emissivity_snow` or None if not set
        """
        return self["EPSLW: Surface Emissivity: Snow"]

    @epslw_surface_emissivity_snow.setter
    def epslw_surface_emissivity_snow(self, value=0.86):
        """  Corresponds to IDD field `EPSLW: Surface Emissivity: Snow`

        """
        self["EPSLW: Surface Emissivity: Snow"] = value

    @property
    def z0_surface_roughness_no_snow(self):
        """field `Z0: Surface Roughness: No Snow`

        |  fields Z0 (No Snow and Snow) describe the height at which an experimentally velocity profile goes to zero.
        |  typical value= .75 cm
        |  Units: cm
        |  Default value: 0.75

        Args:
            value (float): value for IDD Field `Z0: Surface Roughness: No Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `z0_surface_roughness_no_snow` or None if not set
        """
        return self["Z0: Surface Roughness: No Snow"]

    @z0_surface_roughness_no_snow.setter
    def z0_surface_roughness_no_snow(self, value=0.75):
        """  Corresponds to IDD field `Z0: Surface Roughness: No Snow`

        """
        self["Z0: Surface Roughness: No Snow"] = value

    @property
    def z0_surface_roughness_snow(self):
        """field `Z0: Surface Roughness: Snow`

        |  typical value= .05 cm
        |  Units: cm
        |  Default value: 0.25

        Args:
            value (float): value for IDD Field `Z0: Surface Roughness: Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `z0_surface_roughness_snow` or None if not set
        """
        return self["Z0: Surface Roughness: Snow"]

    @z0_surface_roughness_snow.setter
    def z0_surface_roughness_snow(self, value=0.25):
        """  Corresponds to IDD field `Z0: Surface Roughness: Snow`

        """
        self["Z0: Surface Roughness: Snow"] = value

    @property
    def hin_indoor_hconv_downward_flow(self):
        """field `HIN: Indoor HConv: Downward Flow`

        |  These fields specify the combined convective and radiative heat transfer coefficient between
        |  the slab top inside surface and the room air for the cases where heat is flowing downward,
        |  and upward. The program toggles between the two if the direction of the heat flux changes.
        |  Typical values can be found in the ASHRAE Handbook of Fundamentals, but should be
        |  about 6 W/(m2-K) for downward heat flow and 9 W/(m2-K) for upward heat flow.
        |  typical value= 4-10
        |  Units: W/m2-K
        |  Default value: 6.13

        Args:
            value (float): value for IDD Field `HIN: Indoor HConv: Downward Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_indoor_hconv_downward_flow` or None if not set
        """
        return self["HIN: Indoor HConv: Downward Flow"]

    @hin_indoor_hconv_downward_flow.setter
    def hin_indoor_hconv_downward_flow(self, value=6.13):
        """  Corresponds to IDD field `HIN: Indoor HConv: Downward Flow`

        """
        self["HIN: Indoor HConv: Downward Flow"] = value

    @property
    def hin_indoor_hconv_upward(self):
        """field `HIN: Indoor HConv: Upward`

        |  typical value= 4-10
        |  Units: W/m2-K
        |  Default value: 9.26

        Args:
            value (float): value for IDD Field `HIN: Indoor HConv: Upward`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_indoor_hconv_upward` or None if not set
        """
        return self["HIN: Indoor HConv: Upward"]

    @hin_indoor_hconv_upward.setter
    def hin_indoor_hconv_upward(self, value=9.26):
        """  Corresponds to IDD field `HIN: Indoor HConv: Upward`

        """
        self["HIN: Indoor HConv: Upward"] = value




class GroundHeatTransferSlabMatlProps(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:MatlProps`
        This object contains the material properties for the materials
        used in the model. The fields are mostly self explanatory.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'rho: slab material density',
                                       {'name': u'RHO: Slab Material density',
                                        'pyname': u'rho_slab_material_density',
                                        'default': 2300.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'rho: soil density',
                                       {'name': u'RHO: Soil Density',
                                        'pyname': u'rho_soil_density',
                                        'default': 1200.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'cp: slab cp',
                                       {'name': u'CP: Slab CP',
                                        'pyname': u'cp_slab_cp',
                                        'default': 650.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'cp: soil cp',
                                       {'name': u'CP: Soil CP',
                                        'pyname': u'cp_soil_cp',
                                        'default': 1200.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'tcon: slab k',
                                       {'name': u'TCON: Slab k',
                                        'pyname': u'tcon_slab_k',
                                        'default': 0.9,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'tcon: soil k',
                                       {'name': u'TCON: Soil k',
                                        'pyname': u'tcon_soil_k',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:MatlProps',
               'pyname': u'GroundHeatTransferSlabMatlProps',
               'required-object': False,
               'unique-object': False}

    @property
    def rho_slab_material_density(self):
        """field `RHO: Slab Material density`

        |  Density of Slab Material
        |  typical value= 2300.0
        |  Units: kg/m3
        |  Default value: 2300.0

        Args:
            value (float): value for IDD Field `RHO: Slab Material density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rho_slab_material_density` or None if not set
        """
        return self["RHO: Slab Material density"]

    @rho_slab_material_density.setter
    def rho_slab_material_density(self, value=2300.0):
        """  Corresponds to IDD field `RHO: Slab Material density`

        """
        self["RHO: Slab Material density"] = value

    @property
    def rho_soil_density(self):
        """field `RHO: Soil Density`

        |  Density of Soil Material
        |  typical value= 1200.0
        |  Units: kg/m3
        |  Default value: 1200.0

        Args:
            value (float): value for IDD Field `RHO: Soil Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rho_soil_density` or None if not set
        """
        return self["RHO: Soil Density"]

    @rho_soil_density.setter
    def rho_soil_density(self, value=1200.0):
        """  Corresponds to IDD field `RHO: Soil Density`

        """
        self["RHO: Soil Density"] = value

    @property
    def cp_slab_cp(self):
        """field `CP: Slab CP`

        |  Specific Heat of Slab Material
        |  typical value=650.0
        |  Units: J/kg-K
        |  Default value: 650.0

        Args:
            value (float): value for IDD Field `CP: Slab CP`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cp_slab_cp` or None if not set
        """
        return self["CP: Slab CP"]

    @cp_slab_cp.setter
    def cp_slab_cp(self, value=650.0):
        """  Corresponds to IDD field `CP: Slab CP`

        """
        self["CP: Slab CP"] = value

    @property
    def cp_soil_cp(self):
        """field `CP: Soil CP`

        |  Specific Heat of Soil Material
        |  typical value= 1200.0
        |  Units: J/kg-K
        |  Default value: 1200.0

        Args:
            value (float): value for IDD Field `CP: Soil CP`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cp_soil_cp` or None if not set
        """
        return self["CP: Soil CP"]

    @cp_soil_cp.setter
    def cp_soil_cp(self, value=1200.0):
        """  Corresponds to IDD field `CP: Soil CP`

        """
        self["CP: Soil CP"] = value

    @property
    def tcon_slab_k(self):
        """field `TCON: Slab k`

        |  Conductivity of Slab Material
        |  typical value= .9
        |  Units: W/m-K
        |  Default value: 0.9

        Args:
            value (float): value for IDD Field `TCON: Slab k`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tcon_slab_k` or None if not set
        """
        return self["TCON: Slab k"]

    @tcon_slab_k.setter
    def tcon_slab_k(self, value=0.9):
        """  Corresponds to IDD field `TCON: Slab k`

        """
        self["TCON: Slab k"] = value

    @property
    def tcon_soil_k(self):
        """field `TCON: Soil k`

        |  Conductivity of Soil Material
        |  typical value= 1.0
        |  Units: W/m-K
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `TCON: Soil k`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tcon_soil_k` or None if not set
        """
        return self["TCON: Soil k"]

    @tcon_soil_k.setter
    def tcon_soil_k(self, value=1.0):
        """  Corresponds to IDD field `TCON: Soil k`

        """
        self["TCON: Soil k"] = value




class GroundHeatTransferSlabBoundConds(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:BoundConds`
        Supplies some of the boundary conditions used in the ground heat transfer calculations.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'evtr: is surface evapotranspiration modeled',
                                       {'name': u'EVTR: Is surface evapotranspiration modeled',
                                        'pyname': u'evtr_is_surface_evapotranspiration_modeled',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fixbc: is the lower boundary at a fixed temperature',
                                       {'name': u'FIXBC: is the lower boundary at a fixed temperature',
                                        'pyname': u'fixbc_is_the_lower_boundary_at_a_fixed_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'tdeepin',
                                       {'name': u'TDEEPin',
                                        'pyname': u'tdeepin',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'usrhflag: is the ground surface h specified by the user?',
                                       {'name': u'USRHflag: Is the ground surface h specified by the user?',
                                        'pyname': u'usrhflag_is_the_ground_surface_h_specified_by_the_user',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'userh: user specified ground surface heat transfer coefficient',
                                       {'name': u'USERH: User specified ground surface heat transfer coefficient',
                                        'pyname': u'userh_user_specified_ground_surface_heat_transfer_coefficient',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:BoundConds',
               'pyname': u'GroundHeatTransferSlabBoundConds',
               'required-object': False,
               'unique-object': False}

    @property
    def evtr_is_surface_evapotranspiration_modeled(self):
        """field `EVTR: Is surface evapotranspiration modeled`

        |  This field specifies whether or not to use the evapotransporation model.
        |  The inclusion of evapotransporation in the calculation has the greatest
        |  effect in warm dry climates, primarily on the ground surface temperature.
        |  This field can be used to turn the evapotransporation off and on to check
        |  sensitivity to it.

        Args:
            value (str): value for IDD Field `EVTR: Is surface evapotranspiration modeled`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `evtr_is_surface_evapotranspiration_modeled` or None if not set
        """
        return self["EVTR: Is surface evapotranspiration modeled"]

    @evtr_is_surface_evapotranspiration_modeled.setter
    def evtr_is_surface_evapotranspiration_modeled(self, value=None):
        """  Corresponds to IDD field `EVTR: Is surface evapotranspiration modeled`

        """
        self["EVTR: Is surface evapotranspiration modeled"] = value

    @property
    def fixbc_is_the_lower_boundary_at_a_fixed_temperature(self):
        """field `FIXBC: is the lower boundary at a fixed temperature`

        |  This field permits using a fixed temperature at the lower surface of the model
        |  instead of a zero heat flux condition. This change normally has a very small
        |  effect on the results.
        |  FALSE selects the zero flux lower boundary condition

        Args:
            value (str): value for IDD Field `FIXBC: is the lower boundary at a fixed temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fixbc_is_the_lower_boundary_at_a_fixed_temperature` or None if not set
        """
        return self["FIXBC: is the lower boundary at a fixed temperature"]

    @fixbc_is_the_lower_boundary_at_a_fixed_temperature.setter
    def fixbc_is_the_lower_boundary_at_a_fixed_temperature(self, value=None):
        """  Corresponds to IDD field `FIXBC: is the lower boundary at a fixed temperature`

        """
        self["FIXBC: is the lower boundary at a fixed temperature"] = value

    @property
    def tdeepin(self):
        """field `TDEEPin`

        |  User input lower boundary temperature if FIXBC is TRUE
        |  Blank for FIXBC FALSE or to use the calculated 1-D deep ground temperature.
        |  Units: C

        Args:
            value (float): value for IDD Field `TDEEPin`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tdeepin` or None if not set

        """
        return self["TDEEPin"]

    @tdeepin.setter
    def tdeepin(self, value=None):
        """Corresponds to IDD field `TDEEPin`"""
        self["TDEEPin"] = value

    @property
    def usrhflag_is_the_ground_surface_h_specified_by_the_user(self):
        """field `USRHflag: Is the ground surface h specified by the user?`

        |  This field flags the use of a user specified heat transfer coefficient
        |  on the ground surface. This condition is used primarily for testing.
        |  For normal runs (USPHflag is FALSE) and the program calculates the heat
        |  transfer coefficient using the weather conditions.

        Args:
            value (str): value for IDD Field `USRHflag: Is the ground surface h specified by the user?`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `usrhflag_is_the_ground_surface_h_specified_by_the_user` or None if not set
        """
        return self["USRHflag: Is the ground surface h specified by the user?"]

    @usrhflag_is_the_ground_surface_h_specified_by_the_user.setter
    def usrhflag_is_the_ground_surface_h_specified_by_the_user(
            self,
            value=None):
        """  Corresponds to IDD field `USRHflag: Is the ground surface h specified by the user?`

        """
        self[
            "USRHflag: Is the ground surface h specified by the user?"] = value

    @property
    def userh_user_specified_ground_surface_heat_transfer_coefficient(self):
        """field `USERH: User specified ground surface heat transfer coefficient`

        |  Used only if USRHflag is TRUE and the heat transfer coefficient value is
        |  specified in this field.
        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `USERH: User specified ground surface heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `userh_user_specified_ground_surface_heat_transfer_coefficient` or None if not set
        """
        return self[
            "USERH: User specified ground surface heat transfer coefficient"]

    @userh_user_specified_ground_surface_heat_transfer_coefficient.setter
    def userh_user_specified_ground_surface_heat_transfer_coefficient(
            self,
            value=None):
        """  Corresponds to IDD field `USERH: User specified ground surface heat transfer coefficient`

        """
        self[
            "USERH: User specified ground surface heat transfer coefficient"] = value




class GroundHeatTransferSlabBldgProps(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:BldgProps`
        Object provides information about the building and its operating conditions
        Monthly Average Temperature SetPoint fields
        specify the average indoor building set point temperatures for each
        month of the year. These fields are useful for simulating a building
        that is not temperature controlled for some of the year.
        In such a case, the average indoor set point temperatures
        can be obtained by first running the model in EnergyPlus with an
        insulated floor boundary condition, and then using the resulting
        monthly average zone temperatures in these fields.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'iyrs: number of years to iterate',
                                       {'name': u'IYRS: Number of years to iterate',
                                        'pyname': u'iyrs_number_of_years_to_iterate',
                                        'default': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'shape: slab shape',
                                       {'name': u'Shape: Slab shape',
                                        'pyname': u'shape_slab_shape',
                                        'maximum': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'hbldg: building height',
                                       {'name': u'HBLDG: Building height',
                                        'pyname': u'hbldg_building_height',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'tin1: january indoor average temperature setpoint',
                                       {'name': u'TIN1: January Indoor Average Temperature Setpoint',
                                        'pyname': u'tin1_january_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin2: february indoor average temperature setpoint',
                                       {'name': u'TIN2: February Indoor Average Temperature Setpoint',
                                        'pyname': u'tin2_february_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin3: march indoor average temperature setpoint',
                                       {'name': u'TIN3: March Indoor Average Temperature Setpoint',
                                        'pyname': u'tin3_march_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin4: april indoor average temperature setpoint',
                                       {'name': u'TIN4: April Indoor Average Temperature Setpoint',
                                        'pyname': u'tin4_april_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin5: may indoor average temperature setpoint',
                                       {'name': u'TIN5: May Indoor Average Temperature Setpoint',
                                        'pyname': u'tin5_may_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin6: june indoor average temperature setpoint',
                                       {'name': u'TIN6: June Indoor Average Temperature Setpoint',
                                        'pyname': u'tin6_june_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin7: july indoor average temperature setpoint',
                                       {'name': u'TIN7: July Indoor Average Temperature Setpoint',
                                        'pyname': u'tin7_july_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin8: august indoor average temperature setpoint',
                                       {'name': u'TIN8: August Indoor Average Temperature Setpoint',
                                        'pyname': u'tin8_august_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin9: september indoor average temperature setpoint',
                                       {'name': u'TIN9: September Indoor Average Temperature Setpoint',
                                        'pyname': u'tin9_september_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin10: october indoor average temperature setpoint',
                                       {'name': u'TIN10: October Indoor Average Temperature Setpoint',
                                        'pyname': u'tin10_october_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin11: november indoor average temperature setpoint',
                                       {'name': u'TIN11: November Indoor Average Temperature Setpoint',
                                        'pyname': u'tin11_november_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tin12: december indoor average temperature setpoint',
                                       {'name': u'TIN12: December Indoor Average Temperature Setpoint',
                                        'pyname': u'tin12_december_indoor_average_temperature_setpoint',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'tinamp: daily indoor sine wave variation amplitude',
                                       {'name': u'TINAmp: Daily Indoor sine wave variation amplitude',
                                        'pyname': u'tinamp_daily_indoor_sine_wave_variation_amplitude',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'convtol: convergence tolerance',
                                       {'name': u'ConvTol: Convergence Tolerance',
                                        'pyname': u'convtol_convergence_tolerance',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:BldgProps',
               'pyname': u'GroundHeatTransferSlabBldgProps',
               'required-object': False,
               'unique-object': False}

    @property
    def iyrs_number_of_years_to_iterate(self):
        """field `IYRS: Number of years to iterate`

        |  This field specifies the number of years to iterate.
        |  Either the ground heat transfer calculations come to an
        |  an annual steady periodic condition by converging to a tolerance
        |  (see ConvTol field) or it runs for this number of years.
        |  A ten year maximum is usually sufficient.
        |  Default value: 10.0
        |  value >= 1.0

        Args:
            value (float): value for IDD Field `IYRS: Number of years to iterate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `iyrs_number_of_years_to_iterate` or None if not set
        """
        return self["IYRS: Number of years to iterate"]

    @iyrs_number_of_years_to_iterate.setter
    def iyrs_number_of_years_to_iterate(self, value=10.0):
        """  Corresponds to IDD field `IYRS: Number of years to iterate`

        """
        self["IYRS: Number of years to iterate"] = value

    @property
    def shape_slab_shape(self):
        """field `Shape: Slab shape`

        |  Use only the value 0 here. Only a rectangular shape is implemented.

        Args:
            value (float): value for IDD Field `Shape: Slab shape`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shape_slab_shape` or None if not set
        """
        return self["Shape: Slab shape"]

    @shape_slab_shape.setter
    def shape_slab_shape(self, value=None):
        """  Corresponds to IDD field `Shape: Slab shape`

        """
        self["Shape: Slab shape"] = value

    @property
    def hbldg_building_height(self):
        """field `HBLDG: Building height`

        |  This field supplies the building height. This is used to calculate
        |  the building shadowing on the ground.
        |  typical value= 0-20
        |  Units: m

        Args:
            value (float): value for IDD Field `HBLDG: Building height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hbldg_building_height` or None if not set
        """
        return self["HBLDG: Building height"]

    @hbldg_building_height.setter
    def hbldg_building_height(self, value=None):
        """  Corresponds to IDD field `HBLDG: Building height`

        """
        self["HBLDG: Building height"] = value

    @property
    def tin1_january_indoor_average_temperature_setpoint(self):
        """field `TIN1: January Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN1: January Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin1_january_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN1: January Indoor Average Temperature Setpoint"]

    @tin1_january_indoor_average_temperature_setpoint.setter
    def tin1_january_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN1: January Indoor Average Temperature Setpoint`

        """
        self["TIN1: January Indoor Average Temperature Setpoint"] = value

    @property
    def tin2_february_indoor_average_temperature_setpoint(self):
        """field `TIN2: February Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN2: February Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin2_february_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN2: February Indoor Average Temperature Setpoint"]

    @tin2_february_indoor_average_temperature_setpoint.setter
    def tin2_february_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN2: February Indoor Average Temperature Setpoint`

        """
        self["TIN2: February Indoor Average Temperature Setpoint"] = value

    @property
    def tin3_march_indoor_average_temperature_setpoint(self):
        """field `TIN3: March Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN3: March Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin3_march_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN3: March Indoor Average Temperature Setpoint"]

    @tin3_march_indoor_average_temperature_setpoint.setter
    def tin3_march_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN3: March Indoor Average Temperature Setpoint`

        """
        self["TIN3: March Indoor Average Temperature Setpoint"] = value

    @property
    def tin4_april_indoor_average_temperature_setpoint(self):
        """field `TIN4: April Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN4: April Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin4_april_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN4: April Indoor Average Temperature Setpoint"]

    @tin4_april_indoor_average_temperature_setpoint.setter
    def tin4_april_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN4: April Indoor Average Temperature Setpoint`

        """
        self["TIN4: April Indoor Average Temperature Setpoint"] = value

    @property
    def tin5_may_indoor_average_temperature_setpoint(self):
        """field `TIN5: May Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN5: May Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin5_may_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN5: May Indoor Average Temperature Setpoint"]

    @tin5_may_indoor_average_temperature_setpoint.setter
    def tin5_may_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN5: May Indoor Average Temperature Setpoint`

        """
        self["TIN5: May Indoor Average Temperature Setpoint"] = value

    @property
    def tin6_june_indoor_average_temperature_setpoint(self):
        """field `TIN6: June Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN6: June Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin6_june_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN6: June Indoor Average Temperature Setpoint"]

    @tin6_june_indoor_average_temperature_setpoint.setter
    def tin6_june_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN6: June Indoor Average Temperature Setpoint`

        """
        self["TIN6: June Indoor Average Temperature Setpoint"] = value

    @property
    def tin7_july_indoor_average_temperature_setpoint(self):
        """field `TIN7: July Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN7: July Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin7_july_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN7: July Indoor Average Temperature Setpoint"]

    @tin7_july_indoor_average_temperature_setpoint.setter
    def tin7_july_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN7: July Indoor Average Temperature Setpoint`

        """
        self["TIN7: July Indoor Average Temperature Setpoint"] = value

    @property
    def tin8_august_indoor_average_temperature_setpoint(self):
        """field `TIN8: August Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN8: August Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin8_august_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN8: August Indoor Average Temperature Setpoint"]

    @tin8_august_indoor_average_temperature_setpoint.setter
    def tin8_august_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN8: August Indoor Average Temperature Setpoint`

        """
        self["TIN8: August Indoor Average Temperature Setpoint"] = value

    @property
    def tin9_september_indoor_average_temperature_setpoint(self):
        """field `TIN9: September Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN9: September Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin9_september_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN9: September Indoor Average Temperature Setpoint"]

    @tin9_september_indoor_average_temperature_setpoint.setter
    def tin9_september_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN9: September Indoor Average Temperature Setpoint`

        """
        self["TIN9: September Indoor Average Temperature Setpoint"] = value

    @property
    def tin10_october_indoor_average_temperature_setpoint(self):
        """field `TIN10: October Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN10: October Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin10_october_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN10: October Indoor Average Temperature Setpoint"]

    @tin10_october_indoor_average_temperature_setpoint.setter
    def tin10_october_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN10: October Indoor Average Temperature Setpoint`

        """
        self["TIN10: October Indoor Average Temperature Setpoint"] = value

    @property
    def tin11_november_indoor_average_temperature_setpoint(self):
        """field `TIN11: November Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN11: November Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin11_november_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN11: November Indoor Average Temperature Setpoint"]

    @tin11_november_indoor_average_temperature_setpoint.setter
    def tin11_november_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN11: November Indoor Average Temperature Setpoint`

        """
        self["TIN11: November Indoor Average Temperature Setpoint"] = value

    @property
    def tin12_december_indoor_average_temperature_setpoint(self):
        """field `TIN12: December Indoor Average Temperature Setpoint`

        |  see memo on object for more information
        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `TIN12: December Indoor Average Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tin12_december_indoor_average_temperature_setpoint` or None if not set
        """
        return self["TIN12: December Indoor Average Temperature Setpoint"]

    @tin12_december_indoor_average_temperature_setpoint.setter
    def tin12_december_indoor_average_temperature_setpoint(self, value=22.0):
        """  Corresponds to IDD field `TIN12: December Indoor Average Temperature Setpoint`

        """
        self["TIN12: December Indoor Average Temperature Setpoint"] = value

    @property
    def tinamp_daily_indoor_sine_wave_variation_amplitude(self):
        """field `TINAmp: Daily Indoor sine wave variation amplitude`

        |  This field permits imposing a daily sinusoidal variation
        |  in the indoor setpoint temperature to simulate the effect
        |  of a setback profile.
        |  The value specified is the amplitude of the sine wave.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `TINAmp: Daily Indoor sine wave variation amplitude`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tinamp_daily_indoor_sine_wave_variation_amplitude` or None if not set
        """
        return self["TINAmp: Daily Indoor sine wave variation amplitude"]

    @tinamp_daily_indoor_sine_wave_variation_amplitude.setter
    def tinamp_daily_indoor_sine_wave_variation_amplitude(self, value=None):
        """  Corresponds to IDD field `TINAmp: Daily Indoor sine wave variation amplitude`

        """
        self["TINAmp: Daily Indoor sine wave variation amplitude"] = value

    @property
    def convtol_convergence_tolerance(self):
        """field `ConvTol: Convergence Tolerance`

        |  This field specifies the convergence tolerance used to
        |  control the iteration. When the temperature change of all nodes
        |  is less than the convergence value, iteration ceases.
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `ConvTol: Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convtol_convergence_tolerance` or None if not set
        """
        return self["ConvTol: Convergence Tolerance"]

    @convtol_convergence_tolerance.setter
    def convtol_convergence_tolerance(self, value=0.1):
        """  Corresponds to IDD field `ConvTol: Convergence Tolerance`

        """
        self["ConvTol: Convergence Tolerance"] = value




class GroundHeatTransferSlabInsulation(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:Insulation`
        This object supplies the information about insulation used around the slab.
        There are two possible configurations: under the slab or vertical insulation
        around the slab.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'rins: r value of under slab insulation',
                                       {'name': u'RINS: R value of under slab insulation',
                                        'pyname': u'rins_r_value_of_under_slab_insulation',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2-K/W'}),
                                      (u'dins: width of strip of under slab insulation',
                                       {'name': u'DINS: Width of strip of under slab insulation',
                                        'pyname': u'dins_width_of_strip_of_under_slab_insulation',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'rvins: r value of vertical insulation',
                                       {'name': u'RVINS: R value of vertical insulation',
                                        'pyname': u'rvins_r_value_of_vertical_insulation',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2-K/W'}),
                                      (u'zvins: depth of vertical insulation',
                                       {'name': u'ZVINS: Depth of vertical insulation',
                                        'pyname': u'zvins_depth_of_vertical_insulation',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'ivins: flag: is there vertical insulation',
                                       {'name': u'IVINS: Flag: Is there vertical insulation',
                                        'pyname': u'ivins_flag_is_there_vertical_insulation',
                                        'default': 0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [0,
                                                            1],
                                        'autocalculatable': False,
                                        'type': 'integer'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:Insulation',
               'pyname': u'GroundHeatTransferSlabInsulation',
               'required-object': False,
               'unique-object': False}

    @property
    def rins_r_value_of_under_slab_insulation(self):
        """field `RINS: R value of under slab insulation`

        |  This field provides the thermal resistance value
        |  of the under slab insulation. It should be zero
        |  if the vertical insulation configuration is selected.
        |  typical value= 0-2.0
        |  Units: m2-K/W

        Args:
            value (float): value for IDD Field `RINS: R value of under slab insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rins_r_value_of_under_slab_insulation` or None if not set
        """
        return self["RINS: R value of under slab insulation"]

    @rins_r_value_of_under_slab_insulation.setter
    def rins_r_value_of_under_slab_insulation(self, value=None):
        """  Corresponds to IDD field `RINS: R value of under slab insulation`

        """
        self["RINS: R value of under slab insulation"] = value

    @property
    def dins_width_of_strip_of_under_slab_insulation(self):
        """field `DINS: Width of strip of under slab insulation`

        |  This specifies the width of the perimeter strip of insulation
        |  under the slab. It should be zero if for the vertical insulation
        |  configuration is selected.
        |  typical value= 0-2.0
        |  Units: m

        Args:
            value (float): value for IDD Field `DINS: Width of strip of under slab insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dins_width_of_strip_of_under_slab_insulation` or None if not set
        """
        return self["DINS: Width of strip of under slab insulation"]

    @dins_width_of_strip_of_under_slab_insulation.setter
    def dins_width_of_strip_of_under_slab_insulation(self, value=None):
        """  Corresponds to IDD field `DINS: Width of strip of under slab insulation`

        """
        self["DINS: Width of strip of under slab insulation"] = value

    @property
    def rvins_r_value_of_vertical_insulation(self):
        """field `RVINS: R value of vertical insulation`

        |  This field specifies the thermal resistance of the vertical
        |  insulation. It should be zero if the under slab insulation
        |  configuration is selected.
        |  typical value= 0-3.0
        |  Units: m2-K/W

        Args:
            value (float): value for IDD Field `RVINS: R value of vertical insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rvins_r_value_of_vertical_insulation` or None if not set
        """
        return self["RVINS: R value of vertical insulation"]

    @rvins_r_value_of_vertical_insulation.setter
    def rvins_r_value_of_vertical_insulation(self, value=None):
        """  Corresponds to IDD field `RVINS: R value of vertical insulation`

        """
        self["RVINS: R value of vertical insulation"] = value

    @property
    def zvins_depth_of_vertical_insulation(self):
        """field `ZVINS: Depth of vertical insulation`

        |  This field specifies the depth of the vertical insulation
        |  into the ground in meters. It starts at the slab upper surface
        |  and extends into the ground.
        |  It should be zero if the under slab insulation
        |  configuration is selected.
        |  only use values= .2 .4 .6 .8 1.0 1.5 2.0 2.5 3.0
        |  Units: m

        Args:
            value (float): value for IDD Field `ZVINS: Depth of vertical insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zvins_depth_of_vertical_insulation` or None if not set
        """
        return self["ZVINS: Depth of vertical insulation"]

    @zvins_depth_of_vertical_insulation.setter
    def zvins_depth_of_vertical_insulation(self, value=None):
        """  Corresponds to IDD field `ZVINS: Depth of vertical insulation`

        """
        self["ZVINS: Depth of vertical insulation"] = value

    @property
    def ivins_flag_is_there_vertical_insulation(self):
        """field `IVINS: Flag: Is there vertical insulation`

        |  Specifies if the vertical insulation configuration is being used.
        |  values: 1=yes vertical insulation 0=no under-slab insulation

        Args:
            value (int): value for IDD Field `IVINS: Flag: Is there vertical insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `ivins_flag_is_there_vertical_insulation` or None if not set
        """
        return self["IVINS: Flag: Is there vertical insulation"]

    @ivins_flag_is_there_vertical_insulation.setter
    def ivins_flag_is_there_vertical_insulation(self, value=None):
        """  Corresponds to IDD field `IVINS: Flag: Is there vertical insulation`

        """
        self["IVINS: Flag: Is there vertical insulation"] = value




class GroundHeatTransferSlabEquivalentSlab(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:EquivalentSlab`
        Using an equivalent slab allows non-rectangular shapes to be modeled accurately.
        Object uses the area - perimeter (area/perimeter) ratio to determine the
        size of an equivalent rectangular slab.
        EnergyPlus users normally use this option.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'apratio: the area to perimeter ratio for this slab',
                                       {'name': u'APRatio: The area to perimeter ratio for this slab',
                                        'pyname': u'apratio_the_area_to_perimeter_ratio_for_this_slab',
                                        'maximum': 22.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.5,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slabdepth: thickness of slab on grade',
                                       {'name': u'SLABDEPTH: Thickness of slab on grade',
                                        'pyname': u'slabdepth_thickness_of_slab_on_grade',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'clearance: distance from edge of slab to domain edge',
                                       {'name': u'CLEARANCE: Distance from edge of slab to domain edge',
                                        'pyname': u'clearance_distance_from_edge_of_slab_to_domain_edge',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'zclearance: distance from bottom of slab to domain bottom',
                                       {'name': u'ZCLEARANCE: Distance from bottom of slab to domain bottom',
                                        'pyname': u'zclearance_distance_from_bottom_of_slab_to_domain_bottom',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:EquivalentSlab',
               'pyname': u'GroundHeatTransferSlabEquivalentSlab',
               'required-object': False,
               'unique-object': False}

    @property
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self):
        """field `APRatio: The area to perimeter ratio for this slab`

        |  Equivalent square slab is simulated,  side is 4*APRatio.
        |  Units: m
        |  value >= 1.5
        |  value <= 22.0

        Args:
            value (float): value for IDD Field `APRatio: The area to perimeter ratio for this slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `apratio_the_area_to_perimeter_ratio_for_this_slab` or None if not set
        """
        return self["APRatio: The area to perimeter ratio for this slab"]

    @apratio_the_area_to_perimeter_ratio_for_this_slab.setter
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self, value=None):
        """  Corresponds to IDD field `APRatio: The area to perimeter ratio for this slab`

        """
        self["APRatio: The area to perimeter ratio for this slab"] = value

    @property
    def slabdepth_thickness_of_slab_on_grade(self):
        """field `SLABDEPTH: Thickness of slab on grade`

        |  This field specifies the thickness of the slab. The slab top surface is level
        |  with the ground surface, so this is the depth into the ground.
        |  The slab depth has a significant effect on the temperature calculation,
        |  and it is also important for the auto-grid process.
        |  The finite difference grids are set in such a way that they use the slab thickness
        |  to determine the vertical grid spacing. Autogridding will fail if the slab thickness
        |  is specified larger than 0.25 meters.
        |  Units: m
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `SLABDEPTH: Thickness of slab on grade`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slabdepth_thickness_of_slab_on_grade` or None if not set
        """
        return self["SLABDEPTH: Thickness of slab on grade"]

    @slabdepth_thickness_of_slab_on_grade.setter
    def slabdepth_thickness_of_slab_on_grade(self, value=0.1):
        """  Corresponds to IDD field `SLABDEPTH: Thickness of slab on grade`

        """
        self["SLABDEPTH: Thickness of slab on grade"] = value

    @property
    def clearance_distance_from_edge_of_slab_to_domain_edge(self):
        """field `CLEARANCE: Distance from edge of slab to domain edge`

        |  This field specifies the distance from the slab to the edge of
        |  the area that will be modeled with the grid system. It is the basic size
        |  dimension that is used to set the horizontal extent of the domain.
        |  15 meters is a reasonable value.
        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `CLEARANCE: Distance from edge of slab to domain edge`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `clearance_distance_from_edge_of_slab_to_domain_edge` or None if not set
        """
        return self["CLEARANCE: Distance from edge of slab to domain edge"]

    @clearance_distance_from_edge_of_slab_to_domain_edge.setter
    def clearance_distance_from_edge_of_slab_to_domain_edge(self, value=15.0):
        """  Corresponds to IDD field `CLEARANCE: Distance from edge of slab to domain edge`

        """
        self["CLEARANCE: Distance from edge of slab to domain edge"] = value

    @property
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(self):
        """field `ZCLEARANCE: Distance from bottom of slab to domain bottom`

        |  This field specifies the vertical distance from the slab to the
        |  bottom edge of the area that will be modeled with the grid system.
        |  15 meters is a reasonable value.
        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `ZCLEARANCE: Distance from bottom of slab to domain bottom`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zclearance_distance_from_bottom_of_slab_to_domain_bottom` or None if not set
        """
        return self[
            "ZCLEARANCE: Distance from bottom of slab to domain bottom"]

    @zclearance_distance_from_bottom_of_slab_to_domain_bottom.setter
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(
            self,
            value=15.0):
        """  Corresponds to IDD field `ZCLEARANCE: Distance from bottom of slab to domain bottom`

        """
        self[
            "ZCLEARANCE: Distance from bottom of slab to domain bottom"] = value




class GroundHeatTransferSlabAutoGrid(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:AutoGrid`
        AutoGrid only necessary when EquivalentSlab option not chosen.
        Not normally needed by EnergyPlus users.
        This object permits user selection of rectangular slab dimensions.
        NO SLAB DIMENSIONS LESS THAN 6 m.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'slabx: x dimension of the building slab',
                                       {'name': u'SLABX: X dimension of the building slab',
                                        'pyname': u'slabx_x_dimension_of_the_building_slab',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 6.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slaby: y dimension of the building slab',
                                       {'name': u'SLABY: Y dimension of the building slab',
                                        'pyname': u'slaby_y_dimension_of_the_building_slab',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 6.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slabdepth: thickness of slab on grade',
                                       {'name': u'SLABDEPTH: Thickness of slab on grade',
                                        'pyname': u'slabdepth_thickness_of_slab_on_grade',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'clearance: distance from edge of slab to domain edge',
                                       {'name': u'CLEARANCE: Distance from edge of slab to domain edge',
                                        'pyname': u'clearance_distance_from_edge_of_slab_to_domain_edge',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'zclearance: distance from bottom of slab to domain bottom',
                                       {'name': u'ZCLEARANCE: Distance from bottom of slab to domain bottom',
                                        'pyname': u'zclearance_distance_from_bottom_of_slab_to_domain_bottom',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:AutoGrid',
               'pyname': u'GroundHeatTransferSlabAutoGrid',
               'required-object': False,
               'unique-object': False}

    @property
    def slabx_x_dimension_of_the_building_slab(self):
        """field `SLABX: X dimension of the building slab`

        |  typical values= 6 to 60.0
        |  Units: m
        |  value >= 6.0

        Args:
            value (float): value for IDD Field `SLABX: X dimension of the building slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slabx_x_dimension_of_the_building_slab` or None if not set
        """
        return self["SLABX: X dimension of the building slab"]

    @slabx_x_dimension_of_the_building_slab.setter
    def slabx_x_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD field `SLABX: X dimension of the building slab`

        """
        self["SLABX: X dimension of the building slab"] = value

    @property
    def slaby_y_dimension_of_the_building_slab(self):
        """field `SLABY: Y dimension of the building slab`

        |  typical values= 6 to 60.0
        |  Units: m
        |  value >= 6.0

        Args:
            value (float): value for IDD Field `SLABY: Y dimension of the building slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slaby_y_dimension_of_the_building_slab` or None if not set
        """
        return self["SLABY: Y dimension of the building slab"]

    @slaby_y_dimension_of_the_building_slab.setter
    def slaby_y_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD field `SLABY: Y dimension of the building slab`

        """
        self["SLABY: Y dimension of the building slab"] = value

    @property
    def slabdepth_thickness_of_slab_on_grade(self):
        """field `SLABDEPTH: Thickness of slab on grade`

        |  Units: m
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `SLABDEPTH: Thickness of slab on grade`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slabdepth_thickness_of_slab_on_grade` or None if not set
        """
        return self["SLABDEPTH: Thickness of slab on grade"]

    @slabdepth_thickness_of_slab_on_grade.setter
    def slabdepth_thickness_of_slab_on_grade(self, value=0.1):
        """  Corresponds to IDD field `SLABDEPTH: Thickness of slab on grade`

        """
        self["SLABDEPTH: Thickness of slab on grade"] = value

    @property
    def clearance_distance_from_edge_of_slab_to_domain_edge(self):
        """field `CLEARANCE: Distance from edge of slab to domain edge`

        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `CLEARANCE: Distance from edge of slab to domain edge`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `clearance_distance_from_edge_of_slab_to_domain_edge` or None if not set
        """
        return self["CLEARANCE: Distance from edge of slab to domain edge"]

    @clearance_distance_from_edge_of_slab_to_domain_edge.setter
    def clearance_distance_from_edge_of_slab_to_domain_edge(self, value=15.0):
        """  Corresponds to IDD field `CLEARANCE: Distance from edge of slab to domain edge`

        """
        self["CLEARANCE: Distance from edge of slab to domain edge"] = value

    @property
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(self):
        """field `ZCLEARANCE: Distance from bottom of slab to domain bottom`

        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `ZCLEARANCE: Distance from bottom of slab to domain bottom`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zclearance_distance_from_bottom_of_slab_to_domain_bottom` or None if not set
        """
        return self[
            "ZCLEARANCE: Distance from bottom of slab to domain bottom"]

    @zclearance_distance_from_bottom_of_slab_to_domain_bottom.setter
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(
            self,
            value=15.0):
        """  Corresponds to IDD field `ZCLEARANCE: Distance from bottom of slab to domain bottom`

        """
        self[
            "ZCLEARANCE: Distance from bottom of slab to domain bottom"] = value




class GroundHeatTransferSlabManualGrid(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:ManualGrid`
        Manual Grid only necessary when using manual gridding (not recommended)
        Used only in special cases when previous two objects are not used.
        User must input complete gridding information.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'nx: number of cells in the x direction',
                                       {'name': u'NX: Number of cells in the X direction',
                                        'pyname': u'nx_number_of_cells_in_the_x_direction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'ny: number of cells in the y direction',
                                       {'name': u'NY: Number of cells in the Y direction',
                                        'pyname': u'ny_number_of_cells_in_the_y_direction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'nz: number of cells in the z direction',
                                       {'name': u'NZ: Number of cells in the Z direction',
                                        'pyname': u'nz_number_of_cells_in_the_z_direction',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'ibox: x direction cell indicator of slab edge',
                                       {'name': u'IBOX: X direction cell indicator of slab edge',
                                        'pyname': u'ibox_x_direction_cell_indicator_of_slab_edge',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'jbox: y direction cell indicator of slab edge',
                                       {'name': u'JBOX: Y direction cell indicator of slab edge',
                                        'pyname': u'jbox_y_direction_cell_indicator_of_slab_edge',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:ManualGrid',
               'pyname': u'GroundHeatTransferSlabManualGrid',
               'required-object': False,
               'unique-object': False}

    @property
    def nx_number_of_cells_in_the_x_direction(self):
        """field `NX: Number of cells in the X direction`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NX: Number of cells in the X direction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nx_number_of_cells_in_the_x_direction` or None if not set
        """
        return self["NX: Number of cells in the X direction"]

    @nx_number_of_cells_in_the_x_direction.setter
    def nx_number_of_cells_in_the_x_direction(self, value=None):
        """  Corresponds to IDD field `NX: Number of cells in the X direction`

        """
        self["NX: Number of cells in the X direction"] = value

    @property
    def ny_number_of_cells_in_the_y_direction(self):
        """field `NY: Number of cells in the Y direction`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NY: Number of cells in the Y direction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ny_number_of_cells_in_the_y_direction` or None if not set
        """
        return self["NY: Number of cells in the Y direction"]

    @ny_number_of_cells_in_the_y_direction.setter
    def ny_number_of_cells_in_the_y_direction(self, value=None):
        """  Corresponds to IDD field `NY: Number of cells in the Y direction`

        """
        self["NY: Number of cells in the Y direction"] = value

    @property
    def nz_number_of_cells_in_the_z_direction(self):
        """field `NZ: Number of cells in the Z direction`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NZ: Number of cells in the Z direction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nz_number_of_cells_in_the_z_direction` or None if not set
        """
        return self["NZ: Number of cells in the Z direction"]

    @nz_number_of_cells_in_the_z_direction.setter
    def nz_number_of_cells_in_the_z_direction(self, value=None):
        """  Corresponds to IDD field `NZ: Number of cells in the Z direction`

        """
        self["NZ: Number of cells in the Z direction"] = value

    @property
    def ibox_x_direction_cell_indicator_of_slab_edge(self):
        """field `IBOX: X direction cell indicator of slab edge`

        |  typical values= 1-10

        Args:
            value (float): value for IDD Field `IBOX: X direction cell indicator of slab edge`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ibox_x_direction_cell_indicator_of_slab_edge` or None if not set
        """
        return self["IBOX: X direction cell indicator of slab edge"]

    @ibox_x_direction_cell_indicator_of_slab_edge.setter
    def ibox_x_direction_cell_indicator_of_slab_edge(self, value=None):
        """  Corresponds to IDD field `IBOX: X direction cell indicator of slab edge`

        """
        self["IBOX: X direction cell indicator of slab edge"] = value

    @property
    def jbox_y_direction_cell_indicator_of_slab_edge(self):
        """field `JBOX: Y direction cell indicator of slab edge`

        |  typical values= 1-10

        Args:
            value (float): value for IDD Field `JBOX: Y direction cell indicator of slab edge`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `jbox_y_direction_cell_indicator_of_slab_edge` or None if not set
        """
        return self["JBOX: Y direction cell indicator of slab edge"]

    @jbox_y_direction_cell_indicator_of_slab_edge.setter
    def jbox_y_direction_cell_indicator_of_slab_edge(self, value=None):
        """  Corresponds to IDD field `JBOX: Y direction cell indicator of slab edge`

        """
        self["JBOX: Y direction cell indicator of slab edge"] = value




class GroundHeatTransferSlabXface(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:XFACE`
        This is only needed when using manual gridding (not recommended)
        XFACE: X Direction cell face coordinates: m
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:XFACE',
               'pyname': u'GroundHeatTransferSlabXface',
               'required-object': False,
               'unique-object': False}




class GroundHeatTransferSlabYface(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:YFACE`
        This is only needed when using manual gridding (not recommended)
        YFACE: Y Direction cell face coordinates: m,
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:YFACE',
               'pyname': u'GroundHeatTransferSlabYface',
               'required-object': False,
               'unique-object': False}




class GroundHeatTransferSlabZface(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Slab:ZFACE`
        This is only needed when using manual gridding (not recommended)
        ZFACE: Z Direction cell face coordinates: m
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Slab:ZFACE',
               'pyname': u'GroundHeatTransferSlabZface',
               'required-object': False,
               'unique-object': False}




class GroundHeatTransferBasementSimParameters(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:SimParameters`
        Specifies certain parameters that control the Basement preprocessor ground heat
        transfer simulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'f: multiplier for the adi solution',
                                       {'name': u'F: Multiplier for the ADI solution',
                                        'pyname': u'f_multiplier_for_the_adi_solution',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'iyrs: maximum number of yearly iterations:',
                                       {'name': u'IYRS: Maximum number of yearly iterations:',
                                        'pyname': u'iyrs_maximum_number_of_yearly_iterations',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:SimParameters',
               'pyname': u'GroundHeatTransferBasementSimParameters',
               'required-object': False,
               'unique-object': False}

    @property
    def f_multiplier_for_the_adi_solution(self):
        """field `F: Multiplier for the ADI solution`

        |  0<F<1.0,
        |  typically 0.1 (0.3 for high k soil - saturated sand is about 2.6 w/m-K)
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `F: Multiplier for the ADI solution`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `f_multiplier_for_the_adi_solution` or None if not set
        """
        return self["F: Multiplier for the ADI solution"]

    @f_multiplier_for_the_adi_solution.setter
    def f_multiplier_for_the_adi_solution(self, value=None):
        """  Corresponds to IDD field `F: Multiplier for the ADI solution`

        """
        self["F: Multiplier for the ADI solution"] = value

    @property
    def iyrs_maximum_number_of_yearly_iterations(self):
        """field `IYRS: Maximum number of yearly iterations:`

        |  typically 15-30]
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `IYRS: Maximum number of yearly iterations:`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `iyrs_maximum_number_of_yearly_iterations` or None if not set
        """
        return self["IYRS: Maximum number of yearly iterations:"]

    @iyrs_maximum_number_of_yearly_iterations.setter
    def iyrs_maximum_number_of_yearly_iterations(self, value=15.0):
        """  Corresponds to IDD field `IYRS: Maximum number of yearly iterations:`

        """
        self["IYRS: Maximum number of yearly iterations:"] = value




class GroundHeatTransferBasementMatlProps(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:MatlProps`
        Specifies the material properties for the Basement preprocessor ground heat
        transfer simulation. Only the Foundation Wall, Floor Slab, Soil,
        and Gravel properties are currently used.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'nmat: number of materials in this domain',
                                       {'name': u'NMAT: Number of materials in this domain',
                                        'pyname': u'nmat_number_of_materials_in_this_domain',
                                        'maximum': 6.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'density for foundation wall',
                                       {'name': u'Density for Foundation Wall',
                                        'pyname': u'density_for_foundation_wall',
                                        'default': 2243.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'density for floor slab',
                                       {'name': u'density for Floor Slab',
                                        'pyname': u'density_for_floor_slab',
                                        'default': 2243.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'density for ceiling',
                                       {'name': u'density for Ceiling',
                                        'pyname': u'density_for_ceiling',
                                        'default': 311.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'density for soil',
                                       {'name': u'density for Soil',
                                        'pyname': u'density_for_soil',
                                        'default': 1500.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'density for gravel',
                                       {'name': u'density for Gravel',
                                        'pyname': u'density_for_gravel',
                                        'default': 2000.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'density for wood',
                                       {'name': u'density for Wood',
                                        'pyname': u'density_for_wood',
                                        'default': 449.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/m3'}),
                                      (u'specific heat for foundation wall',
                                       {'name': u'Specific heat for foundation wall',
                                        'pyname': u'specific_heat_for_foundation_wall',
                                        'default': 880.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat for floor slab',
                                       {'name': u'Specific heat for floor slab',
                                        'pyname': u'specific_heat_for_floor_slab',
                                        'default': 880.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat for ceiling',
                                       {'name': u'Specific heat for ceiling',
                                        'pyname': u'specific_heat_for_ceiling',
                                        'default': 1530.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat for soil',
                                       {'name': u'Specific heat for soil',
                                        'pyname': u'specific_heat_for_soil',
                                        'default': 840.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat for gravel',
                                       {'name': u'Specific heat for gravel',
                                        'pyname': u'specific_heat_for_gravel',
                                        'default': 720.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'specific heat for wood',
                                       {'name': u'Specific heat for wood',
                                        'pyname': u'specific_heat_for_wood',
                                        'default': 1530.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/kg-K'}),
                                      (u'thermal conductivity for foundation wall',
                                       {'name': u'Thermal conductivity for foundation wall',
                                        'pyname': u'thermal_conductivity_for_foundation_wall',
                                        'default': 1.4,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'thermal conductivity for floor slab',
                                       {'name': u'Thermal conductivity for floor slab',
                                        'pyname': u'thermal_conductivity_for_floor_slab',
                                        'default': 1.4,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'thermal conductivity for ceiling',
                                       {'name': u'Thermal conductivity for ceiling',
                                        'pyname': u'thermal_conductivity_for_ceiling',
                                        'default': 0.09,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'thermal conductivity for soil',
                                       {'name': u'thermal conductivity for soil',
                                        'pyname': u'thermal_conductivity_for_soil',
                                        'default': 1.1,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'thermal conductivity for gravel',
                                       {'name': u'thermal conductivity for gravel',
                                        'pyname': u'thermal_conductivity_for_gravel',
                                        'default': 1.9,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'}),
                                      (u'thermal conductivity for wood',
                                       {'name': u'thermal conductivity for wood',
                                        'pyname': u'thermal_conductivity_for_wood',
                                        'default': 0.12,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m-K'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:MatlProps',
               'pyname': u'GroundHeatTransferBasementMatlProps',
               'required-object': False,
               'unique-object': False}

    @property
    def nmat_number_of_materials_in_this_domain(self):
        """field `NMAT: Number of materials in this domain`

        |  value <= 6.0

        Args:
            value (float): value for IDD Field `NMAT: Number of materials in this domain`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nmat_number_of_materials_in_this_domain` or None if not set
        """
        return self["NMAT: Number of materials in this domain"]

    @nmat_number_of_materials_in_this_domain.setter
    def nmat_number_of_materials_in_this_domain(self, value=None):
        """  Corresponds to IDD field `NMAT: Number of materials in this domain`

        """
        self["NMAT: Number of materials in this domain"] = value

    @property
    def density_for_foundation_wall(self):
        """field `Density for Foundation Wall`

        |  Units: kg/m3
        |  Default value: 2243.0

        Args:
            value (float): value for IDD Field `Density for Foundation Wall`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_for_foundation_wall` or None if not set

        """
        return self["Density for Foundation Wall"]

    @density_for_foundation_wall.setter
    def density_for_foundation_wall(self, value=2243.0):
        """Corresponds to IDD field `Density for Foundation Wall`"""
        self["Density for Foundation Wall"] = value

    @property
    def density_for_floor_slab(self):
        """field `density for Floor Slab`

        |  Units: kg/m3
        |  Default value: 2243.0

        Args:
            value (float): value for IDD Field `density for Floor Slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_for_floor_slab` or None if not set

        """
        return self["density for Floor Slab"]

    @density_for_floor_slab.setter
    def density_for_floor_slab(self, value=2243.0):
        """Corresponds to IDD field `density for Floor Slab`"""
        self["density for Floor Slab"] = value

    @property
    def density_for_ceiling(self):
        """field `density for Ceiling`

        |  Units: kg/m3
        |  Default value: 311.0

        Args:
            value (float): value for IDD Field `density for Ceiling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_for_ceiling` or None if not set

        """
        return self["density for Ceiling"]

    @density_for_ceiling.setter
    def density_for_ceiling(self, value=311.0):
        """Corresponds to IDD field `density for Ceiling`"""
        self["density for Ceiling"] = value

    @property
    def density_for_soil(self):
        """field `density for Soil`

        |  Units: kg/m3
        |  Default value: 1500.0

        Args:
            value (float): value for IDD Field `density for Soil`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_for_soil` or None if not set

        """
        return self["density for Soil"]

    @density_for_soil.setter
    def density_for_soil(self, value=1500.0):
        """Corresponds to IDD field `density for Soil`"""
        self["density for Soil"] = value

    @property
    def density_for_gravel(self):
        """field `density for Gravel`

        |  Units: kg/m3
        |  Default value: 2000.0

        Args:
            value (float): value for IDD Field `density for Gravel`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_for_gravel` or None if not set

        """
        return self["density for Gravel"]

    @density_for_gravel.setter
    def density_for_gravel(self, value=2000.0):
        """Corresponds to IDD field `density for Gravel`"""
        self["density for Gravel"] = value

    @property
    def density_for_wood(self):
        """field `density for Wood`

        |  Units: kg/m3
        |  Default value: 449.0

        Args:
            value (float): value for IDD Field `density for Wood`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `density_for_wood` or None if not set

        """
        return self["density for Wood"]

    @density_for_wood.setter
    def density_for_wood(self, value=449.0):
        """Corresponds to IDD field `density for Wood`"""
        self["density for Wood"] = value

    @property
    def specific_heat_for_foundation_wall(self):
        """field `Specific heat for foundation wall`

        |  Units: J/kg-K
        |  Default value: 880.0

        Args:
            value (float): value for IDD Field `Specific heat for foundation wall`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_for_foundation_wall` or None if not set

        """
        return self["Specific heat for foundation wall"]

    @specific_heat_for_foundation_wall.setter
    def specific_heat_for_foundation_wall(self, value=880.0):
        """Corresponds to IDD field `Specific heat for foundation wall`"""
        self["Specific heat for foundation wall"] = value

    @property
    def specific_heat_for_floor_slab(self):
        """field `Specific heat for floor slab`

        |  Units: J/kg-K
        |  Default value: 880.0

        Args:
            value (float): value for IDD Field `Specific heat for floor slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_for_floor_slab` or None if not set

        """
        return self["Specific heat for floor slab"]

    @specific_heat_for_floor_slab.setter
    def specific_heat_for_floor_slab(self, value=880.0):
        """Corresponds to IDD field `Specific heat for floor slab`"""
        self["Specific heat for floor slab"] = value

    @property
    def specific_heat_for_ceiling(self):
        """field `Specific heat for ceiling`

        |  Units: J/kg-K
        |  Default value: 1530.0

        Args:
            value (float): value for IDD Field `Specific heat for ceiling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_for_ceiling` or None if not set

        """
        return self["Specific heat for ceiling"]

    @specific_heat_for_ceiling.setter
    def specific_heat_for_ceiling(self, value=1530.0):
        """Corresponds to IDD field `Specific heat for ceiling`"""
        self["Specific heat for ceiling"] = value

    @property
    def specific_heat_for_soil(self):
        """field `Specific heat for soil`

        |  Units: J/kg-K
        |  Default value: 840.0

        Args:
            value (float): value for IDD Field `Specific heat for soil`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_for_soil` or None if not set

        """
        return self["Specific heat for soil"]

    @specific_heat_for_soil.setter
    def specific_heat_for_soil(self, value=840.0):
        """Corresponds to IDD field `Specific heat for soil`"""
        self["Specific heat for soil"] = value

    @property
    def specific_heat_for_gravel(self):
        """field `Specific heat for gravel`

        |  Units: J/kg-K
        |  Default value: 720.0

        Args:
            value (float): value for IDD Field `Specific heat for gravel`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_for_gravel` or None if not set

        """
        return self["Specific heat for gravel"]

    @specific_heat_for_gravel.setter
    def specific_heat_for_gravel(self, value=720.0):
        """Corresponds to IDD field `Specific heat for gravel`"""
        self["Specific heat for gravel"] = value

    @property
    def specific_heat_for_wood(self):
        """field `Specific heat for wood`

        |  Units: J/kg-K
        |  Default value: 1530.0

        Args:
            value (float): value for IDD Field `Specific heat for wood`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `specific_heat_for_wood` or None if not set

        """
        return self["Specific heat for wood"]

    @specific_heat_for_wood.setter
    def specific_heat_for_wood(self, value=1530.0):
        """Corresponds to IDD field `Specific heat for wood`"""
        self["Specific heat for wood"] = value

    @property
    def thermal_conductivity_for_foundation_wall(self):
        """field `Thermal conductivity for foundation wall`

        |  Units: W/m-K
        |  Default value: 1.4

        Args:
            value (float): value for IDD Field `Thermal conductivity for foundation wall`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_for_foundation_wall` or None if not set

        """
        return self["Thermal conductivity for foundation wall"]

    @thermal_conductivity_for_foundation_wall.setter
    def thermal_conductivity_for_foundation_wall(self, value=1.4):
        """Corresponds to IDD field `Thermal conductivity for foundation
        wall`"""
        self["Thermal conductivity for foundation wall"] = value

    @property
    def thermal_conductivity_for_floor_slab(self):
        """field `Thermal conductivity for floor slab`

        |  Units: W/m-K
        |  Default value: 1.4

        Args:
            value (float): value for IDD Field `Thermal conductivity for floor slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_for_floor_slab` or None if not set

        """
        return self["Thermal conductivity for floor slab"]

    @thermal_conductivity_for_floor_slab.setter
    def thermal_conductivity_for_floor_slab(self, value=1.4):
        """Corresponds to IDD field `Thermal conductivity for floor slab`"""
        self["Thermal conductivity for floor slab"] = value

    @property
    def thermal_conductivity_for_ceiling(self):
        """field `Thermal conductivity for ceiling`

        |  Units: W/m-K
        |  Default value: 0.09

        Args:
            value (float): value for IDD Field `Thermal conductivity for ceiling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_for_ceiling` or None if not set

        """
        return self["Thermal conductivity for ceiling"]

    @thermal_conductivity_for_ceiling.setter
    def thermal_conductivity_for_ceiling(self, value=0.09):
        """Corresponds to IDD field `Thermal conductivity for ceiling`"""
        self["Thermal conductivity for ceiling"] = value

    @property
    def thermal_conductivity_for_soil(self):
        """field `thermal conductivity for soil`

        |  Units: W/m-K
        |  Default value: 1.1

        Args:
            value (float): value for IDD Field `thermal conductivity for soil`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_for_soil` or None if not set

        """
        return self["thermal conductivity for soil"]

    @thermal_conductivity_for_soil.setter
    def thermal_conductivity_for_soil(self, value=1.1):
        """Corresponds to IDD field `thermal conductivity for soil`"""
        self["thermal conductivity for soil"] = value

    @property
    def thermal_conductivity_for_gravel(self):
        """field `thermal conductivity for gravel`

        |  Units: W/m-K
        |  Default value: 1.9

        Args:
            value (float): value for IDD Field `thermal conductivity for gravel`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_for_gravel` or None if not set

        """
        return self["thermal conductivity for gravel"]

    @thermal_conductivity_for_gravel.setter
    def thermal_conductivity_for_gravel(self, value=1.9):
        """Corresponds to IDD field `thermal conductivity for gravel`"""
        self["thermal conductivity for gravel"] = value

    @property
    def thermal_conductivity_for_wood(self):
        """field `thermal conductivity for wood`

        |  Units: W/m-K
        |  Default value: 0.12

        Args:
            value (float): value for IDD Field `thermal conductivity for wood`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_conductivity_for_wood` or None if not set

        """
        return self["thermal conductivity for wood"]

    @thermal_conductivity_for_wood.setter
    def thermal_conductivity_for_wood(self, value=0.12):
        """Corresponds to IDD field `thermal conductivity for wood`"""
        self["thermal conductivity for wood"] = value




class GroundHeatTransferBasementInsulation(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:Insulation`
        Describes the insulation used on an exterior basement wall for the Basement
        preprocessor ground heat transfer simulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'rext: r value of any exterior insulation',
                                       {'name': u'REXT: R Value of any exterior insulation',
                                        'pyname': u'rext_r_value_of_any_exterior_insulation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2-K/W'}),
                                      (u'insfull: flag: is the wall fully insulated?',
                                       {'name': u'INSFULL: Flag: Is the wall fully insulated?',
                                        'pyname': u'insfull_flag_is_the_wall_fully_insulated',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:Insulation',
               'pyname': u'GroundHeatTransferBasementInsulation',
               'required-object': False,
               'unique-object': False}

    @property
    def rext_r_value_of_any_exterior_insulation(self):
        """field `REXT: R Value of any exterior insulation`

        |  Units: m2-K/W

        Args:
            value (float): value for IDD Field `REXT: R Value of any exterior insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rext_r_value_of_any_exterior_insulation` or None if not set
        """
        return self["REXT: R Value of any exterior insulation"]

    @rext_r_value_of_any_exterior_insulation.setter
    def rext_r_value_of_any_exterior_insulation(self, value=None):
        """  Corresponds to IDD field `REXT: R Value of any exterior insulation`

        """
        self["REXT: R Value of any exterior insulation"] = value

    @property
    def insfull_flag_is_the_wall_fully_insulated(self):
        """field `INSFULL: Flag: Is the wall fully insulated?`

        |  True for full insulation
        |  False for insulation half way down side wall from grade line

        Args:
            value (str): value for IDD Field `INSFULL: Flag: Is the wall fully insulated?`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `insfull_flag_is_the_wall_fully_insulated` or None if not set
        """
        return self["INSFULL: Flag: Is the wall fully insulated?"]

    @insfull_flag_is_the_wall_fully_insulated.setter
    def insfull_flag_is_the_wall_fully_insulated(self, value=None):
        """  Corresponds to IDD field `INSFULL: Flag: Is the wall fully insulated?`

        """
        self["INSFULL: Flag: Is the wall fully insulated?"] = value




class GroundHeatTransferBasementSurfaceProps(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:SurfaceProps`
        Specifies the soil surface properties for the Basement preprocessor ground
        heat transfer simulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'albedo: surface albedo for no snow conditions',
                                       {'name': u'ALBEDO: Surface albedo for No snow conditions',
                                        'pyname': u'albedo_surface_albedo_for_no_snow_conditions',
                                        'default': 0.16,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'albedo: surface albedo for snow conditions',
                                       {'name': u'ALBEDO: Surface albedo for snow conditions',
                                        'pyname': u'albedo_surface_albedo_for_snow_conditions',
                                        'default': 0.4,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'epsln: surface emissivity no snow',
                                       {'name': u'EPSLN: Surface emissivity No Snow',
                                        'pyname': u'epsln_surface_emissivity_no_snow',
                                        'default': 0.94,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'epsln: surface emissivity with snow',
                                       {'name': u'EPSLN: Surface emissivity with Snow',
                                        'pyname': u'epsln_surface_emissivity_with_snow',
                                        'default': 0.86,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'veght: surface roughness no snow conditions',
                                       {'name': u'VEGHT: Surface roughness No snow conditions',
                                        'pyname': u'veght_surface_roughness_no_snow_conditions',
                                        'default': 6.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'cm'}),
                                      (u'veght: surface roughness snow conditions',
                                       {'name': u'VEGHT: Surface roughness Snow conditions',
                                        'pyname': u'veght_surface_roughness_snow_conditions',
                                        'default': 0.25,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'cm'}),
                                      (u'pet: flag, potential evapotranspiration on?',
                                       {'name': u'PET: Flag, Potential evapotranspiration on?',
                                        'pyname': u'pet_flag_potential_evapotranspiration_on',
                                        'default': u'FALSE',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:SurfaceProps',
               'pyname': u'GroundHeatTransferBasementSurfaceProps',
               'required-object': False,
               'unique-object': False}

    @property
    def albedo_surface_albedo_for_no_snow_conditions(self):
        """field `ALBEDO: Surface albedo for No snow conditions`

        |  Default value: 0.16
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `ALBEDO: Surface albedo for No snow conditions`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `albedo_surface_albedo_for_no_snow_conditions` or None if not set
        """
        return self["ALBEDO: Surface albedo for No snow conditions"]

    @albedo_surface_albedo_for_no_snow_conditions.setter
    def albedo_surface_albedo_for_no_snow_conditions(self, value=0.16):
        """  Corresponds to IDD field `ALBEDO: Surface albedo for No snow conditions`

        """
        self["ALBEDO: Surface albedo for No snow conditions"] = value

    @property
    def albedo_surface_albedo_for_snow_conditions(self):
        """field `ALBEDO: Surface albedo for snow conditions`

        |  Default value: 0.4
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `ALBEDO: Surface albedo for snow conditions`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `albedo_surface_albedo_for_snow_conditions` or None if not set
        """
        return self["ALBEDO: Surface albedo for snow conditions"]

    @albedo_surface_albedo_for_snow_conditions.setter
    def albedo_surface_albedo_for_snow_conditions(self, value=0.4):
        """  Corresponds to IDD field `ALBEDO: Surface albedo for snow conditions`

        """
        self["ALBEDO: Surface albedo for snow conditions"] = value

    @property
    def epsln_surface_emissivity_no_snow(self):
        """field `EPSLN: Surface emissivity No Snow`

        |  Default value: 0.94
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `EPSLN: Surface emissivity No Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `epsln_surface_emissivity_no_snow` or None if not set
        """
        return self["EPSLN: Surface emissivity No Snow"]

    @epsln_surface_emissivity_no_snow.setter
    def epsln_surface_emissivity_no_snow(self, value=0.94):
        """  Corresponds to IDD field `EPSLN: Surface emissivity No Snow`

        """
        self["EPSLN: Surface emissivity No Snow"] = value

    @property
    def epsln_surface_emissivity_with_snow(self):
        """field `EPSLN: Surface emissivity with Snow`

        |  Default value: 0.86
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `EPSLN: Surface emissivity with Snow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `epsln_surface_emissivity_with_snow` or None if not set
        """
        return self["EPSLN: Surface emissivity with Snow"]

    @epsln_surface_emissivity_with_snow.setter
    def epsln_surface_emissivity_with_snow(self, value=0.86):
        """  Corresponds to IDD field `EPSLN: Surface emissivity with Snow`

        """
        self["EPSLN: Surface emissivity with Snow"] = value

    @property
    def veght_surface_roughness_no_snow_conditions(self):
        """field `VEGHT: Surface roughness No snow conditions`

        |  Units: cm
        |  Default value: 6.0

        Args:
            value (float): value for IDD Field `VEGHT: Surface roughness No snow conditions`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `veght_surface_roughness_no_snow_conditions` or None if not set
        """
        return self["VEGHT: Surface roughness No snow conditions"]

    @veght_surface_roughness_no_snow_conditions.setter
    def veght_surface_roughness_no_snow_conditions(self, value=6.0):
        """  Corresponds to IDD field `VEGHT: Surface roughness No snow conditions`

        """
        self["VEGHT: Surface roughness No snow conditions"] = value

    @property
    def veght_surface_roughness_snow_conditions(self):
        """field `VEGHT: Surface roughness Snow conditions`

        |  Units: cm
        |  Default value: 0.25

        Args:
            value (float): value for IDD Field `VEGHT: Surface roughness Snow conditions`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `veght_surface_roughness_snow_conditions` or None if not set
        """
        return self["VEGHT: Surface roughness Snow conditions"]

    @veght_surface_roughness_snow_conditions.setter
    def veght_surface_roughness_snow_conditions(self, value=0.25):
        """  Corresponds to IDD field `VEGHT: Surface roughness Snow conditions`

        """
        self["VEGHT: Surface roughness Snow conditions"] = value

    @property
    def pet_flag_potential_evapotranspiration_on(self):
        """field `PET: Flag, Potential evapotranspiration on?`

        |  Typically, PET is False
        |  Default value: FALSE

        Args:
            value (str): value for IDD Field `PET: Flag, Potential evapotranspiration on?`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pet_flag_potential_evapotranspiration_on` or None if not set
        """
        return self["PET: Flag, Potential evapotranspiration on?"]

    @pet_flag_potential_evapotranspiration_on.setter
    def pet_flag_potential_evapotranspiration_on(self, value="FALSE"):
        """  Corresponds to IDD field `PET: Flag, Potential evapotranspiration on?`

        """
        self["PET: Flag, Potential evapotranspiration on?"] = value




class GroundHeatTransferBasementBldgData(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:BldgData`
        Specifies the surface and gravel thicknesses used for the Basement
        preprocessor ground heat transfer simulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'dwall: wall thickness',
                                       {'name': u'DWALL: Wall thickness',
                                        'pyname': u'dwall_wall_thickness',
                                        'default': 0.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.2,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'dslab: floor slab thickness',
                                       {'name': u'DSLAB: Floor slab thickness',
                                        'pyname': u'dslab_floor_slab_thickness',
                                        'default': 0.1,
                                        'minimum>': 0.0,
                                        'maximum': 0.25,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'dgravxy: width of gravel pit beside basement wall',
                                       {'name': u'DGRAVXY: Width of gravel pit beside basement wall',
                                        'pyname': u'dgravxy_width_of_gravel_pit_beside_basement_wall',
                                        'default': 0.3,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'dgravzn: gravel depth extending above the floor slab',
                                       {'name': u'DGRAVZN: Gravel depth extending above the floor slab',
                                        'pyname': u'dgravzn_gravel_depth_extending_above_the_floor_slab',
                                        'default': 0.2,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'dgravzp: gravel depth below the floor slab',
                                       {'name': u'DGRAVZP: Gravel depth below the floor slab',
                                        'pyname': u'dgravzp_gravel_depth_below_the_floor_slab',
                                        'default': 0.1,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:BldgData',
               'pyname': u'GroundHeatTransferBasementBldgData',
               'required-object': False,
               'unique-object': False}

    @property
    def dwall_wall_thickness(self):
        """field `DWALL: Wall thickness`

        |  Units: m
        |  Default value: 0.2
        |  value >= 0.2

        Args:
            value (float): value for IDD Field `DWALL: Wall thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dwall_wall_thickness` or None if not set
        """
        return self["DWALL: Wall thickness"]

    @dwall_wall_thickness.setter
    def dwall_wall_thickness(self, value=0.2):
        """  Corresponds to IDD field `DWALL: Wall thickness`

        """
        self["DWALL: Wall thickness"] = value

    @property
    def dslab_floor_slab_thickness(self):
        """field `DSLAB: Floor slab thickness`

        |  Units: m
        |  Default value: 0.1
        |  value <= 0.25

        Args:
            value (float): value for IDD Field `DSLAB: Floor slab thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dslab_floor_slab_thickness` or None if not set
        """
        return self["DSLAB: Floor slab thickness"]

    @dslab_floor_slab_thickness.setter
    def dslab_floor_slab_thickness(self, value=0.1):
        """  Corresponds to IDD field `DSLAB: Floor slab thickness`

        """
        self["DSLAB: Floor slab thickness"] = value

    @property
    def dgravxy_width_of_gravel_pit_beside_basement_wall(self):
        """field `DGRAVXY: Width of gravel pit beside basement wall`

        |  Units: m
        |  Default value: 0.3

        Args:
            value (float): value for IDD Field `DGRAVXY: Width of gravel pit beside basement wall`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dgravxy_width_of_gravel_pit_beside_basement_wall` or None if not set
        """
        return self["DGRAVXY: Width of gravel pit beside basement wall"]

    @dgravxy_width_of_gravel_pit_beside_basement_wall.setter
    def dgravxy_width_of_gravel_pit_beside_basement_wall(self, value=0.3):
        """  Corresponds to IDD field `DGRAVXY: Width of gravel pit beside basement wall`

        """
        self["DGRAVXY: Width of gravel pit beside basement wall"] = value

    @property
    def dgravzn_gravel_depth_extending_above_the_floor_slab(self):
        """field `DGRAVZN: Gravel depth extending above the floor slab`

        |  Units: m
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `DGRAVZN: Gravel depth extending above the floor slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dgravzn_gravel_depth_extending_above_the_floor_slab` or None if not set
        """
        return self["DGRAVZN: Gravel depth extending above the floor slab"]

    @dgravzn_gravel_depth_extending_above_the_floor_slab.setter
    def dgravzn_gravel_depth_extending_above_the_floor_slab(self, value=0.2):
        """  Corresponds to IDD field `DGRAVZN: Gravel depth extending above the floor slab`

        """
        self["DGRAVZN: Gravel depth extending above the floor slab"] = value

    @property
    def dgravzp_gravel_depth_below_the_floor_slab(self):
        """field `DGRAVZP: Gravel depth below the floor slab`

        |  Units: m
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `DGRAVZP: Gravel depth below the floor slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dgravzp_gravel_depth_below_the_floor_slab` or None if not set
        """
        return self["DGRAVZP: Gravel depth below the floor slab"]

    @dgravzp_gravel_depth_below_the_floor_slab.setter
    def dgravzp_gravel_depth_below_the_floor_slab(self, value=0.1):
        """  Corresponds to IDD field `DGRAVZP: Gravel depth below the floor slab`

        """
        self["DGRAVZP: Gravel depth below the floor slab"] = value




class GroundHeatTransferBasementInterior(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:Interior`
        Provides the information needed to simulate the inside boundary conditions for
        the Basement preprocessor ground heat transfer simulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'cond: flag: is the basement conditioned?',
                                       {'name': u'COND: Flag: Is the basement conditioned?',
                                        'pyname': u'cond_flag_is_the_basement_conditioned',
                                        'default': u'TRUE',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hin: downward convection only heat transfer coefficient',
                                       {'name': u'HIN: Downward convection only heat transfer coefficient',
                                        'pyname': u'hin_downward_convection_only_heat_transfer_coefficient',
                                        'default': 0.92,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'hin: upward convection only heat transfer coefficient',
                                       {'name': u'HIN: Upward convection only heat transfer coefficient',
                                        'pyname': u'hin_upward_convection_only_heat_transfer_coefficient',
                                        'default': 4.04,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'hin: horizontal convection only heat transfer coefficient',
                                       {'name': u'HIN: Horizontal convection only heat transfer coefficient',
                                        'pyname': u'hin_horizontal_convection_only_heat_transfer_coefficient',
                                        'default': 3.08,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'hin: downward combined (convection and radiation) heat transfer coefficient',
                                       {'name': u'HIN: Downward combined (convection and radiation) heat transfer coefficient',
                                        'pyname': u'hin_downward_combined_convection_and_radiation_heat_transfer_coefficient',
                                        'default': 6.13,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'hin: upward combined (convection and radiation) heat transfer coefficient',
                                       {'name': u'HIN: Upward combined (convection and radiation) heat transfer coefficient',
                                        'pyname': u'hin_upward_combined_convection_and_radiation_heat_transfer_coefficient',
                                        'default': 9.26,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'}),
                                      (u'hin: horizontal combined (convection and radiation) heat transfer coefficient',
                                       {'name': u'HIN: Horizontal combined (convection and radiation) heat transfer coefficient',
                                        'pyname': u'hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient',
                                        'default': 8.29,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/m2-K'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:Interior',
               'pyname': u'GroundHeatTransferBasementInterior',
               'required-object': False,
               'unique-object': False}

    @property
    def cond_flag_is_the_basement_conditioned(self):
        """field `COND: Flag: Is the basement conditioned?`

        |  for EnergyPlus this should be TRUE
        |  Default value: TRUE

        Args:
            value (str): value for IDD Field `COND: Flag: Is the basement conditioned?`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cond_flag_is_the_basement_conditioned` or None if not set
        """
        return self["COND: Flag: Is the basement conditioned?"]

    @cond_flag_is_the_basement_conditioned.setter
    def cond_flag_is_the_basement_conditioned(self, value="TRUE"):
        """  Corresponds to IDD field `COND: Flag: Is the basement conditioned?`

        """
        self["COND: Flag: Is the basement conditioned?"] = value

    @property
    def hin_downward_convection_only_heat_transfer_coefficient(self):
        """field `HIN: Downward convection only heat transfer coefficient`

        |  Units: W/m2-K
        |  Default value: 0.92

        Args:
            value (float): value for IDD Field `HIN: Downward convection only heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_downward_convection_only_heat_transfer_coefficient` or None if not set
        """
        return self["HIN: Downward convection only heat transfer coefficient"]

    @hin_downward_convection_only_heat_transfer_coefficient.setter
    def hin_downward_convection_only_heat_transfer_coefficient(
            self,
            value=0.92):
        """  Corresponds to IDD field `HIN: Downward convection only heat transfer coefficient`

        """
        self["HIN: Downward convection only heat transfer coefficient"] = value

    @property
    def hin_upward_convection_only_heat_transfer_coefficient(self):
        """field `HIN: Upward convection only heat transfer coefficient`

        |  Units: W/m2-K
        |  Default value: 4.04

        Args:
            value (float): value for IDD Field `HIN: Upward convection only heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_upward_convection_only_heat_transfer_coefficient` or None if not set
        """
        return self["HIN: Upward convection only heat transfer coefficient"]

    @hin_upward_convection_only_heat_transfer_coefficient.setter
    def hin_upward_convection_only_heat_transfer_coefficient(self, value=4.04):
        """  Corresponds to IDD field `HIN: Upward convection only heat transfer coefficient`

        """
        self["HIN: Upward convection only heat transfer coefficient"] = value

    @property
    def hin_horizontal_convection_only_heat_transfer_coefficient(self):
        """field `HIN: Horizontal convection only heat transfer coefficient`

        |  Units: W/m2-K
        |  Default value: 3.08

        Args:
            value (float): value for IDD Field `HIN: Horizontal convection only heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_horizontal_convection_only_heat_transfer_coefficient` or None if not set
        """
        return self[
            "HIN: Horizontal convection only heat transfer coefficient"]

    @hin_horizontal_convection_only_heat_transfer_coefficient.setter
    def hin_horizontal_convection_only_heat_transfer_coefficient(
            self,
            value=3.08):
        """  Corresponds to IDD field `HIN: Horizontal convection only heat transfer coefficient`

        """
        self[
            "HIN: Horizontal convection only heat transfer coefficient"] = value

    @property
    def hin_downward_combined_convection_and_radiation_heat_transfer_coefficient(
            self):
        """field `HIN: Downward combined (convection and radiation) heat transfer coefficient`

        |  Units: W/m2-K
        |  Default value: 6.13

        Args:
            value (float): value for IDD Field `HIN: Downward combined (convection and radiation) heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_downward_combined_convection_and_radiation_heat_transfer_coefficient` or None if not set
        """
        return self[
            "HIN: Downward combined (convection and radiation) heat transfer coefficient"]

    @hin_downward_combined_convection_and_radiation_heat_transfer_coefficient.setter
    def hin_downward_combined_convection_and_radiation_heat_transfer_coefficient(
            self,
            value=6.13):
        """  Corresponds to IDD field `HIN: Downward combined (convection and radiation) heat transfer coefficient`

        """
        self[
            "HIN: Downward combined (convection and radiation) heat transfer coefficient"] = value

    @property
    def hin_upward_combined_convection_and_radiation_heat_transfer_coefficient(
            self):
        """field `HIN: Upward combined (convection and radiation) heat transfer coefficient`

        |  Units: W/m2-K
        |  Default value: 9.26

        Args:
            value (float): value for IDD Field `HIN: Upward combined (convection and radiation) heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_upward_combined_convection_and_radiation_heat_transfer_coefficient` or None if not set
        """
        return self[
            "HIN: Upward combined (convection and radiation) heat transfer coefficient"]

    @hin_upward_combined_convection_and_radiation_heat_transfer_coefficient.setter
    def hin_upward_combined_convection_and_radiation_heat_transfer_coefficient(
            self,
            value=9.26):
        """  Corresponds to IDD field `HIN: Upward combined (convection and radiation) heat transfer coefficient`

        """
        self[
            "HIN: Upward combined (convection and radiation) heat transfer coefficient"] = value

    @property
    def hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient(
            self):
        """field `HIN: Horizontal combined (convection and radiation) heat transfer coefficient`

        |  Units: W/m2-K
        |  Default value: 8.29

        Args:
            value (float): value for IDD Field `HIN: Horizontal combined (convection and radiation) heat transfer coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient` or None if not set
        """
        return self[
            "HIN: Horizontal combined (convection and radiation) heat transfer coefficient"]

    @hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient.setter
    def hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient(
            self,
            value=8.29):
        """  Corresponds to IDD field `HIN: Horizontal combined (convection and radiation) heat transfer coefficient`

        """
        self[
            "HIN: Horizontal combined (convection and radiation) heat transfer coefficient"] = value




class GroundHeatTransferBasementComBldg(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:ComBldg`
        ComBldg contains the monthly average temperatures (C) and possibility of daily variation amplitude
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'january average temperature',
                                       {'name': u'January average temperature',
                                        'pyname': u'january_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'february average temperature',
                                       {'name': u'February average temperature',
                                        'pyname': u'february_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'march average temperature',
                                       {'name': u'March average temperature',
                                        'pyname': u'march_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'april average temperature',
                                       {'name': u'April average temperature',
                                        'pyname': u'april_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'may average temperature',
                                       {'name': u'May average temperature',
                                        'pyname': u'may_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'june average temperature',
                                       {'name': u'June average temperature',
                                        'pyname': u'june_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'july average temperature',
                                       {'name': u'July average temperature',
                                        'pyname': u'july_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'august average temperature',
                                       {'name': u'August average temperature',
                                        'pyname': u'august_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'september average temperature',
                                       {'name': u'September average temperature',
                                        'pyname': u'september_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'october average temperature',
                                       {'name': u'October average temperature',
                                        'pyname': u'october_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'november average temperature',
                                       {'name': u'November average temperature',
                                        'pyname': u'november_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'december average temperature',
                                       {'name': u'December average temperature',
                                        'pyname': u'december_average_temperature',
                                        'default': 22.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'daily variation sine wave amplitude',
                                       {'name': u'Daily variation sine wave amplitude',
                                        'pyname': u'daily_variation_sine_wave_amplitude',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:ComBldg',
               'pyname': u'GroundHeatTransferBasementComBldg',
               'required-object': False,
               'unique-object': False}

    @property
    def january_average_temperature(self):
        """field `January average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `January average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `january_average_temperature` or None if not set

        """
        return self["January average temperature"]

    @january_average_temperature.setter
    def january_average_temperature(self, value=22.0):
        """Corresponds to IDD field `January average temperature`"""
        self["January average temperature"] = value

    @property
    def february_average_temperature(self):
        """field `February average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `February average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `february_average_temperature` or None if not set

        """
        return self["February average temperature"]

    @february_average_temperature.setter
    def february_average_temperature(self, value=22.0):
        """Corresponds to IDD field `February average temperature`"""
        self["February average temperature"] = value

    @property
    def march_average_temperature(self):
        """field `March average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `March average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `march_average_temperature` or None if not set

        """
        return self["March average temperature"]

    @march_average_temperature.setter
    def march_average_temperature(self, value=22.0):
        """Corresponds to IDD field `March average temperature`"""
        self["March average temperature"] = value

    @property
    def april_average_temperature(self):
        """field `April average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `April average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `april_average_temperature` or None if not set

        """
        return self["April average temperature"]

    @april_average_temperature.setter
    def april_average_temperature(self, value=22.0):
        """Corresponds to IDD field `April average temperature`"""
        self["April average temperature"] = value

    @property
    def may_average_temperature(self):
        """field `May average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `May average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `may_average_temperature` or None if not set

        """
        return self["May average temperature"]

    @may_average_temperature.setter
    def may_average_temperature(self, value=22.0):
        """Corresponds to IDD field `May average temperature`"""
        self["May average temperature"] = value

    @property
    def june_average_temperature(self):
        """field `June average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `June average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `june_average_temperature` or None if not set

        """
        return self["June average temperature"]

    @june_average_temperature.setter
    def june_average_temperature(self, value=22.0):
        """Corresponds to IDD field `June average temperature`"""
        self["June average temperature"] = value

    @property
    def july_average_temperature(self):
        """field `July average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `July average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `july_average_temperature` or None if not set

        """
        return self["July average temperature"]

    @july_average_temperature.setter
    def july_average_temperature(self, value=22.0):
        """Corresponds to IDD field `July average temperature`"""
        self["July average temperature"] = value

    @property
    def august_average_temperature(self):
        """field `August average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `August average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `august_average_temperature` or None if not set

        """
        return self["August average temperature"]

    @august_average_temperature.setter
    def august_average_temperature(self, value=22.0):
        """Corresponds to IDD field `August average temperature`"""
        self["August average temperature"] = value

    @property
    def september_average_temperature(self):
        """field `September average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `September average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `september_average_temperature` or None if not set

        """
        return self["September average temperature"]

    @september_average_temperature.setter
    def september_average_temperature(self, value=22.0):
        """Corresponds to IDD field `September average temperature`"""
        self["September average temperature"] = value

    @property
    def october_average_temperature(self):
        """field `October average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `October average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `october_average_temperature` or None if not set

        """
        return self["October average temperature"]

    @october_average_temperature.setter
    def october_average_temperature(self, value=22.0):
        """Corresponds to IDD field `October average temperature`"""
        self["October average temperature"] = value

    @property
    def november_average_temperature(self):
        """field `November average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `November average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `november_average_temperature` or None if not set

        """
        return self["November average temperature"]

    @november_average_temperature.setter
    def november_average_temperature(self, value=22.0):
        """Corresponds to IDD field `November average temperature`"""
        self["November average temperature"] = value

    @property
    def december_average_temperature(self):
        """field `December average temperature`

        |  Units: C
        |  Default value: 22.0

        Args:
            value (float): value for IDD Field `December average temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `december_average_temperature` or None if not set

        """
        return self["December average temperature"]

    @december_average_temperature.setter
    def december_average_temperature(self, value=22.0):
        """Corresponds to IDD field `December average temperature`"""
        self["December average temperature"] = value

    @property
    def daily_variation_sine_wave_amplitude(self):
        """field `Daily variation sine wave amplitude`

        |  (Normally zero, just for checking)
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Daily variation sine wave amplitude`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `daily_variation_sine_wave_amplitude` or None if not set

        """
        return self["Daily variation sine wave amplitude"]

    @daily_variation_sine_wave_amplitude.setter
    def daily_variation_sine_wave_amplitude(self, value=None):
        """Corresponds to IDD field `Daily variation sine wave amplitude`"""
        self["Daily variation sine wave amplitude"] = value




class GroundHeatTransferBasementEquivSlab(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:EquivSlab`
        Using an equivalent slab allows non-rectangular shapes to be
        modeled accurately.
        The simulation default should be EquivSizing=True
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'apratio: the area to perimeter ratio for this slab',
                                       {'name': u'APRatio: The area to perimeter ratio for this slab',
                                        'pyname': u'apratio_the_area_to_perimeter_ratio_for_this_slab',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'equivsizing: flag',
                                       {'name': u'EquivSizing: Flag',
                                        'pyname': u'equivsizing_flag',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'TRUE',
                                                            u'FALSE'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:EquivSlab',
               'pyname': u'GroundHeatTransferBasementEquivSlab',
               'required-object': False,
               'unique-object': False}

    @property
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self):
        """field `APRatio: The area to perimeter ratio for this slab`

        |  Units: m

        Args:
            value (float): value for IDD Field `APRatio: The area to perimeter ratio for this slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `apratio_the_area_to_perimeter_ratio_for_this_slab` or None if not set
        """
        return self["APRatio: The area to perimeter ratio for this slab"]

    @apratio_the_area_to_perimeter_ratio_for_this_slab.setter
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self, value=None):
        """  Corresponds to IDD field `APRatio: The area to perimeter ratio for this slab`

        """
        self["APRatio: The area to perimeter ratio for this slab"] = value

    @property
    def equivsizing_flag(self):
        """field `EquivSizing: Flag`

        |  Will the dimensions of an equivalent slab be calculated (TRUE)
        |  or will the dimensions be input directly? (FALSE)]
        |  Only advanced special simulations should use FALSE.

        Args:
            value (str): value for IDD Field `EquivSizing: Flag`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equivsizing_flag` or None if not set
        """
        return self["EquivSizing: Flag"]

    @equivsizing_flag.setter
    def equivsizing_flag(self, value=None):
        """  Corresponds to IDD field `EquivSizing: Flag`

        """
        self["EquivSizing: Flag"] = value




class GroundHeatTransferBasementEquivAutoGrid(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:EquivAutoGrid`
        EquivAutoGrid necessary when EquivSizing=TRUE, TRUE is is the normal case.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'clearance: distance from outside of wall to edge of 3-d ground domain',
                                       {'name': u'CLEARANCE: Distance from outside of wall to edge of 3-D ground domain',
                                        'pyname': u'clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slabdepth: thickness of the floor slab',
                                       {'name': u'SlabDepth: Thickness of the floor slab',
                                        'pyname': u'slabdepth_thickness_of_the_floor_slab',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'basedepth: depth of the basement wall below grade',
                                       {'name': u'BaseDepth: Depth of the basement wall below grade',
                                        'pyname': u'basedepth_depth_of_the_basement_wall_below_grade',
                                        'default': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:EquivAutoGrid',
               'pyname': u'GroundHeatTransferBasementEquivAutoGrid',
               'required-object': False,
               'unique-object': False}

    @property
    def clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain(
            self):
        """field `CLEARANCE: Distance from outside of wall to edge of 3-D ground domain`

        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `CLEARANCE: Distance from outside of wall to edge of 3-D ground domain`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain` or None if not set
        """
        return self[
            "CLEARANCE: Distance from outside of wall to edge of 3-D ground domain"]

    @clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain.setter
    def clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain(
            self,
            value=15.0):
        """  Corresponds to IDD field `CLEARANCE: Distance from outside of wall to edge of 3-D ground domain`

        """
        self[
            "CLEARANCE: Distance from outside of wall to edge of 3-D ground domain"] = value

    @property
    def slabdepth_thickness_of_the_floor_slab(self):
        """field `SlabDepth: Thickness of the floor slab`

        |  Units: m
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `SlabDepth: Thickness of the floor slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slabdepth_thickness_of_the_floor_slab` or None if not set
        """
        return self["SlabDepth: Thickness of the floor slab"]

    @slabdepth_thickness_of_the_floor_slab.setter
    def slabdepth_thickness_of_the_floor_slab(self, value=0.1):
        """  Corresponds to IDD field `SlabDepth: Thickness of the floor slab`

        """
        self["SlabDepth: Thickness of the floor slab"] = value

    @property
    def basedepth_depth_of_the_basement_wall_below_grade(self):
        """field `BaseDepth: Depth of the basement wall below grade`

        |  Units: m
        |  Default value: 2.0

        Args:
            value (float): value for IDD Field `BaseDepth: Depth of the basement wall below grade`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basedepth_depth_of_the_basement_wall_below_grade` or None if not set
        """
        return self["BaseDepth: Depth of the basement wall below grade"]

    @basedepth_depth_of_the_basement_wall_below_grade.setter
    def basedepth_depth_of_the_basement_wall_below_grade(self, value=2.0):
        """  Corresponds to IDD field `BaseDepth: Depth of the basement wall below grade`

        """
        self["BaseDepth: Depth of the basement wall below grade"] = value




class GroundHeatTransferBasementAutoGrid(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:AutoGrid`
        AutoGrid only necessary when EquivSizing is false
        If the modeled building is not a rectangle or square, Equivalent
        sizing MUST be used to get accurate results
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'clearance: distance from outside of wall to edge,',
                                       {'name': u'CLEARANCE: Distance from outside of wall to edge,',
                                        'pyname': u'clearance_distance_from_outside_of_wall_to_edge_',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slabx: x dimension of the building slab',
                                       {'name': u'SLABX: X dimension of the building slab',
                                        'pyname': u'slabx_x_dimension_of_the_building_slab',
                                        'maximum': 60.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slaby: y dimension of the building slab',
                                       {'name': u'SLABY: Y dimension of the building slab',
                                        'pyname': u'slaby_y_dimension_of_the_building_slab',
                                        'maximum': 60.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'concagheight: height of the foundation wall above grade',
                                       {'name': u'ConcAGHeight: Height of the foundation wall above grade',
                                        'pyname': u'concagheight_height_of_the_foundation_wall_above_grade',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'slabdepth: thickness of the floor slab',
                                       {'name': u'SlabDepth: Thickness of the floor slab',
                                        'pyname': u'slabdepth_thickness_of_the_floor_slab',
                                        'default': 0.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'basedepth: depth of the basement wall below grade',
                                       {'name': u'BaseDepth: Depth of the basement wall below grade',
                                        'pyname': u'basedepth_depth_of_the_basement_wall_below_grade',
                                        'default': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:AutoGrid',
               'pyname': u'GroundHeatTransferBasementAutoGrid',
               'required-object': False,
               'unique-object': False}

    @property
    def clearance_distance_from_outside_of_wall_to_edge_(self):
        """field `CLEARANCE: Distance from outside of wall to edge,`

        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `CLEARANCE: Distance from outside of wall to edge,`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `clearance_distance_from_outside_of_wall_to_edge_` or None if not set
        """
        return self["CLEARANCE: Distance from outside of wall to edge,"]

    @clearance_distance_from_outside_of_wall_to_edge_.setter
    def clearance_distance_from_outside_of_wall_to_edge_(self, value=15.0):
        """  Corresponds to IDD field `CLEARANCE: Distance from outside of wall to edge,`

        """
        self["CLEARANCE: Distance from outside of wall to edge,"] = value

    @property
    def slabx_x_dimension_of_the_building_slab(self):
        """field `SLABX: X dimension of the building slab`

        |  Units: m
        |  value <= 60.0

        Args:
            value (float): value for IDD Field `SLABX: X dimension of the building slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slabx_x_dimension_of_the_building_slab` or None if not set
        """
        return self["SLABX: X dimension of the building slab"]

    @slabx_x_dimension_of_the_building_slab.setter
    def slabx_x_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD field `SLABX: X dimension of the building slab`

        """
        self["SLABX: X dimension of the building slab"] = value

    @property
    def slaby_y_dimension_of_the_building_slab(self):
        """field `SLABY: Y dimension of the building slab`

        |  Units: m
        |  value <= 60.0

        Args:
            value (float): value for IDD Field `SLABY: Y dimension of the building slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slaby_y_dimension_of_the_building_slab` or None if not set
        """
        return self["SLABY: Y dimension of the building slab"]

    @slaby_y_dimension_of_the_building_slab.setter
    def slaby_y_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD field `SLABY: Y dimension of the building slab`

        """
        self["SLABY: Y dimension of the building slab"] = value

    @property
    def concagheight_height_of_the_foundation_wall_above_grade(self):
        """field `ConcAGHeight: Height of the foundation wall above grade`

        |  Units: m

        Args:
            value (float): value for IDD Field `ConcAGHeight: Height of the foundation wall above grade`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `concagheight_height_of_the_foundation_wall_above_grade` or None if not set
        """
        return self["ConcAGHeight: Height of the foundation wall above grade"]

    @concagheight_height_of_the_foundation_wall_above_grade.setter
    def concagheight_height_of_the_foundation_wall_above_grade(
            self,
            value=None):
        """  Corresponds to IDD field `ConcAGHeight: Height of the foundation wall above grade`

        """
        self["ConcAGHeight: Height of the foundation wall above grade"] = value

    @property
    def slabdepth_thickness_of_the_floor_slab(self):
        """field `SlabDepth: Thickness of the floor slab`

        |  Units: m
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `SlabDepth: Thickness of the floor slab`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `slabdepth_thickness_of_the_floor_slab` or None if not set
        """
        return self["SlabDepth: Thickness of the floor slab"]

    @slabdepth_thickness_of_the_floor_slab.setter
    def slabdepth_thickness_of_the_floor_slab(self, value=0.1):
        """  Corresponds to IDD field `SlabDepth: Thickness of the floor slab`

        """
        self["SlabDepth: Thickness of the floor slab"] = value

    @property
    def basedepth_depth_of_the_basement_wall_below_grade(self):
        """field `BaseDepth: Depth of the basement wall below grade`

        |  Units: m
        |  Default value: 2.0

        Args:
            value (float): value for IDD Field `BaseDepth: Depth of the basement wall below grade`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basedepth_depth_of_the_basement_wall_below_grade` or None if not set
        """
        return self["BaseDepth: Depth of the basement wall below grade"]

    @basedepth_depth_of_the_basement_wall_below_grade.setter
    def basedepth_depth_of_the_basement_wall_below_grade(self, value=2.0):
        """  Corresponds to IDD field `BaseDepth: Depth of the basement wall below grade`

        """
        self["BaseDepth: Depth of the basement wall below grade"] = value




class GroundHeatTransferBasementManualGrid(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:ManualGrid`
        Manual Grid only necessary using manual gridding (not recommended)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'nx: number of cells in the x direction: 20]',
                                       {'name': u'NX: Number of cells in the X direction: 20]',
                                        'pyname': u'nx_number_of_cells_in_the_x_direction_20',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'ny: number of cells in the y direction: 20]',
                                       {'name': u'NY: Number of cells in the Y direction: 20]',
                                        'pyname': u'ny_number_of_cells_in_the_y_direction_20',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'nzag: number of cells in the z direction. above grade: 4 always]',
                                       {'name': u'NZAG: Number of cells in the Z direction. above grade: 4 Always]',
                                        'pyname': u'nzag_number_of_cells_in_the_z_direction_above_grade_4_always',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'nzbg: number of cells in z direction. below grade: 10-35]',
                                       {'name': u'NZBG: Number of cells in Z direction. below grade: 10-35]',
                                        'pyname': u'nzbg_number_of_cells_in_z_direction_below_grade_1035',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'ibase: x direction cell indicator of slab edge: 5-20]',
                                       {'name': u'IBASE: X direction cell indicator of slab edge: 5-20]',
                                        'pyname': u'ibase_x_direction_cell_indicator_of_slab_edge_520',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'jbase: y direction cell indicator of slab edge: 5-20]',
                                       {'name': u'JBASE: Y direction cell indicator of slab edge: 5-20]',
                                        'pyname': u'jbase_y_direction_cell_indicator_of_slab_edge_520',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'kbase: z direction cell indicator of the top of the floor slab: 5-20]',
                                       {'name': u'KBASE: Z direction cell indicator of the top of the floor slab: 5-20]',
                                        'pyname': u'kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:ManualGrid',
               'pyname': u'GroundHeatTransferBasementManualGrid',
               'required-object': False,
               'unique-object': False}

    @property
    def nx_number_of_cells_in_the_x_direction_20(self):
        """field `NX: Number of cells in the X direction: 20]`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NX: Number of cells in the X direction: 20]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nx_number_of_cells_in_the_x_direction_20` or None if not set
        """
        return self["NX: Number of cells in the X direction: 20]"]

    @nx_number_of_cells_in_the_x_direction_20.setter
    def nx_number_of_cells_in_the_x_direction_20(self, value=None):
        """  Corresponds to IDD field `NX: Number of cells in the X direction: 20]`

        """
        self["NX: Number of cells in the X direction: 20]"] = value

    @property
    def ny_number_of_cells_in_the_y_direction_20(self):
        """field `NY: Number of cells in the Y direction: 20]`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NY: Number of cells in the Y direction: 20]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ny_number_of_cells_in_the_y_direction_20` or None if not set
        """
        return self["NY: Number of cells in the Y direction: 20]"]

    @ny_number_of_cells_in_the_y_direction_20.setter
    def ny_number_of_cells_in_the_y_direction_20(self, value=None):
        """  Corresponds to IDD field `NY: Number of cells in the Y direction: 20]`

        """
        self["NY: Number of cells in the Y direction: 20]"] = value

    @property
    def nzag_number_of_cells_in_the_z_direction_above_grade_4_always(self):
        """field `NZAG: Number of cells in the Z direction. above grade: 4 Always]`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NZAG: Number of cells in the Z direction. above grade: 4 Always]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nzag_number_of_cells_in_the_z_direction_above_grade_4_always` or None if not set
        """
        return self[
            "NZAG: Number of cells in the Z direction. above grade: 4 Always]"]

    @nzag_number_of_cells_in_the_z_direction_above_grade_4_always.setter
    def nzag_number_of_cells_in_the_z_direction_above_grade_4_always(
            self,
            value=None):
        """  Corresponds to IDD field `NZAG: Number of cells in the Z direction. above grade: 4 Always]`

        """
        self[
            "NZAG: Number of cells in the Z direction. above grade: 4 Always]"] = value

    @property
    def nzbg_number_of_cells_in_z_direction_below_grade_1035(self):
        """field `NZBG: Number of cells in Z direction. below grade: 10-35]`

        |  value >= 1.0

        Args:
            value (float): value for IDD Field `NZBG: Number of cells in Z direction. below grade: 10-35]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nzbg_number_of_cells_in_z_direction_below_grade_1035` or None if not set
        """
        return self[
            "NZBG: Number of cells in Z direction. below grade: 10-35]"]

    @nzbg_number_of_cells_in_z_direction_below_grade_1035.setter
    def nzbg_number_of_cells_in_z_direction_below_grade_1035(self, value=None):
        """  Corresponds to IDD field `NZBG: Number of cells in Z direction. below grade: 10-35]`

        """
        self[
            "NZBG: Number of cells in Z direction. below grade: 10-35]"] = value

    @property
    def ibase_x_direction_cell_indicator_of_slab_edge_520(self):
        """field `IBASE: X direction cell indicator of slab edge: 5-20]`


        Args:
            value (float): value for IDD Field `IBASE: X direction cell indicator of slab edge: 5-20]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ibase_x_direction_cell_indicator_of_slab_edge_520` or None if not set
        """
        return self["IBASE: X direction cell indicator of slab edge: 5-20]"]

    @ibase_x_direction_cell_indicator_of_slab_edge_520.setter
    def ibase_x_direction_cell_indicator_of_slab_edge_520(self, value=None):
        """  Corresponds to IDD field `IBASE: X direction cell indicator of slab edge: 5-20]`

        """
        self["IBASE: X direction cell indicator of slab edge: 5-20]"] = value

    @property
    def jbase_y_direction_cell_indicator_of_slab_edge_520(self):
        """field `JBASE: Y direction cell indicator of slab edge: 5-20]`


        Args:
            value (float): value for IDD Field `JBASE: Y direction cell indicator of slab edge: 5-20]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `jbase_y_direction_cell_indicator_of_slab_edge_520` or None if not set
        """
        return self["JBASE: Y direction cell indicator of slab edge: 5-20]"]

    @jbase_y_direction_cell_indicator_of_slab_edge_520.setter
    def jbase_y_direction_cell_indicator_of_slab_edge_520(self, value=None):
        """  Corresponds to IDD field `JBASE: Y direction cell indicator of slab edge: 5-20]`

        """
        self["JBASE: Y direction cell indicator of slab edge: 5-20]"] = value

    @property
    def kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520(
            self):
        """field `KBASE: Z direction cell indicator of the top of the floor slab: 5-20]`


        Args:
            value (float): value for IDD Field `KBASE: Z direction cell indicator of the top of the floor slab: 5-20]`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520` or None if not set
        """
        return self[
            "KBASE: Z direction cell indicator of the top of the floor slab: 5-20]"]

    @kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520.setter
    def kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520(
            self,
            value=None):
        """  Corresponds to IDD field `KBASE: Z direction cell indicator of the top of the floor slab: 5-20]`

        """
        self[
            "KBASE: Z direction cell indicator of the top of the floor slab: 5-20]"] = value




class GroundHeatTransferBasementXface(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:XFACE`
        This is only needed when using manual gridding (not recommended)
        XFACE: X Direction cell face coordinates: m
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:XFACE',
               'pyname': u'GroundHeatTransferBasementXface',
               'required-object': False,
               'unique-object': False}




class GroundHeatTransferBasementYface(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:YFACE`
        This is only needed when using manual gridding (not recommended)
        YFACE: Y Direction cell face coordinates: m
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:YFACE',
               'pyname': u'GroundHeatTransferBasementYface',
               'required-object': False,
               'unique-object': False}




class GroundHeatTransferBasementZface(DataObject):

    """ Corresponds to IDD object `GroundHeatTransfer:Basement:ZFACE`
        This is only needed when using manual gridding (not recommended)
        ZFACE: Z Direction cell face coordinates: m
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Detailed Ground Heat Transfer',
               'min-fields': 0,
               'name': u'GroundHeatTransfer:Basement:ZFACE',
               'pyname': u'GroundHeatTransferBasementZface',
               'required-object': False,
               'unique-object': False}


