""" Data objects in group "Natural Ventilation and Duct Leakage"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class AirflowNetworkSimulationControl(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:SimulationControl`
        This object defines the global parameters used in an Airflow Network simulation.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'airflownetwork control',
                                      {'name': u'AirflowNetwork Control',
                                       'pyname': u'airflownetwork_control',
                                       'default': u'NoMultizoneOrDistribution',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'MultizoneWithDistribution',
                                                           u'MultizoneWithoutDistribution',
                                                           u'MultizoneWithDistributionOnlyDuringFanOperation',
                                                           u'NoMultizoneOrDistribution'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'wind pressure coefficient type',
                                      {'name': u'Wind Pressure Coefficient Type',
                                       'pyname': u'wind_pressure_coefficient_type',
                                       'default': u'SurfaceAverageCalculation',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Input',
                                                           u'SurfaceAverageCalculation'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'airflownetwork wind pressure coefficient array name',
                                      {'name': u'AirflowNetwork Wind Pressure Coefficient Array Name',
                                       'pyname': u'airflownetwork_wind_pressure_coefficient_array_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'height selection for local wind pressure calculation',
                                      {'name': u'Height Selection for Local Wind Pressure Calculation',
                                       'pyname': u'height_selection_for_local_wind_pressure_calculation',
                                       'default': u'OpeningHeight',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'ExternalNode',
                                                           u'OpeningHeight'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'building type',
                                      {'name': u'Building Type',
                                       'pyname': u'building_type',
                                       'default': u'LowRise',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'LowRise',
                                                           u'HighRise'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'maximum number of iterations',
                                      {'name': u'Maximum Number of Iterations',
                                       'pyname': u'maximum_number_of_iterations',
                                       'default': 500,
                                       'minimum>': 10,
                                       'maximum': 30000,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'integer',
                                       'unit': u'dimensionless'}),
                                     (u'initialization type',
                                      {'name': u'Initialization Type',
                                       'pyname': u'initialization_type',
                                       'default': u'ZeroNodePressures',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'LinearInitializationMethod',
                                                           u'ZeroNodePressures'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'relative airflow convergence tolerance',
                                      {'name': u'Relative Airflow Convergence Tolerance',
                                       'pyname': u'relative_airflow_convergence_tolerance',
                                       'default': 0.0001,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'absolute airflow convergence tolerance',
                                      {'name': u'Absolute Airflow Convergence Tolerance',
                                       'pyname': u'absolute_airflow_convergence_tolerance',
                                       'default': 1e-06,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s'}),
                                     (u'convergence acceleration limit',
                                      {'name': u'Convergence Acceleration Limit',
                                       'pyname': u'convergence_acceleration_limit',
                                       'default': -0.5,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': -1.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'azimuth angle of long axis of building',
                                      {'name': u'Azimuth Angle of Long Axis of Building',
                                       'pyname': u'azimuth_angle_of_long_axis_of_building',
                                       'default': 0.0,
                                       'maximum': 180.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'ratio of building width along short axis to width along long axis',
                                      {'name': u'Ratio of Building Width Along Short Axis to Width Along Long Axis',
                                       'pyname': u'ratio_of_building_width_along_short_axis_to_width_along_long_axis',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real'}),
                                     (u'height dependence of external node temperature',
                                      {'name': u'Height Dependence of External Node Temperature',
                                       'pyname': u'height_dependence_of_external_node_temperature',
                                       'default': u'No',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Yes',
                                                           u'No'],
                                       'autocalculatable': False,
                                       'type': 'alpha'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 13,
              'name': u'AirflowNetwork:SimulationControl',
              'pyname': u'AirflowNetworkSimulationControl',
              'required-object': False,
              'unique-object': True}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def airflownetwork_control(self):
        """Get airflownetwork_control.

        Returns:
            str: the value of `airflownetwork_control` or None if not set

        """
        return self["AirflowNetwork Control"]

    @airflownetwork_control.setter
    def airflownetwork_control(self, value="NoMultizoneOrDistribution"):
        """  Corresponds to IDD field `AirflowNetwork Control`
        NoMultizoneOrDistribution: Only perform Simple calculations (objects ZoneInfiltration:*,
        ZoneVentilation:*, ZoneMixing, ZoneCrossMixing, ZoneRefrigerationDoorMixing,
        ZoneAirBalance:OutdoorAir, ZoneEarthtube, ZoneThermalChimney, and ZoneCoolTower:Shower);
        MultizoneWithoutDistribution: Use AirflowNetwork objects to simulate multizone
        Airflows driven by wind during simulation time,
        and objects of ZoneInfiltration:*, ZoneVentilation:*, ZoneMixing, ZoneCrossMixing
        ZoneRefrigerationDoorMixing, ZoneAirBalance:OutdoorAir, ZoneEarthtube,
        ZoneThermalChimney, and ZoneCoolTower:Shower are ignored;
        MultizoneWithDistributionOnlyDuringFanOperation: Perform distribution system
        calculations during system fan on time
        and Simple calculations during system Fan off time;
        MultizoneWithDistribution: Perform distribution system calculations during system
        fan on time and multizone Airflow driven by wind during system fan off time.

        Args:
            value (str): value for IDD Field `AirflowNetwork Control`
                Default value: NoMultizoneOrDistribution
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["AirflowNetwork Control"] = value

    @property
    def wind_pressure_coefficient_type(self):
        """Get wind_pressure_coefficient_type.

        Returns:
            str: the value of `wind_pressure_coefficient_type` or None if not set

        """
        return self["Wind Pressure Coefficient Type"]

    @wind_pressure_coefficient_type.setter
    def wind_pressure_coefficient_type(
            self,
            value="SurfaceAverageCalculation"):
        """  Corresponds to IDD field `Wind Pressure Coefficient Type`
        Input: User must enter AirflowNetwork:MultiZone:WindPressureCoefficientArray,
        AirflowNetwork:MultiZone:ExternalNode, and
        AirflowNetwork:MultiZone:WindPressureCoefficientValues objects.
        SurfaceAverageCalculation: used only for rectangular buildings.
        If SurfaceAverageCalculation is selected,
        AirflowNetwork:MultiZone:WindPressureCoefficientArray, AirflowNetwork:MultiZone:ExternalNode,
        and AirflowNetwork:MultiZone:WindPressureCoefficientValues objects are not used.

        Args:
            value (str): value for IDD Field `Wind Pressure Coefficient Type`
                Default value: SurfaceAverageCalculation
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Wind Pressure Coefficient Type"] = value

    @property
    def airflownetwork_wind_pressure_coefficient_array_name(self):
        """Get airflownetwork_wind_pressure_coefficient_array_name.

        Returns:
            str: the value of `airflownetwork_wind_pressure_coefficient_array_name` or None if not set

        """
        return self["AirflowNetwork Wind Pressure Coefficient Array Name"]

    @airflownetwork_wind_pressure_coefficient_array_name.setter
    def airflownetwork_wind_pressure_coefficient_array_name(self, value=None):
        """  Corresponds to IDD field `AirflowNetwork Wind Pressure Coefficient Array Name`
        Used only if Wind Pressure Coefficient Type = Input, otherwise this field may be left blank.

        Args:
            value (str): value for IDD Field `AirflowNetwork Wind Pressure Coefficient Array Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["AirflowNetwork Wind Pressure Coefficient Array Name"] = value

    @property
    def height_selection_for_local_wind_pressure_calculation(self):
        """Get height_selection_for_local_wind_pressure_calculation.

        Returns:
            str: the value of `height_selection_for_local_wind_pressure_calculation` or None if not set

        """
        return self["Height Selection for Local Wind Pressure Calculation"]

    @height_selection_for_local_wind_pressure_calculation.setter
    def height_selection_for_local_wind_pressure_calculation(
            self,
            value="OpeningHeight"):
        """  Corresponds to IDD field `Height Selection for Local Wind Pressure Calculation`
        If ExternalNode is selected, the height given in the
        AirflowNetwork:MultiZone:ExternalNode object will be used.
        If OpeningHeight is selected, the surface opening height (centroid) will be used to
        calculate local wind pressure
        This field is ignored when the choice of the Wind Pressure Coefficient Type field is
        SurfaceAverageCalculation.

        Args:
            value (str): value for IDD Field `Height Selection for Local Wind Pressure Calculation`
                Default value: OpeningHeight
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Height Selection for Local Wind Pressure Calculation"] = value

    @property
    def building_type(self):
        """Get building_type.

        Returns:
            str: the value of `building_type` or None if not set

        """
        return self["Building Type"]

    @building_type.setter
    def building_type(self, value="LowRise"):
        """  Corresponds to IDD field `Building Type`
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation,
        otherwise this field may be left blank.

        Args:
            value (str): value for IDD Field `Building Type`
                Default value: LowRise
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Building Type"] = value

    @property
    def maximum_number_of_iterations(self):
        """Get maximum_number_of_iterations.

        Returns:
            int: the value of `maximum_number_of_iterations` or None if not set

        """
        return self["Maximum Number of Iterations"]

    @maximum_number_of_iterations.setter
    def maximum_number_of_iterations(self, value=500):
        """Corresponds to IDD field `Maximum Number of Iterations` Determines
        the maximum number of iterations used to converge on a solution. If
        this limit is exceeded, the program terminates.

        Args:
            value (int): value for IDD Field `Maximum Number of Iterations`
                Units: dimensionless
                Default value: 500
                value > 10
                value <= 30000
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Number of Iterations"] = value

    @property
    def initialization_type(self):
        """Get initialization_type.

        Returns:
            str: the value of `initialization_type` or None if not set

        """
        return self["Initialization Type"]

    @initialization_type.setter
    def initialization_type(self, value="ZeroNodePressures"):
        """Corresponds to IDD field `Initialization Type`

        Args:
            value (str): value for IDD Field `Initialization Type`
                Default value: ZeroNodePressures
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Initialization Type"] = value

    @property
    def relative_airflow_convergence_tolerance(self):
        """Get relative_airflow_convergence_tolerance.

        Returns:
            float: the value of `relative_airflow_convergence_tolerance` or None if not set

        """
        return self["Relative Airflow Convergence Tolerance"]

    @relative_airflow_convergence_tolerance.setter
    def relative_airflow_convergence_tolerance(self, value=0.0001):
        """Corresponds to IDD field `Relative Airflow Convergence Tolerance`
        This tolerance is defined as the absolute value of the sum of the mass
        Flow Rates divided by the sum of the absolute value of the mass Flow
        Rates. The mass Flow Rates described here refer to the mass Flow Rates
        at all Nodes in the AirflowNetwork model. The solution converges when
        both this tolerance and the tolerance in the next field (Absolute
        Airflow Convergence Tolerance) are satisfied.

        Args:
            value (float): value for IDD Field `Relative Airflow Convergence Tolerance`
                Units: dimensionless
                Default value: 0.0001
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Relative Airflow Convergence Tolerance"] = value

    @property
    def absolute_airflow_convergence_tolerance(self):
        """Get absolute_airflow_convergence_tolerance.

        Returns:
            float: the value of `absolute_airflow_convergence_tolerance` or None if not set

        """
        return self["Absolute Airflow Convergence Tolerance"]

    @absolute_airflow_convergence_tolerance.setter
    def absolute_airflow_convergence_tolerance(self, value=1e-06):
        """Corresponds to IDD field `Absolute Airflow Convergence Tolerance`
        This tolerance is defined as the absolute value of the sum of the mass
        flow rates. The mass flow rates described here refer to the mass flow
        rates at all nodes in the AirflowNetwork model. The solution converges
        when both this tolerance and the tolerance in the previous field
        (Relative Airflow Convergence Tolerance) are satisfied.

        Args:
            value (float): value for IDD Field `Absolute Airflow Convergence Tolerance`
                Units: kg/s
                Default value: 1e-06
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Absolute Airflow Convergence Tolerance"] = value

    @property
    def convergence_acceleration_limit(self):
        """Get convergence_acceleration_limit.

        Returns:
            float: the value of `convergence_acceleration_limit` or None if not set

        """
        return self["Convergence Acceleration Limit"]

    @convergence_acceleration_limit.setter
    def convergence_acceleration_limit(self, value=-0.5):
        """  Corresponds to IDD field `Convergence Acceleration Limit`
        Used only for AirflowNetwork:SimulationControl

        Args:
            value (float): value for IDD Field `Convergence Acceleration Limit`
                Units: dimensionless
                Default value: -0.5
                value >= -1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Convergence Acceleration Limit"] = value

    @property
    def azimuth_angle_of_long_axis_of_building(self):
        """Get azimuth_angle_of_long_axis_of_building.

        Returns:
            float: the value of `azimuth_angle_of_long_axis_of_building` or None if not set

        """
        return self["Azimuth Angle of Long Axis of Building"]

    @azimuth_angle_of_long_axis_of_building.setter
    def azimuth_angle_of_long_axis_of_building(self, value=None):
        """  Corresponds to IDD field `Azimuth Angle of Long Axis of Building`
        Degrees clockwise from true North.
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.

        Args:
            value (float): value for IDD Field `Azimuth Angle of Long Axis of Building`
                Units: deg
                value <= 180.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Azimuth Angle of Long Axis of Building"] = value

    @property
    def ratio_of_building_width_along_short_axis_to_width_along_long_axis(
            self):
        """Get
        ratio_of_building_width_along_short_axis_to_width_along_long_axis.

        Returns:
            float: the value of `ratio_of_building_width_along_short_axis_to_width_along_long_axis` or None if not set

        """
        return self[
            "Ratio of Building Width Along Short Axis to Width Along Long Axis"]

    @ratio_of_building_width_along_short_axis_to_width_along_long_axis.setter
    def ratio_of_building_width_along_short_axis_to_width_along_long_axis(
            self,
            value=1.0):
        """  Corresponds to IDD field `Ratio of Building Width Along Short Axis to Width Along Long Axis`
        Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.

        Args:
            value (float): value for IDD Field `Ratio of Building Width Along Short Axis to Width Along Long Axis`
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Ratio of Building Width Along Short Axis to Width Along Long Axis"] = value

    @property
    def height_dependence_of_external_node_temperature(self):
        """Get height_dependence_of_external_node_temperature.

        Returns:
            str: the value of `height_dependence_of_external_node_temperature` or None if not set

        """
        return self["Height Dependence of External Node Temperature"]

    @height_dependence_of_external_node_temperature.setter
    def height_dependence_of_external_node_temperature(self, value="No"):
        """Corresponds to IDD field `Height Dependence of External Node
        Temperature` If Yes, external node temperature is height dependent. If
        No, external node temperature is based on zero height.

        Args:
            value (str): value for IDD Field `Height Dependence of External Node Temperature`
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Height Dependence of External Node Temperature"] = value




class AirflowNetworkMultiZoneZone(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Zone`
        This object is used to simultaneously control a thermal zone's window and door openings,
        both exterior and interior.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'zone name',
                                      {'name': u'Zone Name',
                                       'pyname': u'zone_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'ventilation control mode',
                                      {'name': u'Ventilation Control Mode',
                                       'pyname': u'ventilation_control_mode',
                                       'default': u'NoVent',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Temperature',
                                                           u'Enthalpy',
                                                           u'Constant',
                                                           u'ASHRAE55Adaptive',
                                                           u'CEN15251Adaptive',
                                                           u'NoVent'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'ventilation control zone temperature setpoint schedule name',
                                      {'name': u'Ventilation Control Zone Temperature Setpoint Schedule Name',
                                       'pyname': u'ventilation_control_zone_temperature_setpoint_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'minimum venting open factor',
                                      {'name': u'Minimum Venting Open Factor',
                                       'pyname': u'minimum_venting_open_factor',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'indoor and outdoor temperature difference lower limit for maximum venting open factor',
                                      {'name': u'Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor',
                                       'default': 0.0,
                                       'maximum<': 100.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaC'}),
                                     (u'indoor and outdoor temperature difference upper limit for minimun venting open factor',
                                      {'name': u'Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor',
                                       'default': 100.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaC'}),
                                     (u'indoor and outdoor enthalpy difference lower limit for maximum venting open factor',
                                      {'name': u'Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor',
                                       'default': 0.0,
                                       'maximum<': 300000.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaJ/kg'}),
                                     (u'indoor and outdoor enthalpy difference upper limit for minimun venting open factor',
                                      {'name': u'Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor',
                                       'default': 300000.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaJ/kg'}),
                                     (u'venting availability schedule name',
                                      {'name': u'Venting Availability Schedule Name',
                                       'pyname': u'venting_availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'single sided wind pressure coefficient algorithm',
                                      {'name': u'Single Sided Wind Pressure Coefficient Algorithm',
                                       'pyname': u'single_sided_wind_pressure_coefficient_algorithm',
                                       'default': u'Standard',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Advanced',
                                                           u'Standard'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'facade width',
                                      {'name': u'Facade Width',
                                       'pyname': u'facade_width',
                                       'default': 10.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 8,
              'name': u'AirflowNetwork:MultiZone:Zone',
              'pyname': u'AirflowNetworkMultiZoneZone',
              'required-object': False,
              'unique-object': False}

    @property
    def zone_name(self):
        """Get zone_name.

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name` Enter the zone name where
        ventilation control is required.

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Zone Name"] = value

    @property
    def ventilation_control_mode(self):
        """Get ventilation_control_mode.

        Returns:
            str: the value of `ventilation_control_mode` or None if not set

        """
        return self["Ventilation Control Mode"]

    @ventilation_control_mode.setter
    def ventilation_control_mode(self, value="NoVent"):
        """  Corresponds to IDD field `Ventilation Control Mode`
        When Ventilation Control Mode = Temperature or Enthalpy, the following
        fields are used to modulate the Ventilation Open Factor for all
        window and door openings in the zone according to the zone's
        indoor-outdoor temperature or enthalpy difference.
        Constant: controlled by field Venting Schedule Name.
        NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).

        Args:
            value (str): value for IDD Field `Ventilation Control Mode`
                Default value: NoVent
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Ventilation Control Mode"] = value

    @property
    def ventilation_control_zone_temperature_setpoint_schedule_name(self):
        """Get ventilation_control_zone_temperature_setpoint_schedule_name.

        Returns:
            str: the value of `ventilation_control_zone_temperature_setpoint_schedule_name` or None if not set

        """
        return self[
            "Ventilation Control Zone Temperature Setpoint Schedule Name"]

    @ventilation_control_zone_temperature_setpoint_schedule_name.setter
    def ventilation_control_zone_temperature_setpoint_schedule_name(
            self,
            value=None):
        """  Corresponds to IDD field `Ventilation Control Zone Temperature Setpoint Schedule Name`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (str): value for IDD Field `Ventilation Control Zone Temperature Setpoint Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Ventilation Control Zone Temperature Setpoint Schedule Name"] = value

    @property
    def minimum_venting_open_factor(self):
        """Get minimum_venting_open_factor.

        Returns:
            float: the value of `minimum_venting_open_factor` or None if not set

        """
        return self["Minimum Venting Open Factor"]

    @minimum_venting_open_factor.setter
    def minimum_venting_open_factor(self, value=None):
        """  Corresponds to IDD field `Minimum Venting Open Factor`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (float): value for IDD Field `Minimum Venting Open Factor`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(
            self):
        """Get indoor_and_outdoor_temperature_difference_lower_limit_for_maximu
        m_venting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(
            self,
            value=None):
        """  Corresponds to IDD field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be less than the corresponding upper value (next field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaC
                value < 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(
            self):
        """Get indoor_and_outdoor_temperature_difference_upper_limit_for_minimu
        n_venting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(
            self,
            value=100.0):
        """  Corresponds to IDD field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaC
                Default value: 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(
            self):
        """Get indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_v
        enting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(
            self,
            value=None):
        """  Corresponds to IDD field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be less than the corresponding upper value (next field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaJ/kg
                value < 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(
            self):
        """Get indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_v
        enting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(
            self,
            value=300000.0):
        """  Corresponds to IDD field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaJ/kg
                Default value: 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def venting_availability_schedule_name(self):
        """Get venting_availability_schedule_name.

        Returns:
            str: the value of `venting_availability_schedule_name` or None if not set

        """
        return self["Venting Availability Schedule Name"]

    @venting_availability_schedule_name.setter
    def venting_availability_schedule_name(self, value=None):
        """  Corresponds to IDD field `Venting Availability Schedule Name`
        Non-zero Schedule value means venting is allowed if other venting control conditions are
        satisfied. A zero (or negative) Schedule value means venting is not allowed under any
        The Schedule values should be greater than or equal to 0 and less than or equal to 1.
        circumstances. If this Schedule is not specified then venting is allowed if
        other venting control conditions are satisfied.
        Not used if Ventilation Control Mode = NoVent.

        Args:
            value (str): value for IDD Field `Venting Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Venting Availability Schedule Name"] = value

    @property
    def single_sided_wind_pressure_coefficient_algorithm(self):
        """Get single_sided_wind_pressure_coefficient_algorithm.

        Returns:
            str: the value of `single_sided_wind_pressure_coefficient_algorithm` or None if not set

        """
        return self["Single Sided Wind Pressure Coefficient Algorithm"]

    @single_sided_wind_pressure_coefficient_algorithm.setter
    def single_sided_wind_pressure_coefficient_algorithm(
            self,
            value="Standard"):
        """Corresponds to IDD field `Single Sided Wind Pressure Coefficient
        Algorithm` Selecting Advanced results in EnergyPlus calculating
        modified Wind Pressure Coefficients to account for wind direction and
        turbulence effects on single sided ventilation rates. Model is only
        valid for zones with 2 openings, both of which are on a single facade.

        Args:
            value (str): value for IDD Field `Single Sided Wind Pressure Coefficient Algorithm`
                Default value: Standard
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Single Sided Wind Pressure Coefficient Algorithm"] = value

    @property
    def facade_width(self):
        """Get facade_width.

        Returns:
            float: the value of `facade_width` or None if not set

        """
        return self["Facade Width"]

    @facade_width.setter
    def facade_width(self, value=10.0):
        """Corresponds to IDD field `Facade Width` This is the whole building
        width along the direction of the facade of this zone.

        Args:
            value (float): value for IDD Field `Facade Width`
                Units: m
                Default value: 10.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Facade Width"] = value




class AirflowNetworkMultiZoneSurface(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface`
        This object specifies the properties of a surface linkage through which air flows.
        Airflow Report: Node 1 as an inside face zone;
        Node 2 as an outside face zone or external node.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'surface name',
                                      {'name': u'Surface Name',
                                       'pyname': u'surface_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'leakage component name',
                                      {'name': u'Leakage Component Name',
                                       'pyname': u'leakage_component_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'external node name',
                                      {'name': u'External Node Name',
                                       'pyname': u'external_node_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'window/door opening factor, or crack factor',
                                      {'name': u'Window/Door Opening Factor, or Crack Factor',
                                       'pyname': u'window_or_door_opening_factor_or_crack_factor',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'ventilation control mode',
                                      {'name': u'Ventilation Control Mode',
                                       'pyname': u'ventilation_control_mode',
                                       'default': u'ZoneLevel',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Temperature',
                                                           u'Enthalpy',
                                                           u'Constant',
                                                           u'ASHRAE55Adaptive',
                                                           u'CEN15251Adaptive',
                                                           u'NoVent',
                                                           u'ZoneLevel',
                                                           u'AdjacentTemperature',
                                                           u'AdjacentEnthalpy'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'ventilation control zone temperature setpoint schedule name',
                                      {'name': u'Ventilation Control Zone Temperature Setpoint Schedule Name',
                                       'pyname': u'ventilation_control_zone_temperature_setpoint_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'minimum venting open factor',
                                      {'name': u'Minimum Venting Open Factor',
                                       'pyname': u'minimum_venting_open_factor',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'indoor and outdoor temperature difference lower limit for maximum venting open factor',
                                      {'name': u'Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor',
                                       'default': 0.0,
                                       'maximum<': 100.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaC'}),
                                     (u'indoor and outdoor temperature difference upper limit for minimun venting open factor',
                                      {'name': u'Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor',
                                       'default': 100.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaC'}),
                                     (u'indoor and outdoor enthalpy difference lower limit for maximum venting open factor',
                                      {'name': u'Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor',
                                       'default': 0.0,
                                       'maximum<': 300000.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaJ/kg'}),
                                     (u'indoor and outdoor enthalpy difference upper limit for minimun venting open factor',
                                      {'name': u'Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor',
                                       'pyname': u'indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor',
                                       'default': 300000.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deltaJ/kg'}),
                                     (u'venting availability schedule name',
                                      {'name': u'Venting Availability Schedule Name',
                                       'pyname': u'venting_availability_schedule_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:MultiZone:Surface',
              'pyname': u'AirflowNetworkMultiZoneSurface',
              'required-object': False,
              'unique-object': False}

    @property
    def surface_name(self):
        """Get surface_name.

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name` Enter the name of a heat
        transfer surface.

        Args:
            value (str): value for IDD Field `Surface Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Surface Name"] = value

    @property
    def leakage_component_name(self):
        """Get leakage_component_name.

        Returns:
            str: the value of `leakage_component_name` or None if not set

        """
        return self["Leakage Component Name"]

    @leakage_component_name.setter
    def leakage_component_name(self, value=None):
        """  Corresponds to IDD field `Leakage Component Name`
        Enter the name of an Airflow Network leakage component. A leakage component is
        one of the following AirflowNetwork:Multizone objects:
        AirflowNetwork:MultiZone:Component:DetailedOpening,
        AirflowNetwork:MultiZone:Component:SimpleOpening,
        AirflowNetwork:MultiZone:Surface:Crack,
        AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea,
        AirflowNetwork:MultiZone:Component:HorizontalOpening, or
        AirflowNetwork:MultiZone:Component:ZoneExhaustFan.
        When the zone exhaust fan name is entered, any surface control fields below A3 are
        ignored when the zone exhaust fan turns on.

        Args:
            value (str): value for IDD Field `Leakage Component Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Leakage Component Name"] = value

    @property
    def external_node_name(self):
        """Get external_node_name.

        Returns:
            str: the value of `external_node_name` or None if not set

        """
        return self["External Node Name"]

    @external_node_name.setter
    def external_node_name(self, value=None):
        """  Corresponds to IDD field `External Node Name`
        Used if Wind Pressure Coefficient Type = Input in the AirflowNetwork:SimulationControl object,
        otherwise this field may be left blank.

        Args:
            value (str): value for IDD Field `External Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["External Node Name"] = value

    @property
    def window_or_door_opening_factor_or_crack_factor(self):
        """Get window_or_door_opening_factor_or_crack_factor.

        Returns:
            float: the value of `window_or_door_opening_factor_or_crack_factor` or None if not set

        """
        return self["Window/Door Opening Factor, or Crack Factor"]

    @window_or_door_opening_factor_or_crack_factor.setter
    def window_or_door_opening_factor_or_crack_factor(self, value=1.0):
        """Corresponds to IDD field `Window/Door Opening Factor, or Crack
        Factor` This field specifies a multiplier for a crack, window, or door.

        Args:
            value (float): value for IDD Field `Window/Door Opening Factor, or Crack Factor`
                Units: dimensionless
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Window/Door Opening Factor, or Crack Factor"] = value

    @property
    def ventilation_control_mode(self):
        """Get ventilation_control_mode.

        Returns:
            str: the value of `ventilation_control_mode` or None if not set

        """
        return self["Ventilation Control Mode"]

    @ventilation_control_mode.setter
    def ventilation_control_mode(self, value="ZoneLevel"):
        """  Corresponds to IDD field `Ventilation Control Mode`
        When Ventilation Control Mode = Temperature or Enthalpy, the following
        fields are used to modulate the Ventilation Open Factor for a
        window or door opening according to the parent zone's
        indoor-outdoor temperature or enthalpy difference.
        When Ventilation Control Mode = AdjacentTemperature or AdjacentEnthalpy, the following
        fields are used to modulate the Ventilation Open Factor for an interior
        window or door opening according to temperature or enthalpy difference
        between the parent zone and the adjacent zone.
        Constant: controlled by field Venting Schedule Name.
        NoVent: control will not open window or door during simulation (Ventilation Open Factor = 0).
        ZoneLevel: control will be controlled by AirflowNetwork:MultiZone:Zone
        Mode.

        Args:
            value (str): value for IDD Field `Ventilation Control Mode`
                Default value: ZoneLevel
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Ventilation Control Mode"] = value

    @property
    def ventilation_control_zone_temperature_setpoint_schedule_name(self):
        """Get ventilation_control_zone_temperature_setpoint_schedule_name.

        Returns:
            str: the value of `ventilation_control_zone_temperature_setpoint_schedule_name` or None if not set

        """
        return self[
            "Ventilation Control Zone Temperature Setpoint Schedule Name"]

    @ventilation_control_zone_temperature_setpoint_schedule_name.setter
    def ventilation_control_zone_temperature_setpoint_schedule_name(
            self,
            value=None):
        """  Corresponds to IDD field `Ventilation Control Zone Temperature Setpoint Schedule Name`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (str): value for IDD Field `Ventilation Control Zone Temperature Setpoint Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Ventilation Control Zone Temperature Setpoint Schedule Name"] = value

    @property
    def minimum_venting_open_factor(self):
        """Get minimum_venting_open_factor.

        Returns:
            float: the value of `minimum_venting_open_factor` or None if not set

        """
        return self["Minimum Venting Open Factor"]

    @minimum_venting_open_factor.setter
    def minimum_venting_open_factor(self, value=None):
        """  Corresponds to IDD field `Minimum Venting Open Factor`
        Used only if Ventilation Control Mode = Temperature or Enthalpy.

        Args:
            value (float): value for IDD Field `Minimum Venting Open Factor`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(
            self):
        """Get indoor_and_outdoor_temperature_difference_lower_limit_for_maximu
        m_venting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor(
            self,
            value=None):
        """  Corresponds to IDD field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaC
                value < 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Temperature Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(
            self):
        """Get indoor_and_outdoor_temperature_difference_upper_limit_for_minimu
        n_venting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor(
            self,
            value=100.0):
        """  Corresponds to IDD field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Temperature.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaC
                Default value: 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Temperature Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(
            self):
        """Get indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_v
        enting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor(
            self,
            value=None):
        """  Corresponds to IDD field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be less than the corresponding upper value (next field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor`
                Units: deltaJ/kg
                value < 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Enthalpy Difference Lower Limit For Maximum Venting Open Factor"] = value

    @property
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(
            self):
        """Get indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_v
        enting_open_factor.

        Returns:
            float: the value of `indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor` or None if not set

        """
        return self[
            "Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"]

    @indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor.setter
    def indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor(
            self,
            value=300000.0):
        """  Corresponds to IDD field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
        Applicable only if Ventilation Control Mode = Enthalpy.
        This value must be greater than the corresponding lower value (previous field).

        Args:
            value (float): value for IDD Field `Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor`
                Units: deltaJ/kg
                Default value: 300000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Indoor and Outdoor Enthalpy Difference Upper Limit for Minimun Venting Open Factor"] = value

    @property
    def venting_availability_schedule_name(self):
        """Get venting_availability_schedule_name.

        Returns:
            str: the value of `venting_availability_schedule_name` or None if not set

        """
        return self["Venting Availability Schedule Name"]

    @venting_availability_schedule_name.setter
    def venting_availability_schedule_name(self, value=None):
        """  Corresponds to IDD field `Venting Availability Schedule Name`
        Non-zero schedule value means venting is allowed if other venting control conditions are
        satisfied. A zero (or negative) schedule value means venting is not allowed under any
        circumstances. The schedule values should be greater than or equal to 0 and less than or
        equal to 1. If this schedule is not specified then venting is allowed if
        other venting control conditions are satisfied.
        Not used if Ventilation Control Mode = NoVent or ZoneLevel.

        Args:
            value (str): value for IDD Field `Venting Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Venting Availability Schedule Name"] = value




class AirflowNetworkMultiZoneReferenceCrackConditions(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:ReferenceCrackConditions`
        This object specifies the conditions under which the air mass flow coefficient was measured.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'reference temperature',
                                      {'name': u'Reference Temperature',
                                       'pyname': u'reference_temperature',
                                       'default': 20.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'C'}),
                                     (u'reference barometric pressure',
                                      {'name': u'Reference Barometric Pressure',
                                       'pyname': u'reference_barometric_pressure',
                                       'default': 101325.0,
                                       'maximum': 120000.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 31000.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'Pa'}),
                                     (u'reference humidity ratio',
                                      {'name': u'Reference Humidity Ratio',
                                       'pyname': u'reference_humidity_ratio',
                                       'default': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kgWater/kgDryAir'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:MultiZone:ReferenceCrackConditions',
              'pyname': u'AirflowNetworkMultiZoneReferenceCrackConditions',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def reference_temperature(self):
        """Get reference_temperature.

        Returns:
            float: the value of `reference_temperature` or None if not set

        """
        return self["Reference Temperature"]

    @reference_temperature.setter
    def reference_temperature(self, value=20.0):
        """Corresponds to IDD field `Reference Temperature` Enter the reference
        temperature under which the surface crack data were obtained.

        Args:
            value (float): value for IDD Field `Reference Temperature`
                Units: C
                Default value: 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Reference Temperature"] = value

    @property
    def reference_barometric_pressure(self):
        """Get reference_barometric_pressure.

        Returns:
            float: the value of `reference_barometric_pressure` or None if not set

        """
        return self["Reference Barometric Pressure"]

    @reference_barometric_pressure.setter
    def reference_barometric_pressure(self, value=101325.0):
        """Corresponds to IDD field `Reference Barometric Pressure` Enter the
        reference barometric pressure under which the surface crack data were
        obtained.

        Args:
            value (float): value for IDD Field `Reference Barometric Pressure`
                Units: Pa
                IP-Units: inHg
                Default value: 101325.0
                value >= 31000.0
                value <= 120000.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Reference Barometric Pressure"] = value

    @property
    def reference_humidity_ratio(self):
        """Get reference_humidity_ratio.

        Returns:
            float: the value of `reference_humidity_ratio` or None if not set

        """
        return self["Reference Humidity Ratio"]

    @reference_humidity_ratio.setter
    def reference_humidity_ratio(self, value=None):
        """Corresponds to IDD field `Reference Humidity Ratio` Enter the
        reference humidity ratio under which the surface crack data were
        obtained.

        Args:
            value (float): value for IDD Field `Reference Humidity Ratio`
                Units: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Reference Humidity Ratio"] = value




class AirflowNetworkMultiZoneSurfaceCrack(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface:Crack`
        This object specifies the properties of airflow through a crack.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'air mass flow coefficient at reference conditions',
                                      {'name': u'Air Mass Flow Coefficient at Reference Conditions',
                                       'pyname': u'air_mass_flow_coefficient_at_reference_conditions',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s'}),
                                     (u'air mass flow exponent',
                                      {'name': u'Air Mass Flow Exponent',
                                       'pyname': u'air_mass_flow_exponent',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'reference crack conditions',
                                      {'name': u'Reference Crack Conditions',
                                       'pyname': u'reference_crack_conditions',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 3,
              'name': u'AirflowNetwork:MultiZone:Surface:Crack',
              'pyname': u'AirflowNetworkMultiZoneSurfaceCrack',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def air_mass_flow_coefficient_at_reference_conditions(self):
        """Get air_mass_flow_coefficient_at_reference_conditions.

        Returns:
            float: the value of `air_mass_flow_coefficient_at_reference_conditions` or None if not set

        """
        return self["Air Mass Flow Coefficient at Reference Conditions"]

    @air_mass_flow_coefficient_at_reference_conditions.setter
    def air_mass_flow_coefficient_at_reference_conditions(self, value=None):
        """Corresponds to IDD field `Air Mass Flow Coefficient at Reference
        Conditions` Enter the air mass flow coefficient at the conditions
        defined in the Reference Crack Conditions object. Defined at 1 Pa
        pressure difference across this crack.

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient at Reference Conditions`
                Units: kg/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Mass Flow Coefficient at Reference Conditions"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent.

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set

        """
        return self["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65):
        """Corresponds to IDD field `Air Mass Flow Exponent` Enter the air mass
        flow exponent for the surface crack.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Mass Flow Exponent"] = value

    @property
    def reference_crack_conditions(self):
        """Get reference_crack_conditions.

        Returns:
            str: the value of `reference_crack_conditions` or None if not set

        """
        return self["Reference Crack Conditions"]

    @reference_crack_conditions.setter
    def reference_crack_conditions(self, value=None):
        """  Corresponds to IDD field `Reference Crack Conditions`
        Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with
        the air mass flow coefficient entered above.

        Args:
            value (str): value for IDD Field `Reference Crack Conditions`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Crack Conditions"] = value




class AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea`
        This object is used to define surface air leakage.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'effective leakage area',
                                      {'name': u'Effective Leakage Area',
                                       'pyname': u'effective_leakage_area',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm2'}),
                                     (u'discharge coefficient',
                                      {'name': u'Discharge Coefficient',
                                       'pyname': u'discharge_coefficient',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'reference pressure difference',
                                      {'name': u'Reference Pressure Difference',
                                       'pyname': u'reference_pressure_difference',
                                       'default': 4.0,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'Pa'}),
                                     (u'air mass flow exponent',
                                      {'name': u'Air Mass Flow Exponent',
                                       'pyname': u'air_mass_flow_exponent',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 5,
              'name': u'AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea',
              'pyname': u'AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def effective_leakage_area(self):
        """Get effective_leakage_area.

        Returns:
            float: the value of `effective_leakage_area` or None if not set

        """
        return self["Effective Leakage Area"]

    @effective_leakage_area.setter
    def effective_leakage_area(self, value=None):
        """Corresponds to IDD field `Effective Leakage Area` Enter the
        effective leakage area.

        Args:
            value (float): value for IDD Field `Effective Leakage Area`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Effective Leakage Area"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient.

        Returns:
            float: the value of `discharge_coefficient` or None if not set

        """
        return self["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=1.0):
        """Corresponds to IDD field `Discharge Coefficient` Enter the
        coefficient used in the air mass flow equation.

        Args:
            value (float): value for IDD Field `Discharge Coefficient`
                Units: dimensionless
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient"] = value

    @property
    def reference_pressure_difference(self):
        """Get reference_pressure_difference.

        Returns:
            float: the value of `reference_pressure_difference` or None if not set

        """
        return self["Reference Pressure Difference"]

    @reference_pressure_difference.setter
    def reference_pressure_difference(self, value=4.0):
        """Corresponds to IDD field `Reference Pressure Difference` Enter the
        pressure difference used to define the air mass flow coefficient and
        exponent.

        Args:
            value (float): value for IDD Field `Reference Pressure Difference`
                Units: Pa
                Default value: 4.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Reference Pressure Difference"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent.

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set

        """
        return self["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65):
        """Corresponds to IDD field `Air Mass Flow Exponent` Enter the exponent
        used in the air mass flow equation.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Mass Flow Exponent"] = value




class AirflowNetworkMultiZoneComponentDetailedOpening(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:DetailedOpening`
        This object specifies the properties of airflow through windows and doors (window, door and
        glass door heat transfer subsurfaces) when they are closed or open.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'air mass flow coefficient when opening is closed',
                                      {'name': u'Air Mass Flow Coefficient When Opening is Closed',
                                       'pyname': u'air_mass_flow_coefficient_when_opening_is_closed',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s-m'}),
                                     (u'air mass flow exponent when opening is closed',
                                      {'name': u'Air Mass Flow Exponent When Opening is Closed',
                                       'pyname': u'air_mass_flow_exponent_when_opening_is_closed',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'type of rectanguler large vertical opening (lvo)',
                                      {'name': u'Type of Rectanguler Large Vertical Opening (LVO)',
                                       'pyname': u'type_of_rectanguler_large_vertical_opening_lvo',
                                       'default': u'NonPivoted',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'NonPivoted',
                                                           u'HorizontallyPivoted'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'extra crack length or height of pivoting axis',
                                      {'name': u'Extra Crack Length or Height of Pivoting Axis',
                                       'pyname': u'extra_crack_length_or_height_of_pivoting_axis',
                                       'default': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'number of sets of opening factor data',
                                      {'name': u'Number of Sets of Opening Factor Data',
                                       'pyname': u'number_of_sets_of_opening_factor_data',
                                       'maximum': 4,
                                       'required-field': True,
                                       'autosizable': False,
                                       'minimum': 2,
                                       'autocalculatable': False,
                                       'type': u'integer'}),
                                     (u'opening factor 1',
                                      {'name': u'Opening Factor 1',
                                       'pyname': u'opening_factor_1',
                                       'default': 0.0,
                                       'maximum': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'discharge coefficient for opening factor 1',
                                      {'name': u'Discharge Coefficient for Opening Factor 1',
                                       'pyname': u'discharge_coefficient_for_opening_factor_1',
                                       'default': 0.001,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'width factor for opening factor 1',
                                      {'name': u'Width Factor for Opening Factor 1',
                                       'pyname': u'width_factor_for_opening_factor_1',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'height factor for opening factor 1',
                                      {'name': u'Height Factor for Opening Factor 1',
                                       'pyname': u'height_factor_for_opening_factor_1',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'start height factor for opening factor 1',
                                      {'name': u'Start Height Factor for Opening Factor 1',
                                       'pyname': u'start_height_factor_for_opening_factor_1',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'opening factor 2',
                                      {'name': u'Opening Factor 2',
                                       'pyname': u'opening_factor_2',
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'discharge coefficient for opening factor 2',
                                      {'name': u'Discharge Coefficient for Opening Factor 2',
                                       'pyname': u'discharge_coefficient_for_opening_factor_2',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'width factor for opening factor 2',
                                      {'name': u'Width Factor for Opening Factor 2',
                                       'pyname': u'width_factor_for_opening_factor_2',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'height factor for opening factor 2',
                                      {'name': u'Height Factor for Opening Factor 2',
                                       'pyname': u'height_factor_for_opening_factor_2',
                                       'default': 1.0,
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'start height factor for opening factor 2',
                                      {'name': u'Start Height Factor for Opening Factor 2',
                                       'pyname': u'start_height_factor_for_opening_factor_2',
                                       'default': 0.0,
                                       'maximum<': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'opening factor 3',
                                      {'name': u'Opening Factor 3',
                                       'pyname': u'opening_factor_3',
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'discharge coefficient for opening factor 3',
                                      {'name': u'Discharge Coefficient for Opening Factor 3',
                                       'pyname': u'discharge_coefficient_for_opening_factor_3',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'width factor for opening factor 3',
                                      {'name': u'Width Factor for Opening Factor 3',
                                       'pyname': u'width_factor_for_opening_factor_3',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'height factor for opening factor 3',
                                      {'name': u'Height Factor for Opening Factor 3',
                                       'pyname': u'height_factor_for_opening_factor_3',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'start height factor for opening factor 3',
                                      {'name': u'Start Height Factor for Opening Factor 3',
                                       'pyname': u'start_height_factor_for_opening_factor_3',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'opening factor 4',
                                      {'name': u'Opening Factor 4',
                                       'pyname': u'opening_factor_4',
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'discharge coefficient for opening factor 4',
                                      {'name': u'Discharge Coefficient for Opening Factor 4',
                                       'pyname': u'discharge_coefficient_for_opening_factor_4',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'width factor for opening factor 4',
                                      {'name': u'Width Factor for Opening Factor 4',
                                       'pyname': u'width_factor_for_opening_factor_4',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'height factor for opening factor 4',
                                      {'name': u'Height Factor for Opening Factor 4',
                                       'pyname': u'height_factor_for_opening_factor_4',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'start height factor for opening factor 4',
                                      {'name': u'Start Height Factor for Opening Factor 4',
                                       'pyname': u'start_height_factor_for_opening_factor_4',
                                       'default': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 16,
              'name': u'AirflowNetwork:MultiZone:Component:DetailedOpening',
              'pyname': u'AirflowNetworkMultiZoneComponentDetailedOpening',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed.

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set

        """
        return self["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD field `Air Mass Flow Coefficient When Opening is Closed`
        Defined at 1 Pa per meter of crack length. Enter the coefficient used in the following
        equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When Opening is Closed`
                Units: kg/s-m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Coefficient When Opening is Closed"] = value

    @property
    def air_mass_flow_exponent_when_opening_is_closed(self):
        """Get air_mass_flow_exponent_when_opening_is_closed.

        Returns:
            float: the value of `air_mass_flow_exponent_when_opening_is_closed` or None if not set

        """
        return self["Air Mass Flow Exponent When Opening is Closed"]

    @air_mass_flow_exponent_when_opening_is_closed.setter
    def air_mass_flow_exponent_when_opening_is_closed(self, value=0.65):
        """  Corresponds to IDD field `Air Mass Flow Exponent When Opening is Closed`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When Opening is Closed`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Exponent When Opening is Closed"] = value

    @property
    def type_of_rectanguler_large_vertical_opening_lvo(self):
        """Get type_of_rectanguler_large_vertical_opening_lvo.

        Returns:
            str: the value of `type_of_rectanguler_large_vertical_opening_lvo` or None if not set

        """
        return self["Type of Rectanguler Large Vertical Opening (LVO)"]

    @type_of_rectanguler_large_vertical_opening_lvo.setter
    def type_of_rectanguler_large_vertical_opening_lvo(
            self,
            value="NonPivoted"):
        """  Corresponds to IDD field `Type of Rectanguler Large Vertical Opening (LVO)`
        Select the type of vertical opening: Non-pivoted opening or Horizontally pivoted opening.

        Args:
            value (str): value for IDD Field `Type of Rectanguler Large Vertical Opening (LVO)`
                Default value: NonPivoted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Type of Rectanguler Large Vertical Opening (LVO)"] = value

    @property
    def extra_crack_length_or_height_of_pivoting_axis(self):
        """Get extra_crack_length_or_height_of_pivoting_axis.

        Returns:
            float: the value of `extra_crack_length_or_height_of_pivoting_axis` or None if not set

        """
        return self["Extra Crack Length or Height of Pivoting Axis"]

    @extra_crack_length_or_height_of_pivoting_axis.setter
    def extra_crack_length_or_height_of_pivoting_axis(self, value=None):
        """  Corresponds to IDD field `Extra Crack Length or Height of Pivoting Axis`
        Extra crack length is used for LVO Non-pivoted type with multiple openable parts.
        Height of pivoting axis is used for LVO Horizontally pivoted type.
        Specifies window or door characteristics that depend on the LVO type.
        For Non-pivoted Type (rectangular windows and doors), this field is the extra crack length
        in meters due to multiple openable parts, if present.  Extra here means in addition
        to the length of the cracks on the top, bottom and sides of the window/door.
        For Horizontally pivoted Type, this field gives the height of the
        pivoting axis measured from the bottom of the glazed part of the window (m).

        Args:
            value (float): value for IDD Field `Extra Crack Length or Height of Pivoting Axis`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Extra Crack Length or Height of Pivoting Axis"] = value

    @property
    def number_of_sets_of_opening_factor_data(self):
        """Get number_of_sets_of_opening_factor_data.

        Returns:
            int: the value of `number_of_sets_of_opening_factor_data` or None if not set

        """
        return self["Number of Sets of Opening Factor Data"]

    @number_of_sets_of_opening_factor_data.setter
    def number_of_sets_of_opening_factor_data(self, value=None):
        """Corresponds to IDD field `Number of Sets of Opening Factor Data`
        Enter the number of the following sets of data for opening factor,
        discharge coefficient, width factor, height factor, and start height
        factor.

        Args:
            value (int): value for IDD Field `Number of Sets of Opening Factor Data`
                value >= 2
                value <= 4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Number of Sets of Opening Factor Data"] = value

    @property
    def opening_factor_1(self):
        """Get opening_factor_1.

        Returns:
            float: the value of `opening_factor_1` or None if not set

        """
        return self["Opening Factor 1"]

    @opening_factor_1.setter
    def opening_factor_1(self, value=None):
        """  Corresponds to IDD field `Opening Factor 1`
        This value must be specified as 0.

        Args:
            value (float): value for IDD Field `Opening Factor 1`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Opening Factor 1"] = value

    @property
    def discharge_coefficient_for_opening_factor_1(self):
        """Get discharge_coefficient_for_opening_factor_1.

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_1` or None if not set

        """
        return self["Discharge Coefficient for Opening Factor 1"]

    @discharge_coefficient_for_opening_factor_1.setter
    def discharge_coefficient_for_opening_factor_1(self, value=0.001):
        """Corresponds to IDD field `Discharge Coefficient for Opening Factor
        1` The Discharge Coefficient indicates the fractional effectiveness for
        air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 1`
                Units: dimensionless
                Default value: 0.001
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient for Opening Factor 1"] = value

    @property
    def width_factor_for_opening_factor_1(self):
        """Get width_factor_for_opening_factor_1.

        Returns:
            float: the value of `width_factor_for_opening_factor_1` or None if not set

        """
        return self["Width Factor for Opening Factor 1"]

    @width_factor_for_opening_factor_1.setter
    def width_factor_for_opening_factor_1(self, value=None):
        """Corresponds to IDD field `Width Factor for Opening Factor 1` The
        Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 1`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Width Factor for Opening Factor 1"] = value

    @property
    def height_factor_for_opening_factor_1(self):
        """Get height_factor_for_opening_factor_1.

        Returns:
            float: the value of `height_factor_for_opening_factor_1` or None if not set

        """
        return self["Height Factor for Opening Factor 1"]

    @height_factor_for_opening_factor_1.setter
    def height_factor_for_opening_factor_1(self, value=None):
        """Corresponds to IDD field `Height Factor for Opening Factor 1` The
        Height Factor is the opening height divided by the window or door
        height.

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 1`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Height Factor for Opening Factor 1"] = value

    @property
    def start_height_factor_for_opening_factor_1(self):
        """Get start_height_factor_for_opening_factor_1.

        Returns:
            float: the value of `start_height_factor_for_opening_factor_1` or None if not set

        """
        return self["Start Height Factor for Opening Factor 1"]

    @start_height_factor_for_opening_factor_1.setter
    def start_height_factor_for_opening_factor_1(self, value=None):
        """  Corresponds to IDD field `Start Height Factor for Opening Factor 1`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 1`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Start Height Factor for Opening Factor 1"] = value

    @property
    def opening_factor_2(self):
        """Get opening_factor_2.

        Returns:
            float: the value of `opening_factor_2` or None if not set

        """
        return self["Opening Factor 2"]

    @opening_factor_2.setter
    def opening_factor_2(self, value=None):
        """  Corresponds to IDD field `Opening Factor 2`
        If Number of Sets of Opening Factor Data = 2, this value must be 1.0.
        If Number of Sets of Opening Factor Data = 3, this value must be less than 1.0.
        If Number of Sets of Opening Factor Data = 4, this value must be less than the
        value entered for Opening factor 3 and greater than the value entered
        for Opening factor 1.

        Args:
            value (float): value for IDD Field `Opening Factor 2`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Opening Factor 2"] = value

    @property
    def discharge_coefficient_for_opening_factor_2(self):
        """Get discharge_coefficient_for_opening_factor_2.

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_2` or None if not set

        """
        return self["Discharge Coefficient for Opening Factor 2"]

    @discharge_coefficient_for_opening_factor_2.setter
    def discharge_coefficient_for_opening_factor_2(self, value=1.0):
        """Corresponds to IDD field `Discharge Coefficient for Opening Factor
        2` The Discharge Coefficient indicates the fractional effectiveness for
        air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 2`
                Units: dimensionless
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient for Opening Factor 2"] = value

    @property
    def width_factor_for_opening_factor_2(self):
        """Get width_factor_for_opening_factor_2.

        Returns:
            float: the value of `width_factor_for_opening_factor_2` or None if not set

        """
        return self["Width Factor for Opening Factor 2"]

    @width_factor_for_opening_factor_2.setter
    def width_factor_for_opening_factor_2(self, value=1.0):
        """Corresponds to IDD field `Width Factor for Opening Factor 2` The
        Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 2`
                Units: dimensionless
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Width Factor for Opening Factor 2"] = value

    @property
    def height_factor_for_opening_factor_2(self):
        """Get height_factor_for_opening_factor_2.

        Returns:
            float: the value of `height_factor_for_opening_factor_2` or None if not set

        """
        return self["Height Factor for Opening Factor 2"]

    @height_factor_for_opening_factor_2.setter
    def height_factor_for_opening_factor_2(self, value=1.0):
        """Corresponds to IDD field `Height Factor for Opening Factor 2` The
        Height Factor is the opening height divided by the window or door
        height.

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 2`
                Units: dimensionless
                Default value: 1.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Height Factor for Opening Factor 2"] = value

    @property
    def start_height_factor_for_opening_factor_2(self):
        """Get start_height_factor_for_opening_factor_2.

        Returns:
            float: the value of `start_height_factor_for_opening_factor_2` or None if not set

        """
        return self["Start Height Factor for Opening Factor 2"]

    @start_height_factor_for_opening_factor_2.setter
    def start_height_factor_for_opening_factor_2(self, value=None):
        """  Corresponds to IDD field `Start Height Factor for Opening Factor 2`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 2`
                Units: dimensionless
                value < 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Start Height Factor for Opening Factor 2"] = value

    @property
    def opening_factor_3(self):
        """Get opening_factor_3.

        Returns:
            float: the value of `opening_factor_3` or None if not set

        """
        return self["Opening Factor 3"]

    @opening_factor_3.setter
    def opening_factor_3(self, value=None):
        """  Corresponds to IDD field `Opening Factor 3`
        If Number of Sets of Opening Factor Data = 3, this value must be 1.0.
        If Number of Sets of Opening Factor Data = 4, this value must be less than 1.0,
        and greater than value entered for Opening factor 2.

        Args:
            value (float): value for IDD Field `Opening Factor 3`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Opening Factor 3"] = value

    @property
    def discharge_coefficient_for_opening_factor_3(self):
        """Get discharge_coefficient_for_opening_factor_3.

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_3` or None if not set

        """
        return self["Discharge Coefficient for Opening Factor 3"]

    @discharge_coefficient_for_opening_factor_3.setter
    def discharge_coefficient_for_opening_factor_3(self, value=None):
        """Corresponds to IDD field `Discharge Coefficient for Opening Factor
        3` The Discharge Coefficient indicates the fractional effectiveness for
        air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 3`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient for Opening Factor 3"] = value

    @property
    def width_factor_for_opening_factor_3(self):
        """Get width_factor_for_opening_factor_3.

        Returns:
            float: the value of `width_factor_for_opening_factor_3` or None if not set

        """
        return self["Width Factor for Opening Factor 3"]

    @width_factor_for_opening_factor_3.setter
    def width_factor_for_opening_factor_3(self, value=None):
        """Corresponds to IDD field `Width Factor for Opening Factor 3` The
        Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 3`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Width Factor for Opening Factor 3"] = value

    @property
    def height_factor_for_opening_factor_3(self):
        """Get height_factor_for_opening_factor_3.

        Returns:
            float: the value of `height_factor_for_opening_factor_3` or None if not set

        """
        return self["Height Factor for Opening Factor 3"]

    @height_factor_for_opening_factor_3.setter
    def height_factor_for_opening_factor_3(self, value=None):
        """Corresponds to IDD field `Height Factor for Opening Factor 3` The
        Height Factor is the opening height divided by the window or door
        height.

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 3`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Height Factor for Opening Factor 3"] = value

    @property
    def start_height_factor_for_opening_factor_3(self):
        """Get start_height_factor_for_opening_factor_3.

        Returns:
            float: the value of `start_height_factor_for_opening_factor_3` or None if not set

        """
        return self["Start Height Factor for Opening Factor 3"]

    @start_height_factor_for_opening_factor_3.setter
    def start_height_factor_for_opening_factor_3(self, value=None):
        """  Corresponds to IDD field `Start Height Factor for Opening Factor 3`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 3`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Start Height Factor for Opening Factor 3"] = value

    @property
    def opening_factor_4(self):
        """Get opening_factor_4.

        Returns:
            float: the value of `opening_factor_4` or None if not set

        """
        return self["Opening Factor 4"]

    @opening_factor_4.setter
    def opening_factor_4(self, value=None):
        """  Corresponds to IDD field `Opening Factor 4`
        If Number of Sets of Opening Factor Data = 4, this value must be 1.0

        Args:
            value (float): value for IDD Field `Opening Factor 4`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Opening Factor 4"] = value

    @property
    def discharge_coefficient_for_opening_factor_4(self):
        """Get discharge_coefficient_for_opening_factor_4.

        Returns:
            float: the value of `discharge_coefficient_for_opening_factor_4` or None if not set

        """
        return self["Discharge Coefficient for Opening Factor 4"]

    @discharge_coefficient_for_opening_factor_4.setter
    def discharge_coefficient_for_opening_factor_4(self, value=None):
        """Corresponds to IDD field `Discharge Coefficient for Opening Factor
        4` The Discharge Coefficient indicates the fractional effectiveness for
        air flow through a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Opening Factor 4`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient for Opening Factor 4"] = value

    @property
    def width_factor_for_opening_factor_4(self):
        """Get width_factor_for_opening_factor_4.

        Returns:
            float: the value of `width_factor_for_opening_factor_4` or None if not set

        """
        return self["Width Factor for Opening Factor 4"]

    @width_factor_for_opening_factor_4.setter
    def width_factor_for_opening_factor_4(self, value=None):
        """Corresponds to IDD field `Width Factor for Opening Factor 4` The
        Width Factor is the opening width divided by the window or door width.

        Args:
            value (float): value for IDD Field `Width Factor for Opening Factor 4`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Width Factor for Opening Factor 4"] = value

    @property
    def height_factor_for_opening_factor_4(self):
        """Get height_factor_for_opening_factor_4.

        Returns:
            float: the value of `height_factor_for_opening_factor_4` or None if not set

        """
        return self["Height Factor for Opening Factor 4"]

    @height_factor_for_opening_factor_4.setter
    def height_factor_for_opening_factor_4(self, value=None):
        """Corresponds to IDD field `Height Factor for Opening Factor 4` The
        Height Factor is the opening height divided by the window or door
        height.

        Args:
            value (float): value for IDD Field `Height Factor for Opening Factor 4`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Height Factor for Opening Factor 4"] = value

    @property
    def start_height_factor_for_opening_factor_4(self):
        """Get start_height_factor_for_opening_factor_4.

        Returns:
            float: the value of `start_height_factor_for_opening_factor_4` or None if not set

        """
        return self["Start Height Factor for Opening Factor 4"]

    @start_height_factor_for_opening_factor_4.setter
    def start_height_factor_for_opening_factor_4(self, value=None):
        """  Corresponds to IDD field `Start Height Factor for Opening Factor 4`
        The Start Height Factor is the Start Height divided by the window or door height.
        Start Height is the distance between the bottom of the window or door and the
        bottom of the window or door opening. The sum of the Height Factor and the Start Height
        Factor must be less than 1.0 in order to have the opening within the window or door
        dimensions.

        Args:
            value (float): value for IDD Field `Start Height Factor for Opening Factor 4`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Start Height Factor for Opening Factor 4"] = value




class AirflowNetworkMultiZoneComponentSimpleOpening(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:SimpleOpening`
        This object specifies the properties of air flow through windows and doors (window, door and
        glass door heat transfer subsurfaces) when they are closed or open.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'air mass flow coefficient when opening is closed',
                                      {'name': u'Air Mass Flow Coefficient When Opening is Closed',
                                       'pyname': u'air_mass_flow_coefficient_when_opening_is_closed',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s-m'}),
                                     (u'air mass flow exponent when opening is closed',
                                      {'name': u'Air Mass Flow Exponent When Opening is Closed',
                                       'pyname': u'air_mass_flow_exponent_when_opening_is_closed',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'minimum density difference for two-way flow',
                                      {'name': u'Minimum Density Difference for Two-Way Flow',
                                       'pyname': u'minimum_density_difference_for_twoway_flow',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/m3'}),
                                     (u'discharge coefficient',
                                      {'name': u'Discharge Coefficient',
                                       'pyname': u'discharge_coefficient',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 5,
              'name': u'AirflowNetwork:MultiZone:Component:SimpleOpening',
              'pyname': u'AirflowNetworkMultiZoneComponentSimpleOpening',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed.

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set

        """
        return self["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD field `Air Mass Flow Coefficient When Opening is Closed`
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When Opening is Closed`
                Units: kg/s-m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Coefficient When Opening is Closed"] = value

    @property
    def air_mass_flow_exponent_when_opening_is_closed(self):
        """Get air_mass_flow_exponent_when_opening_is_closed.

        Returns:
            float: the value of `air_mass_flow_exponent_when_opening_is_closed` or None if not set

        """
        return self["Air Mass Flow Exponent When Opening is Closed"]

    @air_mass_flow_exponent_when_opening_is_closed.setter
    def air_mass_flow_exponent_when_opening_is_closed(self, value=0.65):
        """  Corresponds to IDD field `Air Mass Flow Exponent When Opening is Closed`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening (window or door) is closed.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When Opening is Closed`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Exponent When Opening is Closed"] = value

    @property
    def minimum_density_difference_for_twoway_flow(self):
        """Get minimum_density_difference_for_twoway_flow.

        Returns:
            float: the value of `minimum_density_difference_for_twoway_flow` or None if not set

        """
        return self["Minimum Density Difference for Two-Way Flow"]

    @minimum_density_difference_for_twoway_flow.setter
    def minimum_density_difference_for_twoway_flow(self, value=None):
        """  Corresponds to IDD field `Minimum Density Difference for Two-Way Flow`
        Enter the minimum density difference above which two-way flow may occur due to stack effect.

        Args:
            value (float): value for IDD Field `Minimum Density Difference for Two-Way Flow`
                Units: kg/m3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Minimum Density Difference for Two-Way Flow"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient.

        Returns:
            float: the value of `discharge_coefficient` or None if not set

        """
        return self["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=None):
        """Corresponds to IDD field `Discharge Coefficient` The Discharge
        Coefficient indicates the fractional effectiveness for air flow through
        a window or door at that Opening Factor.

        Args:
            value (float): value for IDD Field `Discharge Coefficient`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient"] = value




class AirflowNetworkMultiZoneComponentHorizontalOpening(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:HorizontalOpening`
        This object specifies the properties of air flow through a horizontal opening
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'air mass flow coefficient when opening is closed',
                                      {'name': u'Air Mass Flow Coefficient When Opening is Closed',
                                       'pyname': u'air_mass_flow_coefficient_when_opening_is_closed',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s-m'}),
                                     (u'air mass flow exponent when opening is closed',
                                      {'name': u'Air Mass Flow Exponent When Opening is Closed',
                                       'pyname': u'air_mass_flow_exponent_when_opening_is_closed',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'sloping plane angle',
                                      {'name': u'Sloping Plane Angle',
                                       'pyname': u'sloping_plane_angle',
                                       'default': 90.0,
                                       'minimum>': 0.0,
                                       'maximum': 90.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'discharge coefficient',
                                      {'name': u'Discharge Coefficient',
                                       'pyname': u'discharge_coefficient',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 5,
              'name': u'AirflowNetwork:MultiZone:Component:HorizontalOpening',
              'pyname': u'AirflowNetworkMultiZoneComponentHorizontalOpening',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def air_mass_flow_coefficient_when_opening_is_closed(self):
        """Get air_mass_flow_coefficient_when_opening_is_closed.

        Returns:
            float: the value of `air_mass_flow_coefficient_when_opening_is_closed` or None if not set

        """
        return self["Air Mass Flow Coefficient When Opening is Closed"]

    @air_mass_flow_coefficient_when_opening_is_closed.setter
    def air_mass_flow_coefficient_when_opening_is_closed(self, value=None):
        """  Corresponds to IDD field `Air Mass Flow Coefficient When Opening is Closed`
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation:
        Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening is closed.

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When Opening is Closed`
                Units: kg/s-m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Coefficient When Opening is Closed"] = value

    @property
    def air_mass_flow_exponent_when_opening_is_closed(self):
        """Get air_mass_flow_exponent_when_opening_is_closed.

        Returns:
            float: the value of `air_mass_flow_exponent_when_opening_is_closed` or None if not set

        """
        return self["Air Mass Flow Exponent When Opening is Closed"]

    @air_mass_flow_exponent_when_opening_is_closed.setter
    def air_mass_flow_exponent_when_opening_is_closed(self, value=0.65):
        """  Corresponds to IDD field `Air Mass Flow Exponent When Opening is Closed`
        Enter the exponent used in the following equation:
        Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when opening is closed.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When Opening is Closed`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Exponent When Opening is Closed"] = value

    @property
    def sloping_plane_angle(self):
        """Get sloping_plane_angle.

        Returns:
            float: the value of `sloping_plane_angle` or None if not set

        """
        return self["Sloping Plane Angle"]

    @sloping_plane_angle.setter
    def sloping_plane_angle(self, value=90.0):
        """  Corresponds to IDD field `Sloping Plane Angle`
        Sloping plane angle = 90 is equivalent to fully open.

        Args:
            value (float): value for IDD Field `Sloping Plane Angle`
                Units: deg
                Default value: 90.0
                value <= 90.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Sloping Plane Angle"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient.

        Returns:
            float: the value of `discharge_coefficient` or None if not set

        """
        return self["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=None):
        """Corresponds to IDD field `Discharge Coefficient` The Discharge
        Coefficient indicates the fractional effectiveness for air flow through
        the opening at that Opening Factor.

        Args:
            value (float): value for IDD Field `Discharge Coefficient`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Discharge Coefficient"] = value




class AirflowNetworkMultiZoneComponentZoneExhaustFan(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:Component:ZoneExhaustFan`
        This object specifies the additional properties for a zone exhaust fan
        to perform multizone airflow calculations.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'air mass flow coefficient when the zone exhaust fan is off at reference conditions',
                                      {'name': u'Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions',
                                       'pyname': u'air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s'}),
                                     (u'air mass flow exponent when the zone exhaust fan is off',
                                      {'name': u'Air Mass Flow Exponent When the Zone Exhaust Fan is Off',
                                       'pyname': u'air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'reference crack conditions',
                                      {'name': u'Reference Crack Conditions',
                                       'pyname': u'reference_crack_conditions',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 3,
              'name': u'AirflowNetwork:MultiZone:Component:ZoneExhaustFan',
              'pyname': u'AirflowNetworkMultiZoneComponentZoneExhaustFan',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD field `Name`
        Enter the name of a Fan:ZoneExhaust object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Name"] = value

    @property
    def air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions(
            self):
        """Get air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_re
        ference_conditions.

        Returns:
            float: the value of `air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions` or None if not set

        """
        return self[
            "Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"]

    @air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions.setter
    def air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions(
            self,
            value=None):
        """  Corresponds to IDD field `Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions`
        Enter the air mass flow coefficient at the conditions defined
        in the Reference Crack Conditions object.
        Defined at 1 Pa pressure difference. Enter the coefficient used in the following
        equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when the fan is off.

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions`
                Units: kg/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Air Mass Flow Coefficient When the Zone Exhaust Fan is Off at Reference Conditions"] = value

    @property
    def air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off(self):
        """Get air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off.

        Returns:
            float: the value of `air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off` or None if not set

        """
        return self["Air Mass Flow Exponent When the Zone Exhaust Fan is Off"]

    @air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off.setter
    def air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off(
            self,
            value=0.65):
        """  Corresponds to IDD field `Air Mass Flow Exponent When the Zone Exhaust Fan is Off`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent.
        Used only when the fan is off.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent When the Zone Exhaust Fan is Off`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Exponent When the Zone Exhaust Fan is Off"] = value

    @property
    def reference_crack_conditions(self):
        """Get reference_crack_conditions.

        Returns:
            str: the value of `reference_crack_conditions` or None if not set

        """
        return self["Reference Crack Conditions"]

    @reference_crack_conditions.setter
    def reference_crack_conditions(self, value=None):
        """  Corresponds to IDD field `Reference Crack Conditions`
        Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with
        the air mass flow coefficient entered above.

        Args:
            value (str): value for IDD Field `Reference Crack Conditions`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Reference Crack Conditions"] = value




class AirflowNetworkMultiZoneExternalNode(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:ExternalNode`
        This object defines outdoor environmental conditions outside of the building.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'external node height',
                                      {'name': u'External Node Height',
                                       'pyname': u'external_node_height',
                                       'default': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'wind pressure coefficient values object name',
                                      {'name': u'Wind Pressure Coefficient Values Object Name',
                                       'pyname': u'wind_pressure_coefficient_values_object_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 3,
              'name': u'AirflowNetwork:MultiZone:ExternalNode',
              'pyname': u'AirflowNetworkMultiZoneExternalNode',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.
        This node name will be referenced by a particular building facade.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def external_node_height(self):
        """Get external_node_height.

        Returns:
            float: the value of `external_node_height` or None if not set

        """
        return self["External Node Height"]

    @external_node_height.setter
    def external_node_height(self, value=None):
        """Corresponds to IDD field `External Node Height` Designates the
        reference height used to calculate relative pressure.

        Args:
            value (float): value for IDD Field `External Node Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["External Node Height"] = value

    @property
    def wind_pressure_coefficient_values_object_name(self):
        """Get wind_pressure_coefficient_values_object_name.

        Returns:
            str: the value of `wind_pressure_coefficient_values_object_name` or None if not set

        """
        return self["Wind Pressure Coefficient Values Object Name"]

    @wind_pressure_coefficient_values_object_name.setter
    def wind_pressure_coefficient_values_object_name(self, value=None):
        """  Corresponds to IDD field `Wind Pressure Coefficient Values Object Name`
        Enter the name of the AirflowNetwork:MultiZone:WindPressureCoefficientValues object.

        Args:
            value (str): value for IDD Field `Wind Pressure Coefficient Values Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Wind Pressure Coefficient Values Object Name"] = value




class AirflowNetworkMultiZoneWindPressureCoefficientArray(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:WindPressureCoefficientArray`
        Used only if Wind Pressure Coefficient (WPC) Type = Input in the AirflowNetwork:SimulationControl
        object. Number of WPC Values in the corresponding AirflowNetwork:MultiZone:WindPressureCoefficientValues
        object must be the same as the number of wind directions specified for
        this AirflowNetwork:MultiZone:WindPressureCoefficientArray object.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'wind direction 1',
                                      {'name': u'Wind Direction 1',
                                       'pyname': u'wind_direction_1',
                                       'maximum': 360.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 2',
                                      {'name': u'Wind Direction 2',
                                       'pyname': u'wind_direction_2',
                                       'maximum': 360.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 3',
                                      {'name': u'Wind Direction 3',
                                       'pyname': u'wind_direction_3',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 4',
                                      {'name': u'Wind Direction 4',
                                       'pyname': u'wind_direction_4',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 5',
                                      {'name': u'Wind Direction 5',
                                       'pyname': u'wind_direction_5',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 6',
                                      {'name': u'Wind Direction 6',
                                       'pyname': u'wind_direction_6',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 7',
                                      {'name': u'Wind Direction 7',
                                       'pyname': u'wind_direction_7',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 8',
                                      {'name': u'Wind Direction 8',
                                       'pyname': u'wind_direction_8',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 9',
                                      {'name': u'Wind Direction 9',
                                       'pyname': u'wind_direction_9',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 10',
                                      {'name': u'Wind Direction 10',
                                       'pyname': u'wind_direction_10',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 11',
                                      {'name': u'Wind Direction 11',
                                       'pyname': u'wind_direction_11',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 12',
                                      {'name': u'Wind Direction 12',
                                       'pyname': u'wind_direction_12',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 13',
                                      {'name': u'Wind Direction 13',
                                       'pyname': u'wind_direction_13',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 14',
                                      {'name': u'Wind Direction 14',
                                       'pyname': u'wind_direction_14',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 15',
                                      {'name': u'Wind Direction 15',
                                       'pyname': u'wind_direction_15',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 16',
                                      {'name': u'Wind Direction 16',
                                       'pyname': u'wind_direction_16',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 17',
                                      {'name': u'Wind Direction 17',
                                       'pyname': u'wind_direction_17',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 18',
                                      {'name': u'Wind Direction 18',
                                       'pyname': u'wind_direction_18',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 19',
                                      {'name': u'Wind Direction 19',
                                       'pyname': u'wind_direction_19',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 20',
                                      {'name': u'Wind Direction 20',
                                       'pyname': u'wind_direction_20',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 21',
                                      {'name': u'Wind Direction 21',
                                       'pyname': u'wind_direction_21',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 22',
                                      {'name': u'Wind Direction 22',
                                       'pyname': u'wind_direction_22',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 23',
                                      {'name': u'Wind Direction 23',
                                       'pyname': u'wind_direction_23',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 24',
                                      {'name': u'Wind Direction 24',
                                       'pyname': u'wind_direction_24',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 25',
                                      {'name': u'Wind Direction 25',
                                       'pyname': u'wind_direction_25',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 26',
                                      {'name': u'Wind Direction 26',
                                       'pyname': u'wind_direction_26',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 27',
                                      {'name': u'Wind Direction 27',
                                       'pyname': u'wind_direction_27',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 28',
                                      {'name': u'Wind Direction 28',
                                       'pyname': u'wind_direction_28',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 29',
                                      {'name': u'Wind Direction 29',
                                       'pyname': u'wind_direction_29',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 30',
                                      {'name': u'Wind Direction 30',
                                       'pyname': u'wind_direction_30',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 31',
                                      {'name': u'Wind Direction 31',
                                       'pyname': u'wind_direction_31',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 32',
                                      {'name': u'Wind Direction 32',
                                       'pyname': u'wind_direction_32',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 33',
                                      {'name': u'Wind Direction 33',
                                       'pyname': u'wind_direction_33',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 34',
                                      {'name': u'Wind Direction 34',
                                       'pyname': u'wind_direction_34',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 35',
                                      {'name': u'Wind Direction 35',
                                       'pyname': u'wind_direction_35',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'}),
                                     (u'wind direction 36',
                                      {'name': u'Wind Direction 36',
                                       'pyname': u'wind_direction_36',
                                       'maximum': 360.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'deg'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 3,
              'name': u'AirflowNetwork:MultiZone:WindPressureCoefficientArray',
              'pyname': u'AirflowNetworkMultiZoneWindPressureCoefficientArray',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for the object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def wind_direction_1(self):
        """Get wind_direction_1.

        Returns:
            float: the value of `wind_direction_1` or None if not set

        """
        return self["Wind Direction 1"]

    @wind_direction_1.setter
    def wind_direction_1(self, value=None):
        """Corresponds to IDD field `Wind Direction 1` Enter the wind direction
        corresponding to the 1st WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 1`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 1"] = value

    @property
    def wind_direction_2(self):
        """Get wind_direction_2.

        Returns:
            float: the value of `wind_direction_2` or None if not set

        """
        return self["Wind Direction 2"]

    @wind_direction_2.setter
    def wind_direction_2(self, value=None):
        """Corresponds to IDD field `Wind Direction 2` Enter the wind direction
        corresponding to the 2nd WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 2`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 2"] = value

    @property
    def wind_direction_3(self):
        """Get wind_direction_3.

        Returns:
            float: the value of `wind_direction_3` or None if not set

        """
        return self["Wind Direction 3"]

    @wind_direction_3.setter
    def wind_direction_3(self, value=None):
        """Corresponds to IDD field `Wind Direction 3` Enter the wind direction
        corresponding to the 3rd WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 3`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 3"] = value

    @property
    def wind_direction_4(self):
        """Get wind_direction_4.

        Returns:
            float: the value of `wind_direction_4` or None if not set

        """
        return self["Wind Direction 4"]

    @wind_direction_4.setter
    def wind_direction_4(self, value=None):
        """Corresponds to IDD field `Wind Direction 4` Enter the wind direction
        corresponding to the 4th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 4`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 4"] = value

    @property
    def wind_direction_5(self):
        """Get wind_direction_5.

        Returns:
            float: the value of `wind_direction_5` or None if not set

        """
        return self["Wind Direction 5"]

    @wind_direction_5.setter
    def wind_direction_5(self, value=None):
        """Corresponds to IDD field `Wind Direction 5` Enter the wind direction
        corresponding to the 5th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 5`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 5"] = value

    @property
    def wind_direction_6(self):
        """Get wind_direction_6.

        Returns:
            float: the value of `wind_direction_6` or None if not set

        """
        return self["Wind Direction 6"]

    @wind_direction_6.setter
    def wind_direction_6(self, value=None):
        """Corresponds to IDD field `Wind Direction 6` Enter the wind direction
        corresponding to the 6th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 6`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 6"] = value

    @property
    def wind_direction_7(self):
        """Get wind_direction_7.

        Returns:
            float: the value of `wind_direction_7` or None if not set

        """
        return self["Wind Direction 7"]

    @wind_direction_7.setter
    def wind_direction_7(self, value=None):
        """Corresponds to IDD field `Wind Direction 7` Enter the wind direction
        corresponding to the 7th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 7`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 7"] = value

    @property
    def wind_direction_8(self):
        """Get wind_direction_8.

        Returns:
            float: the value of `wind_direction_8` or None if not set

        """
        return self["Wind Direction 8"]

    @wind_direction_8.setter
    def wind_direction_8(self, value=None):
        """Corresponds to IDD field `Wind Direction 8` Enter the wind direction
        corresponding to the 8th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 8`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 8"] = value

    @property
    def wind_direction_9(self):
        """Get wind_direction_9.

        Returns:
            float: the value of `wind_direction_9` or None if not set

        """
        return self["Wind Direction 9"]

    @wind_direction_9.setter
    def wind_direction_9(self, value=None):
        """Corresponds to IDD field `Wind Direction 9` Enter the wind direction
        corresponding to the 9th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 9`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 9"] = value

    @property
    def wind_direction_10(self):
        """Get wind_direction_10.

        Returns:
            float: the value of `wind_direction_10` or None if not set

        """
        return self["Wind Direction 10"]

    @wind_direction_10.setter
    def wind_direction_10(self, value=None):
        """Corresponds to IDD field `Wind Direction 10` Enter the wind
        direction corresponding to the 10th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 10`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 10"] = value

    @property
    def wind_direction_11(self):
        """Get wind_direction_11.

        Returns:
            float: the value of `wind_direction_11` or None if not set

        """
        return self["Wind Direction 11"]

    @wind_direction_11.setter
    def wind_direction_11(self, value=None):
        """Corresponds to IDD field `Wind Direction 11` Enter the wind
        direction corresponding to the 11th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 11`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 11"] = value

    @property
    def wind_direction_12(self):
        """Get wind_direction_12.

        Returns:
            float: the value of `wind_direction_12` or None if not set

        """
        return self["Wind Direction 12"]

    @wind_direction_12.setter
    def wind_direction_12(self, value=None):
        """Corresponds to IDD field `Wind Direction 12` Enter the wind
        direction corresponding to the 12th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 12`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 12"] = value

    @property
    def wind_direction_13(self):
        """Get wind_direction_13.

        Returns:
            float: the value of `wind_direction_13` or None if not set

        """
        return self["Wind Direction 13"]

    @wind_direction_13.setter
    def wind_direction_13(self, value=None):
        """Corresponds to IDD field `Wind Direction 13` Enter the wind
        direction corresponding to the 13th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 13`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 13"] = value

    @property
    def wind_direction_14(self):
        """Get wind_direction_14.

        Returns:
            float: the value of `wind_direction_14` or None if not set

        """
        return self["Wind Direction 14"]

    @wind_direction_14.setter
    def wind_direction_14(self, value=None):
        """Corresponds to IDD field `Wind Direction 14` Enter the wind
        direction corresponding to the 14th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 14`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 14"] = value

    @property
    def wind_direction_15(self):
        """Get wind_direction_15.

        Returns:
            float: the value of `wind_direction_15` or None if not set

        """
        return self["Wind Direction 15"]

    @wind_direction_15.setter
    def wind_direction_15(self, value=None):
        """Corresponds to IDD field `Wind Direction 15` Enter the wind
        direction corresponding to the 15th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 15`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 15"] = value

    @property
    def wind_direction_16(self):
        """Get wind_direction_16.

        Returns:
            float: the value of `wind_direction_16` or None if not set

        """
        return self["Wind Direction 16"]

    @wind_direction_16.setter
    def wind_direction_16(self, value=None):
        """Corresponds to IDD field `Wind Direction 16` Enter the wind
        direction corresponding to the 16th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 16`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 16"] = value

    @property
    def wind_direction_17(self):
        """Get wind_direction_17.

        Returns:
            float: the value of `wind_direction_17` or None if not set

        """
        return self["Wind Direction 17"]

    @wind_direction_17.setter
    def wind_direction_17(self, value=None):
        """Corresponds to IDD field `Wind Direction 17` Enter the wind
        direction corresponding to the 17th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 17`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 17"] = value

    @property
    def wind_direction_18(self):
        """Get wind_direction_18.

        Returns:
            float: the value of `wind_direction_18` or None if not set

        """
        return self["Wind Direction 18"]

    @wind_direction_18.setter
    def wind_direction_18(self, value=None):
        """Corresponds to IDD field `Wind Direction 18` Enter the wind
        direction corresponding to the 18th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 18`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 18"] = value

    @property
    def wind_direction_19(self):
        """Get wind_direction_19.

        Returns:
            float: the value of `wind_direction_19` or None if not set

        """
        return self["Wind Direction 19"]

    @wind_direction_19.setter
    def wind_direction_19(self, value=None):
        """Corresponds to IDD field `Wind Direction 19` Enter the wind
        direction corresponding to the 19th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 19`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 19"] = value

    @property
    def wind_direction_20(self):
        """Get wind_direction_20.

        Returns:
            float: the value of `wind_direction_20` or None if not set

        """
        return self["Wind Direction 20"]

    @wind_direction_20.setter
    def wind_direction_20(self, value=None):
        """Corresponds to IDD field `Wind Direction 20` Enter the wind
        direction corresponding to the 20th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 20`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 20"] = value

    @property
    def wind_direction_21(self):
        """Get wind_direction_21.

        Returns:
            float: the value of `wind_direction_21` or None if not set

        """
        return self["Wind Direction 21"]

    @wind_direction_21.setter
    def wind_direction_21(self, value=None):
        """Corresponds to IDD field `Wind Direction 21` Enter the wind
        direction corresponding to the 21st WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 21`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 21"] = value

    @property
    def wind_direction_22(self):
        """Get wind_direction_22.

        Returns:
            float: the value of `wind_direction_22` or None if not set

        """
        return self["Wind Direction 22"]

    @wind_direction_22.setter
    def wind_direction_22(self, value=None):
        """Corresponds to IDD field `Wind Direction 22` Enter the wind
        direction corresponding to the 22nd WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 22`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 22"] = value

    @property
    def wind_direction_23(self):
        """Get wind_direction_23.

        Returns:
            float: the value of `wind_direction_23` or None if not set

        """
        return self["Wind Direction 23"]

    @wind_direction_23.setter
    def wind_direction_23(self, value=None):
        """Corresponds to IDD field `Wind Direction 23` Enter the wind
        direction corresponding to the 23rd WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 23`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 23"] = value

    @property
    def wind_direction_24(self):
        """Get wind_direction_24.

        Returns:
            float: the value of `wind_direction_24` or None if not set

        """
        return self["Wind Direction 24"]

    @wind_direction_24.setter
    def wind_direction_24(self, value=None):
        """Corresponds to IDD field `Wind Direction 24` Enter the wind
        direction corresponding to the 24th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 24`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 24"] = value

    @property
    def wind_direction_25(self):
        """Get wind_direction_25.

        Returns:
            float: the value of `wind_direction_25` or None if not set

        """
        return self["Wind Direction 25"]

    @wind_direction_25.setter
    def wind_direction_25(self, value=None):
        """Corresponds to IDD field `Wind Direction 25` Enter the wind
        direction corresponding to the 25th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 25`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 25"] = value

    @property
    def wind_direction_26(self):
        """Get wind_direction_26.

        Returns:
            float: the value of `wind_direction_26` or None if not set

        """
        return self["Wind Direction 26"]

    @wind_direction_26.setter
    def wind_direction_26(self, value=None):
        """Corresponds to IDD field `Wind Direction 26` Enter the wind
        direction corresponding to the 26th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 26`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 26"] = value

    @property
    def wind_direction_27(self):
        """Get wind_direction_27.

        Returns:
            float: the value of `wind_direction_27` or None if not set

        """
        return self["Wind Direction 27"]

    @wind_direction_27.setter
    def wind_direction_27(self, value=None):
        """Corresponds to IDD field `Wind Direction 27` Enter the wind
        direction corresponding to the 27th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 27`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 27"] = value

    @property
    def wind_direction_28(self):
        """Get wind_direction_28.

        Returns:
            float: the value of `wind_direction_28` or None if not set

        """
        return self["Wind Direction 28"]

    @wind_direction_28.setter
    def wind_direction_28(self, value=None):
        """Corresponds to IDD field `Wind Direction 28` Enter the wind
        direction corresponding to the 28th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 28`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 28"] = value

    @property
    def wind_direction_29(self):
        """Get wind_direction_29.

        Returns:
            float: the value of `wind_direction_29` or None if not set

        """
        return self["Wind Direction 29"]

    @wind_direction_29.setter
    def wind_direction_29(self, value=None):
        """Corresponds to IDD field `Wind Direction 29` Enter the wind
        direction corresponding to the 29th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 29`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 29"] = value

    @property
    def wind_direction_30(self):
        """Get wind_direction_30.

        Returns:
            float: the value of `wind_direction_30` or None if not set

        """
        return self["Wind Direction 30"]

    @wind_direction_30.setter
    def wind_direction_30(self, value=None):
        """Corresponds to IDD field `Wind Direction 30` Enter the wind
        direction corresponding to the 30th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 30`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 30"] = value

    @property
    def wind_direction_31(self):
        """Get wind_direction_31.

        Returns:
            float: the value of `wind_direction_31` or None if not set

        """
        return self["Wind Direction 31"]

    @wind_direction_31.setter
    def wind_direction_31(self, value=None):
        """Corresponds to IDD field `Wind Direction 31` Enter the wind
        direction corresponding to the 31st WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 31`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 31"] = value

    @property
    def wind_direction_32(self):
        """Get wind_direction_32.

        Returns:
            float: the value of `wind_direction_32` or None if not set

        """
        return self["Wind Direction 32"]

    @wind_direction_32.setter
    def wind_direction_32(self, value=None):
        """Corresponds to IDD field `Wind Direction 32` Enter the wind
        direction corresponding to the 32nd WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 32`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 32"] = value

    @property
    def wind_direction_33(self):
        """Get wind_direction_33.

        Returns:
            float: the value of `wind_direction_33` or None if not set

        """
        return self["Wind Direction 33"]

    @wind_direction_33.setter
    def wind_direction_33(self, value=None):
        """Corresponds to IDD field `Wind Direction 33` Enter the wind
        direction corresponding to the 33rd WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 33`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 33"] = value

    @property
    def wind_direction_34(self):
        """Get wind_direction_34.

        Returns:
            float: the value of `wind_direction_34` or None if not set

        """
        return self["Wind Direction 34"]

    @wind_direction_34.setter
    def wind_direction_34(self, value=None):
        """Corresponds to IDD field `Wind Direction 34` Enter the wind
        direction corresponding to the 34th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 34`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 34"] = value

    @property
    def wind_direction_35(self):
        """Get wind_direction_35.

        Returns:
            float: the value of `wind_direction_35` or None if not set

        """
        return self["Wind Direction 35"]

    @wind_direction_35.setter
    def wind_direction_35(self, value=None):
        """Corresponds to IDD field `Wind Direction 35` Enter the wind
        direction corresponding to the 35th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 35`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 35"] = value

    @property
    def wind_direction_36(self):
        """Get wind_direction_36.

        Returns:
            float: the value of `wind_direction_36` or None if not set

        """
        return self["Wind Direction 36"]

    @wind_direction_36.setter
    def wind_direction_36(self, value=None):
        """Corresponds to IDD field `Wind Direction 36` Enter the wind
        direction corresponding to the 36th WPC Array value.

        Args:
            value (float): value for IDD Field `Wind Direction 36`
                Units: deg
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Direction 36"] = value




class AirflowNetworkMultiZoneWindPressureCoefficientValues(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:MultiZone:WindPressureCoefficientValues`
        Used only if Wind Pressure Coefficient (WPC) Type = INPUT in the AirflowNetwork:SimulationControl
        object. The number of WPC numeric inputs must correspond to the number of wind direction
        inputs in the AirflowNetwork:Multizone:WindPressureCoefficientArray object.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'airflownetwork:multizone:windpressurecoefficientarray name',
                                      {'name': u'AirflowNetwork:MultiZone:WindPressureCoefficientArray Name',
                                       'pyname': u'airflownetworkmultizonewindpressurecoefficientarray_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'wind pressure coefficient value 1',
                                      {'name': u'Wind Pressure Coefficient Value 1',
                                       'pyname': u'wind_pressure_coefficient_value_1',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 2',
                                      {'name': u'Wind Pressure Coefficient Value 2',
                                       'pyname': u'wind_pressure_coefficient_value_2',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 3',
                                      {'name': u'Wind Pressure Coefficient Value 3',
                                       'pyname': u'wind_pressure_coefficient_value_3',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 4',
                                      {'name': u'Wind Pressure Coefficient Value 4',
                                       'pyname': u'wind_pressure_coefficient_value_4',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 5',
                                      {'name': u'Wind Pressure Coefficient Value 5',
                                       'pyname': u'wind_pressure_coefficient_value_5',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 6',
                                      {'name': u'Wind Pressure Coefficient Value 6',
                                       'pyname': u'wind_pressure_coefficient_value_6',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 7',
                                      {'name': u'Wind Pressure Coefficient Value 7',
                                       'pyname': u'wind_pressure_coefficient_value_7',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 8',
                                      {'name': u'Wind Pressure Coefficient Value 8',
                                       'pyname': u'wind_pressure_coefficient_value_8',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 9',
                                      {'name': u'Wind Pressure Coefficient Value 9',
                                       'pyname': u'wind_pressure_coefficient_value_9',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 10',
                                      {'name': u'Wind Pressure Coefficient Value 10',
                                       'pyname': u'wind_pressure_coefficient_value_10',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 11',
                                      {'name': u'Wind Pressure Coefficient Value 11',
                                       'pyname': u'wind_pressure_coefficient_value_11',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 12',
                                      {'name': u'Wind Pressure Coefficient Value 12',
                                       'pyname': u'wind_pressure_coefficient_value_12',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 13',
                                      {'name': u'Wind Pressure Coefficient Value 13',
                                       'pyname': u'wind_pressure_coefficient_value_13',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 14',
                                      {'name': u'Wind Pressure Coefficient Value 14',
                                       'pyname': u'wind_pressure_coefficient_value_14',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 15',
                                      {'name': u'Wind Pressure Coefficient Value 15',
                                       'pyname': u'wind_pressure_coefficient_value_15',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 16',
                                      {'name': u'Wind Pressure Coefficient Value 16',
                                       'pyname': u'wind_pressure_coefficient_value_16',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 17',
                                      {'name': u'Wind Pressure Coefficient Value 17',
                                       'pyname': u'wind_pressure_coefficient_value_17',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 18',
                                      {'name': u'Wind Pressure Coefficient Value 18',
                                       'pyname': u'wind_pressure_coefficient_value_18',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 19',
                                      {'name': u'Wind Pressure Coefficient Value 19',
                                       'pyname': u'wind_pressure_coefficient_value_19',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 20',
                                      {'name': u'Wind Pressure Coefficient Value 20',
                                       'pyname': u'wind_pressure_coefficient_value_20',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 21',
                                      {'name': u'Wind Pressure Coefficient Value 21',
                                       'pyname': u'wind_pressure_coefficient_value_21',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 22',
                                      {'name': u'Wind Pressure Coefficient Value 22',
                                       'pyname': u'wind_pressure_coefficient_value_22',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 23',
                                      {'name': u'Wind Pressure Coefficient Value 23',
                                       'pyname': u'wind_pressure_coefficient_value_23',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 24',
                                      {'name': u'Wind Pressure Coefficient Value 24',
                                       'pyname': u'wind_pressure_coefficient_value_24',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 25',
                                      {'name': u'Wind Pressure Coefficient Value 25',
                                       'pyname': u'wind_pressure_coefficient_value_25',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 26',
                                      {'name': u'Wind Pressure Coefficient Value 26',
                                       'pyname': u'wind_pressure_coefficient_value_26',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 27',
                                      {'name': u'Wind Pressure Coefficient Value 27',
                                       'pyname': u'wind_pressure_coefficient_value_27',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 28',
                                      {'name': u'Wind Pressure Coefficient Value 28',
                                       'pyname': u'wind_pressure_coefficient_value_28',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 29',
                                      {'name': u'Wind Pressure Coefficient Value 29',
                                       'pyname': u'wind_pressure_coefficient_value_29',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 30',
                                      {'name': u'Wind Pressure Coefficient Value 30',
                                       'pyname': u'wind_pressure_coefficient_value_30',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 31',
                                      {'name': u'Wind Pressure Coefficient Value 31',
                                       'pyname': u'wind_pressure_coefficient_value_31',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 32',
                                      {'name': u'Wind Pressure Coefficient Value 32',
                                       'pyname': u'wind_pressure_coefficient_value_32',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 33',
                                      {'name': u'Wind Pressure Coefficient Value 33',
                                       'pyname': u'wind_pressure_coefficient_value_33',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 34',
                                      {'name': u'Wind Pressure Coefficient Value 34',
                                       'pyname': u'wind_pressure_coefficient_value_34',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 35',
                                      {'name': u'Wind Pressure Coefficient Value 35',
                                       'pyname': u'wind_pressure_coefficient_value_35',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'wind pressure coefficient value 36',
                                      {'name': u'Wind Pressure Coefficient Value 36',
                                       'pyname': u'wind_pressure_coefficient_value_36',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:MultiZone:WindPressureCoefficientValues',
              'pyname': u'AirflowNetworkMultiZoneWindPressureCoefficientValues',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def airflownetworkmultizonewindpressurecoefficientarray_name(self):
        """Get airflownetworkmultizonewindpressurecoefficientarray_name.

        Returns:
            str: the value of `airflownetworkmultizonewindpressurecoefficientarray_name` or None if not set

        """
        return self[
            "AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"]

    @airflownetworkmultizonewindpressurecoefficientarray_name.setter
    def airflownetworkmultizonewindpressurecoefficientarray_name(
            self,
            value=None):
        """  Corresponds to IDD field `AirflowNetwork:MultiZone:WindPressureCoefficientArray Name`
        Enter the name of the AirflowNetwork:Multizone:WindPressureCoefficientArray object.

        Args:
            value (str): value for IDD Field `AirflowNetwork:MultiZone:WindPressureCoefficientArray Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "AirflowNetwork:MultiZone:WindPressureCoefficientArray Name"] = value

    @property
    def wind_pressure_coefficient_value_1(self):
        """Get wind_pressure_coefficient_value_1.

        Returns:
            float: the value of `wind_pressure_coefficient_value_1` or None if not set

        """
        return self["Wind Pressure Coefficient Value 1"]

    @wind_pressure_coefficient_value_1.setter
    def wind_pressure_coefficient_value_1(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 1` Enter
        the WPC Value corresponding to the 1st wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 1`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 1"] = value

    @property
    def wind_pressure_coefficient_value_2(self):
        """Get wind_pressure_coefficient_value_2.

        Returns:
            float: the value of `wind_pressure_coefficient_value_2` or None if not set

        """
        return self["Wind Pressure Coefficient Value 2"]

    @wind_pressure_coefficient_value_2.setter
    def wind_pressure_coefficient_value_2(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 2` Enter
        the WPC Value corresponding to the 2nd wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 2`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 2"] = value

    @property
    def wind_pressure_coefficient_value_3(self):
        """Get wind_pressure_coefficient_value_3.

        Returns:
            float: the value of `wind_pressure_coefficient_value_3` or None if not set

        """
        return self["Wind Pressure Coefficient Value 3"]

    @wind_pressure_coefficient_value_3.setter
    def wind_pressure_coefficient_value_3(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 3` Enter
        the WPC Value corresponding to the 3rd wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 3`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 3"] = value

    @property
    def wind_pressure_coefficient_value_4(self):
        """Get wind_pressure_coefficient_value_4.

        Returns:
            float: the value of `wind_pressure_coefficient_value_4` or None if not set

        """
        return self["Wind Pressure Coefficient Value 4"]

    @wind_pressure_coefficient_value_4.setter
    def wind_pressure_coefficient_value_4(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 4` Enter
        the WPC Value corresponding to the 4th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 4`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 4"] = value

    @property
    def wind_pressure_coefficient_value_5(self):
        """Get wind_pressure_coefficient_value_5.

        Returns:
            float: the value of `wind_pressure_coefficient_value_5` or None if not set

        """
        return self["Wind Pressure Coefficient Value 5"]

    @wind_pressure_coefficient_value_5.setter
    def wind_pressure_coefficient_value_5(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 5` Enter
        the WPC Value corresponding to the 5th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 5`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 5"] = value

    @property
    def wind_pressure_coefficient_value_6(self):
        """Get wind_pressure_coefficient_value_6.

        Returns:
            float: the value of `wind_pressure_coefficient_value_6` or None if not set

        """
        return self["Wind Pressure Coefficient Value 6"]

    @wind_pressure_coefficient_value_6.setter
    def wind_pressure_coefficient_value_6(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 6` Enter
        the WPC Value corresponding to the 6th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 6`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 6"] = value

    @property
    def wind_pressure_coefficient_value_7(self):
        """Get wind_pressure_coefficient_value_7.

        Returns:
            float: the value of `wind_pressure_coefficient_value_7` or None if not set

        """
        return self["Wind Pressure Coefficient Value 7"]

    @wind_pressure_coefficient_value_7.setter
    def wind_pressure_coefficient_value_7(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 7` Enter
        the WPC Value corresponding to the 7th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 7`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 7"] = value

    @property
    def wind_pressure_coefficient_value_8(self):
        """Get wind_pressure_coefficient_value_8.

        Returns:
            float: the value of `wind_pressure_coefficient_value_8` or None if not set

        """
        return self["Wind Pressure Coefficient Value 8"]

    @wind_pressure_coefficient_value_8.setter
    def wind_pressure_coefficient_value_8(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 8` Enter
        the WPC Value corresponding to the 8th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 8`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 8"] = value

    @property
    def wind_pressure_coefficient_value_9(self):
        """Get wind_pressure_coefficient_value_9.

        Returns:
            float: the value of `wind_pressure_coefficient_value_9` or None if not set

        """
        return self["Wind Pressure Coefficient Value 9"]

    @wind_pressure_coefficient_value_9.setter
    def wind_pressure_coefficient_value_9(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 9` Enter
        the WPC Value corresponding to the 9th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 9`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 9"] = value

    @property
    def wind_pressure_coefficient_value_10(self):
        """Get wind_pressure_coefficient_value_10.

        Returns:
            float: the value of `wind_pressure_coefficient_value_10` or None if not set

        """
        return self["Wind Pressure Coefficient Value 10"]

    @wind_pressure_coefficient_value_10.setter
    def wind_pressure_coefficient_value_10(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 10` Enter
        the WPC Value corresponding to the 10th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 10`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 10"] = value

    @property
    def wind_pressure_coefficient_value_11(self):
        """Get wind_pressure_coefficient_value_11.

        Returns:
            float: the value of `wind_pressure_coefficient_value_11` or None if not set

        """
        return self["Wind Pressure Coefficient Value 11"]

    @wind_pressure_coefficient_value_11.setter
    def wind_pressure_coefficient_value_11(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 11` Enter
        the WPC Value corresponding to the 11th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 11`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 11"] = value

    @property
    def wind_pressure_coefficient_value_12(self):
        """Get wind_pressure_coefficient_value_12.

        Returns:
            float: the value of `wind_pressure_coefficient_value_12` or None if not set

        """
        return self["Wind Pressure Coefficient Value 12"]

    @wind_pressure_coefficient_value_12.setter
    def wind_pressure_coefficient_value_12(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 12` Enter
        the WPC Value corresponding to the 12th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 12`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 12"] = value

    @property
    def wind_pressure_coefficient_value_13(self):
        """Get wind_pressure_coefficient_value_13.

        Returns:
            float: the value of `wind_pressure_coefficient_value_13` or None if not set

        """
        return self["Wind Pressure Coefficient Value 13"]

    @wind_pressure_coefficient_value_13.setter
    def wind_pressure_coefficient_value_13(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 13` Enter
        the WPC Value corresponding to the 13th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 13`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 13"] = value

    @property
    def wind_pressure_coefficient_value_14(self):
        """Get wind_pressure_coefficient_value_14.

        Returns:
            float: the value of `wind_pressure_coefficient_value_14` or None if not set

        """
        return self["Wind Pressure Coefficient Value 14"]

    @wind_pressure_coefficient_value_14.setter
    def wind_pressure_coefficient_value_14(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 14` Enter
        the WPC Value corresponding to the 14th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 14`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 14"] = value

    @property
    def wind_pressure_coefficient_value_15(self):
        """Get wind_pressure_coefficient_value_15.

        Returns:
            float: the value of `wind_pressure_coefficient_value_15` or None if not set

        """
        return self["Wind Pressure Coefficient Value 15"]

    @wind_pressure_coefficient_value_15.setter
    def wind_pressure_coefficient_value_15(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 15` Enter
        the WPC Value corresponding to the 15th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 15`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 15"] = value

    @property
    def wind_pressure_coefficient_value_16(self):
        """Get wind_pressure_coefficient_value_16.

        Returns:
            float: the value of `wind_pressure_coefficient_value_16` or None if not set

        """
        return self["Wind Pressure Coefficient Value 16"]

    @wind_pressure_coefficient_value_16.setter
    def wind_pressure_coefficient_value_16(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 16` Enter
        the WPC Value corresponding to the 16th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 16`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 16"] = value

    @property
    def wind_pressure_coefficient_value_17(self):
        """Get wind_pressure_coefficient_value_17.

        Returns:
            float: the value of `wind_pressure_coefficient_value_17` or None if not set

        """
        return self["Wind Pressure Coefficient Value 17"]

    @wind_pressure_coefficient_value_17.setter
    def wind_pressure_coefficient_value_17(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 17` Enter
        the WPC Value corresponding to the 17th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 17`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 17"] = value

    @property
    def wind_pressure_coefficient_value_18(self):
        """Get wind_pressure_coefficient_value_18.

        Returns:
            float: the value of `wind_pressure_coefficient_value_18` or None if not set

        """
        return self["Wind Pressure Coefficient Value 18"]

    @wind_pressure_coefficient_value_18.setter
    def wind_pressure_coefficient_value_18(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 18` Enter
        the WPC Value corresponding to the 18th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 18`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 18"] = value

    @property
    def wind_pressure_coefficient_value_19(self):
        """Get wind_pressure_coefficient_value_19.

        Returns:
            float: the value of `wind_pressure_coefficient_value_19` or None if not set

        """
        return self["Wind Pressure Coefficient Value 19"]

    @wind_pressure_coefficient_value_19.setter
    def wind_pressure_coefficient_value_19(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 19` Enter
        the WPC Value corresponding to the 19th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 19`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 19"] = value

    @property
    def wind_pressure_coefficient_value_20(self):
        """Get wind_pressure_coefficient_value_20.

        Returns:
            float: the value of `wind_pressure_coefficient_value_20` or None if not set

        """
        return self["Wind Pressure Coefficient Value 20"]

    @wind_pressure_coefficient_value_20.setter
    def wind_pressure_coefficient_value_20(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 20` Enter
        the WPC Value corresponding to the 20th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 20`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 20"] = value

    @property
    def wind_pressure_coefficient_value_21(self):
        """Get wind_pressure_coefficient_value_21.

        Returns:
            float: the value of `wind_pressure_coefficient_value_21` or None if not set

        """
        return self["Wind Pressure Coefficient Value 21"]

    @wind_pressure_coefficient_value_21.setter
    def wind_pressure_coefficient_value_21(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 21` Enter
        the WPC Value corresponding to the 21st wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 21`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 21"] = value

    @property
    def wind_pressure_coefficient_value_22(self):
        """Get wind_pressure_coefficient_value_22.

        Returns:
            float: the value of `wind_pressure_coefficient_value_22` or None if not set

        """
        return self["Wind Pressure Coefficient Value 22"]

    @wind_pressure_coefficient_value_22.setter
    def wind_pressure_coefficient_value_22(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 22` Enter
        the WPC Value corresponding to the 22nd wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 22`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 22"] = value

    @property
    def wind_pressure_coefficient_value_23(self):
        """Get wind_pressure_coefficient_value_23.

        Returns:
            float: the value of `wind_pressure_coefficient_value_23` or None if not set

        """
        return self["Wind Pressure Coefficient Value 23"]

    @wind_pressure_coefficient_value_23.setter
    def wind_pressure_coefficient_value_23(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 23` Enter
        the WPC Value corresponding to the 23rd wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 23`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 23"] = value

    @property
    def wind_pressure_coefficient_value_24(self):
        """Get wind_pressure_coefficient_value_24.

        Returns:
            float: the value of `wind_pressure_coefficient_value_24` or None if not set

        """
        return self["Wind Pressure Coefficient Value 24"]

    @wind_pressure_coefficient_value_24.setter
    def wind_pressure_coefficient_value_24(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 24` Enter
        the WPC Value corresponding to the 24th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 24`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 24"] = value

    @property
    def wind_pressure_coefficient_value_25(self):
        """Get wind_pressure_coefficient_value_25.

        Returns:
            float: the value of `wind_pressure_coefficient_value_25` or None if not set

        """
        return self["Wind Pressure Coefficient Value 25"]

    @wind_pressure_coefficient_value_25.setter
    def wind_pressure_coefficient_value_25(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 25` Enter
        the WPC Value corresponding to the 25th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 25`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 25"] = value

    @property
    def wind_pressure_coefficient_value_26(self):
        """Get wind_pressure_coefficient_value_26.

        Returns:
            float: the value of `wind_pressure_coefficient_value_26` or None if not set

        """
        return self["Wind Pressure Coefficient Value 26"]

    @wind_pressure_coefficient_value_26.setter
    def wind_pressure_coefficient_value_26(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 26` Enter
        the WPC Value corresponding to the 26th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 26`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 26"] = value

    @property
    def wind_pressure_coefficient_value_27(self):
        """Get wind_pressure_coefficient_value_27.

        Returns:
            float: the value of `wind_pressure_coefficient_value_27` or None if not set

        """
        return self["Wind Pressure Coefficient Value 27"]

    @wind_pressure_coefficient_value_27.setter
    def wind_pressure_coefficient_value_27(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 27` Enter
        the WPC Value corresponding to the 27th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 27`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 27"] = value

    @property
    def wind_pressure_coefficient_value_28(self):
        """Get wind_pressure_coefficient_value_28.

        Returns:
            float: the value of `wind_pressure_coefficient_value_28` or None if not set

        """
        return self["Wind Pressure Coefficient Value 28"]

    @wind_pressure_coefficient_value_28.setter
    def wind_pressure_coefficient_value_28(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 28` Enter
        the WPC Value corresponding to the 28th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 28`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 28"] = value

    @property
    def wind_pressure_coefficient_value_29(self):
        """Get wind_pressure_coefficient_value_29.

        Returns:
            float: the value of `wind_pressure_coefficient_value_29` or None if not set

        """
        return self["Wind Pressure Coefficient Value 29"]

    @wind_pressure_coefficient_value_29.setter
    def wind_pressure_coefficient_value_29(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 29` Enter
        the WPC Value corresponding to the 29th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 29`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 29"] = value

    @property
    def wind_pressure_coefficient_value_30(self):
        """Get wind_pressure_coefficient_value_30.

        Returns:
            float: the value of `wind_pressure_coefficient_value_30` or None if not set

        """
        return self["Wind Pressure Coefficient Value 30"]

    @wind_pressure_coefficient_value_30.setter
    def wind_pressure_coefficient_value_30(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 30` Enter
        the WPC Value corresponding to the 30th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 30`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 30"] = value

    @property
    def wind_pressure_coefficient_value_31(self):
        """Get wind_pressure_coefficient_value_31.

        Returns:
            float: the value of `wind_pressure_coefficient_value_31` or None if not set

        """
        return self["Wind Pressure Coefficient Value 31"]

    @wind_pressure_coefficient_value_31.setter
    def wind_pressure_coefficient_value_31(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 31` Enter
        the WPC Value corresponding to the 31st wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 31`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 31"] = value

    @property
    def wind_pressure_coefficient_value_32(self):
        """Get wind_pressure_coefficient_value_32.

        Returns:
            float: the value of `wind_pressure_coefficient_value_32` or None if not set

        """
        return self["Wind Pressure Coefficient Value 32"]

    @wind_pressure_coefficient_value_32.setter
    def wind_pressure_coefficient_value_32(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 32` Enter
        the WPC Value corresponding to the 32nd wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 32`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 32"] = value

    @property
    def wind_pressure_coefficient_value_33(self):
        """Get wind_pressure_coefficient_value_33.

        Returns:
            float: the value of `wind_pressure_coefficient_value_33` or None if not set

        """
        return self["Wind Pressure Coefficient Value 33"]

    @wind_pressure_coefficient_value_33.setter
    def wind_pressure_coefficient_value_33(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 33` Enter
        the WPC Value corresponding to the 33rd wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 33`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 33"] = value

    @property
    def wind_pressure_coefficient_value_34(self):
        """Get wind_pressure_coefficient_value_34.

        Returns:
            float: the value of `wind_pressure_coefficient_value_34` or None if not set

        """
        return self["Wind Pressure Coefficient Value 34"]

    @wind_pressure_coefficient_value_34.setter
    def wind_pressure_coefficient_value_34(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 34` Enter
        the WPC Value corresponding to the 34th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 34`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 34"] = value

    @property
    def wind_pressure_coefficient_value_35(self):
        """Get wind_pressure_coefficient_value_35.

        Returns:
            float: the value of `wind_pressure_coefficient_value_35` or None if not set

        """
        return self["Wind Pressure Coefficient Value 35"]

    @wind_pressure_coefficient_value_35.setter
    def wind_pressure_coefficient_value_35(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 35` Enter
        the WPC Value corresponding to the 35th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 35`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 35"] = value

    @property
    def wind_pressure_coefficient_value_36(self):
        """Get wind_pressure_coefficient_value_36.

        Returns:
            float: the value of `wind_pressure_coefficient_value_36` or None if not set

        """
        return self["Wind Pressure Coefficient Value 36"]

    @wind_pressure_coefficient_value_36.setter
    def wind_pressure_coefficient_value_36(self, value=None):
        """Corresponds to IDD field `Wind Pressure Coefficient Value 36` Enter
        the WPC Value corresponding to the 36th wind direction.

        Args:
            value (float): value for IDD Field `Wind Pressure Coefficient Value 36`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Wind Pressure Coefficient Value 36"] = value




class AirflowNetworkDistributionNode(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Node`
        This object represents an air distribution node in the AirflowNetwork model.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'component name or node name',
                                      {'name': u'Component Name or Node Name',
                                       'pyname': u'component_name_or_node_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'component object type or node type',
                                      {'name': u'Component Object Type or Node Type',
                                       'pyname': u'component_object_type_or_node_type',
                                       'default': u'Other',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'AirLoopHVAC:ZoneMixer',
                                                           u'AirLoopHVAC:ZoneSplitter',
                                                           u'AirLoopHVAC:OutdoorAirSystem',
                                                           u'OAMixerOutdoorAirStreamNode',
                                                           u'OutdoorAir:NodeList',
                                                           u'OutdoorAir:Node',
                                                           u'Other'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'node height',
                                      {'name': u'Node Height',
                                       'pyname': u'node_height',
                                       'default': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:Distribution:Node',
              'pyname': u'AirflowNetworkDistributionNode',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def component_name_or_node_name(self):
        """Get component_name_or_node_name.

        Returns:
            str: the value of `component_name_or_node_name` or None if not set

        """
        return self["Component Name or Node Name"]

    @component_name_or_node_name.setter
    def component_name_or_node_name(self, value=None):
        """  Corresponds to IDD field `Component Name or Node Name`
        Designates node names defined in another object. The node name may occur in air branches.
        Enter a node name to represent a node already defined in an air loop.
        Leave this field blank if the Node or Object Type field below is entered as
        AirLoopHVAC:ZoneMixer, AirLoopHVAC:ZoneSplitter, AirLoopHVAC:OutdoorAirSystem, or Other.

        Args:
            value (str): value for IDD Field `Component Name or Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Component Name or Node Name"] = value

    @property
    def component_object_type_or_node_type(self):
        """Get component_object_type_or_node_type.

        Returns:
            str: the value of `component_object_type_or_node_type` or None if not set

        """
        return self["Component Object Type or Node Type"]

    @component_object_type_or_node_type.setter
    def component_object_type_or_node_type(self, value="Other"):
        """  Corresponds to IDD field `Component Object Type or Node Type`
        Designates Node type for the Node or Component Name defined in the field above.
        AirLoopHVAC:ZoneMixer -- Represents a AirLoopHVAC:ZoneMixer object.
        AirLoopHVAC:ZoneSplitter -- Represents a AirLoopHVAC:ZoneSplitter object.
        AirLoopHVAC:OutdoorAirSystem -- Represents an AirLoopHVAC:OutdoorAirSystem object.
        OAMixerOutdoorAirStreamNode -- Represents an external node used in the OutdoorAir:Mixer
        OutdoorAir:NodeList -- Represents an external node when a heat exchanger is used before
        the OutdoorAir:Mixer
        OutdoorAir:Node -- Represents an external node when a heat exchanger is used before
        the OutdoorAir:Mixer
        Other -- none of the above, the Node name already defined in the previous field is part
        of an air loop.

        Args:
            value (str): value for IDD Field `Component Object Type or Node Type`
                Default value: Other
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Component Object Type or Node Type"] = value

    @property
    def node_height(self):
        """Get node_height.

        Returns:
            float: the value of `node_height` or None if not set

        """
        return self["Node Height"]

    @node_height.setter
    def node_height(self, value=None):
        """Corresponds to IDD field `Node Height` Enter the reference height
        used to calculate the relative pressure.

        Args:
            value (float): value for IDD Field `Node Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Node Height"] = value




class AirflowNetworkDistributionComponentLeak(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Leak`
        This object defines the characteristics of a supply or return air leak.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'air mass flow coefficient',
                                      {'name': u'Air Mass Flow Coefficient',
                                       'pyname': u'air_mass_flow_coefficient',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/s'}),
                                     (u'air mass flow exponent',
                                      {'name': u'Air Mass Flow Exponent',
                                       'pyname': u'air_mass_flow_exponent',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 3,
              'name': u'AirflowNetwork:Distribution:Component:Leak',
              'pyname': u'AirflowNetworkDistributionComponentLeak',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def air_mass_flow_coefficient(self):
        """Get air_mass_flow_coefficient.

        Returns:
            float: the value of `air_mass_flow_coefficient` or None if not set

        """
        return self["Air Mass Flow Coefficient"]

    @air_mass_flow_coefficient.setter
    def air_mass_flow_coefficient(self, value=None):
        """  Corresponds to IDD field `Air Mass Flow Coefficient`
        Defined at 1 Pa pressure difference across this component.
        Enter the coefficient used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent

        Args:
            value (float): value for IDD Field `Air Mass Flow Coefficient`
                Units: kg/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Coefficient"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent.

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set

        """
        return self["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65):
        """  Corresponds to IDD field `Air Mass Flow Exponent`
        Enter the exponent used in the following equation:
        Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Air Mass Flow Exponent"] = value




class AirflowNetworkDistributionComponentLeakageRatio(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:LeakageRatio`
        This object is used to define supply and return air leaks with respect to the fan's maximum
        air flow rate.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'effective leakage ratio',
                                      {'name': u'Effective Leakage Ratio',
                                       'pyname': u'effective_leakage_ratio',
                                       'minimum>': 0.0,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'maximum flow rate',
                                      {'name': u'Maximum Flow Rate',
                                       'pyname': u'maximum_flow_rate',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm3/s'}),
                                     (u'reference pressure difference',
                                      {'name': u'Reference Pressure Difference',
                                       'pyname': u'reference_pressure_difference',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'Pa'}),
                                     (u'air mass flow exponent',
                                      {'name': u'Air Mass Flow Exponent',
                                       'pyname': u'air_mass_flow_exponent',
                                       'default': 0.65,
                                       'maximum': 1.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.5,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 5,
              'name': u'AirflowNetwork:Distribution:Component:LeakageRatio',
              'pyname': u'AirflowNetworkDistributionComponentLeakageRatio',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def effective_leakage_ratio(self):
        """Get effective_leakage_ratio.

        Returns:
            float: the value of `effective_leakage_ratio` or None if not set

        """
        return self["Effective Leakage Ratio"]

    @effective_leakage_ratio.setter
    def effective_leakage_ratio(self, value=None):
        """Corresponds to IDD field `Effective Leakage Ratio` Defined as a
        ratio of leak flow rate to the maximum flow rate.

        Args:
            value (float): value for IDD Field `Effective Leakage Ratio`
                Units: dimensionless
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Effective Leakage Ratio"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate.

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate` Enter the maximum air
        flow rate in this air loop.

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Maximum Flow Rate"] = value

    @property
    def reference_pressure_difference(self):
        """Get reference_pressure_difference.

        Returns:
            float: the value of `reference_pressure_difference` or None if not set

        """
        return self["Reference Pressure Difference"]

    @reference_pressure_difference.setter
    def reference_pressure_difference(self, value=None):
        """Corresponds to IDD field `Reference Pressure Difference` Enter the
        pressure corresponding to the Effective leakage ratio entered above.

        Args:
            value (float): value for IDD Field `Reference Pressure Difference`
                Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Reference Pressure Difference"] = value

    @property
    def air_mass_flow_exponent(self):
        """Get air_mass_flow_exponent.

        Returns:
            float: the value of `air_mass_flow_exponent` or None if not set

        """
        return self["Air Mass Flow Exponent"]

    @air_mass_flow_exponent.setter
    def air_mass_flow_exponent(self, value=0.65):
        """Corresponds to IDD field `Air Mass Flow Exponent` Enter the exponent
        used in the air mass flow equation.

        Args:
            value (float): value for IDD Field `Air Mass Flow Exponent`
                Units: dimensionless
                Default value: 0.65
                value >= 0.5
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Mass Flow Exponent"] = value




class AirflowNetworkDistributionComponentDuct(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Duct`
        This object defines the relationship between pressure and air flow through the duct.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'duct length',
                                      {'name': u'Duct Length',
                                       'pyname': u'duct_length',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'hydraulic diameter',
                                      {'name': u'Hydraulic Diameter',
                                       'pyname': u'hydraulic_diameter',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'cross section area',
                                      {'name': u'Cross Section Area',
                                       'pyname': u'cross_section_area',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm2'}),
                                     (u'surface roughness',
                                      {'name': u'Surface Roughness',
                                       'pyname': u'surface_roughness',
                                       'default': 0.0009,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'coefficient for local dynamic loss due to fitting',
                                      {'name': u'Coefficient for Local Dynamic Loss Due to Fitting',
                                       'pyname': u'coefficient_for_local_dynamic_loss_due_to_fitting',
                                       'default': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'dimensionless'}),
                                     (u'overall heat transmittance coefficient (u-factor) from air to air',
                                      {'name': u'Overall Heat Transmittance Coefficient (U-Factor) from Air to Air',
                                       'pyname': u'overall_heat_transmittance_coefficient_ufactor_from_air_to_air',
                                       'default': 0.772,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'W/m2-K'}),
                                     (u'overall moisture transmittance coefficient from air to air',
                                      {'name': u'Overall Moisture Transmittance Coefficient from Air to Air',
                                       'pyname': u'overall_moisture_transmittance_coefficient_from_air_to_air',
                                       'default': 0.001,
                                       'minimum>': 0.0,
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'kg/m2'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 8,
              'name': u'AirflowNetwork:Distribution:Component:Duct',
              'pyname': u'AirflowNetworkDistributionComponentDuct',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def duct_length(self):
        """Get duct_length.

        Returns:
            float: the value of `duct_length` or None if not set

        """
        return self["Duct Length"]

    @duct_length.setter
    def duct_length(self, value=None):
        """Corresponds to IDD field `Duct Length` Enter the length of the duct.

        Args:
            value (float): value for IDD Field `Duct Length`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Duct Length"] = value

    @property
    def hydraulic_diameter(self):
        """Get hydraulic_diameter.

        Returns:
            float: the value of `hydraulic_diameter` or None if not set

        """
        return self["Hydraulic Diameter"]

    @hydraulic_diameter.setter
    def hydraulic_diameter(self, value=None):
        """Corresponds to IDD field `Hydraulic Diameter` Enter the hydraulic
        diameter of the duct. Hydraulic diameter is defined as 4 multiplied by
        cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `Hydraulic Diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Hydraulic Diameter"] = value

    @property
    def cross_section_area(self):
        """Get cross_section_area.

        Returns:
            float: the value of `cross_section_area` or None if not set

        """
        return self["Cross Section Area"]

    @cross_section_area.setter
    def cross_section_area(self, value=None):
        """Corresponds to IDD field `Cross Section Area` Enter the cross
        section area of the duct.

        Args:
            value (float): value for IDD Field `Cross Section Area`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Cross Section Area"] = value

    @property
    def surface_roughness(self):
        """Get surface_roughness.

        Returns:
            float: the value of `surface_roughness` or None if not set

        """
        return self["Surface Roughness"]

    @surface_roughness.setter
    def surface_roughness(self, value=0.0009):
        """Corresponds to IDD field `Surface Roughness` Enter the inside
        surface roughness of the duct.

        Args:
            value (float): value for IDD Field `Surface Roughness`
                Units: m
                Default value: 0.0009
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Surface Roughness"] = value

    @property
    def coefficient_for_local_dynamic_loss_due_to_fitting(self):
        """Get coefficient_for_local_dynamic_loss_due_to_fitting.

        Returns:
            float: the value of `coefficient_for_local_dynamic_loss_due_to_fitting` or None if not set

        """
        return self["Coefficient for Local Dynamic Loss Due to Fitting"]

    @coefficient_for_local_dynamic_loss_due_to_fitting.setter
    def coefficient_for_local_dynamic_loss_due_to_fitting(self, value=None):
        """Corresponds to IDD field `Coefficient for Local Dynamic Loss Due to
        Fitting` Enter the coefficient used to calculate dynamic losses of
        fittings (e.g. elbows).

        Args:
            value (float): value for IDD Field `Coefficient for Local Dynamic Loss Due to Fitting`
                Units: dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Coefficient for Local Dynamic Loss Due to Fitting"] = value

    @property
    def overall_heat_transmittance_coefficient_ufactor_from_air_to_air(self):
        """Get overall_heat_transmittance_coefficient_ufactor_from_air_to_air.

        Returns:
            float: the value of `overall_heat_transmittance_coefficient_ufactor_from_air_to_air` or None if not set

        """
        return self[
            "Overall Heat Transmittance Coefficient (U-Factor) from Air to Air"]

    @overall_heat_transmittance_coefficient_ufactor_from_air_to_air.setter
    def overall_heat_transmittance_coefficient_ufactor_from_air_to_air(
            self,
            value=0.772):
        """  Corresponds to IDD field `Overall Heat Transmittance Coefficient (U-Factor) from Air to Air`
        including film coefficients at both surfaces
        Enter the overall U-value for this duct.
        Default value of 0.772 is equivalent to 1.06 m2-K/W (R6) duct insulation with
        film coefficients for outside and inside equal to 5 and 25 W/m2-K, respectively.

        Args:
            value (float): value for IDD Field `Overall Heat Transmittance Coefficient (U-Factor) from Air to Air`
                Units: W/m2-K
                Default value: 0.772
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self[
            "Overall Heat Transmittance Coefficient (U-Factor) from Air to Air"] = value

    @property
    def overall_moisture_transmittance_coefficient_from_air_to_air(self):
        """Get overall_moisture_transmittance_coefficient_from_air_to_air.

        Returns:
            float: the value of `overall_moisture_transmittance_coefficient_from_air_to_air` or None if not set

        """
        return self[
            "Overall Moisture Transmittance Coefficient from Air to Air"]

    @overall_moisture_transmittance_coefficient_from_air_to_air.setter
    def overall_moisture_transmittance_coefficient_from_air_to_air(
            self,
            value=0.001):
        """Corresponds to IDD field `Overall Moisture Transmittance Coefficient
        from Air to Air` Enter the overall moisture transmittance coefficient
        including moisture film coefficients at both surfaces.

        Args:
            value (float): value for IDD Field `Overall Moisture Transmittance Coefficient from Air to Air`
                Units: kg/m2
                Default value: 0.001
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self[
            "Overall Moisture Transmittance Coefficient from Air to Air"] = value




class AirflowNetworkDistributionComponentFan(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Fan`
        This object defines the name of the constant volume supply Air Fan used in an Air loop.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'fan name',
                                      {'name': u'Fan Name',
                                       'pyname': u'fan_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'supply fan object type',
                                      {'name': u'Supply Fan Object Type',
                                       'pyname': u'supply_fan_object_type',
                                       'default': u'Fan:ConstantVolume',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Fan:OnOff',
                                                           u'Fan:ConstantVolume',
                                                           u'Fan:VariableVolume'],
                                       'autocalculatable': False,
                                       'type': 'alpha'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 2,
              'name': u'AirflowNetwork:Distribution:Component:Fan',
              'pyname': u'AirflowNetworkDistributionComponentFan',
              'required-object': False,
              'unique-object': False}

    @property
    def fan_name(self):
        """Get fan_name.

        Returns:
            str: the value of `fan_name` or None if not set

        """
        return self["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """Corresponds to IDD field `Fan Name` Enter the name of the constant
        volume fan in the primary air loop.

        Args:
            value (str): value for IDD Field `Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fan Name"] = value

    @property
    def supply_fan_object_type(self):
        """Get supply_fan_object_type.

        Returns:
            str: the value of `supply_fan_object_type` or None if not set

        """
        return self["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value="Fan:ConstantVolume"):
        """Corresponds to IDD field `Supply Fan Object Type`

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`
                Default value: Fan:ConstantVolume
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Supply Fan Object Type"] = value




class AirflowNetworkDistributionComponentCoil(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:Coil`
        This object defines the name of a coil used in an air loop.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'coil name',
                                      {'name': u'Coil Name',
                                       'pyname': u'coil_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'coil object type',
                                      {'name': u'Coil Object Type',
                                       'pyname': u'coil_object_type',
                                       'required-field': True,
                                       'autosizable': False,
                                       'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                           u'Coil:Heating:Gas',
                                                           u'Coil:Heating:Electric',
                                                           u'Coil:Heating:DX:SingleSpeed',
                                                           u'Coil:Cooling:Water',
                                                           u'Coil:Heating:Water',
                                                           u'Coil:Cooling:Water:DetailedGeometry',
                                                           u'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
                                                           u'Coil:Cooling:DX:MultiSpeed',
                                                           u'Coil:Heating:DX:MultiSpeed',
                                                           u'Coil:Heating:Desuperheater'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'air path length',
                                      {'name': u'Air Path Length',
                                       'pyname': u'air_path_length',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'air path hydraulic diameter',
                                      {'name': u'Air Path Hydraulic Diameter',
                                       'pyname': u'air_path_hydraulic_diameter',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:Distribution:Component:Coil',
              'pyname': u'AirflowNetworkDistributionComponentCoil',
              'required-object': False,
              'unique-object': False}

    @property
    def coil_name(self):
        """Get coil_name.

        Returns:
            str: the value of `coil_name` or None if not set

        """
        return self["Coil Name"]

    @coil_name.setter
    def coil_name(self, value=None):
        """Corresponds to IDD field `Coil Name` Enter the name of a cooling or
        heating coil in the primary Air loop.

        Args:
            value (str): value for IDD Field `Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Coil Name"] = value

    @property
    def coil_object_type(self):
        """Get coil_object_type.

        Returns:
            str: the value of `coil_object_type` or None if not set

        """
        return self["Coil Object Type"]

    @coil_object_type.setter
    def coil_object_type(self, value=None):
        """Corresponds to IDD field `Coil Object Type` Select the type of coil
        corresponding to the name entered in the field above.

        Args:
            value (str): value for IDD Field `Coil Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Coil Object Type"] = value

    @property
    def air_path_length(self):
        """Get air_path_length.

        Returns:
            float: the value of `air_path_length` or None if not set

        """
        return self["Air Path Length"]

    @air_path_length.setter
    def air_path_length(self, value=None):
        """Corresponds to IDD field `Air Path Length` Enter the air path length
        (depth) for the coil.

        Args:
            value (float): value for IDD Field `Air Path Length`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Path Length"] = value

    @property
    def air_path_hydraulic_diameter(self):
        """Get air_path_hydraulic_diameter.

        Returns:
            float: the value of `air_path_hydraulic_diameter` or None if not set

        """
        return self["Air Path Hydraulic Diameter"]

    @air_path_hydraulic_diameter.setter
    def air_path_hydraulic_diameter(self, value=None):
        """Corresponds to IDD field `Air Path Hydraulic Diameter` Enter the
        hydraulic diameter of this coil. The hydraulic diameter is defined as 4
        multiplied by the cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `Air Path Hydraulic Diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Path Hydraulic Diameter"] = value




class AirflowNetworkDistributionComponentHeatExchanger(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:HeatExchanger`
        This object defines the name of an air-to-air heat exchanger used in an air loop.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'heatexchanger name',
                                      {'name': u'HeatExchanger Name',
                                       'pyname': u'heatexchanger_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'heatexchanger object type',
                                      {'name': u'HeatExchanger Object Type',
                                       'pyname': u'heatexchanger_object_type',
                                       'required-field': True,
                                       'autosizable': False,
                                       'accepted-values': [u'HeatExchanger:AirToAir:FlatPlate',
                                                           u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                           u'HeatExchanger:Desiccant:BalancedFlow'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'air path length',
                                      {'name': u'Air Path Length',
                                       'pyname': u'air_path_length',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'air path hydraulic diameter',
                                      {'name': u'Air Path Hydraulic Diameter',
                                       'pyname': u'air_path_hydraulic_diameter',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:Distribution:Component:HeatExchanger',
              'pyname': u'AirflowNetworkDistributionComponentHeatExchanger',
              'required-object': False,
              'unique-object': False}

    @property
    def heatexchanger_name(self):
        """Get heatexchanger_name.

        Returns:
            str: the value of `heatexchanger_name` or None if not set

        """
        return self["HeatExchanger Name"]

    @heatexchanger_name.setter
    def heatexchanger_name(self, value=None):
        """  Corresponds to IDD field `HeatExchanger Name`
        Enter the name of an air-to-air heat exchanger in the primary Air loop.

        Args:
            value (str): value for IDD Field `HeatExchanger Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["HeatExchanger Name"] = value

    @property
    def heatexchanger_object_type(self):
        """Get heatexchanger_object_type.

        Returns:
            str: the value of `heatexchanger_object_type` or None if not set

        """
        return self["HeatExchanger Object Type"]

    @heatexchanger_object_type.setter
    def heatexchanger_object_type(self, value=None):
        """Corresponds to IDD field `HeatExchanger Object Type` Select the type
        of heat exchanger corresponding to the name entered in the field above.

        Args:
            value (str): value for IDD Field `HeatExchanger Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["HeatExchanger Object Type"] = value

    @property
    def air_path_length(self):
        """Get air_path_length.

        Returns:
            float: the value of `air_path_length` or None if not set

        """
        return self["Air Path Length"]

    @air_path_length.setter
    def air_path_length(self, value=None):
        """Corresponds to IDD field `Air Path Length` Enter the air path length
        (depth) for the heat exchanger.

        Args:
            value (float): value for IDD Field `Air Path Length`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Path Length"] = value

    @property
    def air_path_hydraulic_diameter(self):
        """Get air_path_hydraulic_diameter.

        Returns:
            float: the value of `air_path_hydraulic_diameter` or None if not set

        """
        return self["Air Path Hydraulic Diameter"]

    @air_path_hydraulic_diameter.setter
    def air_path_hydraulic_diameter(self, value=None):
        """Corresponds to IDD field `Air Path Hydraulic Diameter` Enter the
        hydraulic diameter of this heat exchanger. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `Air Path Hydraulic Diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Path Hydraulic Diameter"] = value




class AirflowNetworkDistributionComponentTerminalUnit(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:TerminalUnit`
        This object defines the name of a terminal unit in an air loop.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'terminal unit name',
                                      {'name': u'Terminal Unit Name',
                                       'pyname': u'terminal_unit_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'terminal unit object type',
                                      {'name': u'Terminal Unit Object Type',
                                       'pyname': u'terminal_unit_object_type',
                                       'required-field': True,
                                       'autosizable': False,
                                       'accepted-values': [u'AirTerminal:SingleDuct:ConstantVolume:Reheat',
                                                           u'AirTerminal:SingleDuct:VAV:Reheat'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'air path length',
                                      {'name': u'Air Path Length',
                                       'pyname': u'air_path_length',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'}),
                                     (u'air path hydraulic diameter',
                                      {'name': u'Air Path Hydraulic Diameter',
                                       'pyname': u'air_path_hydraulic_diameter',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:Distribution:Component:TerminalUnit',
              'pyname': u'AirflowNetworkDistributionComponentTerminalUnit',
              'required-object': False,
              'unique-object': False}

    @property
    def terminal_unit_name(self):
        """Get terminal_unit_name.

        Returns:
            str: the value of `terminal_unit_name` or None if not set

        """
        return self["Terminal Unit Name"]

    @terminal_unit_name.setter
    def terminal_unit_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Name` Enter the name of a
        terminal unit in the AirLoopHVAC.

        Args:
            value (str): value for IDD Field `Terminal Unit Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Terminal Unit Name"] = value

    @property
    def terminal_unit_object_type(self):
        """Get terminal_unit_object_type.

        Returns:
            str: the value of `terminal_unit_object_type` or None if not set

        """
        return self["Terminal Unit Object Type"]

    @terminal_unit_object_type.setter
    def terminal_unit_object_type(self, value=None):
        """Corresponds to IDD field `Terminal Unit Object Type` Select the type
        of terminal unit corresponding to the name entered in the field above.

        Args:
            value (str): value for IDD Field `Terminal Unit Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Terminal Unit Object Type"] = value

    @property
    def air_path_length(self):
        """Get air_path_length.

        Returns:
            float: the value of `air_path_length` or None if not set

        """
        return self["Air Path Length"]

    @air_path_length.setter
    def air_path_length(self, value=None):
        """Corresponds to IDD field `Air Path Length` Enter the air path length
        (depth) for the terminal unit.

        Args:
            value (float): value for IDD Field `Air Path Length`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Path Length"] = value

    @property
    def air_path_hydraulic_diameter(self):
        """Get air_path_hydraulic_diameter.

        Returns:
            float: the value of `air_path_hydraulic_diameter` or None if not set

        """
        return self["Air Path Hydraulic Diameter"]

    @air_path_hydraulic_diameter.setter
    def air_path_hydraulic_diameter(self, value=None):
        """Corresponds to IDD field `Air Path Hydraulic Diameter` Enter the
        hydraulic diameter of this terminal unit. The hydraulic diameter is
        defined as 4 multiplied by the cross section area divided by perimeter.

        Args:
            value (float): value for IDD Field `Air Path Hydraulic Diameter`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Air Path Hydraulic Diameter"] = value




class AirflowNetworkDistributionComponentConstantPressureDrop(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Component:ConstantPressureDrop`
        This object defines the characteristics of a constant pressure drop component (e.g. filter).
        Each node connected to this object can not be a node of mixer, splitter, a node of air primary
        loop, or zone equipment loop. It is recommended to connect to a duct component at both ends.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'pressure difference across the component',
                                      {'name': u'Pressure Difference Across the Component',
                                       'pyname': u'pressure_difference_across_the_component',
                                       'minimum>': 0.0,
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'Pa'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 2,
              'name': u'AirflowNetwork:Distribution:Component:ConstantPressureDrop',
              'pyname': u'AirflowNetworkDistributionComponentConstantPressureDrop',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def pressure_difference_across_the_component(self):
        """Get pressure_difference_across_the_component.

        Returns:
            float: the value of `pressure_difference_across_the_component` or None if not set

        """
        return self["Pressure Difference Across the Component"]

    @pressure_difference_across_the_component.setter
    def pressure_difference_across_the_component(self, value=None):
        """Corresponds to IDD field `Pressure Difference Across the Component`
        Enter the pressure drop across this component.

        Args:
            value (float): value for IDD Field `Pressure Difference Across the Component`
                Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Pressure Difference Across the Component"] = value




class AirflowNetworkDistributionLinkage(DataObject):

    """ Corresponds to IDD object `AirflowNetwork:Distribution:Linkage`
        This object defines the connection between two nodes and a component.
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'node 1 name',
                                      {'name': u'Node 1 Name',
                                       'pyname': u'node_1_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'node 2 name',
                                      {'name': u'Node 2 Name',
                                       'pyname': u'node_2_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'component name',
                                      {'name': u'Component Name',
                                       'pyname': u'component_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'thermal zone name',
                                      {'name': u'Thermal Zone Name',
                                       'pyname': u'thermal_zone_name',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'})]),
              'format': None,
              'group': u'Natural Ventilation and Duct Leakage',
              'min-fields': 4,
              'name': u'AirflowNetwork:Distribution:Linkage',
              'pyname': u'AirflowNetworkDistributionLinkage',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name` Enter a unique name for this object.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def node_1_name(self):
        """Get node_1_name.

        Returns:
            str: the value of `node_1_name` or None if not set

        """
        return self["Node 1 Name"]

    @node_1_name.setter
    def node_1_name(self, value=None):
        """Corresponds to IDD field `Node 1 Name` Enter the name of zone or
        AirflowNetwork Node.

        Args:
            value (str): value for IDD Field `Node 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Node 1 Name"] = value

    @property
    def node_2_name(self):
        """Get node_2_name.

        Returns:
            str: the value of `node_2_name` or None if not set

        """
        return self["Node 2 Name"]

    @node_2_name.setter
    def node_2_name(self, value=None):
        """Corresponds to IDD field `Node 2 Name` Enter the name of zone or
        AirflowNetwork Node.

        Args:
            value (str): value for IDD Field `Node 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Node 2 Name"] = value

    @property
    def component_name(self):
        """Get component_name.

        Returns:
            str: the value of `component_name` or None if not set

        """
        return self["Component Name"]

    @component_name.setter
    def component_name(self, value=None):
        """  Corresponds to IDD field `Component Name`
        Enter the name of an AirflowNetwork component. A component is one of the
        following AirflowNetwork:Distribution:Component objects: Leak, LeakageRatio,
        Duct, ConstantVolumeFan, Coil, TerminalUnit, ConstantPressureDrop, or HeatExchanger.

        Args:
            value (str): value for IDD Field `Component Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Component Name"] = value

    @property
    def thermal_zone_name(self):
        """Get thermal_zone_name.

        Returns:
            str: the value of `thermal_zone_name` or None if not set

        """
        return self["Thermal Zone Name"]

    @thermal_zone_name.setter
    def thermal_zone_name(self, value=None):
        """  Corresponds to IDD field `Thermal Zone Name`
        Only used if component = AirflowNetwork:Distribution:Component:Duct
        The zone name is where AirflowNetwork:Distribution:Component:Duct is exposed. Leave this field blank if the duct
        conduction loss is ignored.

        Args:
            value (str): value for IDD Field `Thermal Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["Thermal Zone Name"] = value


