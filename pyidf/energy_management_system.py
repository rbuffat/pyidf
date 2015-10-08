""" Data objects in group "Energy Management System"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class EnergyManagementSystemSensor(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:Sensor`
        Declares EMS variable as a sensor
        a list of output variables and meters that can be reported are available after a run on
        the report (.rdd) or meter dictionary file (.mdd) if the Output:VariableDictionary
        has been requested.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'output:variable or output:meter index key name',
                                       {'name': u'Output:Variable or Output:Meter Index Key Name',
                                        'pyname': u'outputvariable_or_outputmeter_index_key_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'output:variable or output:meter name',
                                       {'name': u'Output:Variable or Output:Meter Name',
                                        'pyname': u'outputvariable_or_outputmeter_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 3,
               'name': u'EnergyManagementSystem:Sensor',
               'pyname': u'EnergyManagementSystemSensor',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

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
    def outputvariable_or_outputmeter_index_key_name(self):
        """field `Output:Variable or Output:Meter Index Key Name`


        Args:
            value (str): value for IDD Field `Output:Variable or Output:Meter Index Key Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outputvariable_or_outputmeter_index_key_name` or None if not set
        """
        return self["Output:Variable or Output:Meter Index Key Name"]

    @outputvariable_or_outputmeter_index_key_name.setter
    def outputvariable_or_outputmeter_index_key_name(self, value=None):
        """  Corresponds to IDD field `Output:Variable or Output:Meter Index Key Name`

        """
        self["Output:Variable or Output:Meter Index Key Name"] = value

    @property
    def outputvariable_or_outputmeter_name(self):
        """field `Output:Variable or Output:Meter Name`


        Args:
            value (str): value for IDD Field `Output:Variable or Output:Meter Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outputvariable_or_outputmeter_name` or None if not set
        """
        return self["Output:Variable or Output:Meter Name"]

    @outputvariable_or_outputmeter_name.setter
    def outputvariable_or_outputmeter_name(self, value=None):
        """  Corresponds to IDD field `Output:Variable or Output:Meter Name`

        """
        self["Output:Variable or Output:Meter Name"] = value




class EnergyManagementSystemActuator(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:Actuator`
        Hardware portion of EMS used to set up actuators in the model
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component unique name',
                                       {'name': u'Actuated Component Unique Name',
                                        'pyname': u'actuated_component_unique_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component type',
                                       {'name': u'Actuated Component Type',
                                        'pyname': u'actuated_component_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'actuated component control type',
                                       {'name': u'Actuated Component Control Type',
                                        'pyname': u'actuated_component_control_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 4,
               'name': u'EnergyManagementSystem:Actuator',
               'pyname': u'EnergyManagementSystemActuator',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

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
    def actuated_component_unique_name(self):
        """field `Actuated Component Unique Name`

        Args:
            value (str): value for IDD Field `Actuated Component Unique Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_unique_name` or None if not set

        """
        return self["Actuated Component Unique Name"]

    @actuated_component_unique_name.setter
    def actuated_component_unique_name(self, value=None):
        """Corresponds to IDD field `Actuated Component Unique Name`"""
        self["Actuated Component Unique Name"] = value

    @property
    def actuated_component_type(self):
        """field `Actuated Component Type`

        Args:
            value (str): value for IDD Field `Actuated Component Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_type` or None if not set

        """
        return self["Actuated Component Type"]

    @actuated_component_type.setter
    def actuated_component_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Type`"""
        self["Actuated Component Type"] = value

    @property
    def actuated_component_control_type(self):
        """field `Actuated Component Control Type`

        Args:
            value (str): value for IDD Field `Actuated Component Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuated_component_control_type` or None if not set

        """
        return self["Actuated Component Control Type"]

    @actuated_component_control_type.setter
    def actuated_component_control_type(self, value=None):
        """Corresponds to IDD field `Actuated Component Control Type`"""
        self["Actuated Component Control Type"] = value




