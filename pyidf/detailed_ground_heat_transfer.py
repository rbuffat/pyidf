from collections import OrderedDict

class GroundHeatTransferControl(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Control`
        Object determines if the Slab and Basement preprocessors
        are going to be executed.
    
    """
    internal_name = "GroundHeatTransfer:Control"
    field_count = 3
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Control`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Run Basement Preprocessor"] = None
        self._data["Run Slab Preprocessor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.run_basement_preprocessor = None
        else:
            self.run_basement_preprocessor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.run_slab_preprocessor = None
        else:
            self.run_slab_preprocessor = vals[i]
        i += 1
        if i >= len(vals):
            return

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
        This field is included for consistency.11

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def run_basement_preprocessor(self):
        """Get run_basement_preprocessor

        Returns:
            str: the value of `run_basement_preprocessor` or None if not set
        """
        return self._data["Run Basement Preprocessor"]

    @run_basement_preprocessor.setter
    def run_basement_preprocessor(self, value="No"):
        """  Corresponds to IDD Field `run_basement_preprocessor`

        Args:
            value (str): value for IDD Field `run_basement_preprocessor`
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
                                 'for field `run_basement_preprocessor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_basement_preprocessor`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `run_basement_preprocessor`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `run_basement_preprocessor`'.format(value))
            value = vals[value_lower]

        self._data["Run Basement Preprocessor"] = value

    @property
    def run_slab_preprocessor(self):
        """Get run_slab_preprocessor

        Returns:
            str: the value of `run_slab_preprocessor` or None if not set
        """
        return self._data["Run Slab Preprocessor"]

    @run_slab_preprocessor.setter
    def run_slab_preprocessor(self, value="No"):
        """  Corresponds to IDD Field `run_slab_preprocessor`

        Args:
            value (str): value for IDD Field `run_slab_preprocessor`
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
                                 'for field `run_slab_preprocessor`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_slab_preprocessor`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `run_slab_preprocessor`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `run_slab_preprocessor`'.format(value))
            value = vals[value_lower]

        self._data["Run Slab Preprocessor"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabMaterials(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:Materials`
        Object gives an overall description of the slab ground heat transfer model.
    
    """
    internal_name = "GroundHeatTransfer:Slab:Materials"
    field_count = 9
    required_fields = ["NMAT: Number of materials"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:Materials`
        """
        self._data = OrderedDict()
        self._data["NMAT: Number of materials"] = None
        self._data["ALBEDO: Surface Albedo: No Snow"] = None
        self._data["ALBEDO: Surface Albedo: Snow"] = None
        self._data["EPSLW: Surface Emissivity: No Snow"] = None
        self._data["EPSLW: Surface Emissivity: Snow"] = None
        self._data["Z0: Surface Roughness: No Snow"] = None
        self._data["Z0: Surface Roughness: Snow"] = None
        self._data["HIN: Indoor HConv: Downward Flow"] = None
        self._data["HIN: Indoor HConv: Upward"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.nmat_number_of_materials = None
        else:
            self.nmat_number_of_materials = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.albedo_surface_albedo_no_snow = None
        else:
            self.albedo_surface_albedo_no_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.albedo_surface_albedo_snow = None
        else:
            self.albedo_surface_albedo_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.epslw_surface_emissivity_no_snow = None
        else:
            self.epslw_surface_emissivity_no_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.epslw_surface_emissivity_snow = None
        else:
            self.epslw_surface_emissivity_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.z0_surface_roughness_no_snow = None
        else:
            self.z0_surface_roughness_no_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.z0_surface_roughness_snow = None
        else:
            self.z0_surface_roughness_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_indoor_hconv_downward_flow = None
        else:
            self.hin_indoor_hconv_downward_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_indoor_hconv_upward = None
        else:
            self.hin_indoor_hconv_upward = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def nmat_number_of_materials(self):
        """Get nmat_number_of_materials

        Returns:
            float: the value of `nmat_number_of_materials` or None if not set
        """
        return self._data["NMAT: Number of materials"]

    @nmat_number_of_materials.setter
    def nmat_number_of_materials(self, value=None):
        """  Corresponds to IDD Field `nmat_number_of_materials`
        This field specifies the number of different materials that will be used in the model.
        Typically only a ground material and a slab material are used. (2 materials)

        Args:
            value (float): value for IDD Field `nmat_number_of_materials`
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
                                 'for field `nmat_number_of_materials`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nmat_number_of_materials`')

        self._data["NMAT: Number of materials"] = value

    @property
    def albedo_surface_albedo_no_snow(self):
        """Get albedo_surface_albedo_no_snow

        Returns:
            float: the value of `albedo_surface_albedo_no_snow` or None if not set
        """
        return self._data["ALBEDO: Surface Albedo: No Snow"]

    @albedo_surface_albedo_no_snow.setter
    def albedo_surface_albedo_no_snow(self, value=0.16 ):
        """  Corresponds to IDD Field `albedo_surface_albedo_no_snow`
        Two fields specify the albedo value of the surface: first for no snow coverage days;
        second for days with snow coverage. The albedo is the solar reflectivity of the surface,
        and can vary from 0.05 for blacktop to 0.95 for fresh snow.
        Typical values for North America reported by Bahnfleth range from 0.16 to 0.4.

        Args:
            value (float): value for IDD Field `albedo_surface_albedo_no_snow`
                Default value: 0.16
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
                                 'for field `albedo_surface_albedo_no_snow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `albedo_surface_albedo_no_snow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `albedo_surface_albedo_no_snow`')

        self._data["ALBEDO: Surface Albedo: No Snow"] = value

    @property
    def albedo_surface_albedo_snow(self):
        """Get albedo_surface_albedo_snow

        Returns:
            float: the value of `albedo_surface_albedo_snow` or None if not set
        """
        return self._data["ALBEDO: Surface Albedo: Snow"]

    @albedo_surface_albedo_snow.setter
    def albedo_surface_albedo_snow(self, value=0.4 ):
        """  Corresponds to IDD Field `albedo_surface_albedo_snow`

        Args:
            value (float): value for IDD Field `albedo_surface_albedo_snow`
                Default value: 0.4
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
                                 'for field `albedo_surface_albedo_snow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `albedo_surface_albedo_snow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `albedo_surface_albedo_snow`')

        self._data["ALBEDO: Surface Albedo: Snow"] = value

    @property
    def epslw_surface_emissivity_no_snow(self):
        """Get epslw_surface_emissivity_no_snow

        Returns:
            float: the value of `epslw_surface_emissivity_no_snow` or None if not set
        """
        return self._data["EPSLW: Surface Emissivity: No Snow"]

    @epslw_surface_emissivity_no_snow.setter
    def epslw_surface_emissivity_no_snow(self, value=0.94 ):
        """  Corresponds to IDD Field `epslw_surface_emissivity_no_snow`
        EPSLW (No Snow and Snow) specifies the long wavelength (thermal) emissivity of the ground surface.
        primarily important for nighttime radiation to sky.
        typical value .95

        Args:
            value (float): value for IDD Field `epslw_surface_emissivity_no_snow`
                Default value: 0.94
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
                                 'for field `epslw_surface_emissivity_no_snow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `epslw_surface_emissivity_no_snow`')

        self._data["EPSLW: Surface Emissivity: No Snow"] = value

    @property
    def epslw_surface_emissivity_snow(self):
        """Get epslw_surface_emissivity_snow

        Returns:
            float: the value of `epslw_surface_emissivity_snow` or None if not set
        """
        return self._data["EPSLW: Surface Emissivity: Snow"]

    @epslw_surface_emissivity_snow.setter
    def epslw_surface_emissivity_snow(self, value=0.86 ):
        """  Corresponds to IDD Field `epslw_surface_emissivity_snow`

        Args:
            value (float): value for IDD Field `epslw_surface_emissivity_snow`
                Default value: 0.86
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
                                 'for field `epslw_surface_emissivity_snow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `epslw_surface_emissivity_snow`')

        self._data["EPSLW: Surface Emissivity: Snow"] = value

    @property
    def z0_surface_roughness_no_snow(self):
        """Get z0_surface_roughness_no_snow

        Returns:
            float: the value of `z0_surface_roughness_no_snow` or None if not set
        """
        return self._data["Z0: Surface Roughness: No Snow"]

    @z0_surface_roughness_no_snow.setter
    def z0_surface_roughness_no_snow(self, value=0.75 ):
        """  Corresponds to IDD Field `z0_surface_roughness_no_snow`
        fields Z0 (No Snow and Snow) describe the height at which an experimentally velocity profile goes to zero.
        typical value= .75 cm

        Args:
            value (float): value for IDD Field `z0_surface_roughness_no_snow`
                Units: cm
                Default value: 0.75
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
                                 'for field `z0_surface_roughness_no_snow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `z0_surface_roughness_no_snow`')

        self._data["Z0: Surface Roughness: No Snow"] = value

    @property
    def z0_surface_roughness_snow(self):
        """Get z0_surface_roughness_snow

        Returns:
            float: the value of `z0_surface_roughness_snow` or None if not set
        """
        return self._data["Z0: Surface Roughness: Snow"]

    @z0_surface_roughness_snow.setter
    def z0_surface_roughness_snow(self, value=0.25 ):
        """  Corresponds to IDD Field `z0_surface_roughness_snow`
        typical value= .05 cm

        Args:
            value (float): value for IDD Field `z0_surface_roughness_snow`
                Units: cm
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `z0_surface_roughness_snow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `z0_surface_roughness_snow`')

        self._data["Z0: Surface Roughness: Snow"] = value

    @property
    def hin_indoor_hconv_downward_flow(self):
        """Get hin_indoor_hconv_downward_flow

        Returns:
            float: the value of `hin_indoor_hconv_downward_flow` or None if not set
        """
        return self._data["HIN: Indoor HConv: Downward Flow"]

    @hin_indoor_hconv_downward_flow.setter
    def hin_indoor_hconv_downward_flow(self, value=6.13 ):
        """  Corresponds to IDD Field `hin_indoor_hconv_downward_flow`
        These fields specify the combined convective and radiative heat transfer coefficient between
        the slab top inside surface and the room air for the cases where heat is flowing downward,
        and upward. The program toggles between the two if the direction of the heat flux changes.
        Typical values can be found in the ASHRAE Handbook of Fundamentals, but should be
        about 6 W/(m2-K) for downward heat flow and 9 W/(m2-K) for upward heat flow.
        typical value= 4-10

        Args:
            value (float): value for IDD Field `hin_indoor_hconv_downward_flow`
                Units: W/m2-K
                Default value: 6.13
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
                                 'for field `hin_indoor_hconv_downward_flow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_indoor_hconv_downward_flow`')

        self._data["HIN: Indoor HConv: Downward Flow"] = value

    @property
    def hin_indoor_hconv_upward(self):
        """Get hin_indoor_hconv_upward

        Returns:
            float: the value of `hin_indoor_hconv_upward` or None if not set
        """
        return self._data["HIN: Indoor HConv: Upward"]

    @hin_indoor_hconv_upward.setter
    def hin_indoor_hconv_upward(self, value=9.26 ):
        """  Corresponds to IDD Field `hin_indoor_hconv_upward`
        typical value= 4-10

        Args:
            value (float): value for IDD Field `hin_indoor_hconv_upward`
                Units: W/m2-K
                Default value: 9.26
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
                                 'for field `hin_indoor_hconv_upward`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_indoor_hconv_upward`')

        self._data["HIN: Indoor HConv: Upward"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabMatlProps(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:MatlProps`
        This object contains the material properties for the materials
        used in the model. The fields are mostly self explanatory.
    
    """
    internal_name = "GroundHeatTransfer:Slab:MatlProps"
    field_count = 6
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:MatlProps`
        """
        self._data = OrderedDict()
        self._data["RHO: Slab Material density"] = None
        self._data["RHO: Soil Density"] = None
        self._data["CP: Slab CP"] = None
        self._data["CP: Soil CP"] = None
        self._data["TCON: Slab k"] = None
        self._data["TCON: Soil k"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.rho_slab_material_density = None
        else:
            self.rho_slab_material_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rho_soil_density = None
        else:
            self.rho_soil_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cp_slab_cp = None
        else:
            self.cp_slab_cp = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cp_soil_cp = None
        else:
            self.cp_soil_cp = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tcon_slab_k = None
        else:
            self.tcon_slab_k = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tcon_soil_k = None
        else:
            self.tcon_soil_k = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def rho_slab_material_density(self):
        """Get rho_slab_material_density

        Returns:
            float: the value of `rho_slab_material_density` or None if not set
        """
        return self._data["RHO: Slab Material density"]

    @rho_slab_material_density.setter
    def rho_slab_material_density(self, value=2300.0 ):
        """  Corresponds to IDD Field `rho_slab_material_density`
        Density of Slab Material
        typical value= 2300.0

        Args:
            value (float): value for IDD Field `rho_slab_material_density`
                Units: kg/m3
                Default value: 2300.0
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
                                 'for field `rho_slab_material_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rho_slab_material_density`')

        self._data["RHO: Slab Material density"] = value

    @property
    def rho_soil_density(self):
        """Get rho_soil_density

        Returns:
            float: the value of `rho_soil_density` or None if not set
        """
        return self._data["RHO: Soil Density"]

    @rho_soil_density.setter
    def rho_soil_density(self, value=1200.0 ):
        """  Corresponds to IDD Field `rho_soil_density`
        Density of Soil Material
        typical value= 1200.0

        Args:
            value (float): value for IDD Field `rho_soil_density`
                Units: kg/m3
                Default value: 1200.0
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
                                 'for field `rho_soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rho_soil_density`')

        self._data["RHO: Soil Density"] = value

    @property
    def cp_slab_cp(self):
        """Get cp_slab_cp

        Returns:
            float: the value of `cp_slab_cp` or None if not set
        """
        return self._data["CP: Slab CP"]

    @cp_slab_cp.setter
    def cp_slab_cp(self, value=650.0 ):
        """  Corresponds to IDD Field `cp_slab_cp`
        Specific Heat of Slab Material
        typical value=650.0

        Args:
            value (float): value for IDD Field `cp_slab_cp`
                Units: J/kg-K
                Default value: 650.0
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
                                 'for field `cp_slab_cp`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cp_slab_cp`')

        self._data["CP: Slab CP"] = value

    @property
    def cp_soil_cp(self):
        """Get cp_soil_cp

        Returns:
            float: the value of `cp_soil_cp` or None if not set
        """
        return self._data["CP: Soil CP"]

    @cp_soil_cp.setter
    def cp_soil_cp(self, value=1200.0 ):
        """  Corresponds to IDD Field `cp_soil_cp`
        Specific Heat of Soil Material
        typical value= 1200.0

        Args:
            value (float): value for IDD Field `cp_soil_cp`
                Units: J/kg-K
                Default value: 1200.0
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
                                 'for field `cp_soil_cp`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cp_soil_cp`')

        self._data["CP: Soil CP"] = value

    @property
    def tcon_slab_k(self):
        """Get tcon_slab_k

        Returns:
            float: the value of `tcon_slab_k` or None if not set
        """
        return self._data["TCON: Slab k"]

    @tcon_slab_k.setter
    def tcon_slab_k(self, value=0.9 ):
        """  Corresponds to IDD Field `tcon_slab_k`
        Conductivity of Slab Material
        typical value= .9

        Args:
            value (float): value for IDD Field `tcon_slab_k`
                Units: W/m-K
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
                                 'for field `tcon_slab_k`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tcon_slab_k`')

        self._data["TCON: Slab k"] = value

    @property
    def tcon_soil_k(self):
        """Get tcon_soil_k

        Returns:
            float: the value of `tcon_soil_k` or None if not set
        """
        return self._data["TCON: Soil k"]

    @tcon_soil_k.setter
    def tcon_soil_k(self, value=1.0 ):
        """  Corresponds to IDD Field `tcon_soil_k`
        Conductivity of Soil Material
        typical value= 1.0

        Args:
            value (float): value for IDD Field `tcon_soil_k`
                Units: W/m-K
                Default value: 1.0
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
                                 'for field `tcon_soil_k`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tcon_soil_k`')

        self._data["TCON: Soil k"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabBoundConds(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:BoundConds`
        Supplies some of the boundary conditions used in the ground heat transfer calculations.
    
    """
    internal_name = "GroundHeatTransfer:Slab:BoundConds"
    field_count = 5
    required_fields = ["EVTR: Is surface evapotranspiration modeled", "FIXBC: is the lower boundary at a fixed temperature", "USRHflag: Is the ground surface h specified by the user?"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:BoundConds`
        """
        self._data = OrderedDict()
        self._data["EVTR: Is surface evapotranspiration modeled"] = None
        self._data["FIXBC: is the lower boundary at a fixed temperature"] = None
        self._data["TDEEPin"] = None
        self._data["USRHflag: Is the ground surface h specified by the user?"] = None
        self._data["USERH: User specified ground surface heat transfer coefficient"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.evtr_is_surface_evapotranspiration_modeled = None
        else:
            self.evtr_is_surface_evapotranspiration_modeled = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fixbc_is_the_lower_boundary_at_a_fixed_temperature = None
        else:
            self.fixbc_is_the_lower_boundary_at_a_fixed_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tdeepin = None
        else:
            self.tdeepin = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.usrhflag_is_the_ground_surface_h_specified_by_the_user = None
        else:
            self.usrhflag_is_the_ground_surface_h_specified_by_the_user = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.userh_user_specified_ground_surface_heat_transfer_coefficient = None
        else:
            self.userh_user_specified_ground_surface_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def evtr_is_surface_evapotranspiration_modeled(self):
        """Get evtr_is_surface_evapotranspiration_modeled

        Returns:
            str: the value of `evtr_is_surface_evapotranspiration_modeled` or None if not set
        """
        return self._data["EVTR: Is surface evapotranspiration modeled"]

    @evtr_is_surface_evapotranspiration_modeled.setter
    def evtr_is_surface_evapotranspiration_modeled(self, value=None):
        """  Corresponds to IDD Field `evtr_is_surface_evapotranspiration_modeled`
        This field specifies whether or not to use the evapotransporation model.
        The inclusion of evapotransporation in the calculation has the greatest
        effect in warm dry climates, primarily on the ground surface temperature.
        This field can be used to turn the evapotransporation off and on to check
        sensitivity to it.

        Args:
            value (str): value for IDD Field `evtr_is_surface_evapotranspiration_modeled`
                Accepted values are:
                      - TRUE
                      - FALSE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `evtr_is_surface_evapotranspiration_modeled`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `evtr_is_surface_evapotranspiration_modeled`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `evtr_is_surface_evapotranspiration_modeled`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `evtr_is_surface_evapotranspiration_modeled`'.format(value))
            value = vals[value_lower]

        self._data["EVTR: Is surface evapotranspiration modeled"] = value

    @property
    def fixbc_is_the_lower_boundary_at_a_fixed_temperature(self):
        """Get fixbc_is_the_lower_boundary_at_a_fixed_temperature

        Returns:
            str: the value of `fixbc_is_the_lower_boundary_at_a_fixed_temperature` or None if not set
        """
        return self._data["FIXBC: is the lower boundary at a fixed temperature"]

    @fixbc_is_the_lower_boundary_at_a_fixed_temperature.setter
    def fixbc_is_the_lower_boundary_at_a_fixed_temperature(self, value=None):
        """  Corresponds to IDD Field `fixbc_is_the_lower_boundary_at_a_fixed_temperature`
        This field permits using a fixed temperature at the lower surface of the model
        instead of a zero heat flux condition. This change normally has a very small
        effect on the results.
        FALSE selects the zero flux lower boundary condition

        Args:
            value (str): value for IDD Field `fixbc_is_the_lower_boundary_at_a_fixed_temperature`
                Accepted values are:
                      - TRUE
                      - FALSE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fixbc_is_the_lower_boundary_at_a_fixed_temperature`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fixbc_is_the_lower_boundary_at_a_fixed_temperature`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fixbc_is_the_lower_boundary_at_a_fixed_temperature`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `fixbc_is_the_lower_boundary_at_a_fixed_temperature`'.format(value))
            value = vals[value_lower]

        self._data["FIXBC: is the lower boundary at a fixed temperature"] = value

    @property
    def tdeepin(self):
        """Get tdeepin

        Returns:
            float: the value of `tdeepin` or None if not set
        """
        return self._data["TDEEPin"]

    @tdeepin.setter
    def tdeepin(self, value=None):
        """  Corresponds to IDD Field `tdeepin`
        User input lower boundary temperature if FIXBC is TRUE
        Blank for FIXBC FALSE or to use the calculated 1-D deep ground temperature.

        Args:
            value (float): value for IDD Field `tdeepin`
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
                                 'for field `tdeepin`'.format(value))

        self._data["TDEEPin"] = value

    @property
    def usrhflag_is_the_ground_surface_h_specified_by_the_user(self):
        """Get usrhflag_is_the_ground_surface_h_specified_by_the_user

        Returns:
            str: the value of `usrhflag_is_the_ground_surface_h_specified_by_the_user` or None if not set
        """
        return self._data["USRHflag: Is the ground surface h specified by the user?"]

    @usrhflag_is_the_ground_surface_h_specified_by_the_user.setter
    def usrhflag_is_the_ground_surface_h_specified_by_the_user(self, value=None):
        """  Corresponds to IDD Field `usrhflag_is_the_ground_surface_h_specified_by_the_user`
        This field flags the use of a user specified heat transfer coefficient
        on the ground surface. This condition is used primarily for testing.
        For normal runs (USPHflag is FALSE) and the program calculates the heat
        transfer coefficient using the weather conditions.

        Args:
            value (str): value for IDD Field `usrhflag_is_the_ground_surface_h_specified_by_the_user`
                Accepted values are:
                      - TRUE
                      - FALSE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `usrhflag_is_the_ground_surface_h_specified_by_the_user`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `usrhflag_is_the_ground_surface_h_specified_by_the_user`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `usrhflag_is_the_ground_surface_h_specified_by_the_user`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `usrhflag_is_the_ground_surface_h_specified_by_the_user`'.format(value))
            value = vals[value_lower]

        self._data["USRHflag: Is the ground surface h specified by the user?"] = value

    @property
    def userh_user_specified_ground_surface_heat_transfer_coefficient(self):
        """Get userh_user_specified_ground_surface_heat_transfer_coefficient

        Returns:
            float: the value of `userh_user_specified_ground_surface_heat_transfer_coefficient` or None if not set
        """
        return self._data["USERH: User specified ground surface heat transfer coefficient"]

    @userh_user_specified_ground_surface_heat_transfer_coefficient.setter
    def userh_user_specified_ground_surface_heat_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `userh_user_specified_ground_surface_heat_transfer_coefficient`
        Used only if USRHflag is TRUE and the heat transfer coefficient value is
        specified in this field.

        Args:
            value (float): value for IDD Field `userh_user_specified_ground_surface_heat_transfer_coefficient`
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
                                 'for field `userh_user_specified_ground_surface_heat_transfer_coefficient`'.format(value))

        self._data["USERH: User specified ground surface heat transfer coefficient"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabBldgProps(object):
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
    internal_name = "GroundHeatTransfer:Slab:BldgProps"
    field_count = 17
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:BldgProps`
        """
        self._data = OrderedDict()
        self._data["IYRS: Number of years to iterate"] = None
        self._data["Shape: Slab shape"] = None
        self._data["HBLDG: Building height"] = None
        self._data["TIN1: January Indoor Average Temperature Setpoint"] = None
        self._data["TIN2: February Indoor Average Temperature Setpoint"] = None
        self._data["TIN3: March Indoor Average Temperature Setpoint"] = None
        self._data["TIN4: April Indoor Average Temperature Setpoint"] = None
        self._data["TIN5: May Indoor Average Temperature Setpoint"] = None
        self._data["TIN6: June Indoor Average Temperature Setpoint"] = None
        self._data["TIN7: July Indoor Average Temperature Setpoint"] = None
        self._data["TIN8: August Indoor Average Temperature Setpoint"] = None
        self._data["TIN9: September Indoor Average Temperature Setpoint"] = None
        self._data["TIN10: October Indoor Average Temperature Setpoint"] = None
        self._data["TIN11: November Indoor Average Temperature Setpoint"] = None
        self._data["TIN12: December Indoor Average Temperature Setpoint"] = None
        self._data["TINAmp: Daily Indoor sine wave variation amplitude"] = None
        self._data["ConvTol: Convergence Tolerance"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.iyrs_number_of_years_to_iterate = None
        else:
            self.iyrs_number_of_years_to_iterate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shape_slab_shape = None
        else:
            self.shape_slab_shape = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hbldg_building_height = None
        else:
            self.hbldg_building_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin1_january_indoor_average_temperature_setpoint = None
        else:
            self.tin1_january_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin2_february_indoor_average_temperature_setpoint = None
        else:
            self.tin2_february_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin3_march_indoor_average_temperature_setpoint = None
        else:
            self.tin3_march_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin4_april_indoor_average_temperature_setpoint = None
        else:
            self.tin4_april_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin5_may_indoor_average_temperature_setpoint = None
        else:
            self.tin5_may_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin6_june_indoor_average_temperature_setpoint = None
        else:
            self.tin6_june_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin7_july_indoor_average_temperature_setpoint = None
        else:
            self.tin7_july_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin8_august_indoor_average_temperature_setpoint = None
        else:
            self.tin8_august_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin9_september_indoor_average_temperature_setpoint = None
        else:
            self.tin9_september_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin10_october_indoor_average_temperature_setpoint = None
        else:
            self.tin10_october_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin11_november_indoor_average_temperature_setpoint = None
        else:
            self.tin11_november_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tin12_december_indoor_average_temperature_setpoint = None
        else:
            self.tin12_december_indoor_average_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tinamp_daily_indoor_sine_wave_variation_amplitude = None
        else:
            self.tinamp_daily_indoor_sine_wave_variation_amplitude = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convtol_convergence_tolerance = None
        else:
            self.convtol_convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def iyrs_number_of_years_to_iterate(self):
        """Get iyrs_number_of_years_to_iterate

        Returns:
            float: the value of `iyrs_number_of_years_to_iterate` or None if not set
        """
        return self._data["IYRS: Number of years to iterate"]

    @iyrs_number_of_years_to_iterate.setter
    def iyrs_number_of_years_to_iterate(self, value=10.0 ):
        """  Corresponds to IDD Field `iyrs_number_of_years_to_iterate`
        This field specifies the number of years to iterate.
        Either the ground heat transfer calculations come to an
        an annual steady periodic condition by converging to a tolerance
        (see ConvTol field) or it runs for this number of years.
        A ten year maximum is usually sufficient.

        Args:
            value (float): value for IDD Field `iyrs_number_of_years_to_iterate`
                Default value: 10.0
                value >= 1.0
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
                                 'for field `iyrs_number_of_years_to_iterate`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `iyrs_number_of_years_to_iterate`')

        self._data["IYRS: Number of years to iterate"] = value

    @property
    def shape_slab_shape(self):
        """Get shape_slab_shape

        Returns:
            float: the value of `shape_slab_shape` or None if not set
        """
        return self._data["Shape: Slab shape"]

    @shape_slab_shape.setter
    def shape_slab_shape(self, value=None):
        """  Corresponds to IDD Field `shape_slab_shape`
        Use only the value 0 here. Only a rectangular shape is implemented.

        Args:
            value (float): value for IDD Field `shape_slab_shape`
                value >= 0.0
                value <= 0.0
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
                                 'for field `shape_slab_shape`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shape_slab_shape`')
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `shape_slab_shape`')

        self._data["Shape: Slab shape"] = value

    @property
    def hbldg_building_height(self):
        """Get hbldg_building_height

        Returns:
            float: the value of `hbldg_building_height` or None if not set
        """
        return self._data["HBLDG: Building height"]

    @hbldg_building_height.setter
    def hbldg_building_height(self, value=None):
        """  Corresponds to IDD Field `hbldg_building_height`
        This field supplies the building height. This is used to calculate
        the building shadowing on the ground.
        typical value= 0-20

        Args:
            value (float): value for IDD Field `hbldg_building_height`
                Units: m
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
                                 'for field `hbldg_building_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `hbldg_building_height`')

        self._data["HBLDG: Building height"] = value

    @property
    def tin1_january_indoor_average_temperature_setpoint(self):
        """Get tin1_january_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin1_january_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN1: January Indoor Average Temperature Setpoint"]

    @tin1_january_indoor_average_temperature_setpoint.setter
    def tin1_january_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin1_january_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin1_january_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin1_january_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN1: January Indoor Average Temperature Setpoint"] = value

    @property
    def tin2_february_indoor_average_temperature_setpoint(self):
        """Get tin2_february_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin2_february_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN2: February Indoor Average Temperature Setpoint"]

    @tin2_february_indoor_average_temperature_setpoint.setter
    def tin2_february_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin2_february_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin2_february_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin2_february_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN2: February Indoor Average Temperature Setpoint"] = value

    @property
    def tin3_march_indoor_average_temperature_setpoint(self):
        """Get tin3_march_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin3_march_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN3: March Indoor Average Temperature Setpoint"]

    @tin3_march_indoor_average_temperature_setpoint.setter
    def tin3_march_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin3_march_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin3_march_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin3_march_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN3: March Indoor Average Temperature Setpoint"] = value

    @property
    def tin4_april_indoor_average_temperature_setpoint(self):
        """Get tin4_april_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin4_april_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN4: April Indoor Average Temperature Setpoint"]

    @tin4_april_indoor_average_temperature_setpoint.setter
    def tin4_april_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin4_april_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin4_april_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin4_april_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN4: April Indoor Average Temperature Setpoint"] = value

    @property
    def tin5_may_indoor_average_temperature_setpoint(self):
        """Get tin5_may_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin5_may_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN5: May Indoor Average Temperature Setpoint"]

    @tin5_may_indoor_average_temperature_setpoint.setter
    def tin5_may_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin5_may_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin5_may_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin5_may_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN5: May Indoor Average Temperature Setpoint"] = value

    @property
    def tin6_june_indoor_average_temperature_setpoint(self):
        """Get tin6_june_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin6_june_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN6: June Indoor Average Temperature Setpoint"]

    @tin6_june_indoor_average_temperature_setpoint.setter
    def tin6_june_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin6_june_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin6_june_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin6_june_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN6: June Indoor Average Temperature Setpoint"] = value

    @property
    def tin7_july_indoor_average_temperature_setpoint(self):
        """Get tin7_july_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin7_july_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN7: July Indoor Average Temperature Setpoint"]

    @tin7_july_indoor_average_temperature_setpoint.setter
    def tin7_july_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin7_july_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin7_july_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin7_july_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN7: July Indoor Average Temperature Setpoint"] = value

    @property
    def tin8_august_indoor_average_temperature_setpoint(self):
        """Get tin8_august_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin8_august_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN8: August Indoor Average Temperature Setpoint"]

    @tin8_august_indoor_average_temperature_setpoint.setter
    def tin8_august_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin8_august_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin8_august_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin8_august_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN8: August Indoor Average Temperature Setpoint"] = value

    @property
    def tin9_september_indoor_average_temperature_setpoint(self):
        """Get tin9_september_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin9_september_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN9: September Indoor Average Temperature Setpoint"]

    @tin9_september_indoor_average_temperature_setpoint.setter
    def tin9_september_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin9_september_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin9_september_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin9_september_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN9: September Indoor Average Temperature Setpoint"] = value

    @property
    def tin10_october_indoor_average_temperature_setpoint(self):
        """Get tin10_october_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin10_october_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN10: October Indoor Average Temperature Setpoint"]

    @tin10_october_indoor_average_temperature_setpoint.setter
    def tin10_october_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin10_october_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin10_october_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin10_october_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN10: October Indoor Average Temperature Setpoint"] = value

    @property
    def tin11_november_indoor_average_temperature_setpoint(self):
        """Get tin11_november_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin11_november_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN11: November Indoor Average Temperature Setpoint"]

    @tin11_november_indoor_average_temperature_setpoint.setter
    def tin11_november_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin11_november_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin11_november_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin11_november_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN11: November Indoor Average Temperature Setpoint"] = value

    @property
    def tin12_december_indoor_average_temperature_setpoint(self):
        """Get tin12_december_indoor_average_temperature_setpoint

        Returns:
            float: the value of `tin12_december_indoor_average_temperature_setpoint` or None if not set
        """
        return self._data["TIN12: December Indoor Average Temperature Setpoint"]

    @tin12_december_indoor_average_temperature_setpoint.setter
    def tin12_december_indoor_average_temperature_setpoint(self, value=22.0 ):
        """  Corresponds to IDD Field `tin12_december_indoor_average_temperature_setpoint`
        see memo on object for more information

        Args:
            value (float): value for IDD Field `tin12_december_indoor_average_temperature_setpoint`
                Units: C
                Default value: 22.0
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
                                 'for field `tin12_december_indoor_average_temperature_setpoint`'.format(value))

        self._data["TIN12: December Indoor Average Temperature Setpoint"] = value

    @property
    def tinamp_daily_indoor_sine_wave_variation_amplitude(self):
        """Get tinamp_daily_indoor_sine_wave_variation_amplitude

        Returns:
            float: the value of `tinamp_daily_indoor_sine_wave_variation_amplitude` or None if not set
        """
        return self._data["TINAmp: Daily Indoor sine wave variation amplitude"]

    @tinamp_daily_indoor_sine_wave_variation_amplitude.setter
    def tinamp_daily_indoor_sine_wave_variation_amplitude(self, value=0.0 ):
        """  Corresponds to IDD Field `tinamp_daily_indoor_sine_wave_variation_amplitude`
        This field permits imposing a daily sinusoidal variation
        in the indoor setpoint temperature to simulate the effect
        of a setback profile.
        The value specified is the amplitude of the sine wave.

        Args:
            value (float): value for IDD Field `tinamp_daily_indoor_sine_wave_variation_amplitude`
                Units: deltaC
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
                                 'for field `tinamp_daily_indoor_sine_wave_variation_amplitude`'.format(value))

        self._data["TINAmp: Daily Indoor sine wave variation amplitude"] = value

    @property
    def convtol_convergence_tolerance(self):
        """Get convtol_convergence_tolerance

        Returns:
            float: the value of `convtol_convergence_tolerance` or None if not set
        """
        return self._data["ConvTol: Convergence Tolerance"]

    @convtol_convergence_tolerance.setter
    def convtol_convergence_tolerance(self, value=0.1 ):
        """  Corresponds to IDD Field `convtol_convergence_tolerance`
        This field specifies the convergence tolerance used to
        control the iteration. When the temperature change of all nodes
        is less than the convergence value, iteration ceases.

        Args:
            value (float): value for IDD Field `convtol_convergence_tolerance`
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
                                 'for field `convtol_convergence_tolerance`'.format(value))

        self._data["ConvTol: Convergence Tolerance"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabInsulation(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:Insulation`
        This object supplies the information about insulation used around the slab.
        There are two possible configurations: under the slab or vertical insulation
        around the slab.
    
    """
    internal_name = "GroundHeatTransfer:Slab:Insulation"
    field_count = 5
    required_fields = ["IVINS: Flag: Is there vertical insulation"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:Insulation`
        """
        self._data = OrderedDict()
        self._data["RINS: R value of under slab insulation"] = None
        self._data["DINS: Width of strip of under slab insulation"] = None
        self._data["RVINS: R value of vertical insulation"] = None
        self._data["ZVINS: Depth of vertical insulation"] = None
        self._data["IVINS: Flag: Is there vertical insulation"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.rins_r_value_of_under_slab_insulation = None
        else:
            self.rins_r_value_of_under_slab_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dins_width_of_strip_of_under_slab_insulation = None
        else:
            self.dins_width_of_strip_of_under_slab_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rvins_r_value_of_vertical_insulation = None
        else:
            self.rvins_r_value_of_vertical_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zvins_depth_of_vertical_insulation = None
        else:
            self.zvins_depth_of_vertical_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ivins_flag_is_there_vertical_insulation = None
        else:
            self.ivins_flag_is_there_vertical_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def rins_r_value_of_under_slab_insulation(self):
        """Get rins_r_value_of_under_slab_insulation

        Returns:
            float: the value of `rins_r_value_of_under_slab_insulation` or None if not set
        """
        return self._data["RINS: R value of under slab insulation"]

    @rins_r_value_of_under_slab_insulation.setter
    def rins_r_value_of_under_slab_insulation(self, value=0.0 ):
        """  Corresponds to IDD Field `rins_r_value_of_under_slab_insulation`
        This field provides the thermal resistance value
        of the under slab insulation. It should be zero
        if the vertical insulation configuration is selected.
        typical value= 0-2.0

        Args:
            value (float): value for IDD Field `rins_r_value_of_under_slab_insulation`
                Units: m2-K/W
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
                                 'for field `rins_r_value_of_under_slab_insulation`'.format(value))

        self._data["RINS: R value of under slab insulation"] = value

    @property
    def dins_width_of_strip_of_under_slab_insulation(self):
        """Get dins_width_of_strip_of_under_slab_insulation

        Returns:
            float: the value of `dins_width_of_strip_of_under_slab_insulation` or None if not set
        """
        return self._data["DINS: Width of strip of under slab insulation"]

    @dins_width_of_strip_of_under_slab_insulation.setter
    def dins_width_of_strip_of_under_slab_insulation(self, value=0.0 ):
        """  Corresponds to IDD Field `dins_width_of_strip_of_under_slab_insulation`
        This specifies the width of the perimeter strip of insulation
        under the slab. It should be zero if for the vertical insulation
        configuration is selected.
        typical value= 0-2.0

        Args:
            value (float): value for IDD Field `dins_width_of_strip_of_under_slab_insulation`
                Units: m
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
                                 'for field `dins_width_of_strip_of_under_slab_insulation`'.format(value))

        self._data["DINS: Width of strip of under slab insulation"] = value

    @property
    def rvins_r_value_of_vertical_insulation(self):
        """Get rvins_r_value_of_vertical_insulation

        Returns:
            float: the value of `rvins_r_value_of_vertical_insulation` or None if not set
        """
        return self._data["RVINS: R value of vertical insulation"]

    @rvins_r_value_of_vertical_insulation.setter
    def rvins_r_value_of_vertical_insulation(self, value=0.0 ):
        """  Corresponds to IDD Field `rvins_r_value_of_vertical_insulation`
        This field specifies the thermal resistance of the vertical
        insulation. It should be zero if the under slab insulation
        configuration is selected.
        typical value= 0-3.0

        Args:
            value (float): value for IDD Field `rvins_r_value_of_vertical_insulation`
                Units: m2-K/W
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
                                 'for field `rvins_r_value_of_vertical_insulation`'.format(value))

        self._data["RVINS: R value of vertical insulation"] = value

    @property
    def zvins_depth_of_vertical_insulation(self):
        """Get zvins_depth_of_vertical_insulation

        Returns:
            float: the value of `zvins_depth_of_vertical_insulation` or None if not set
        """
        return self._data["ZVINS: Depth of vertical insulation"]

    @zvins_depth_of_vertical_insulation.setter
    def zvins_depth_of_vertical_insulation(self, value=0.0 ):
        """  Corresponds to IDD Field `zvins_depth_of_vertical_insulation`
        This field specifies the depth of the vertical insulation
        into the ground in meters. It starts at the slab upper surface
        and extends into the ground.
        It should be zero if the under slab insulation
        configuration is selected.
        only use values= .2 .4 .6 .8 1.0 1.5 2.0 2.5 3.0

        Args:
            value (float): value for IDD Field `zvins_depth_of_vertical_insulation`
                Units: m
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
                                 'for field `zvins_depth_of_vertical_insulation`'.format(value))

        self._data["ZVINS: Depth of vertical insulation"] = value

    @property
    def ivins_flag_is_there_vertical_insulation(self):
        """Get ivins_flag_is_there_vertical_insulation

        Returns:
            str: the value of `ivins_flag_is_there_vertical_insulation` or None if not set
        """
        return self._data["IVINS: Flag: Is there vertical insulation"]

    @ivins_flag_is_there_vertical_insulation.setter
    def ivins_flag_is_there_vertical_insulation(self, value="0"):
        """  Corresponds to IDD Field `ivins_flag_is_there_vertical_insulation`
        Specifies if the vertical insulation configuration is being used.
        values: 1=yes vertical insulation 0=no underslab insulation

        Args:
            value (str): value for IDD Field `ivins_flag_is_there_vertical_insulation`
                Accepted values are:
                      - 0
                      - 1
                Default value: 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ivins_flag_is_there_vertical_insulation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ivins_flag_is_there_vertical_insulation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ivins_flag_is_there_vertical_insulation`')
            vals = {}
            vals["0"] = "0"
            vals["1"] = "1"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ivins_flag_is_there_vertical_insulation`'.format(value))
            value = vals[value_lower]

        self._data["IVINS: Flag: Is there vertical insulation"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabEquivalentSlab(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:EquivalentSlab`
        Using an equivalent slab allows non-rectangular shapes to be modeled accurately.
        Object uses the area - perimeter (area/perimeter) ratio to determine the
        size of an equivalent rectangular slab.
        EnergyPlus users normally use this option.
    
    """
    internal_name = "GroundHeatTransfer:Slab:EquivalentSlab"
    field_count = 4
    required_fields = ["APRatio: The area to perimeter ratio for this slab"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:EquivalentSlab`
        """
        self._data = OrderedDict()
        self._data["APRatio: The area to perimeter ratio for this slab"] = None
        self._data["SLABDEPTH: Thickness of slab on grade"] = None
        self._data["CLEARANCE: Distance from edge of slab to domain edge"] = None
        self._data["ZCLEARANCE: Distance from bottom of slab to domain bottom"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.apratio_the_area_to_perimeter_ratio_for_this_slab = None
        else:
            self.apratio_the_area_to_perimeter_ratio_for_this_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slabdepth_thickness_of_slab_on_grade = None
        else:
            self.slabdepth_thickness_of_slab_on_grade = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.clearance_distance_from_edge_of_slab_to_domain_edge = None
        else:
            self.clearance_distance_from_edge_of_slab_to_domain_edge = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zclearance_distance_from_bottom_of_slab_to_domain_bottom = None
        else:
            self.zclearance_distance_from_bottom_of_slab_to_domain_bottom = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self):
        """Get apratio_the_area_to_perimeter_ratio_for_this_slab

        Returns:
            float: the value of `apratio_the_area_to_perimeter_ratio_for_this_slab` or None if not set
        """
        return self._data["APRatio: The area to perimeter ratio for this slab"]

    @apratio_the_area_to_perimeter_ratio_for_this_slab.setter
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self, value=None):
        """  Corresponds to IDD Field `apratio_the_area_to_perimeter_ratio_for_this_slab`
        Equivalent square slab is simulated,  side is 4*APRatio.

        Args:
            value (float): value for IDD Field `apratio_the_area_to_perimeter_ratio_for_this_slab`
                Units: m
                value >= 1.5
                value <= 22.0
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
                                 'for field `apratio_the_area_to_perimeter_ratio_for_this_slab`'.format(value))
            if value < 1.5:
                raise ValueError('value need to be greater or equal 1.5 '
                                 'for field `apratio_the_area_to_perimeter_ratio_for_this_slab`')
            if value > 22.0:
                raise ValueError('value need to be smaller 22.0 '
                                 'for field `apratio_the_area_to_perimeter_ratio_for_this_slab`')

        self._data["APRatio: The area to perimeter ratio for this slab"] = value

    @property
    def slabdepth_thickness_of_slab_on_grade(self):
        """Get slabdepth_thickness_of_slab_on_grade

        Returns:
            float: the value of `slabdepth_thickness_of_slab_on_grade` or None if not set
        """
        return self._data["SLABDEPTH: Thickness of slab on grade"]

    @slabdepth_thickness_of_slab_on_grade.setter
    def slabdepth_thickness_of_slab_on_grade(self, value=0.1 ):
        """  Corresponds to IDD Field `slabdepth_thickness_of_slab_on_grade`
        This field specifies the thickness of the slab. The slab top surface is level
        with the ground surface, so this is the depth into the ground.
        The slab depth has a significant effect on the temperature calculation,
        and it is also important for the auto-grid process.
        The finite difference grids are set in such a way that they use the slab thickness
        to determine the vertical grid spacing. Autogridding will fail if the slab thickness
        is specified larger than 0.25 meters.

        Args:
            value (float): value for IDD Field `slabdepth_thickness_of_slab_on_grade`
                Units: m
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
                                 'for field `slabdepth_thickness_of_slab_on_grade`'.format(value))

        self._data["SLABDEPTH: Thickness of slab on grade"] = value

    @property
    def clearance_distance_from_edge_of_slab_to_domain_edge(self):
        """Get clearance_distance_from_edge_of_slab_to_domain_edge

        Returns:
            float: the value of `clearance_distance_from_edge_of_slab_to_domain_edge` or None if not set
        """
        return self._data["CLEARANCE: Distance from edge of slab to domain edge"]

    @clearance_distance_from_edge_of_slab_to_domain_edge.setter
    def clearance_distance_from_edge_of_slab_to_domain_edge(self, value=15.0 ):
        """  Corresponds to IDD Field `clearance_distance_from_edge_of_slab_to_domain_edge`
        This field specifies the distance from the slab to the edge of
        the area that will be modeled with the grid system. It is the basic size
        dimension that is used to set the horizontal extent of the domain.
        15 meters is a reasonable value.

        Args:
            value (float): value for IDD Field `clearance_distance_from_edge_of_slab_to_domain_edge`
                Units: m
                Default value: 15.0
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
                                 'for field `clearance_distance_from_edge_of_slab_to_domain_edge`'.format(value))

        self._data["CLEARANCE: Distance from edge of slab to domain edge"] = value

    @property
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(self):
        """Get zclearance_distance_from_bottom_of_slab_to_domain_bottom

        Returns:
            float: the value of `zclearance_distance_from_bottom_of_slab_to_domain_bottom` or None if not set
        """
        return self._data["ZCLEARANCE: Distance from bottom of slab to domain bottom"]

    @zclearance_distance_from_bottom_of_slab_to_domain_bottom.setter
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(self, value=15.0 ):
        """  Corresponds to IDD Field `zclearance_distance_from_bottom_of_slab_to_domain_bottom`
        This field specifies the vertical distance from the slab to the
        bottom edge of the area that will be modeled with the grid system.
        15 meters is a reasonable value.

        Args:
            value (float): value for IDD Field `zclearance_distance_from_bottom_of_slab_to_domain_bottom`
                Units: m
                Default value: 15.0
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
                                 'for field `zclearance_distance_from_bottom_of_slab_to_domain_bottom`'.format(value))

        self._data["ZCLEARANCE: Distance from bottom of slab to domain bottom"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabAutoGrid(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:AutoGrid`
        AutoGrid only necessary when EquivalentSlab option not chosen.
        Not normally needed by EnergyPlus users.
        This object permits user selection of rectangular slab dimensions.
        NO SLAB DIMENSIONS LESS THAN 6 m.
    
    """
    internal_name = "GroundHeatTransfer:Slab:AutoGrid"
    field_count = 5
    required_fields = ["SLABX: X dimension of the building slab", "SLABY: Y dimension of the building slab"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:AutoGrid`
        """
        self._data = OrderedDict()
        self._data["SLABX: X dimension of the building slab"] = None
        self._data["SLABY: Y dimension of the building slab"] = None
        self._data["SLABDEPTH: Thickness of slab on grade"] = None
        self._data["CLEARANCE: Distance from edge of slab to domain edge"] = None
        self._data["ZCLEARANCE: Distance from bottom of slab to domain bottom"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.slabx_x_dimension_of_the_building_slab = None
        else:
            self.slabx_x_dimension_of_the_building_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slaby_y_dimension_of_the_building_slab = None
        else:
            self.slaby_y_dimension_of_the_building_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slabdepth_thickness_of_slab_on_grade = None
        else:
            self.slabdepth_thickness_of_slab_on_grade = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.clearance_distance_from_edge_of_slab_to_domain_edge = None
        else:
            self.clearance_distance_from_edge_of_slab_to_domain_edge = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zclearance_distance_from_bottom_of_slab_to_domain_bottom = None
        else:
            self.zclearance_distance_from_bottom_of_slab_to_domain_bottom = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def slabx_x_dimension_of_the_building_slab(self):
        """Get slabx_x_dimension_of_the_building_slab

        Returns:
            float: the value of `slabx_x_dimension_of_the_building_slab` or None if not set
        """
        return self._data["SLABX: X dimension of the building slab"]

    @slabx_x_dimension_of_the_building_slab.setter
    def slabx_x_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD Field `slabx_x_dimension_of_the_building_slab`
        typical values= 6 to 60.0

        Args:
            value (float): value for IDD Field `slabx_x_dimension_of_the_building_slab`
                Units: m
                value >= 6.0
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
                                 'for field `slabx_x_dimension_of_the_building_slab`'.format(value))
            if value < 6.0:
                raise ValueError('value need to be greater or equal 6.0 '
                                 'for field `slabx_x_dimension_of_the_building_slab`')

        self._data["SLABX: X dimension of the building slab"] = value

    @property
    def slaby_y_dimension_of_the_building_slab(self):
        """Get slaby_y_dimension_of_the_building_slab

        Returns:
            float: the value of `slaby_y_dimension_of_the_building_slab` or None if not set
        """
        return self._data["SLABY: Y dimension of the building slab"]

    @slaby_y_dimension_of_the_building_slab.setter
    def slaby_y_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD Field `slaby_y_dimension_of_the_building_slab`
        typical values= 6 to 60.0

        Args:
            value (float): value for IDD Field `slaby_y_dimension_of_the_building_slab`
                Units: m
                value >= 6.0
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
                                 'for field `slaby_y_dimension_of_the_building_slab`'.format(value))
            if value < 6.0:
                raise ValueError('value need to be greater or equal 6.0 '
                                 'for field `slaby_y_dimension_of_the_building_slab`')

        self._data["SLABY: Y dimension of the building slab"] = value

    @property
    def slabdepth_thickness_of_slab_on_grade(self):
        """Get slabdepth_thickness_of_slab_on_grade

        Returns:
            float: the value of `slabdepth_thickness_of_slab_on_grade` or None if not set
        """
        return self._data["SLABDEPTH: Thickness of slab on grade"]

    @slabdepth_thickness_of_slab_on_grade.setter
    def slabdepth_thickness_of_slab_on_grade(self, value=0.1 ):
        """  Corresponds to IDD Field `slabdepth_thickness_of_slab_on_grade`

        Args:
            value (float): value for IDD Field `slabdepth_thickness_of_slab_on_grade`
                Units: m
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
                                 'for field `slabdepth_thickness_of_slab_on_grade`'.format(value))

        self._data["SLABDEPTH: Thickness of slab on grade"] = value

    @property
    def clearance_distance_from_edge_of_slab_to_domain_edge(self):
        """Get clearance_distance_from_edge_of_slab_to_domain_edge

        Returns:
            float: the value of `clearance_distance_from_edge_of_slab_to_domain_edge` or None if not set
        """
        return self._data["CLEARANCE: Distance from edge of slab to domain edge"]

    @clearance_distance_from_edge_of_slab_to_domain_edge.setter
    def clearance_distance_from_edge_of_slab_to_domain_edge(self, value=15.0 ):
        """  Corresponds to IDD Field `clearance_distance_from_edge_of_slab_to_domain_edge`

        Args:
            value (float): value for IDD Field `clearance_distance_from_edge_of_slab_to_domain_edge`
                Units: m
                Default value: 15.0
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
                                 'for field `clearance_distance_from_edge_of_slab_to_domain_edge`'.format(value))

        self._data["CLEARANCE: Distance from edge of slab to domain edge"] = value

    @property
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(self):
        """Get zclearance_distance_from_bottom_of_slab_to_domain_bottom

        Returns:
            float: the value of `zclearance_distance_from_bottom_of_slab_to_domain_bottom` or None if not set
        """
        return self._data["ZCLEARANCE: Distance from bottom of slab to domain bottom"]

    @zclearance_distance_from_bottom_of_slab_to_domain_bottom.setter
    def zclearance_distance_from_bottom_of_slab_to_domain_bottom(self, value=15.0 ):
        """  Corresponds to IDD Field `zclearance_distance_from_bottom_of_slab_to_domain_bottom`

        Args:
            value (float): value for IDD Field `zclearance_distance_from_bottom_of_slab_to_domain_bottom`
                Units: m
                Default value: 15.0
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
                                 'for field `zclearance_distance_from_bottom_of_slab_to_domain_bottom`'.format(value))

        self._data["ZCLEARANCE: Distance from bottom of slab to domain bottom"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferSlabManualGrid(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Slab:ManualGrid`
        Manual Grid only necessary when using manual gridding (not recommended)
        Used only in special cases when previous two objects are not used.
        User must input complete gridding information.
    
    """
    internal_name = "GroundHeatTransfer:Slab:ManualGrid"
    field_count = 5
    required_fields = ["NX: Number of cells in the X direction", "NY: Number of cells in the Y direction", "NZ: Number of cells in the Z direction", "IBOX: X direction cell indicator of slab edge", "JBOX: Y direction cell indicator of slab edge"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Slab:ManualGrid`
        """
        self._data = OrderedDict()
        self._data["NX: Number of cells in the X direction"] = None
        self._data["NY: Number of cells in the Y direction"] = None
        self._data["NZ: Number of cells in the Z direction"] = None
        self._data["IBOX: X direction cell indicator of slab edge"] = None
        self._data["JBOX: Y direction cell indicator of slab edge"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.nx_number_of_cells_in_the_x_direction = None
        else:
            self.nx_number_of_cells_in_the_x_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ny_number_of_cells_in_the_y_direction = None
        else:
            self.ny_number_of_cells_in_the_y_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nz_number_of_cells_in_the_z_direction = None
        else:
            self.nz_number_of_cells_in_the_z_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ibox_x_direction_cell_indicator_of_slab_edge = None
        else:
            self.ibox_x_direction_cell_indicator_of_slab_edge = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.jbox_y_direction_cell_indicator_of_slab_edge = None
        else:
            self.jbox_y_direction_cell_indicator_of_slab_edge = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def nx_number_of_cells_in_the_x_direction(self):
        """Get nx_number_of_cells_in_the_x_direction

        Returns:
            float: the value of `nx_number_of_cells_in_the_x_direction` or None if not set
        """
        return self._data["NX: Number of cells in the X direction"]

    @nx_number_of_cells_in_the_x_direction.setter
    def nx_number_of_cells_in_the_x_direction(self, value=None):
        """  Corresponds to IDD Field `nx_number_of_cells_in_the_x_direction`

        Args:
            value (float): value for IDD Field `nx_number_of_cells_in_the_x_direction`
                value >= 1.0
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
                                 'for field `nx_number_of_cells_in_the_x_direction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `nx_number_of_cells_in_the_x_direction`')

        self._data["NX: Number of cells in the X direction"] = value

    @property
    def ny_number_of_cells_in_the_y_direction(self):
        """Get ny_number_of_cells_in_the_y_direction

        Returns:
            float: the value of `ny_number_of_cells_in_the_y_direction` or None if not set
        """
        return self._data["NY: Number of cells in the Y direction"]

    @ny_number_of_cells_in_the_y_direction.setter
    def ny_number_of_cells_in_the_y_direction(self, value=None):
        """  Corresponds to IDD Field `ny_number_of_cells_in_the_y_direction`

        Args:
            value (float): value for IDD Field `ny_number_of_cells_in_the_y_direction`
                value >= 1.0
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
                                 'for field `ny_number_of_cells_in_the_y_direction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `ny_number_of_cells_in_the_y_direction`')

        self._data["NY: Number of cells in the Y direction"] = value

    @property
    def nz_number_of_cells_in_the_z_direction(self):
        """Get nz_number_of_cells_in_the_z_direction

        Returns:
            float: the value of `nz_number_of_cells_in_the_z_direction` or None if not set
        """
        return self._data["NZ: Number of cells in the Z direction"]

    @nz_number_of_cells_in_the_z_direction.setter
    def nz_number_of_cells_in_the_z_direction(self, value=None):
        """  Corresponds to IDD Field `nz_number_of_cells_in_the_z_direction`

        Args:
            value (float): value for IDD Field `nz_number_of_cells_in_the_z_direction`
                value >= 1.0
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
                                 'for field `nz_number_of_cells_in_the_z_direction`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `nz_number_of_cells_in_the_z_direction`')

        self._data["NZ: Number of cells in the Z direction"] = value

    @property
    def ibox_x_direction_cell_indicator_of_slab_edge(self):
        """Get ibox_x_direction_cell_indicator_of_slab_edge

        Returns:
            float: the value of `ibox_x_direction_cell_indicator_of_slab_edge` or None if not set
        """
        return self._data["IBOX: X direction cell indicator of slab edge"]

    @ibox_x_direction_cell_indicator_of_slab_edge.setter
    def ibox_x_direction_cell_indicator_of_slab_edge(self, value=None):
        """  Corresponds to IDD Field `ibox_x_direction_cell_indicator_of_slab_edge`
        typical values= 1-10

        Args:
            value (float): value for IDD Field `ibox_x_direction_cell_indicator_of_slab_edge`
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
                                 'for field `ibox_x_direction_cell_indicator_of_slab_edge`'.format(value))

        self._data["IBOX: X direction cell indicator of slab edge"] = value

    @property
    def jbox_y_direction_cell_indicator_of_slab_edge(self):
        """Get jbox_y_direction_cell_indicator_of_slab_edge

        Returns:
            float: the value of `jbox_y_direction_cell_indicator_of_slab_edge` or None if not set
        """
        return self._data["JBOX: Y direction cell indicator of slab edge"]

    @jbox_y_direction_cell_indicator_of_slab_edge.setter
    def jbox_y_direction_cell_indicator_of_slab_edge(self, value=None):
        """  Corresponds to IDD Field `jbox_y_direction_cell_indicator_of_slab_edge`
        typical values= 1-10

        Args:
            value (float): value for IDD Field `jbox_y_direction_cell_indicator_of_slab_edge`
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
                                 'for field `jbox_y_direction_cell_indicator_of_slab_edge`'.format(value))

        self._data["JBOX: Y direction cell indicator of slab edge"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementSimParameters(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:SimParameters`
        Specifies certain parameters that control the Basement preprocessor ground heat
        transfer simulation.
    
    """
    internal_name = "GroundHeatTransfer:Basement:SimParameters"
    field_count = 2
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:SimParameters`
        """
        self._data = OrderedDict()
        self._data["F: Multiplier for the ADI solution"] = None
        self._data["IYRS: Maximum number of yearly iterations:"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.f_multiplier_for_the_adi_solution = None
        else:
            self.f_multiplier_for_the_adi_solution = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.iyrs_maximum_number_of_yearly_iterations = None
        else:
            self.iyrs_maximum_number_of_yearly_iterations = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def f_multiplier_for_the_adi_solution(self):
        """Get f_multiplier_for_the_adi_solution

        Returns:
            float: the value of `f_multiplier_for_the_adi_solution` or None if not set
        """
        return self._data["F: Multiplier for the ADI solution"]

    @f_multiplier_for_the_adi_solution.setter
    def f_multiplier_for_the_adi_solution(self, value=None):
        """  Corresponds to IDD Field `f_multiplier_for_the_adi_solution`
        0<F<1.0,
        typically 0.1 (0.3 for high k soil - saturated sand is about 2.6 w/m-K)

        Args:
            value (float): value for IDD Field `f_multiplier_for_the_adi_solution`
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
                                 'for field `f_multiplier_for_the_adi_solution`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `f_multiplier_for_the_adi_solution`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `f_multiplier_for_the_adi_solution`')

        self._data["F: Multiplier for the ADI solution"] = value

    @property
    def iyrs_maximum_number_of_yearly_iterations(self):
        """Get iyrs_maximum_number_of_yearly_iterations

        Returns:
            float: the value of `iyrs_maximum_number_of_yearly_iterations` or None if not set
        """
        return self._data["IYRS: Maximum number of yearly iterations:"]

    @iyrs_maximum_number_of_yearly_iterations.setter
    def iyrs_maximum_number_of_yearly_iterations(self, value=15.0 ):
        """  Corresponds to IDD Field `iyrs_maximum_number_of_yearly_iterations`
        typically 15-30]

        Args:
            value (float): value for IDD Field `iyrs_maximum_number_of_yearly_iterations`
                Default value: 15.0
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
                                 'for field `iyrs_maximum_number_of_yearly_iterations`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `iyrs_maximum_number_of_yearly_iterations`')

        self._data["IYRS: Maximum number of yearly iterations:"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementMatlProps(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:MatlProps`
        Specifies the material properties for the Basement preprocessor ground heat
        transfer simulation. Only the Foundation Wall, Floor Slab, Soil,
        and Gravel properties are currently used.
    
    """
    internal_name = "GroundHeatTransfer:Basement:MatlProps"
    field_count = 19
    required_fields = ["NMAT: Number of materials in this domain"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:MatlProps`
        """
        self._data = OrderedDict()
        self._data["NMAT: Number of materials in this domain"] = None
        self._data["Density for Foundation Wall"] = None
        self._data["density for Floor Slab"] = None
        self._data["density for Ceiling"] = None
        self._data["density for Soil"] = None
        self._data["density for Gravel"] = None
        self._data["density for Wood"] = None
        self._data["Specific heat for foundation wall"] = None
        self._data["Specific heat for floor slab"] = None
        self._data["Specific heat for ceiling"] = None
        self._data["Specific heat for soil"] = None
        self._data["Specific heat for gravel"] = None
        self._data["Specific heat for wood"] = None
        self._data["Thermal conductivity for foundation wall"] = None
        self._data["Thermal conductivity for floor slab"] = None
        self._data["Thermal conductivity for ceiling"] = None
        self._data["thermal conductivity for soil"] = None
        self._data["thermal conductivity for gravel"] = None
        self._data["thermal conductivity for wood"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.nmat_number_of_materials_in_this_domain = None
        else:
            self.nmat_number_of_materials_in_this_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.density_for_foundation_wall = None
        else:
            self.density_for_foundation_wall = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.density_for_floor_slab = None
        else:
            self.density_for_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.density_for_ceiling = None
        else:
            self.density_for_ceiling = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.density_for_soil = None
        else:
            self.density_for_soil = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.density_for_gravel = None
        else:
            self.density_for_gravel = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.density_for_wood = None
        else:
            self.density_for_wood = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_heat_for_foundation_wall = None
        else:
            self.specific_heat_for_foundation_wall = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_heat_for_floor_slab = None
        else:
            self.specific_heat_for_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_heat_for_ceiling = None
        else:
            self.specific_heat_for_ceiling = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_heat_for_soil = None
        else:
            self.specific_heat_for_soil = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_heat_for_gravel = None
        else:
            self.specific_heat_for_gravel = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_heat_for_wood = None
        else:
            self.specific_heat_for_wood = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conductivity_for_foundation_wall = None
        else:
            self.thermal_conductivity_for_foundation_wall = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conductivity_for_floor_slab = None
        else:
            self.thermal_conductivity_for_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conductivity_for_ceiling = None
        else:
            self.thermal_conductivity_for_ceiling = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conductivity_for_soil = None
        else:
            self.thermal_conductivity_for_soil = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conductivity_for_gravel = None
        else:
            self.thermal_conductivity_for_gravel = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conductivity_for_wood = None
        else:
            self.thermal_conductivity_for_wood = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def nmat_number_of_materials_in_this_domain(self):
        """Get nmat_number_of_materials_in_this_domain

        Returns:
            float: the value of `nmat_number_of_materials_in_this_domain` or None if not set
        """
        return self._data["NMAT: Number of materials in this domain"]

    @nmat_number_of_materials_in_this_domain.setter
    def nmat_number_of_materials_in_this_domain(self, value=None):
        """  Corresponds to IDD Field `nmat_number_of_materials_in_this_domain`

        Args:
            value (float): value for IDD Field `nmat_number_of_materials_in_this_domain`
                value <= 6.0
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
                                 'for field `nmat_number_of_materials_in_this_domain`'.format(value))
            if value > 6.0:
                raise ValueError('value need to be smaller 6.0 '
                                 'for field `nmat_number_of_materials_in_this_domain`')

        self._data["NMAT: Number of materials in this domain"] = value

    @property
    def density_for_foundation_wall(self):
        """Get density_for_foundation_wall

        Returns:
            float: the value of `density_for_foundation_wall` or None if not set
        """
        return self._data["Density for Foundation Wall"]

    @density_for_foundation_wall.setter
    def density_for_foundation_wall(self, value=2243.0 ):
        """  Corresponds to IDD Field `density_for_foundation_wall`

        Args:
            value (float): value for IDD Field `density_for_foundation_wall`
                Units: kg/m3
                Default value: 2243.0
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
                                 'for field `density_for_foundation_wall`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density_for_foundation_wall`')

        self._data["Density for Foundation Wall"] = value

    @property
    def density_for_floor_slab(self):
        """Get density_for_floor_slab

        Returns:
            float: the value of `density_for_floor_slab` or None if not set
        """
        return self._data["density for Floor Slab"]

    @density_for_floor_slab.setter
    def density_for_floor_slab(self, value=2243.0 ):
        """  Corresponds to IDD Field `density_for_floor_slab`

        Args:
            value (float): value for IDD Field `density_for_floor_slab`
                Units: kg/m3
                Default value: 2243.0
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
                                 'for field `density_for_floor_slab`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density_for_floor_slab`')

        self._data["density for Floor Slab"] = value

    @property
    def density_for_ceiling(self):
        """Get density_for_ceiling

        Returns:
            float: the value of `density_for_ceiling` or None if not set
        """
        return self._data["density for Ceiling"]

    @density_for_ceiling.setter
    def density_for_ceiling(self, value=311.0 ):
        """  Corresponds to IDD Field `density_for_ceiling`

        Args:
            value (float): value for IDD Field `density_for_ceiling`
                Units: kg/m3
                Default value: 311.0
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
                                 'for field `density_for_ceiling`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density_for_ceiling`')

        self._data["density for Ceiling"] = value

    @property
    def density_for_soil(self):
        """Get density_for_soil

        Returns:
            float: the value of `density_for_soil` or None if not set
        """
        return self._data["density for Soil"]

    @density_for_soil.setter
    def density_for_soil(self, value=1500.0 ):
        """  Corresponds to IDD Field `density_for_soil`

        Args:
            value (float): value for IDD Field `density_for_soil`
                Units: kg/m3
                Default value: 1500.0
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
                                 'for field `density_for_soil`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density_for_soil`')

        self._data["density for Soil"] = value

    @property
    def density_for_gravel(self):
        """Get density_for_gravel

        Returns:
            float: the value of `density_for_gravel` or None if not set
        """
        return self._data["density for Gravel"]

    @density_for_gravel.setter
    def density_for_gravel(self, value=2000.0 ):
        """  Corresponds to IDD Field `density_for_gravel`

        Args:
            value (float): value for IDD Field `density_for_gravel`
                Units: kg/m3
                Default value: 2000.0
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
                                 'for field `density_for_gravel`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density_for_gravel`')

        self._data["density for Gravel"] = value

    @property
    def density_for_wood(self):
        """Get density_for_wood

        Returns:
            float: the value of `density_for_wood` or None if not set
        """
        return self._data["density for Wood"]

    @density_for_wood.setter
    def density_for_wood(self, value=449.0 ):
        """  Corresponds to IDD Field `density_for_wood`

        Args:
            value (float): value for IDD Field `density_for_wood`
                Units: kg/m3
                Default value: 449.0
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
                                 'for field `density_for_wood`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `density_for_wood`')

        self._data["density for Wood"] = value

    @property
    def specific_heat_for_foundation_wall(self):
        """Get specific_heat_for_foundation_wall

        Returns:
            float: the value of `specific_heat_for_foundation_wall` or None if not set
        """
        return self._data["Specific heat for foundation wall"]

    @specific_heat_for_foundation_wall.setter
    def specific_heat_for_foundation_wall(self, value=880.0 ):
        """  Corresponds to IDD Field `specific_heat_for_foundation_wall`

        Args:
            value (float): value for IDD Field `specific_heat_for_foundation_wall`
                Units: J/kg-K
                Default value: 880.0
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
                                 'for field `specific_heat_for_foundation_wall`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_for_foundation_wall`')

        self._data["Specific heat for foundation wall"] = value

    @property
    def specific_heat_for_floor_slab(self):
        """Get specific_heat_for_floor_slab

        Returns:
            float: the value of `specific_heat_for_floor_slab` or None if not set
        """
        return self._data["Specific heat for floor slab"]

    @specific_heat_for_floor_slab.setter
    def specific_heat_for_floor_slab(self, value=880.0 ):
        """  Corresponds to IDD Field `specific_heat_for_floor_slab`

        Args:
            value (float): value for IDD Field `specific_heat_for_floor_slab`
                Units: J/kg-K
                Default value: 880.0
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
                                 'for field `specific_heat_for_floor_slab`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_for_floor_slab`')

        self._data["Specific heat for floor slab"] = value

    @property
    def specific_heat_for_ceiling(self):
        """Get specific_heat_for_ceiling

        Returns:
            float: the value of `specific_heat_for_ceiling` or None if not set
        """
        return self._data["Specific heat for ceiling"]

    @specific_heat_for_ceiling.setter
    def specific_heat_for_ceiling(self, value=1530.0 ):
        """  Corresponds to IDD Field `specific_heat_for_ceiling`

        Args:
            value (float): value for IDD Field `specific_heat_for_ceiling`
                Units: J/kg-K
                Default value: 1530.0
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
                                 'for field `specific_heat_for_ceiling`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_for_ceiling`')

        self._data["Specific heat for ceiling"] = value

    @property
    def specific_heat_for_soil(self):
        """Get specific_heat_for_soil

        Returns:
            float: the value of `specific_heat_for_soil` or None if not set
        """
        return self._data["Specific heat for soil"]

    @specific_heat_for_soil.setter
    def specific_heat_for_soil(self, value=840.0 ):
        """  Corresponds to IDD Field `specific_heat_for_soil`

        Args:
            value (float): value for IDD Field `specific_heat_for_soil`
                Units: J/kg-K
                Default value: 840.0
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
                                 'for field `specific_heat_for_soil`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_for_soil`')

        self._data["Specific heat for soil"] = value

    @property
    def specific_heat_for_gravel(self):
        """Get specific_heat_for_gravel

        Returns:
            float: the value of `specific_heat_for_gravel` or None if not set
        """
        return self._data["Specific heat for gravel"]

    @specific_heat_for_gravel.setter
    def specific_heat_for_gravel(self, value=720.0 ):
        """  Corresponds to IDD Field `specific_heat_for_gravel`

        Args:
            value (float): value for IDD Field `specific_heat_for_gravel`
                Units: J/kg-K
                Default value: 720.0
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
                                 'for field `specific_heat_for_gravel`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_for_gravel`')

        self._data["Specific heat for gravel"] = value

    @property
    def specific_heat_for_wood(self):
        """Get specific_heat_for_wood

        Returns:
            float: the value of `specific_heat_for_wood` or None if not set
        """
        return self._data["Specific heat for wood"]

    @specific_heat_for_wood.setter
    def specific_heat_for_wood(self, value=1530.0 ):
        """  Corresponds to IDD Field `specific_heat_for_wood`

        Args:
            value (float): value for IDD Field `specific_heat_for_wood`
                Units: J/kg-K
                Default value: 1530.0
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
                                 'for field `specific_heat_for_wood`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `specific_heat_for_wood`')

        self._data["Specific heat for wood"] = value

    @property
    def thermal_conductivity_for_foundation_wall(self):
        """Get thermal_conductivity_for_foundation_wall

        Returns:
            float: the value of `thermal_conductivity_for_foundation_wall` or None if not set
        """
        return self._data["Thermal conductivity for foundation wall"]

    @thermal_conductivity_for_foundation_wall.setter
    def thermal_conductivity_for_foundation_wall(self, value=1.4 ):
        """  Corresponds to IDD Field `thermal_conductivity_for_foundation_wall`

        Args:
            value (float): value for IDD Field `thermal_conductivity_for_foundation_wall`
                Units: W/m-K
                Default value: 1.4
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
                                 'for field `thermal_conductivity_for_foundation_wall`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_for_foundation_wall`')

        self._data["Thermal conductivity for foundation wall"] = value

    @property
    def thermal_conductivity_for_floor_slab(self):
        """Get thermal_conductivity_for_floor_slab

        Returns:
            float: the value of `thermal_conductivity_for_floor_slab` or None if not set
        """
        return self._data["Thermal conductivity for floor slab"]

    @thermal_conductivity_for_floor_slab.setter
    def thermal_conductivity_for_floor_slab(self, value=1.4 ):
        """  Corresponds to IDD Field `thermal_conductivity_for_floor_slab`

        Args:
            value (float): value for IDD Field `thermal_conductivity_for_floor_slab`
                Units: W/m-K
                Default value: 1.4
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
                                 'for field `thermal_conductivity_for_floor_slab`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_for_floor_slab`')

        self._data["Thermal conductivity for floor slab"] = value

    @property
    def thermal_conductivity_for_ceiling(self):
        """Get thermal_conductivity_for_ceiling

        Returns:
            float: the value of `thermal_conductivity_for_ceiling` or None if not set
        """
        return self._data["Thermal conductivity for ceiling"]

    @thermal_conductivity_for_ceiling.setter
    def thermal_conductivity_for_ceiling(self, value=0.09 ):
        """  Corresponds to IDD Field `thermal_conductivity_for_ceiling`

        Args:
            value (float): value for IDD Field `thermal_conductivity_for_ceiling`
                Units: W/m-K
                Default value: 0.09
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
                                 'for field `thermal_conductivity_for_ceiling`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_for_ceiling`')

        self._data["Thermal conductivity for ceiling"] = value

    @property
    def thermal_conductivity_for_soil(self):
        """Get thermal_conductivity_for_soil

        Returns:
            float: the value of `thermal_conductivity_for_soil` or None if not set
        """
        return self._data["thermal conductivity for soil"]

    @thermal_conductivity_for_soil.setter
    def thermal_conductivity_for_soil(self, value=1.1 ):
        """  Corresponds to IDD Field `thermal_conductivity_for_soil`

        Args:
            value (float): value for IDD Field `thermal_conductivity_for_soil`
                Units: W/m-K
                Default value: 1.1
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
                                 'for field `thermal_conductivity_for_soil`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_for_soil`')

        self._data["thermal conductivity for soil"] = value

    @property
    def thermal_conductivity_for_gravel(self):
        """Get thermal_conductivity_for_gravel

        Returns:
            float: the value of `thermal_conductivity_for_gravel` or None if not set
        """
        return self._data["thermal conductivity for gravel"]

    @thermal_conductivity_for_gravel.setter
    def thermal_conductivity_for_gravel(self, value=1.9 ):
        """  Corresponds to IDD Field `thermal_conductivity_for_gravel`

        Args:
            value (float): value for IDD Field `thermal_conductivity_for_gravel`
                Units: W/m-K
                Default value: 1.9
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
                                 'for field `thermal_conductivity_for_gravel`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_for_gravel`')

        self._data["thermal conductivity for gravel"] = value

    @property
    def thermal_conductivity_for_wood(self):
        """Get thermal_conductivity_for_wood

        Returns:
            float: the value of `thermal_conductivity_for_wood` or None if not set
        """
        return self._data["thermal conductivity for wood"]

    @thermal_conductivity_for_wood.setter
    def thermal_conductivity_for_wood(self, value=0.12 ):
        """  Corresponds to IDD Field `thermal_conductivity_for_wood`

        Args:
            value (float): value for IDD Field `thermal_conductivity_for_wood`
                Units: W/m-K
                Default value: 0.12
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
                                 'for field `thermal_conductivity_for_wood`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermal_conductivity_for_wood`')

        self._data["thermal conductivity for wood"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementInsulation(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:Insulation`
        Describes the insulation used on an exterior basement wall for the Basement
        preprocessor ground heat transfer simulation.
    
    """
    internal_name = "GroundHeatTransfer:Basement:Insulation"
    field_count = 2
    required_fields = ["INSFULL: Flag: Is the wall fully insulated?"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:Insulation`
        """
        self._data = OrderedDict()
        self._data["REXT: R Value of any exterior insulation"] = None
        self._data["INSFULL: Flag: Is the wall fully insulated?"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.rext_r_value_of_any_exterior_insulation = None
        else:
            self.rext_r_value_of_any_exterior_insulation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.insfull_flag_is_the_wall_fully_insulated = None
        else:
            self.insfull_flag_is_the_wall_fully_insulated = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def rext_r_value_of_any_exterior_insulation(self):
        """Get rext_r_value_of_any_exterior_insulation

        Returns:
            float: the value of `rext_r_value_of_any_exterior_insulation` or None if not set
        """
        return self._data["REXT: R Value of any exterior insulation"]

    @rext_r_value_of_any_exterior_insulation.setter
    def rext_r_value_of_any_exterior_insulation(self, value=None):
        """  Corresponds to IDD Field `rext_r_value_of_any_exterior_insulation`

        Args:
            value (float): value for IDD Field `rext_r_value_of_any_exterior_insulation`
                Units: m2-K/W
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
                                 'for field `rext_r_value_of_any_exterior_insulation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rext_r_value_of_any_exterior_insulation`')

        self._data["REXT: R Value of any exterior insulation"] = value

    @property
    def insfull_flag_is_the_wall_fully_insulated(self):
        """Get insfull_flag_is_the_wall_fully_insulated

        Returns:
            str: the value of `insfull_flag_is_the_wall_fully_insulated` or None if not set
        """
        return self._data["INSFULL: Flag: Is the wall fully insulated?"]

    @insfull_flag_is_the_wall_fully_insulated.setter
    def insfull_flag_is_the_wall_fully_insulated(self, value=None):
        """  Corresponds to IDD Field `insfull_flag_is_the_wall_fully_insulated`
        True for full insulation
        False for insulation half way down side wall from grade line

        Args:
            value (str): value for IDD Field `insfull_flag_is_the_wall_fully_insulated`
                Accepted values are:
                      - TRUE
                      - FALSE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `insfull_flag_is_the_wall_fully_insulated`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `insfull_flag_is_the_wall_fully_insulated`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `insfull_flag_is_the_wall_fully_insulated`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `insfull_flag_is_the_wall_fully_insulated`'.format(value))
            value = vals[value_lower]

        self._data["INSFULL: Flag: Is the wall fully insulated?"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementSurfaceProps(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:SurfaceProps`
        Specifies the soil surface properties for the Basement preprocessor ground
        heat transfer simulation.
    
    """
    internal_name = "GroundHeatTransfer:Basement:SurfaceProps"
    field_count = 7
    required_fields = ["PET: Flag, Potential evapotranspiration on?"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:SurfaceProps`
        """
        self._data = OrderedDict()
        self._data["ALBEDO: Surface albedo for No snow conditions"] = None
        self._data["ALBEDO: Surface albedo for snow conditions"] = None
        self._data["EPSLN: Surface emissivity No Snow"] = None
        self._data["EPSLN: Surface emissivity with Snow"] = None
        self._data["VEGHT: Surface roughness No snow conditions"] = None
        self._data["VEGHT: Surface roughness Snow conditions"] = None
        self._data["PET: Flag, Potential evapotranspiration on?"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.albedo_surface_albedo_for_no_snow_conditions = None
        else:
            self.albedo_surface_albedo_for_no_snow_conditions = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.albedo_surface_albedo_for_snow_conditions = None
        else:
            self.albedo_surface_albedo_for_snow_conditions = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.epsln_surface_emissivity_no_snow = None
        else:
            self.epsln_surface_emissivity_no_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.epsln_surface_emissivity_with_snow = None
        else:
            self.epsln_surface_emissivity_with_snow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.veght_surface_roughness_no_snow_conditions = None
        else:
            self.veght_surface_roughness_no_snow_conditions = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.veght_surface_roughness_snow_conditions = None
        else:
            self.veght_surface_roughness_snow_conditions = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pet_flag_potential_evapotranspiration_on = None
        else:
            self.pet_flag_potential_evapotranspiration_on = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def albedo_surface_albedo_for_no_snow_conditions(self):
        """Get albedo_surface_albedo_for_no_snow_conditions

        Returns:
            float: the value of `albedo_surface_albedo_for_no_snow_conditions` or None if not set
        """
        return self._data["ALBEDO: Surface albedo for No snow conditions"]

    @albedo_surface_albedo_for_no_snow_conditions.setter
    def albedo_surface_albedo_for_no_snow_conditions(self, value=0.16 ):
        """  Corresponds to IDD Field `albedo_surface_albedo_for_no_snow_conditions`

        Args:
            value (float): value for IDD Field `albedo_surface_albedo_for_no_snow_conditions`
                Default value: 0.16
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
                                 'for field `albedo_surface_albedo_for_no_snow_conditions`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `albedo_surface_albedo_for_no_snow_conditions`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `albedo_surface_albedo_for_no_snow_conditions`')

        self._data["ALBEDO: Surface albedo for No snow conditions"] = value

    @property
    def albedo_surface_albedo_for_snow_conditions(self):
        """Get albedo_surface_albedo_for_snow_conditions

        Returns:
            float: the value of `albedo_surface_albedo_for_snow_conditions` or None if not set
        """
        return self._data["ALBEDO: Surface albedo for snow conditions"]

    @albedo_surface_albedo_for_snow_conditions.setter
    def albedo_surface_albedo_for_snow_conditions(self, value=0.4 ):
        """  Corresponds to IDD Field `albedo_surface_albedo_for_snow_conditions`

        Args:
            value (float): value for IDD Field `albedo_surface_albedo_for_snow_conditions`
                Default value: 0.4
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
                                 'for field `albedo_surface_albedo_for_snow_conditions`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `albedo_surface_albedo_for_snow_conditions`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `albedo_surface_albedo_for_snow_conditions`')

        self._data["ALBEDO: Surface albedo for snow conditions"] = value

    @property
    def epsln_surface_emissivity_no_snow(self):
        """Get epsln_surface_emissivity_no_snow

        Returns:
            float: the value of `epsln_surface_emissivity_no_snow` or None if not set
        """
        return self._data["EPSLN: Surface emissivity No Snow"]

    @epsln_surface_emissivity_no_snow.setter
    def epsln_surface_emissivity_no_snow(self, value=0.94 ):
        """  Corresponds to IDD Field `epsln_surface_emissivity_no_snow`

        Args:
            value (float): value for IDD Field `epsln_surface_emissivity_no_snow`
                Default value: 0.94
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
                                 'for field `epsln_surface_emissivity_no_snow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `epsln_surface_emissivity_no_snow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `epsln_surface_emissivity_no_snow`')

        self._data["EPSLN: Surface emissivity No Snow"] = value

    @property
    def epsln_surface_emissivity_with_snow(self):
        """Get epsln_surface_emissivity_with_snow

        Returns:
            float: the value of `epsln_surface_emissivity_with_snow` or None if not set
        """
        return self._data["EPSLN: Surface emissivity with Snow"]

    @epsln_surface_emissivity_with_snow.setter
    def epsln_surface_emissivity_with_snow(self, value=0.86 ):
        """  Corresponds to IDD Field `epsln_surface_emissivity_with_snow`

        Args:
            value (float): value for IDD Field `epsln_surface_emissivity_with_snow`
                Default value: 0.86
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
                                 'for field `epsln_surface_emissivity_with_snow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `epsln_surface_emissivity_with_snow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `epsln_surface_emissivity_with_snow`')

        self._data["EPSLN: Surface emissivity with Snow"] = value

    @property
    def veght_surface_roughness_no_snow_conditions(self):
        """Get veght_surface_roughness_no_snow_conditions

        Returns:
            float: the value of `veght_surface_roughness_no_snow_conditions` or None if not set
        """
        return self._data["VEGHT: Surface roughness No snow conditions"]

    @veght_surface_roughness_no_snow_conditions.setter
    def veght_surface_roughness_no_snow_conditions(self, value=6.0 ):
        """  Corresponds to IDD Field `veght_surface_roughness_no_snow_conditions`

        Args:
            value (float): value for IDD Field `veght_surface_roughness_no_snow_conditions`
                Units: cm
                Default value: 6.0
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
                                 'for field `veght_surface_roughness_no_snow_conditions`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `veght_surface_roughness_no_snow_conditions`')

        self._data["VEGHT: Surface roughness No snow conditions"] = value

    @property
    def veght_surface_roughness_snow_conditions(self):
        """Get veght_surface_roughness_snow_conditions

        Returns:
            float: the value of `veght_surface_roughness_snow_conditions` or None if not set
        """
        return self._data["VEGHT: Surface roughness Snow conditions"]

    @veght_surface_roughness_snow_conditions.setter
    def veght_surface_roughness_snow_conditions(self, value=0.25 ):
        """  Corresponds to IDD Field `veght_surface_roughness_snow_conditions`

        Args:
            value (float): value for IDD Field `veght_surface_roughness_snow_conditions`
                Units: cm
                Default value: 0.25
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
                                 'for field `veght_surface_roughness_snow_conditions`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `veght_surface_roughness_snow_conditions`')

        self._data["VEGHT: Surface roughness Snow conditions"] = value

    @property
    def pet_flag_potential_evapotranspiration_on(self):
        """Get pet_flag_potential_evapotranspiration_on

        Returns:
            str: the value of `pet_flag_potential_evapotranspiration_on` or None if not set
        """
        return self._data["PET: Flag, Potential evapotranspiration on?"]

    @pet_flag_potential_evapotranspiration_on.setter
    def pet_flag_potential_evapotranspiration_on(self, value="FALSE"):
        """  Corresponds to IDD Field `pet_flag_potential_evapotranspiration_on`
        Typically, PET is False

        Args:
            value (str): value for IDD Field `pet_flag_potential_evapotranspiration_on`
                Accepted values are:
                      - TRUE
                      - FALSE
                Default value: FALSE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `pet_flag_potential_evapotranspiration_on`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pet_flag_potential_evapotranspiration_on`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pet_flag_potential_evapotranspiration_on`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `pet_flag_potential_evapotranspiration_on`'.format(value))
            value = vals[value_lower]

        self._data["PET: Flag, Potential evapotranspiration on?"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementBldgData(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:BldgData`
        Specifies the surface and gravel thicknesses used for the Basement
        preprocessor ground heat transfer simulation.
    
    """
    internal_name = "GroundHeatTransfer:Basement:BldgData"
    field_count = 5
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:BldgData`
        """
        self._data = OrderedDict()
        self._data["DWALL: Wall thickness"] = None
        self._data["DSLAB: Floor slab thickness"] = None
        self._data["DGRAVXY: Width of gravel pit beside basement wall"] = None
        self._data["DGRAVZN: Gravel depth extending above the floor slab"] = None
        self._data["DGRAVZP: Gravel depth below the floor slab"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.dwall_wall_thickness = None
        else:
            self.dwall_wall_thickness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dslab_floor_slab_thickness = None
        else:
            self.dslab_floor_slab_thickness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dgravxy_width_of_gravel_pit_beside_basement_wall = None
        else:
            self.dgravxy_width_of_gravel_pit_beside_basement_wall = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dgravzn_gravel_depth_extending_above_the_floor_slab = None
        else:
            self.dgravzn_gravel_depth_extending_above_the_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dgravzp_gravel_depth_below_the_floor_slab = None
        else:
            self.dgravzp_gravel_depth_below_the_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def dwall_wall_thickness(self):
        """Get dwall_wall_thickness

        Returns:
            float: the value of `dwall_wall_thickness` or None if not set
        """
        return self._data["DWALL: Wall thickness"]

    @dwall_wall_thickness.setter
    def dwall_wall_thickness(self, value=0.2 ):
        """  Corresponds to IDD Field `dwall_wall_thickness`

        Args:
            value (float): value for IDD Field `dwall_wall_thickness`
                Units: m
                Default value: 0.2
                value >= 0.2
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
                                 'for field `dwall_wall_thickness`'.format(value))
            if value < 0.2:
                raise ValueError('value need to be greater or equal 0.2 '
                                 'for field `dwall_wall_thickness`')

        self._data["DWALL: Wall thickness"] = value

    @property
    def dslab_floor_slab_thickness(self):
        """Get dslab_floor_slab_thickness

        Returns:
            float: the value of `dslab_floor_slab_thickness` or None if not set
        """
        return self._data["DSLAB: Floor slab thickness"]

    @dslab_floor_slab_thickness.setter
    def dslab_floor_slab_thickness(self, value=0.1 ):
        """  Corresponds to IDD Field `dslab_floor_slab_thickness`

        Args:
            value (float): value for IDD Field `dslab_floor_slab_thickness`
                Units: m
                Default value: 0.1
                value > 0.0
                value <= 0.25
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
                                 'for field `dslab_floor_slab_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dslab_floor_slab_thickness`')
            if value > 0.25:
                raise ValueError('value need to be smaller 0.25 '
                                 'for field `dslab_floor_slab_thickness`')

        self._data["DSLAB: Floor slab thickness"] = value

    @property
    def dgravxy_width_of_gravel_pit_beside_basement_wall(self):
        """Get dgravxy_width_of_gravel_pit_beside_basement_wall

        Returns:
            float: the value of `dgravxy_width_of_gravel_pit_beside_basement_wall` or None if not set
        """
        return self._data["DGRAVXY: Width of gravel pit beside basement wall"]

    @dgravxy_width_of_gravel_pit_beside_basement_wall.setter
    def dgravxy_width_of_gravel_pit_beside_basement_wall(self, value=0.3 ):
        """  Corresponds to IDD Field `dgravxy_width_of_gravel_pit_beside_basement_wall`

        Args:
            value (float): value for IDD Field `dgravxy_width_of_gravel_pit_beside_basement_wall`
                Units: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `dgravxy_width_of_gravel_pit_beside_basement_wall`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dgravxy_width_of_gravel_pit_beside_basement_wall`')

        self._data["DGRAVXY: Width of gravel pit beside basement wall"] = value

    @property
    def dgravzn_gravel_depth_extending_above_the_floor_slab(self):
        """Get dgravzn_gravel_depth_extending_above_the_floor_slab

        Returns:
            float: the value of `dgravzn_gravel_depth_extending_above_the_floor_slab` or None if not set
        """
        return self._data["DGRAVZN: Gravel depth extending above the floor slab"]

    @dgravzn_gravel_depth_extending_above_the_floor_slab.setter
    def dgravzn_gravel_depth_extending_above_the_floor_slab(self, value=0.2 ):
        """  Corresponds to IDD Field `dgravzn_gravel_depth_extending_above_the_floor_slab`

        Args:
            value (float): value for IDD Field `dgravzn_gravel_depth_extending_above_the_floor_slab`
                Units: m
                Default value: 0.2
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
                                 'for field `dgravzn_gravel_depth_extending_above_the_floor_slab`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dgravzn_gravel_depth_extending_above_the_floor_slab`')

        self._data["DGRAVZN: Gravel depth extending above the floor slab"] = value

    @property
    def dgravzp_gravel_depth_below_the_floor_slab(self):
        """Get dgravzp_gravel_depth_below_the_floor_slab

        Returns:
            float: the value of `dgravzp_gravel_depth_below_the_floor_slab` or None if not set
        """
        return self._data["DGRAVZP: Gravel depth below the floor slab"]

    @dgravzp_gravel_depth_below_the_floor_slab.setter
    def dgravzp_gravel_depth_below_the_floor_slab(self, value=0.1 ):
        """  Corresponds to IDD Field `dgravzp_gravel_depth_below_the_floor_slab`

        Args:
            value (float): value for IDD Field `dgravzp_gravel_depth_below_the_floor_slab`
                Units: m
                Default value: 0.1
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
                                 'for field `dgravzp_gravel_depth_below_the_floor_slab`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `dgravzp_gravel_depth_below_the_floor_slab`')

        self._data["DGRAVZP: Gravel depth below the floor slab"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementInterior(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:Interior`
        Provides the information needed to simulate the inside boundary conditions for
        the Basement preprocessor ground heat transfer simulation.
    
    """
    internal_name = "GroundHeatTransfer:Basement:Interior"
    field_count = 7
    required_fields = ["COND: Flag: Is the basement conditioned?"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:Interior`
        """
        self._data = OrderedDict()
        self._data["COND: Flag: Is the basement conditioned?"] = None
        self._data["HIN: Downward convection only heat transfer coefficient"] = None
        self._data["HIN: Upward convection only heat transfer coefficient"] = None
        self._data["HIN: Horizontal convection only heat transfer coefficient"] = None
        self._data["HIN: Downward combined (convection and radiation) heat transfer coefficient"] = None
        self._data["HIN: Upward combined (convection and radiation) heat transfer coefficient"] = None
        self._data["HIN: Horizontal combined (convection and radiation) heat transfer coefficient"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.cond_flag_is_the_basement_conditioned = None
        else:
            self.cond_flag_is_the_basement_conditioned = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_downward_convection_only_heat_transfer_coefficient = None
        else:
            self.hin_downward_convection_only_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_upward_convection_only_heat_transfer_coefficient = None
        else:
            self.hin_upward_convection_only_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_horizontal_convection_only_heat_transfer_coefficient = None
        else:
            self.hin_horizontal_convection_only_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_downward_combined_convection_and_radiation_heat_transfer_coefficient = None
        else:
            self.hin_downward_combined_convection_and_radiation_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_upward_combined_convection_and_radiation_heat_transfer_coefficient = None
        else:
            self.hin_upward_combined_convection_and_radiation_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient = None
        else:
            self.hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def cond_flag_is_the_basement_conditioned(self):
        """Get cond_flag_is_the_basement_conditioned

        Returns:
            str: the value of `cond_flag_is_the_basement_conditioned` or None if not set
        """
        return self._data["COND: Flag: Is the basement conditioned?"]

    @cond_flag_is_the_basement_conditioned.setter
    def cond_flag_is_the_basement_conditioned(self, value="TRUE"):
        """  Corresponds to IDD Field `cond_flag_is_the_basement_conditioned`
        for EnergyPlus this should be TRUE

        Args:
            value (str): value for IDD Field `cond_flag_is_the_basement_conditioned`
                Accepted values are:
                      - TRUE
                      - FALSE
                Default value: TRUE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cond_flag_is_the_basement_conditioned`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cond_flag_is_the_basement_conditioned`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cond_flag_is_the_basement_conditioned`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `cond_flag_is_the_basement_conditioned`'.format(value))
            value = vals[value_lower]

        self._data["COND: Flag: Is the basement conditioned?"] = value

    @property
    def hin_downward_convection_only_heat_transfer_coefficient(self):
        """Get hin_downward_convection_only_heat_transfer_coefficient

        Returns:
            float: the value of `hin_downward_convection_only_heat_transfer_coefficient` or None if not set
        """
        return self._data["HIN: Downward convection only heat transfer coefficient"]

    @hin_downward_convection_only_heat_transfer_coefficient.setter
    def hin_downward_convection_only_heat_transfer_coefficient(self, value=0.92 ):
        """  Corresponds to IDD Field `hin_downward_convection_only_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `hin_downward_convection_only_heat_transfer_coefficient`
                Units: W/m2-K
                Default value: 0.92
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
                                 'for field `hin_downward_convection_only_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_downward_convection_only_heat_transfer_coefficient`')

        self._data["HIN: Downward convection only heat transfer coefficient"] = value

    @property
    def hin_upward_convection_only_heat_transfer_coefficient(self):
        """Get hin_upward_convection_only_heat_transfer_coefficient

        Returns:
            float: the value of `hin_upward_convection_only_heat_transfer_coefficient` or None if not set
        """
        return self._data["HIN: Upward convection only heat transfer coefficient"]

    @hin_upward_convection_only_heat_transfer_coefficient.setter
    def hin_upward_convection_only_heat_transfer_coefficient(self, value=4.04 ):
        """  Corresponds to IDD Field `hin_upward_convection_only_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `hin_upward_convection_only_heat_transfer_coefficient`
                Units: W/m2-K
                Default value: 4.04
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
                                 'for field `hin_upward_convection_only_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_upward_convection_only_heat_transfer_coefficient`')

        self._data["HIN: Upward convection only heat transfer coefficient"] = value

    @property
    def hin_horizontal_convection_only_heat_transfer_coefficient(self):
        """Get hin_horizontal_convection_only_heat_transfer_coefficient

        Returns:
            float: the value of `hin_horizontal_convection_only_heat_transfer_coefficient` or None if not set
        """
        return self._data["HIN: Horizontal convection only heat transfer coefficient"]

    @hin_horizontal_convection_only_heat_transfer_coefficient.setter
    def hin_horizontal_convection_only_heat_transfer_coefficient(self, value=3.08 ):
        """  Corresponds to IDD Field `hin_horizontal_convection_only_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `hin_horizontal_convection_only_heat_transfer_coefficient`
                Units: W/m2-K
                Default value: 3.08
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
                                 'for field `hin_horizontal_convection_only_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_horizontal_convection_only_heat_transfer_coefficient`')

        self._data["HIN: Horizontal convection only heat transfer coefficient"] = value

    @property
    def hin_downward_combined_convection_and_radiation_heat_transfer_coefficient(self):
        """Get hin_downward_combined_convection_and_radiation_heat_transfer_coefficient

        Returns:
            float: the value of `hin_downward_combined_convection_and_radiation_heat_transfer_coefficient` or None if not set
        """
        return self._data["HIN: Downward combined (convection and radiation) heat transfer coefficient"]

    @hin_downward_combined_convection_and_radiation_heat_transfer_coefficient.setter
    def hin_downward_combined_convection_and_radiation_heat_transfer_coefficient(self, value=6.13 ):
        """  Corresponds to IDD Field `hin_downward_combined_convection_and_radiation_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `hin_downward_combined_convection_and_radiation_heat_transfer_coefficient`
                Units: W/m2-K
                Default value: 6.13
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
                                 'for field `hin_downward_combined_convection_and_radiation_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_downward_combined_convection_and_radiation_heat_transfer_coefficient`')

        self._data["HIN: Downward combined (convection and radiation) heat transfer coefficient"] = value

    @property
    def hin_upward_combined_convection_and_radiation_heat_transfer_coefficient(self):
        """Get hin_upward_combined_convection_and_radiation_heat_transfer_coefficient

        Returns:
            float: the value of `hin_upward_combined_convection_and_radiation_heat_transfer_coefficient` or None if not set
        """
        return self._data["HIN: Upward combined (convection and radiation) heat transfer coefficient"]

    @hin_upward_combined_convection_and_radiation_heat_transfer_coefficient.setter
    def hin_upward_combined_convection_and_radiation_heat_transfer_coefficient(self, value=9.26 ):
        """  Corresponds to IDD Field `hin_upward_combined_convection_and_radiation_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `hin_upward_combined_convection_and_radiation_heat_transfer_coefficient`
                Units: W/m2-K
                Default value: 9.26
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
                                 'for field `hin_upward_combined_convection_and_radiation_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_upward_combined_convection_and_radiation_heat_transfer_coefficient`')

        self._data["HIN: Upward combined (convection and radiation) heat transfer coefficient"] = value

    @property
    def hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient(self):
        """Get hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient

        Returns:
            float: the value of `hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient` or None if not set
        """
        return self._data["HIN: Horizontal combined (convection and radiation) heat transfer coefficient"]

    @hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient.setter
    def hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient(self, value=8.29 ):
        """  Corresponds to IDD Field `hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient`

        Args:
            value (float): value for IDD Field `hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient`
                Units: W/m2-K
                Default value: 8.29
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
                                 'for field `hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient`')

        self._data["HIN: Horizontal combined (convection and radiation) heat transfer coefficient"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementComBldg(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:ComBldg`
        ComBldg contains the monthly average temperatures (C) and possibility of daily variation amplitude
    
    """
    internal_name = "GroundHeatTransfer:Basement:ComBldg"
    field_count = 13
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:ComBldg`
        """
        self._data = OrderedDict()
        self._data["January average temperature"] = None
        self._data["February average temperature"] = None
        self._data["March average temperature"] = None
        self._data["April average temperature"] = None
        self._data["May average temperature"] = None
        self._data["June average temperature"] = None
        self._data["July average temperature"] = None
        self._data["August average temperature"] = None
        self._data["September average temperature"] = None
        self._data["October average temperature"] = None
        self._data["November average temperature"] = None
        self._data["December average temperature"] = None
        self._data["Daily variation sine wave amplitude"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.january_average_temperature = None
        else:
            self.january_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.february_average_temperature = None
        else:
            self.february_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.march_average_temperature = None
        else:
            self.march_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.april_average_temperature = None
        else:
            self.april_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.may_average_temperature = None
        else:
            self.may_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.june_average_temperature = None
        else:
            self.june_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.july_average_temperature = None
        else:
            self.july_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.august_average_temperature = None
        else:
            self.august_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.september_average_temperature = None
        else:
            self.september_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.october_average_temperature = None
        else:
            self.october_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.november_average_temperature = None
        else:
            self.november_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.december_average_temperature = None
        else:
            self.december_average_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.daily_variation_sine_wave_amplitude = None
        else:
            self.daily_variation_sine_wave_amplitude = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def january_average_temperature(self):
        """Get january_average_temperature

        Returns:
            float: the value of `january_average_temperature` or None if not set
        """
        return self._data["January average temperature"]

    @january_average_temperature.setter
    def january_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `january_average_temperature`

        Args:
            value (float): value for IDD Field `january_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `january_average_temperature`'.format(value))

        self._data["January average temperature"] = value

    @property
    def february_average_temperature(self):
        """Get february_average_temperature

        Returns:
            float: the value of `february_average_temperature` or None if not set
        """
        return self._data["February average temperature"]

    @february_average_temperature.setter
    def february_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `february_average_temperature`

        Args:
            value (float): value for IDD Field `february_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `february_average_temperature`'.format(value))

        self._data["February average temperature"] = value

    @property
    def march_average_temperature(self):
        """Get march_average_temperature

        Returns:
            float: the value of `march_average_temperature` or None if not set
        """
        return self._data["March average temperature"]

    @march_average_temperature.setter
    def march_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `march_average_temperature`

        Args:
            value (float): value for IDD Field `march_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `march_average_temperature`'.format(value))

        self._data["March average temperature"] = value

    @property
    def april_average_temperature(self):
        """Get april_average_temperature

        Returns:
            float: the value of `april_average_temperature` or None if not set
        """
        return self._data["April average temperature"]

    @april_average_temperature.setter
    def april_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `april_average_temperature`

        Args:
            value (float): value for IDD Field `april_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `april_average_temperature`'.format(value))

        self._data["April average temperature"] = value

    @property
    def may_average_temperature(self):
        """Get may_average_temperature

        Returns:
            float: the value of `may_average_temperature` or None if not set
        """
        return self._data["May average temperature"]

    @may_average_temperature.setter
    def may_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `may_average_temperature`

        Args:
            value (float): value for IDD Field `may_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `may_average_temperature`'.format(value))

        self._data["May average temperature"] = value

    @property
    def june_average_temperature(self):
        """Get june_average_temperature

        Returns:
            float: the value of `june_average_temperature` or None if not set
        """
        return self._data["June average temperature"]

    @june_average_temperature.setter
    def june_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `june_average_temperature`

        Args:
            value (float): value for IDD Field `june_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `june_average_temperature`'.format(value))

        self._data["June average temperature"] = value

    @property
    def july_average_temperature(self):
        """Get july_average_temperature

        Returns:
            float: the value of `july_average_temperature` or None if not set
        """
        return self._data["July average temperature"]

    @july_average_temperature.setter
    def july_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `july_average_temperature`

        Args:
            value (float): value for IDD Field `july_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `july_average_temperature`'.format(value))

        self._data["July average temperature"] = value

    @property
    def august_average_temperature(self):
        """Get august_average_temperature

        Returns:
            float: the value of `august_average_temperature` or None if not set
        """
        return self._data["August average temperature"]

    @august_average_temperature.setter
    def august_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `august_average_temperature`

        Args:
            value (float): value for IDD Field `august_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `august_average_temperature`'.format(value))

        self._data["August average temperature"] = value

    @property
    def september_average_temperature(self):
        """Get september_average_temperature

        Returns:
            float: the value of `september_average_temperature` or None if not set
        """
        return self._data["September average temperature"]

    @september_average_temperature.setter
    def september_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `september_average_temperature`

        Args:
            value (float): value for IDD Field `september_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `september_average_temperature`'.format(value))

        self._data["September average temperature"] = value

    @property
    def october_average_temperature(self):
        """Get october_average_temperature

        Returns:
            float: the value of `october_average_temperature` or None if not set
        """
        return self._data["October average temperature"]

    @october_average_temperature.setter
    def october_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `october_average_temperature`

        Args:
            value (float): value for IDD Field `october_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `october_average_temperature`'.format(value))

        self._data["October average temperature"] = value

    @property
    def november_average_temperature(self):
        """Get november_average_temperature

        Returns:
            float: the value of `november_average_temperature` or None if not set
        """
        return self._data["November average temperature"]

    @november_average_temperature.setter
    def november_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `november_average_temperature`

        Args:
            value (float): value for IDD Field `november_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `november_average_temperature`'.format(value))

        self._data["November average temperature"] = value

    @property
    def december_average_temperature(self):
        """Get december_average_temperature

        Returns:
            float: the value of `december_average_temperature` or None if not set
        """
        return self._data["December average temperature"]

    @december_average_temperature.setter
    def december_average_temperature(self, value=22.0 ):
        """  Corresponds to IDD Field `december_average_temperature`

        Args:
            value (float): value for IDD Field `december_average_temperature`
                Units: C
                Default value: 22.0
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
                                 'for field `december_average_temperature`'.format(value))

        self._data["December average temperature"] = value

    @property
    def daily_variation_sine_wave_amplitude(self):
        """Get daily_variation_sine_wave_amplitude

        Returns:
            float: the value of `daily_variation_sine_wave_amplitude` or None if not set
        """
        return self._data["Daily variation sine wave amplitude"]

    @daily_variation_sine_wave_amplitude.setter
    def daily_variation_sine_wave_amplitude(self, value=0.0 ):
        """  Corresponds to IDD Field `daily_variation_sine_wave_amplitude`
        (Normally zero, just for checking)

        Args:
            value (float): value for IDD Field `daily_variation_sine_wave_amplitude`
                Units: deltaC
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
                                 'for field `daily_variation_sine_wave_amplitude`'.format(value))

        self._data["Daily variation sine wave amplitude"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementEquivSlab(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:EquivSlab`
        Using an equivalent slab allows non-rectangular shapes to be
        modeled accurately.
        The simulation default should be EquivSizing=True
    
    """
    internal_name = "GroundHeatTransfer:Basement:EquivSlab"
    field_count = 2
    required_fields = ["APRatio: The area to perimeter ratio for this slab", "EquivSizing: Flag"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:EquivSlab`
        """
        self._data = OrderedDict()
        self._data["APRatio: The area to perimeter ratio for this slab"] = None
        self._data["EquivSizing: Flag"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.apratio_the_area_to_perimeter_ratio_for_this_slab = None
        else:
            self.apratio_the_area_to_perimeter_ratio_for_this_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equivsizing_flag = None
        else:
            self.equivsizing_flag = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self):
        """Get apratio_the_area_to_perimeter_ratio_for_this_slab

        Returns:
            float: the value of `apratio_the_area_to_perimeter_ratio_for_this_slab` or None if not set
        """
        return self._data["APRatio: The area to perimeter ratio for this slab"]

    @apratio_the_area_to_perimeter_ratio_for_this_slab.setter
    def apratio_the_area_to_perimeter_ratio_for_this_slab(self, value=None):
        """  Corresponds to IDD Field `apratio_the_area_to_perimeter_ratio_for_this_slab`

        Args:
            value (float): value for IDD Field `apratio_the_area_to_perimeter_ratio_for_this_slab`
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
                                 'for field `apratio_the_area_to_perimeter_ratio_for_this_slab`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `apratio_the_area_to_perimeter_ratio_for_this_slab`')

        self._data["APRatio: The area to perimeter ratio for this slab"] = value

    @property
    def equivsizing_flag(self):
        """Get equivsizing_flag

        Returns:
            str: the value of `equivsizing_flag` or None if not set
        """
        return self._data["EquivSizing: Flag"]

    @equivsizing_flag.setter
    def equivsizing_flag(self, value=None):
        """  Corresponds to IDD Field `equivsizing_flag`
        Will the dimensions of an equivalent slab be calculated (TRUE)
        or will the dimensions be input directly? (FALSE)]
        Only advanced special simulations should use FALSE.

        Args:
            value (str): value for IDD Field `equivsizing_flag`
                Accepted values are:
                      - TRUE
                      - FALSE
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equivsizing_flag`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equivsizing_flag`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `equivsizing_flag`')
            vals = {}
            vals["true"] = "TRUE"
            vals["false"] = "FALSE"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `equivsizing_flag`'.format(value))
            value = vals[value_lower]

        self._data["EquivSizing: Flag"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementEquivAutoGrid(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:EquivAutoGrid`
        EquivAutoGrid necessary when EquivSizing=TRUE, TRUE is is the normal case.
    
    """
    internal_name = "GroundHeatTransfer:Basement:EquivAutoGrid"
    field_count = 3
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:EquivAutoGrid`
        """
        self._data = OrderedDict()
        self._data["CLEARANCE: Distance from outside of wall to edge of 3-D ground domain"] = None
        self._data["SlabDepth: Thickness of the floor slab"] = None
        self._data["BaseDepth: Depth of the basement wall below grade"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain = None
        else:
            self.clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slabdepth_thickness_of_the_floor_slab = None
        else:
            self.slabdepth_thickness_of_the_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basedepth_depth_of_the_basement_wall_below_grade = None
        else:
            self.basedepth_depth_of_the_basement_wall_below_grade = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain(self):
        """Get clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain

        Returns:
            float: the value of `clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain` or None if not set
        """
        return self._data["CLEARANCE: Distance from outside of wall to edge of 3-D ground domain"]

    @clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain.setter
    def clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain(self, value=15.0 ):
        """  Corresponds to IDD Field `clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain`

        Args:
            value (float): value for IDD Field `clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain`
                Units: m
                Default value: 15.0
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
                                 'for field `clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `clearance_distance_from_outside_of_wall_to_edge_of_3d_ground_domain`')

        self._data["CLEARANCE: Distance from outside of wall to edge of 3-D ground domain"] = value

    @property
    def slabdepth_thickness_of_the_floor_slab(self):
        """Get slabdepth_thickness_of_the_floor_slab

        Returns:
            float: the value of `slabdepth_thickness_of_the_floor_slab` or None if not set
        """
        return self._data["SlabDepth: Thickness of the floor slab"]

    @slabdepth_thickness_of_the_floor_slab.setter
    def slabdepth_thickness_of_the_floor_slab(self, value=0.1 ):
        """  Corresponds to IDD Field `slabdepth_thickness_of_the_floor_slab`

        Args:
            value (float): value for IDD Field `slabdepth_thickness_of_the_floor_slab`
                Units: m
                Default value: 0.1
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
                                 'for field `slabdepth_thickness_of_the_floor_slab`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slabdepth_thickness_of_the_floor_slab`')

        self._data["SlabDepth: Thickness of the floor slab"] = value

    @property
    def basedepth_depth_of_the_basement_wall_below_grade(self):
        """Get basedepth_depth_of_the_basement_wall_below_grade

        Returns:
            float: the value of `basedepth_depth_of_the_basement_wall_below_grade` or None if not set
        """
        return self._data["BaseDepth: Depth of the basement wall below grade"]

    @basedepth_depth_of_the_basement_wall_below_grade.setter
    def basedepth_depth_of_the_basement_wall_below_grade(self, value=2.0 ):
        """  Corresponds to IDD Field `basedepth_depth_of_the_basement_wall_below_grade`

        Args:
            value (float): value for IDD Field `basedepth_depth_of_the_basement_wall_below_grade`
                Units: m
                Default value: 2.0
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
                                 'for field `basedepth_depth_of_the_basement_wall_below_grade`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basedepth_depth_of_the_basement_wall_below_grade`')

        self._data["BaseDepth: Depth of the basement wall below grade"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementAutoGrid(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:AutoGrid`
        AutoGrid only necessary when EquivSizing is false
        If the modelled building is not a rectangle or square, Equivalent
        sizing MUST be used to get accurate results
    
    """
    internal_name = "GroundHeatTransfer:Basement:AutoGrid"
    field_count = 6
    required_fields = ["SLABX: X dimension of the building slab", "SLABY: Y dimension of the building slab"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:AutoGrid`
        """
        self._data = OrderedDict()
        self._data["CLEARANCE: Distance from outside of wall to edge,"] = None
        self._data["SLABX: X dimension of the building slab"] = None
        self._data["SLABY: Y dimension of the building slab"] = None
        self._data["ConcAGHeight: Height of the foundation wall above grade"] = None
        self._data["SlabDepth: Thickness of the floor slab"] = None
        self._data["BaseDepth: Depth of the basement wall below grade"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.clearance_distance_from_outside_of_wall_to_edge_ = None
        else:
            self.clearance_distance_from_outside_of_wall_to_edge_ = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slabx_x_dimension_of_the_building_slab = None
        else:
            self.slabx_x_dimension_of_the_building_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slaby_y_dimension_of_the_building_slab = None
        else:
            self.slaby_y_dimension_of_the_building_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.concagheight_height_of_the_foundation_wall_above_grade = None
        else:
            self.concagheight_height_of_the_foundation_wall_above_grade = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slabdepth_thickness_of_the_floor_slab = None
        else:
            self.slabdepth_thickness_of_the_floor_slab = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basedepth_depth_of_the_basement_wall_below_grade = None
        else:
            self.basedepth_depth_of_the_basement_wall_below_grade = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def clearance_distance_from_outside_of_wall_to_edge_(self):
        """Get clearance_distance_from_outside_of_wall_to_edge_

        Returns:
            float: the value of `clearance_distance_from_outside_of_wall_to_edge_` or None if not set
        """
        return self._data["CLEARANCE: Distance from outside of wall to edge,"]

    @clearance_distance_from_outside_of_wall_to_edge_.setter
    def clearance_distance_from_outside_of_wall_to_edge_(self, value=15.0 ):
        """  Corresponds to IDD Field `clearance_distance_from_outside_of_wall_to_edge_`

        Args:
            value (float): value for IDD Field `clearance_distance_from_outside_of_wall_to_edge_`
                Units: m
                Default value: 15.0
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
                                 'for field `clearance_distance_from_outside_of_wall_to_edge_`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `clearance_distance_from_outside_of_wall_to_edge_`')

        self._data["CLEARANCE: Distance from outside of wall to edge,"] = value

    @property
    def slabx_x_dimension_of_the_building_slab(self):
        """Get slabx_x_dimension_of_the_building_slab

        Returns:
            float: the value of `slabx_x_dimension_of_the_building_slab` or None if not set
        """
        return self._data["SLABX: X dimension of the building slab"]

    @slabx_x_dimension_of_the_building_slab.setter
    def slabx_x_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD Field `slabx_x_dimension_of_the_building_slab`

        Args:
            value (float): value for IDD Field `slabx_x_dimension_of_the_building_slab`
                Units: m
                value >= 0.0
                value <= 60.0
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
                                 'for field `slabx_x_dimension_of_the_building_slab`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slabx_x_dimension_of_the_building_slab`')
            if value > 60.0:
                raise ValueError('value need to be smaller 60.0 '
                                 'for field `slabx_x_dimension_of_the_building_slab`')

        self._data["SLABX: X dimension of the building slab"] = value

    @property
    def slaby_y_dimension_of_the_building_slab(self):
        """Get slaby_y_dimension_of_the_building_slab

        Returns:
            float: the value of `slaby_y_dimension_of_the_building_slab` or None if not set
        """
        return self._data["SLABY: Y dimension of the building slab"]

    @slaby_y_dimension_of_the_building_slab.setter
    def slaby_y_dimension_of_the_building_slab(self, value=None):
        """  Corresponds to IDD Field `slaby_y_dimension_of_the_building_slab`

        Args:
            value (float): value for IDD Field `slaby_y_dimension_of_the_building_slab`
                Units: m
                value >= 0.0
                value <= 60.0
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
                                 'for field `slaby_y_dimension_of_the_building_slab`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `slaby_y_dimension_of_the_building_slab`')
            if value > 60.0:
                raise ValueError('value need to be smaller 60.0 '
                                 'for field `slaby_y_dimension_of_the_building_slab`')

        self._data["SLABY: Y dimension of the building slab"] = value

    @property
    def concagheight_height_of_the_foundation_wall_above_grade(self):
        """Get concagheight_height_of_the_foundation_wall_above_grade

        Returns:
            float: the value of `concagheight_height_of_the_foundation_wall_above_grade` or None if not set
        """
        return self._data["ConcAGHeight: Height of the foundation wall above grade"]

    @concagheight_height_of_the_foundation_wall_above_grade.setter
    def concagheight_height_of_the_foundation_wall_above_grade(self, value=0.0 ):
        """  Corresponds to IDD Field `concagheight_height_of_the_foundation_wall_above_grade`

        Args:
            value (float): value for IDD Field `concagheight_height_of_the_foundation_wall_above_grade`
                Units: m
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
                                 'for field `concagheight_height_of_the_foundation_wall_above_grade`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `concagheight_height_of_the_foundation_wall_above_grade`')

        self._data["ConcAGHeight: Height of the foundation wall above grade"] = value

    @property
    def slabdepth_thickness_of_the_floor_slab(self):
        """Get slabdepth_thickness_of_the_floor_slab

        Returns:
            float: the value of `slabdepth_thickness_of_the_floor_slab` or None if not set
        """
        return self._data["SlabDepth: Thickness of the floor slab"]

    @slabdepth_thickness_of_the_floor_slab.setter
    def slabdepth_thickness_of_the_floor_slab(self, value=0.1 ):
        """  Corresponds to IDD Field `slabdepth_thickness_of_the_floor_slab`

        Args:
            value (float): value for IDD Field `slabdepth_thickness_of_the_floor_slab`
                Units: m
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
                                 'for field `slabdepth_thickness_of_the_floor_slab`'.format(value))

        self._data["SlabDepth: Thickness of the floor slab"] = value

    @property
    def basedepth_depth_of_the_basement_wall_below_grade(self):
        """Get basedepth_depth_of_the_basement_wall_below_grade

        Returns:
            float: the value of `basedepth_depth_of_the_basement_wall_below_grade` or None if not set
        """
        return self._data["BaseDepth: Depth of the basement wall below grade"]

    @basedepth_depth_of_the_basement_wall_below_grade.setter
    def basedepth_depth_of_the_basement_wall_below_grade(self, value=2.0 ):
        """  Corresponds to IDD Field `basedepth_depth_of_the_basement_wall_below_grade`

        Args:
            value (float): value for IDD Field `basedepth_depth_of_the_basement_wall_below_grade`
                Units: m
                Default value: 2.0
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
                                 'for field `basedepth_depth_of_the_basement_wall_below_grade`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basedepth_depth_of_the_basement_wall_below_grade`')

        self._data["BaseDepth: Depth of the basement wall below grade"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class GroundHeatTransferBasementManualGrid(object):
    """ Corresponds to IDD object `GroundHeatTransfer:Basement:ManualGrid`
        Manual Grid only necessary using manual gridding (not recommended)
    
    """
    internal_name = "GroundHeatTransfer:Basement:ManualGrid"
    field_count = 7
    required_fields = ["NX: Number of cells in the X direction: 20]", "NY: Number of cells in the Y direction: 20]", "NZAG: Number of cells in the Z direction. above grade: 4 Always]", "NZBG: Number of cells in Z direction. below grade: 10-35]", "IBASE: X direction cell indicator of slab edge: 5-20]", "JBASE: Y direction cell indicator of slab edge: 5-20]", "KBASE: Z direction cell indicator of the top of the floor slab: 5-20]"]

    def __init__(self):
        """ Init data dictionary object for IDD  `GroundHeatTransfer:Basement:ManualGrid`
        """
        self._data = OrderedDict()
        self._data["NX: Number of cells in the X direction: 20]"] = None
        self._data["NY: Number of cells in the Y direction: 20]"] = None
        self._data["NZAG: Number of cells in the Z direction. above grade: 4 Always]"] = None
        self._data["NZBG: Number of cells in Z direction. below grade: 10-35]"] = None
        self._data["IBASE: X direction cell indicator of slab edge: 5-20]"] = None
        self._data["JBASE: Y direction cell indicator of slab edge: 5-20]"] = None
        self._data["KBASE: Z direction cell indicator of the top of the floor slab: 5-20]"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.nx_number_of_cells_in_the_x_direction_20 = None
        else:
            self.nx_number_of_cells_in_the_x_direction_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ny_number_of_cells_in_the_y_direction_20 = None
        else:
            self.ny_number_of_cells_in_the_y_direction_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nzag_number_of_cells_in_the_z_direction_above_grade_4_always = None
        else:
            self.nzag_number_of_cells_in_the_z_direction_above_grade_4_always = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nzbg_number_of_cells_in_z_direction_below_grade_1035 = None
        else:
            self.nzbg_number_of_cells_in_z_direction_below_grade_1035 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ibase_x_direction_cell_indicator_of_slab_edge_520 = None
        else:
            self.ibase_x_direction_cell_indicator_of_slab_edge_520 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.jbase_y_direction_cell_indicator_of_slab_edge_520 = None
        else:
            self.jbase_y_direction_cell_indicator_of_slab_edge_520 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520 = None
        else:
            self.kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def nx_number_of_cells_in_the_x_direction_20(self):
        """Get nx_number_of_cells_in_the_x_direction_20

        Returns:
            float: the value of `nx_number_of_cells_in_the_x_direction_20` or None if not set
        """
        return self._data["NX: Number of cells in the X direction: 20]"]

    @nx_number_of_cells_in_the_x_direction_20.setter
    def nx_number_of_cells_in_the_x_direction_20(self, value=None):
        """  Corresponds to IDD Field `nx_number_of_cells_in_the_x_direction_20`

        Args:
            value (float): value for IDD Field `nx_number_of_cells_in_the_x_direction_20`
                value >= 1.0
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
                                 'for field `nx_number_of_cells_in_the_x_direction_20`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `nx_number_of_cells_in_the_x_direction_20`')

        self._data["NX: Number of cells in the X direction: 20]"] = value

    @property
    def ny_number_of_cells_in_the_y_direction_20(self):
        """Get ny_number_of_cells_in_the_y_direction_20

        Returns:
            float: the value of `ny_number_of_cells_in_the_y_direction_20` or None if not set
        """
        return self._data["NY: Number of cells in the Y direction: 20]"]

    @ny_number_of_cells_in_the_y_direction_20.setter
    def ny_number_of_cells_in_the_y_direction_20(self, value=None):
        """  Corresponds to IDD Field `ny_number_of_cells_in_the_y_direction_20`

        Args:
            value (float): value for IDD Field `ny_number_of_cells_in_the_y_direction_20`
                value >= 1.0
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
                                 'for field `ny_number_of_cells_in_the_y_direction_20`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `ny_number_of_cells_in_the_y_direction_20`')

        self._data["NY: Number of cells in the Y direction: 20]"] = value

    @property
    def nzag_number_of_cells_in_the_z_direction_above_grade_4_always(self):
        """Get nzag_number_of_cells_in_the_z_direction_above_grade_4_always

        Returns:
            float: the value of `nzag_number_of_cells_in_the_z_direction_above_grade_4_always` or None if not set
        """
        return self._data["NZAG: Number of cells in the Z direction. above grade: 4 Always]"]

    @nzag_number_of_cells_in_the_z_direction_above_grade_4_always.setter
    def nzag_number_of_cells_in_the_z_direction_above_grade_4_always(self, value=None):
        """  Corresponds to IDD Field `nzag_number_of_cells_in_the_z_direction_above_grade_4_always`

        Args:
            value (float): value for IDD Field `nzag_number_of_cells_in_the_z_direction_above_grade_4_always`
                value >= 1.0
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
                                 'for field `nzag_number_of_cells_in_the_z_direction_above_grade_4_always`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `nzag_number_of_cells_in_the_z_direction_above_grade_4_always`')

        self._data["NZAG: Number of cells in the Z direction. above grade: 4 Always]"] = value

    @property
    def nzbg_number_of_cells_in_z_direction_below_grade_1035(self):
        """Get nzbg_number_of_cells_in_z_direction_below_grade_1035

        Returns:
            float: the value of `nzbg_number_of_cells_in_z_direction_below_grade_1035` or None if not set
        """
        return self._data["NZBG: Number of cells in Z direction. below grade: 10-35]"]

    @nzbg_number_of_cells_in_z_direction_below_grade_1035.setter
    def nzbg_number_of_cells_in_z_direction_below_grade_1035(self, value=None):
        """  Corresponds to IDD Field `nzbg_number_of_cells_in_z_direction_below_grade_1035`

        Args:
            value (float): value for IDD Field `nzbg_number_of_cells_in_z_direction_below_grade_1035`
                value >= 1.0
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
                                 'for field `nzbg_number_of_cells_in_z_direction_below_grade_1035`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `nzbg_number_of_cells_in_z_direction_below_grade_1035`')

        self._data["NZBG: Number of cells in Z direction. below grade: 10-35]"] = value

    @property
    def ibase_x_direction_cell_indicator_of_slab_edge_520(self):
        """Get ibase_x_direction_cell_indicator_of_slab_edge_520

        Returns:
            float: the value of `ibase_x_direction_cell_indicator_of_slab_edge_520` or None if not set
        """
        return self._data["IBASE: X direction cell indicator of slab edge: 5-20]"]

    @ibase_x_direction_cell_indicator_of_slab_edge_520.setter
    def ibase_x_direction_cell_indicator_of_slab_edge_520(self, value=None):
        """  Corresponds to IDD Field `ibase_x_direction_cell_indicator_of_slab_edge_520`

        Args:
            value (float): value for IDD Field `ibase_x_direction_cell_indicator_of_slab_edge_520`
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
                                 'for field `ibase_x_direction_cell_indicator_of_slab_edge_520`'.format(value))

        self._data["IBASE: X direction cell indicator of slab edge: 5-20]"] = value

    @property
    def jbase_y_direction_cell_indicator_of_slab_edge_520(self):
        """Get jbase_y_direction_cell_indicator_of_slab_edge_520

        Returns:
            float: the value of `jbase_y_direction_cell_indicator_of_slab_edge_520` or None if not set
        """
        return self._data["JBASE: Y direction cell indicator of slab edge: 5-20]"]

    @jbase_y_direction_cell_indicator_of_slab_edge_520.setter
    def jbase_y_direction_cell_indicator_of_slab_edge_520(self, value=None):
        """  Corresponds to IDD Field `jbase_y_direction_cell_indicator_of_slab_edge_520`

        Args:
            value (float): value for IDD Field `jbase_y_direction_cell_indicator_of_slab_edge_520`
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
                                 'for field `jbase_y_direction_cell_indicator_of_slab_edge_520`'.format(value))

        self._data["JBASE: Y direction cell indicator of slab edge: 5-20]"] = value

    @property
    def kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520(self):
        """Get kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520

        Returns:
            float: the value of `kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520` or None if not set
        """
        return self._data["KBASE: Z direction cell indicator of the top of the floor slab: 5-20]"]

    @kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520.setter
    def kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520(self, value=None):
        """  Corresponds to IDD Field `kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520`

        Args:
            value (float): value for IDD Field `kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520`
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
                                 'for field `kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_520`'.format(value))

        self._data["KBASE: Z direction cell indicator of the top of the floor slab: 5-20]"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])