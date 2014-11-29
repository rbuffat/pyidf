from collections import OrderedDict

class ShadowCalculation(object):
    """ Corresponds to IDD object `ShadowCalculation`
        This object is used to control details of the solar, shading, and daylighting models
    """
    internal_name = "ShadowCalculation"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ShadowCalculation`
        """
        self._data = OrderedDict()
        self._data["Calculation Method"] = None
        self._data["Calculation Frequency"] = None
        self._data["Maximum Figures in Shadow Overlap Calculations"] = None
        self._data["Polygon Clipping Algorithm"] = None
        self._data["Sky Diffuse Modeling Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.calculation_method = None
        else:
            self.calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.calculation_frequency = None
        else:
            self.calculation_frequency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_figures_in_shadow_overlap_calculations = None
        else:
            self.maximum_figures_in_shadow_overlap_calculations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.polygon_clipping_algorithm = None
        else:
            self.polygon_clipping_algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sky_diffuse_modeling_algorithm = None
        else:
            self.sky_diffuse_modeling_algorithm = vals[i]
        i += 1

    @property
    def calculation_method(self):
        """Get calculation_method

        Returns:
            str: the value of `calculation_method` or None if not set
        """
        return self._data["Calculation Method"]

    @calculation_method.setter
    def calculation_method(self, value="AverageOverDaysInFrequency"):
        """  Corresponds to IDD Field `calculation_method`
        choose calculation method. note that TimestepFrequency is only needed for certain cases
        and can increase execution time significantly.

        Args:
            value (str): value for IDD Field `calculation_method`
                Accepted values are:
                      - AverageOverDaysInFrequency
                      - TimestepFrequency
                Default value: AverageOverDaysInFrequency
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `calculation_method`')
            vals = set()
            vals.add("AverageOverDaysInFrequency")
            vals.add("TimestepFrequency")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `calculation_method`'.format(value))

        self._data["Calculation Method"] = value

    @property
    def calculation_frequency(self):
        """Get calculation_frequency

        Returns:
            int: the value of `calculation_frequency` or None if not set
        """
        return self._data["Calculation Frequency"]

    @calculation_frequency.setter
    def calculation_frequency(self, value=20 ):
        """  Corresponds to IDD Field `calculation_frequency`
        enter number of days
        this field is only used if the previous field is set to AverageOverDaysInFrequency
        0=Use Default Periodic Calculation|<else> calculate every <value> day
        only really applicable to RunPeriods
        warning issued if >31

        Args:
            value (int): value for IDD Field `calculation_frequency`
                Default value: 20
                value >= 1
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
                                 'for field `calculation_frequency`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `calculation_frequency`')

        self._data["Calculation Frequency"] = value

    @property
    def maximum_figures_in_shadow_overlap_calculations(self):
        """Get maximum_figures_in_shadow_overlap_calculations

        Returns:
            int: the value of `maximum_figures_in_shadow_overlap_calculations` or None if not set
        """
        return self._data["Maximum Figures in Shadow Overlap Calculations"]

    @maximum_figures_in_shadow_overlap_calculations.setter
    def maximum_figures_in_shadow_overlap_calculations(self, value=15000 ):
        """  Corresponds to IDD Field `maximum_figures_in_shadow_overlap_calculations`
        Number of allowable figures in shadow overlap calculations

        Args:
            value (int): value for IDD Field `maximum_figures_in_shadow_overlap_calculations`
                Default value: 15000
                value >= 200
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
                                 'for field `maximum_figures_in_shadow_overlap_calculations`'.format(value))
            if value < 200:
                raise ValueError('value need to be greater or equal 200 '
                                 'for field `maximum_figures_in_shadow_overlap_calculations`')

        self._data["Maximum Figures in Shadow Overlap Calculations"] = value

    @property
    def polygon_clipping_algorithm(self):
        """Get polygon_clipping_algorithm

        Returns:
            str: the value of `polygon_clipping_algorithm` or None if not set
        """
        return self._data["Polygon Clipping Algorithm"]

    @polygon_clipping_algorithm.setter
    def polygon_clipping_algorithm(self, value=None):
        """  Corresponds to IDD Field `polygon_clipping_algorithm`
        Advanced Feature.  Internal default is SutherlandHodgman
        Refer to InputOutput Reference and Engineering Reference for more information

        Args:
            value (str): value for IDD Field `polygon_clipping_algorithm`
                Accepted values are:
                      - ConvexWeilerAtherton
                      - SutherlandHodgman
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `polygon_clipping_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `polygon_clipping_algorithm`')
            vals = set()
            vals.add("ConvexWeilerAtherton")
            vals.add("SutherlandHodgman")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `polygon_clipping_algorithm`'.format(value))

        self._data["Polygon Clipping Algorithm"] = value

    @property
    def sky_diffuse_modeling_algorithm(self):
        """Get sky_diffuse_modeling_algorithm

        Returns:
            str: the value of `sky_diffuse_modeling_algorithm` or None if not set
        """
        return self._data["Sky Diffuse Modeling Algorithm"]

    @sky_diffuse_modeling_algorithm.setter
    def sky_diffuse_modeling_algorithm(self, value=None):
        """  Corresponds to IDD Field `sky_diffuse_modeling_algorithm`
        Advanced Feature.  Internal default is SimpleSkyDiffuseModeling
        If you have shading elements that change transmittance over the
        year, you may wish to choose the detailed method.
        Refer to InputOutput Reference and Engineering Reference for more information

        Args:
            value (str): value for IDD Field `sky_diffuse_modeling_algorithm`
                Accepted values are:
                      - SimpleSkyDiffuseModeling
                      - DetailedSkyDiffuseModeling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sky_diffuse_modeling_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sky_diffuse_modeling_algorithm`')
            vals = set()
            vals.add("SimpleSkyDiffuseModeling")
            vals.add("DetailedSkyDiffuseModeling")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `sky_diffuse_modeling_algorithm`'.format(value))

        self._data["Sky Diffuse Modeling Algorithm"] = value

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
        out.append(self._to_str(self.calculation_method))
        out.append(self._to_str(self.calculation_frequency))
        out.append(self._to_str(self.maximum_figures_in_shadow_overlap_calculations))
        out.append(self._to_str(self.polygon_clipping_algorithm))
        out.append(self._to_str(self.sky_diffuse_modeling_algorithm))
        return ",".join(out)