class EnergyManagementSystemProgramCallingManager(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:ProgramCallingManager`
        Input EMS program. a program needs a name
        a description of when it should be called
        and then lines of program code for EMS Runtime language
    """
    _schema = {'extensible-fields': OrderedDict([(u'program name 1',
                                                  {'name': u'Program Name 1',
                                                   'pyname': u'program_name_1',
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
                                      (u'energyplus model calling point',
                                       {'name': u'EnergyPlus Model Calling Point',
                                        'pyname': u'energyplus_model_calling_point',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BeginNewEnvironment',
                                                            u'AfterNewEnvironmentWarmUpIsComplete',
                                                            u'BeginTimestepBeforePredictor',
                                                            u'AfterPredictorBeforeHVACManagers',
                                                            u'AfterPredictorAfterHVACManagers',
                                                            u'InsideHVACSystemIterationLoop',
                                                            u'EndOfZoneTimestepBeforeZoneReporting',
                                                            u'EndOfZoneTimestepAfterZoneReporting',
                                                            u'EndOfSystemTimestepBeforeHVACReporting',
                                                            u'EndOfSystemTimestepAfterHVACReporting',
                                                            u'EndOfZoneSizing',
                                                            u'EndOfSystemSizing',
                                                            u'AfterComponentInputReadIn',
                                                            u'UserDefinedComponentModel',
                                                            u'UnitarySystemSizing'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 3,
               'name': u'EnergyManagementSystem:ProgramCallingManager',
               'pyname': u'EnergyManagementSystemProgramCallingManager',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  no spaces allowed in name

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
    def energyplus_model_calling_point(self):
        """field `EnergyPlus Model Calling Point`

        Args:
            value (str): value for IDD Field `EnergyPlus Model Calling Point`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `energyplus_model_calling_point` or None if not set

        """
        return self["EnergyPlus Model Calling Point"]

    @energyplus_model_calling_point.setter
    def energyplus_model_calling_point(self, value=None):
        """Corresponds to IDD field `EnergyPlus Model Calling Point`"""
        self["EnergyPlus Model Calling Point"] = value

    def add_extensible(self,
                       program_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            program_name_1 (str): value for IDD Field `Program Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        program_name_1 = self.check_value("Program Name 1", program_name_1)
        vals.append(program_name_1)
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




class EnergyManagementSystemOutputVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:OutputVariable`
        This object sets up an EnergyPlus output variable from an Erl variable
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'ems variable name',
                                       {'name': u'EMS Variable Name',
                                        'pyname': u'ems_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'type of data in variable',
                                       {'name': u'Type of Data in Variable',
                                        'pyname': u'type_of_data_in_variable',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Averaged',
                                                            u'Summed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'update frequency',
                                       {'name': u'Update Frequency',
                                        'pyname': u'update_frequency',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneTimestep',
                                                            u'SystemTimestep'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ems program or subroutine name',
                                       {'name': u'EMS Program or Subroutine Name',
                                        'pyname': u'ems_program_or_subroutine_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'units',
                                       {'name': u'Units',
                                        'pyname': u'units',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 4,
               'name': u'EnergyManagementSystem:OutputVariable',
               'pyname': u'EnergyManagementSystemOutputVariable',
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
    def ems_variable_name(self):
        """field `EMS Variable Name`

        |  must be an acceptable EMS variable

        Args:
            value (str): value for IDD Field `EMS Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ems_variable_name` or None if not set

        """
        return self["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """Corresponds to IDD field `EMS Variable Name`"""
        self["EMS Variable Name"] = value

    @property
    def type_of_data_in_variable(self):
        """field `Type of Data in Variable`

        Args:
            value (str): value for IDD Field `Type of Data in Variable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `type_of_data_in_variable` or None if not set

        """
        return self["Type of Data in Variable"]

    @type_of_data_in_variable.setter
    def type_of_data_in_variable(self, value=None):
        """Corresponds to IDD field `Type of Data in Variable`"""
        self["Type of Data in Variable"] = value

    @property
    def update_frequency(self):
        """field `Update Frequency`

        Args:
            value (str): value for IDD Field `Update Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `update_frequency` or None if not set

        """
        return self["Update Frequency"]

    @update_frequency.setter
    def update_frequency(self, value=None):
        """Corresponds to IDD field `Update Frequency`"""
        self["Update Frequency"] = value

    @property
    def ems_program_or_subroutine_name(self):
        """field `EMS Program or Subroutine Name`

        |  optional for global scope variables, required for local scope variables

        Args:
            value (str): value for IDD Field `EMS Program or Subroutine Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ems_program_or_subroutine_name` or None if not set

        """
        return self["EMS Program or Subroutine Name"]

    @ems_program_or_subroutine_name.setter
    def ems_program_or_subroutine_name(self, value=None):
        """Corresponds to IDD field `EMS Program or Subroutine Name`"""
        self["EMS Program or Subroutine Name"] = value

    @property
    def units(self):
        """field `Units`

        |  optional but will result in dimensionless units for blank
        |  EnergyPlus units are standard SI units

        Args:
            value (str): value for IDD Field `Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `units` or None if not set

        """
        return self["Units"]

    @units.setter
    def units(self, value=None):
        """Corresponds to IDD field `Units`"""
        self["Units"] = value




class EnergyManagementSystemMeteredOutputVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:MeteredOutputVariable`
        This object sets up an EnergyPlus output variable from an Erl variable
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'ems variable name',
                                       {'name': u'EMS Variable Name',
                                        'pyname': u'ems_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'update frequency',
                                       {'name': u'Update Frequency',
                                        'pyname': u'update_frequency',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneTimestep',
                                                            u'SystemTimestep'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ems program or subroutine name',
                                       {'name': u'EMS Program or Subroutine Name',
                                        'pyname': u'ems_program_or_subroutine_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'resource type',
                                       {'name': u'Resource Type',
                                        'pyname': u'resource_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'Gasoline',
                                                            u'Diesel',
                                                            u'Coal',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Propane',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'WaterUse',
                                                            u'OnSiteWaterProduced',
                                                            u'MainsWaterSupply',
                                                            u'RainWaterCollected',
                                                            u'WellWaterDrawn',
                                                            u'CondensateWaterCollected',
                                                            u'EnergyTransfer',
                                                            u'Steam',
                                                            u'DistrictCooling',
                                                            u'DistrictHeating',
                                                            u'ElectricityProducedOnSite',
                                                            u'SolarWaterHeating',
                                                            u'SolarAirHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'group type',
                                       {'name': u'Group Type',
                                        'pyname': u'group_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Building',
                                                            u'HVAC',
                                                            u'Plant',
                                                            u'System'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'end-use category',
                                       {'name': u'End-Use Category',
                                        'pyname': u'enduse_category',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'InteriorLights',
                                                            u'ExteriorLights',
                                                            u'InteriorEquipment',
                                                            u'ExteriorEquipment',
                                                            u'Fans',
                                                            u'Pumps',
                                                            u'HeatRejection',
                                                            u'Humidifier',
                                                            u'HeatRecovery',
                                                            u'WaterSystems',
                                                            u'Refrigeration',
                                                            u'OnSiteGeneration',
                                                            u'HeatingCoils',
                                                            u'CoolingCoils',
                                                            u'Chillers',
                                                            u'Boilers',
                                                            u'Baseboard',
                                                            u'HeatRecoveryForCooling',
                                                            u'HeatRecoveryForHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'units',
                                       {'name': u'Units',
                                        'pyname': u'units',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 7,
               'name': u'EnergyManagementSystem:MeteredOutputVariable',
               'pyname': u'EnergyManagementSystemMeteredOutputVariable',
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
    def ems_variable_name(self):
        """field `EMS Variable Name`

        |  must be an acceptable EMS variable, no spaces

        Args:
            value (str): value for IDD Field `EMS Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ems_variable_name` or None if not set

        """
        return self["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """Corresponds to IDD field `EMS Variable Name`"""
        self["EMS Variable Name"] = value

    @property
    def update_frequency(self):
        """field `Update Frequency`

        Args:
            value (str): value for IDD Field `Update Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `update_frequency` or None if not set

        """
        return self["Update Frequency"]

    @update_frequency.setter
    def update_frequency(self, value=None):
        """Corresponds to IDD field `Update Frequency`"""
        self["Update Frequency"] = value

    @property
    def ems_program_or_subroutine_name(self):
        """field `EMS Program or Subroutine Name`

        |  optional for global scope variables, required for local scope variables

        Args:
            value (str): value for IDD Field `EMS Program or Subroutine Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ems_program_or_subroutine_name` or None if not set

        """
        return self["EMS Program or Subroutine Name"]

    @ems_program_or_subroutine_name.setter
    def ems_program_or_subroutine_name(self, value=None):
        """Corresponds to IDD field `EMS Program or Subroutine Name`"""
        self["EMS Program or Subroutine Name"] = value

    @property
    def resource_type(self):
        """field `Resource Type`

        |  choose the type of fuel, water, electricity, pollution or heat rate that should be metered.

        Args:
            value (str): value for IDD Field `Resource Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `resource_type` or None if not set

        """
        return self["Resource Type"]

    @resource_type.setter
    def resource_type(self, value=None):
        """Corresponds to IDD field `Resource Type`"""
        self["Resource Type"] = value

    @property
    def group_type(self):
        """field `Group Type`

        |  choose a general classification, building (internal services), HVAC (air systems), or plant (hydronic systems), or system

        Args:
            value (str): value for IDD Field `Group Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `group_type` or None if not set

        """
        return self["Group Type"]

    @group_type.setter
    def group_type(self, value=None):
        """Corresponds to IDD field `Group Type`"""
        self["Group Type"] = value

    @property
    def enduse_category(self):
        """field `End-Use Category`

        |  choose how the metered output should be classified for end-use category

        Args:
            value (str): value for IDD Field `End-Use Category`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_category` or None if not set
        """
        return self["End-Use Category"]

    @enduse_category.setter
    def enduse_category(self, value=None):
        """  Corresponds to IDD field `End-Use Category`

        """
        self["End-Use Category"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  enter a user-defined subcategory for this metered output

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value=None):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def units(self):
        """field `Units`

        |  optional but will result in dimensionless units for blank
        |  EnergyPlus units are standard SI units

        Args:
            value (str): value for IDD Field `Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `units` or None if not set

        """
        return self["Units"]

    @units.setter
    def units(self, value=None):
        """Corresponds to IDD field `Units`"""
        self["Units"] = value




class EnergyManagementSystemTrendVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:TrendVariable`
        This object sets up an EMS trend variable from an Erl variable
        A trend variable logs values across timesteps
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'ems variable name',
                                       {'name': u'EMS Variable Name',
                                        'pyname': u'ems_variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'number of timesteps to be logged',
                                       {'name': u'Number of Timesteps to be Logged',
                                        'pyname': u'number_of_timesteps_to_be_logged',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 3,
               'name': u'EnergyManagementSystem:TrendVariable',
               'pyname': u'EnergyManagementSystemTrendVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  no spaces allowed in name

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
    def ems_variable_name(self):
        """field `EMS Variable Name`

        |  must be a global scope EMS variable

        Args:
            value (str): value for IDD Field `EMS Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ems_variable_name` or None if not set

        """
        return self["EMS Variable Name"]

    @ems_variable_name.setter
    def ems_variable_name(self, value=None):
        """Corresponds to IDD field `EMS Variable Name`"""
        self["EMS Variable Name"] = value

    @property
    def number_of_timesteps_to_be_logged(self):
        """field `Number of Timesteps to be Logged`

        |  value >= 1

        Args:
            value (int): value for IDD Field `Number of Timesteps to be Logged`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_timesteps_to_be_logged` or None if not set

        """
        return self["Number of Timesteps to be Logged"]

    @number_of_timesteps_to_be_logged.setter
    def number_of_timesteps_to_be_logged(self, value=None):
        """Corresponds to IDD field `Number of Timesteps to be Logged`"""
        self["Number of Timesteps to be Logged"] = value




class EnergyManagementSystemInternalVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:InternalVariable`
        Declares EMS variable as an internal data variable
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'internal data index key name',
                                       {'name': u'Internal Data Index Key Name',
                                        'pyname': u'internal_data_index_key_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'internal data type',
                                       {'name': u'Internal Data Type',
                                        'pyname': u'internal_data_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 3,
               'name': u'EnergyManagementSystem:InternalVariable',
               'pyname': u'EnergyManagementSystemInternalVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

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
    def internal_data_index_key_name(self):
        """field `Internal Data Index Key Name`

        Args:
            value (str): value for IDD Field `Internal Data Index Key Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `internal_data_index_key_name` or None if not set

        """
        return self["Internal Data Index Key Name"]

    @internal_data_index_key_name.setter
    def internal_data_index_key_name(self, value=None):
        """Corresponds to IDD field `Internal Data Index Key Name`"""
        self["Internal Data Index Key Name"] = value

    @property
    def internal_data_type(self):
        """field `Internal Data Type`

        Args:
            value (str): value for IDD Field `Internal Data Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `internal_data_type` or None if not set

        """
        return self["Internal Data Type"]

    @internal_data_type.setter
    def internal_data_type(self, value=None):
        """Corresponds to IDD field `Internal Data Type`"""
        self["Internal Data Type"] = value




class EnergyManagementSystemCurveOrTableIndexVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:CurveOrTableIndexVariable`
        Declares EMS variable that identifies a curve or table
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'curve or table object name',
                                       {'name': u'Curve or Table Object Name',
                                        'pyname': u'curve_or_table_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 2,
               'name': u'EnergyManagementSystem:CurveOrTableIndexVariable',
               'pyname': u'EnergyManagementSystemCurveOrTableIndexVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

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
    def curve_or_table_object_name(self):
        """field `Curve or Table Object Name`

        Args:
            value (str): value for IDD Field `Curve or Table Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `curve_or_table_object_name` or None if not set

        """
        return self["Curve or Table Object Name"]

    @curve_or_table_object_name.setter
    def curve_or_table_object_name(self, value=None):
        """Corresponds to IDD field `Curve or Table Object Name`"""
        self["Curve or Table Object Name"] = value




class EnergyManagementSystemConstructionIndexVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:ConstructionIndexVariable`
        Declares EMS variable that identifies a construction
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'construction object name',
                                       {'name': u'Construction Object Name',
                                        'pyname': u'construction_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 2,
               'name': u'EnergyManagementSystem:ConstructionIndexVariable',
               'pyname': u'EnergyManagementSystemConstructionIndexVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This name becomes a variable for use in Erl programs
        |  no spaces allowed in name

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
    def construction_object_name(self):
        """field `Construction Object Name`

        Args:
            value (str): value for IDD Field `Construction Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `construction_object_name` or None if not set

        """
        return self["Construction Object Name"]

    @construction_object_name.setter
    def construction_object_name(self, value=None):
        """Corresponds to IDD field `Construction Object Name`"""
        self["Construction Object Name"] = value




class EnergyManagementSystemProgram(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:Program`
        This input defines an Erl program
        Each field after the name is a line of EMS Runtime Language
    """
    _schema = {'extensible-fields': OrderedDict([(u'program line 1',
                                                  {'name': u'Program Line 1',
                                                   'pyname': u'program_line_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 2,
               'name': u'EnergyManagementSystem:Program',
               'pyname': u'EnergyManagementSystemProgram',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  no spaces allowed in name

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
                       program_line_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            program_line_1 (str): value for IDD Field `Program Line 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        program_line_1 = self.check_value("Program Line 1", program_line_1)
        vals.append(program_line_1)
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




class EnergyManagementSystemSubroutine(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:Subroutine`
        This input defines an Erl program subroutine
        Each field after the name is a line of EMS Runtime Language
    """
    _schema = {'extensible-fields': OrderedDict([(u'program line',
                                                  {'name': u'Program Line',
                                                   'pyname': u'program_line',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 2,
               'name': u'EnergyManagementSystem:Subroutine',
               'pyname': u'EnergyManagementSystemSubroutine',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  no spaces allowed in name

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
                       program_line=None,
                       ):
        """Add values for extensible fields.

        Args:

            program_line (str): value for IDD Field `Program Line`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        program_line = self.check_value("Program Line", program_line)
        vals.append(program_line)
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




class EnergyManagementSystemGlobalVariable(DataObject):

    """ Corresponds to IDD object `EnergyManagementSystem:GlobalVariable`
        Declares Erl variable as having global scope
        No spaces allowed in names used for Erl variables
    """
    _schema = {'extensible-fields': OrderedDict([(u'erl variable 1 name',
                                                  {'name': u'Erl Variable 1 Name',
                                                   'pyname': u'erl_variable_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Energy Management System',
               'min-fields': 1,
               'name': u'EnergyManagementSystem:GlobalVariable',
               'pyname': u'EnergyManagementSystemGlobalVariable',
               'required-object': False,
               'unique-object': False}

    def add_extensible(self,
                       erl_variable_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            erl_variable_1_name (str): value for IDD Field `Erl Variable 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        erl_variable_1_name = self.check_value(
            "Erl Variable 1 Name",
            erl_variable_1_name)
        vals.append(erl_variable_1_name)
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


