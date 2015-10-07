""" Data objects in group "Water Systems"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class WaterUseEquipment(DataObject):

    """ Corresponds to IDD object `WaterUse:Equipment`
        A generalized object for simulating all water end uses. Hot and cold water uses are
        included, as well as controlled mixing of hot and cold water at the tap. The
        WaterUse:Equipment object can be used stand-alone, or coupled into a plant loop using
        the WaterUse:Connections object (see below). The WaterUse:Connections object allows
        water uses to be linked to WaterUse:Storage objects to store and draw reclaimed water.
        The object can also simulate drainwater heat recovery.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'peak flow rate',
                                       {'name': u'Peak Flow Rate',
                                        'pyname': u'peak_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'flow rate fraction schedule name',
                                       {'name': u'Flow Rate Fraction Schedule Name',
                                        'pyname': u'flow_rate_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'target temperature schedule name',
                                       {'name': u'Target Temperature Schedule Name',
                                        'pyname': u'target_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hot water supply temperature schedule name',
                                       {'name': u'Hot Water Supply Temperature Schedule Name',
                                        'pyname': u'hot_water_supply_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cold water supply temperature schedule name',
                                       {'name': u'Cold Water Supply Temperature Schedule Name',
                                        'pyname': u'cold_water_supply_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sensible fraction schedule name',
                                       {'name': u'Sensible Fraction Schedule Name',
                                        'pyname': u'sensible_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'latent fraction schedule name',
                                       {'name': u'Latent Fraction Schedule Name',
                                        'pyname': u'latent_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Water Systems',
               'min-fields': 0,
               'name': u'WaterUse:Equipment',
               'pyname': u'WaterUseEquipment',
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
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def peak_flow_rate(self):
        """field `Peak Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Peak Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `peak_flow_rate` or None if not set

        """
        return self["Peak Flow Rate"]

    @peak_flow_rate.setter
    def peak_flow_rate(self, value=None):
        """Corresponds to IDD field `Peak Flow Rate`"""
        self["Peak Flow Rate"] = value

    @property
    def flow_rate_fraction_schedule_name(self):
        """field `Flow Rate Fraction Schedule Name`

        |  Defaults to 1.0 at all times

        Args:
            value (str): value for IDD Field `Flow Rate Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `flow_rate_fraction_schedule_name` or None if not set

        """
        return self["Flow Rate Fraction Schedule Name"]

    @flow_rate_fraction_schedule_name.setter
    def flow_rate_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Flow Rate Fraction Schedule Name`"""
        self["Flow Rate Fraction Schedule Name"] = value

    @property
    def target_temperature_schedule_name(self):
        """field `Target Temperature Schedule Name`

        |  Defaults to hot water supply temperature

        Args:
            value (str): value for IDD Field `Target Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `target_temperature_schedule_name` or None if not set

        """
        return self["Target Temperature Schedule Name"]

    @target_temperature_schedule_name.setter
    def target_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Target Temperature Schedule Name`"""
        self["Target Temperature Schedule Name"] = value

    @property
    def hot_water_supply_temperature_schedule_name(self):
        """field `Hot Water Supply Temperature Schedule Name`

        |  Defaults to cold water supply temperature

        Args:
            value (str): value for IDD Field `Hot Water Supply Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_supply_temperature_schedule_name` or None if not set

        """
        return self["Hot Water Supply Temperature Schedule Name"]

    @hot_water_supply_temperature_schedule_name.setter
    def hot_water_supply_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Hot Water Supply Temperature Schedule
        Name`"""
        self["Hot Water Supply Temperature Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """field `Cold Water Supply Temperature Schedule Name`

        |  Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `Cold Water Supply Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set

        """
        return self["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cold Water Supply Temperature Schedule
        Name`"""
        self["Cold Water Supply Temperature Schedule Name"] = value

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

    @property
    def sensible_fraction_schedule_name(self):
        """field `Sensible Fraction Schedule Name`

        |  Defaults to 0.0 at all times

        Args:
            value (str): value for IDD Field `Sensible Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sensible_fraction_schedule_name` or None if not set

        """
        return self["Sensible Fraction Schedule Name"]

    @sensible_fraction_schedule_name.setter
    def sensible_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Sensible Fraction Schedule Name`"""
        self["Sensible Fraction Schedule Name"] = value

    @property
    def latent_fraction_schedule_name(self):
        """field `Latent Fraction Schedule Name`

        |  Defaults to 0.0 at all times

        Args:
            value (str): value for IDD Field `Latent Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `latent_fraction_schedule_name` or None if not set

        """
        return self["Latent Fraction Schedule Name"]

    @latent_fraction_schedule_name.setter
    def latent_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Latent Fraction Schedule Name`"""
        self["Latent Fraction Schedule Name"] = value




class WaterUseConnections(DataObject):

    """ Corresponds to IDD object `WaterUse:Connections`
        A subsystem that groups together multiple WaterUse:Equipment components.
        As its name suggests, the object provides connections that are shared by these
        components, including: 1. Inlet node and outlet node connections to a plant loop
        2. Connections to WaterUse:Storage objects to store and draw reclaimed water
        3. Internal connections to simulate drainwater heat recovery.
    """
    _schema = {'extensible-fields': OrderedDict([(u'water use equipment 1 name',
                                                  {'name': u'Water Use Equipment 1 Name',
                                                   'pyname': u'water_use_equipment_1_name',
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
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply water storage tank name',
                                       {'name': u'Supply Water Storage Tank Name',
                                        'pyname': u'supply_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'reclamation water storage tank name',
                                       {'name': u'Reclamation Water Storage Tank Name',
                                        'pyname': u'reclamation_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hot water supply temperature schedule name',
                                       {'name': u'Hot Water Supply Temperature Schedule Name',
                                        'pyname': u'hot_water_supply_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cold water supply temperature schedule name',
                                       {'name': u'Cold Water Supply Temperature Schedule Name',
                                        'pyname': u'cold_water_supply_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'drain water heat exchanger type',
                                       {'name': u'Drain Water Heat Exchanger Type',
                                        'pyname': u'drain_water_heat_exchanger_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Ideal',
                                                            u'CounterFlow',
                                                            u'CrossFlow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'drain water heat exchanger destination',
                                       {'name': u'Drain Water Heat Exchanger Destination',
                                        'pyname': u'drain_water_heat_exchanger_destination',
                                        'default': u'Plant',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Plant',
                                                            u'Equipment',
                                                            u'PlantAndEquipment'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'drain water heat exchanger u-factor times area',
                                       {'name': u'Drain Water Heat Exchanger U-Factor Times Area',
                                        'pyname': u'drain_water_heat_exchanger_ufactor_times_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'})]),
               'format': None,
               'group': u'Water Systems',
               'min-fields': 0,
               'name': u'WaterUse:Connections',
               'pyname': u'WaterUseConnections',
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
    def inlet_node_name(self):
        """field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """field `Supply Water Storage Tank Name`

        |  If blank, or tank is empty, defaults to fresh water from the mains

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set

        """
        return self["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Supply Water Storage Tank Name`"""
        self["Supply Water Storage Tank Name"] = value

    @property
    def reclamation_water_storage_tank_name(self):
        """field `Reclamation Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Reclamation Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reclamation_water_storage_tank_name` or None if not set

        """
        return self["Reclamation Water Storage Tank Name"]

    @reclamation_water_storage_tank_name.setter
    def reclamation_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Reclamation Water Storage Tank Name`"""
        self["Reclamation Water Storage Tank Name"] = value

    @property
    def hot_water_supply_temperature_schedule_name(self):
        """field `Hot Water Supply Temperature Schedule Name`

        |  Defaults to cold water supply temperature

        Args:
            value (str): value for IDD Field `Hot Water Supply Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_supply_temperature_schedule_name` or None if not set

        """
        return self["Hot Water Supply Temperature Schedule Name"]

    @hot_water_supply_temperature_schedule_name.setter
    def hot_water_supply_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Hot Water Supply Temperature Schedule
        Name`"""
        self["Hot Water Supply Temperature Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """field `Cold Water Supply Temperature Schedule Name`

        |  Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `Cold Water Supply Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set

        """
        return self["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cold Water Supply Temperature Schedule
        Name`"""
        self["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def drain_water_heat_exchanger_type(self):
        """field `Drain Water Heat Exchanger Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Drain Water Heat Exchanger Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drain_water_heat_exchanger_type` or None if not set

        """
        return self["Drain Water Heat Exchanger Type"]

    @drain_water_heat_exchanger_type.setter
    def drain_water_heat_exchanger_type(self, value="None"):
        """Corresponds to IDD field `Drain Water Heat Exchanger Type`"""
        self["Drain Water Heat Exchanger Type"] = value

    @property
    def drain_water_heat_exchanger_destination(self):
        """field `Drain Water Heat Exchanger Destination`

        |  Default value: Plant

        Args:
            value (str): value for IDD Field `Drain Water Heat Exchanger Destination`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drain_water_heat_exchanger_destination` or None if not set

        """
        return self["Drain Water Heat Exchanger Destination"]

    @drain_water_heat_exchanger_destination.setter
    def drain_water_heat_exchanger_destination(self, value="Plant"):
        """Corresponds to IDD field `Drain Water Heat Exchanger Destination`"""
        self["Drain Water Heat Exchanger Destination"] = value

    @property
    def drain_water_heat_exchanger_ufactor_times_area(self):
        """field `Drain Water Heat Exchanger U-Factor Times Area`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Drain Water Heat Exchanger U-Factor Times Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drain_water_heat_exchanger_ufactor_times_area` or None if not set
        """
        return self["Drain Water Heat Exchanger U-Factor Times Area"]

    @drain_water_heat_exchanger_ufactor_times_area.setter
    def drain_water_heat_exchanger_ufactor_times_area(self, value=None):
        """  Corresponds to IDD field `Drain Water Heat Exchanger U-Factor Times Area`

        """
        self["Drain Water Heat Exchanger U-Factor Times Area"] = value

    def add_extensible(self,
                       water_use_equipment_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            water_use_equipment_1_name (str): value for IDD Field `Water Use Equipment 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        water_use_equipment_1_name = self.check_value(
            "Water Use Equipment 1 Name",
            water_use_equipment_1_name)
        vals.append(water_use_equipment_1_name)
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




class WaterUseStorage(DataObject):

    """ Corresponds to IDD object `WaterUse:Storage`
        A water storage tank. If the building model is to include any on-site
        water collection, wells, or storing and reuse of graywater, then a WaterUse:Storage
        object is needed. Each WaterUse:Storage can serve as a central node and make
        connections to numerous sources of supply or numerous components with demand. If a
        maximum capacity is not specified, the tank is assumed to have unlimited capacity.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'water quality subcategory',
                                       {'name': u'Water Quality Subcategory',
                                        'pyname': u'water_quality_subcategory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'maximum capacity',
                                       {'name': u'Maximum Capacity',
                                        'pyname': u'maximum_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'initial volume',
                                       {'name': u'Initial Volume',
                                        'pyname': u'initial_volume',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'design in flow rate',
                                       {'name': u'Design In Flow Rate',
                                        'pyname': u'design_in_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'design out flow rate',
                                       {'name': u'Design Out Flow Rate',
                                        'pyname': u'design_out_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'overflow destination',
                                       {'name': u'Overflow Destination',
                                        'pyname': u'overflow_destination',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'type of supply controlled by float valve',
                                       {'name': u'Type of Supply Controlled by Float Valve',
                                        'pyname': u'type_of_supply_controlled_by_float_valve',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Mains',
                                                            u'GroundwaterWell',
                                                            u'OtherTank'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'float valve on capacity',
                                       {'name': u'Float Valve On Capacity',
                                        'pyname': u'float_valve_on_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'float valve off capacity',
                                       {'name': u'Float Valve Off Capacity',
                                        'pyname': u'float_valve_off_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'backup mains capacity',
                                       {'name': u'Backup Mains Capacity',
                                        'pyname': u'backup_mains_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'other tank name',
                                       {'name': u'Other Tank Name',
                                        'pyname': u'other_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'water thermal mode',
                                       {'name': u'Water Thermal Mode',
                                        'pyname': u'water_thermal_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ScheduledTemperature',
                                                            u'ThermalModel'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water temperature schedule name',
                                       {'name': u'Water Temperature Schedule Name',
                                        'pyname': u'water_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature indicator',
                                       {'name': u'Ambient Temperature Indicator',
                                        'pyname': u'ambient_temperature_indicator',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ambient temperature schedule name',
                                       {'name': u'Ambient Temperature Schedule Name',
                                        'pyname': u'ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank surface area',
                                       {'name': u'Tank Surface Area',
                                        'pyname': u'tank_surface_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'tank u value',
                                       {'name': u'Tank U Value',
                                        'pyname': u'tank_u_value',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'tank outside surface material name',
                                       {'name': u'Tank Outside Surface Material Name',
                                        'pyname': u'tank_outside_surface_material_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Water Systems',
               'min-fields': 0,
               'name': u'WaterUse:Storage',
               'pyname': u'WaterUseStorage',
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
    def water_quality_subcategory(self):
        """field `Water Quality Subcategory`

        Args:
            value (str): value for IDD Field `Water Quality Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_quality_subcategory` or None if not set

        """
        return self["Water Quality Subcategory"]

    @water_quality_subcategory.setter
    def water_quality_subcategory(self, value=None):
        """Corresponds to IDD field `Water Quality Subcategory`"""
        self["Water Quality Subcategory"] = value

    @property
    def maximum_capacity(self):
        """field `Maximum Capacity`

        |  Defaults to unlimited capacity.
        |  Units: m3

        Args:
            value (float): value for IDD Field `Maximum Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_capacity` or None if not set

        """
        return self["Maximum Capacity"]

    @maximum_capacity.setter
    def maximum_capacity(self, value=None):
        """Corresponds to IDD field `Maximum Capacity`"""
        self["Maximum Capacity"] = value

    @property
    def initial_volume(self):
        """field `Initial Volume`

        |  Units: m3

        Args:
            value (float): value for IDD Field `Initial Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_volume` or None if not set

        """
        return self["Initial Volume"]

    @initial_volume.setter
    def initial_volume(self, value=None):
        """Corresponds to IDD field `Initial Volume`"""
        self["Initial Volume"] = value

    @property
    def design_in_flow_rate(self):
        """field `Design In Flow Rate`

        |  Defaults to unlimited flow.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design In Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_in_flow_rate` or None if not set

        """
        return self["Design In Flow Rate"]

    @design_in_flow_rate.setter
    def design_in_flow_rate(self, value=None):
        """Corresponds to IDD field `Design In Flow Rate`"""
        self["Design In Flow Rate"] = value

    @property
    def design_out_flow_rate(self):
        """field `Design Out Flow Rate`

        |  Defaults to unlimited flow.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Out Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_out_flow_rate` or None if not set

        """
        return self["Design Out Flow Rate"]

    @design_out_flow_rate.setter
    def design_out_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Out Flow Rate`"""
        self["Design Out Flow Rate"] = value

    @property
    def overflow_destination(self):
        """field `Overflow Destination`

        |  If blank, overflow is discarded

        Args:
            value (str): value for IDD Field `Overflow Destination`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `overflow_destination` or None if not set

        """
        return self["Overflow Destination"]

    @overflow_destination.setter
    def overflow_destination(self, value=None):
        """Corresponds to IDD field `Overflow Destination`"""
        self["Overflow Destination"] = value

    @property
    def type_of_supply_controlled_by_float_valve(self):
        """field `Type of Supply Controlled by Float Valve`

        Args:
            value (str): value for IDD Field `Type of Supply Controlled by Float Valve`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `type_of_supply_controlled_by_float_valve` or None if not set

        """
        return self["Type of Supply Controlled by Float Valve"]

    @type_of_supply_controlled_by_float_valve.setter
    def type_of_supply_controlled_by_float_valve(self, value=None):
        """Corresponds to IDD field `Type of Supply Controlled by Float
        Valve`"""
        self["Type of Supply Controlled by Float Valve"] = value

    @property
    def float_valve_on_capacity(self):
        """field `Float Valve On Capacity`

        |  Lower range of target storage level e.g. float valve kicks on
        |  Units: m3

        Args:
            value (float): value for IDD Field `Float Valve On Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `float_valve_on_capacity` or None if not set

        """
        return self["Float Valve On Capacity"]

    @float_valve_on_capacity.setter
    def float_valve_on_capacity(self, value=None):
        """Corresponds to IDD field `Float Valve On Capacity`"""
        self["Float Valve On Capacity"] = value

    @property
    def float_valve_off_capacity(self):
        """field `Float Valve Off Capacity`

        |  Upper range of target storage level e.g. float valve kicks off
        |  Units: m3

        Args:
            value (float): value for IDD Field `Float Valve Off Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `float_valve_off_capacity` or None if not set

        """
        return self["Float Valve Off Capacity"]

    @float_valve_off_capacity.setter
    def float_valve_off_capacity(self, value=None):
        """Corresponds to IDD field `Float Valve Off Capacity`"""
        self["Float Valve Off Capacity"] = value

    @property
    def backup_mains_capacity(self):
        """field `Backup Mains Capacity`

        |  Lower range of secondary target storage level
        |  used to keep tanks at a minimum level using
        |  mains water if well can't keep up
        |  Units: m3

        Args:
            value (float): value for IDD Field `Backup Mains Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `backup_mains_capacity` or None if not set

        """
        return self["Backup Mains Capacity"]

    @backup_mains_capacity.setter
    def backup_mains_capacity(self, value=None):
        """Corresponds to IDD field `Backup Mains Capacity`"""
        self["Backup Mains Capacity"] = value

    @property
    def other_tank_name(self):
        """field `Other Tank Name`

        Args:
            value (str): value for IDD Field `Other Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `other_tank_name` or None if not set

        """
        return self["Other Tank Name"]

    @other_tank_name.setter
    def other_tank_name(self, value=None):
        """Corresponds to IDD field `Other Tank Name`"""
        self["Other Tank Name"] = value

    @property
    def water_thermal_mode(self):
        """field `Water Thermal Mode`

        Args:
            value (str): value for IDD Field `Water Thermal Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_thermal_mode` or None if not set

        """
        return self["Water Thermal Mode"]

    @water_thermal_mode.setter
    def water_thermal_mode(self, value=None):
        """Corresponds to IDD field `Water Thermal Mode`"""
        self["Water Thermal Mode"] = value

    @property
    def water_temperature_schedule_name(self):
        """field `Water Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Water Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_temperature_schedule_name` or None if not set

        """
        return self["Water Temperature Schedule Name"]

    @water_temperature_schedule_name.setter
    def water_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Water Temperature Schedule Name`"""
        self["Water Temperature Schedule Name"] = value

    @property
    def ambient_temperature_indicator(self):
        """field `Ambient Temperature Indicator`

        Args:
            value (str): value for IDD Field `Ambient Temperature Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set

        """
        return self["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Indicator`"""
        self["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set

        """
        return self["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Schedule Name`"""
        self["Ambient Temperature Schedule Name"] = value

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

    @property
    def tank_surface_area(self):
        """field `Tank Surface Area`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Tank Surface Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_surface_area` or None if not set

        """
        return self["Tank Surface Area"]

    @tank_surface_area.setter
    def tank_surface_area(self, value=None):
        """Corresponds to IDD field `Tank Surface Area`"""
        self["Tank Surface Area"] = value

    @property
    def tank_u_value(self):
        """field `Tank U Value`

        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Tank U Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_u_value` or None if not set

        """
        return self["Tank U Value"]

    @tank_u_value.setter
    def tank_u_value(self, value=None):
        """Corresponds to IDD field `Tank U Value`"""
        self["Tank U Value"] = value

    @property
    def tank_outside_surface_material_name(self):
        """field `Tank Outside Surface Material Name`

        Args:
            value (str): value for IDD Field `Tank Outside Surface Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_outside_surface_material_name` or None if not set

        """
        return self["Tank Outside Surface Material Name"]

    @tank_outside_surface_material_name.setter
    def tank_outside_surface_material_name(self, value=None):
        """Corresponds to IDD field `Tank Outside Surface Material Name`"""
        self["Tank Outside Surface Material Name"] = value




class WaterUseWell(DataObject):

    """ Corresponds to IDD object `WaterUse:Well`
        Simulates on-site water supply from a well. Well water is pumped out of the ground
        into a WaterUse:Storage. The operation of the ground water well is controlled by the
        associated WaterUse:Storage which is assumed to be operated as a vented cistern with
        no pressure tank.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'storage tank name',
                                       {'name': u'Storage Tank Name',
                                        'pyname': u'storage_tank_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pump depth',
                                       {'name': u'Pump Depth',
                                        'pyname': u'pump_depth',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'pump rated flow rate',
                                       {'name': u'Pump Rated Flow Rate',
                                        'pyname': u'pump_rated_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'pump rated head',
                                       {'name': u'Pump Rated Head',
                                        'pyname': u'pump_rated_head',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'pump rated power consumption',
                                       {'name': u'Pump Rated Power Consumption',
                                        'pyname': u'pump_rated_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'pump efficiency',
                                       {'name': u'Pump Efficiency',
                                        'pyname': u'pump_efficiency',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'well recovery rate',
                                       {'name': u'Well Recovery Rate',
                                        'pyname': u'well_recovery_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'nominal well storage volume',
                                       {'name': u'Nominal Well Storage Volume',
                                        'pyname': u'nominal_well_storage_volume',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'water table depth mode',
                                       {'name': u'Water Table Depth Mode',
                                        'pyname': u'water_table_depth_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water table depth',
                                       {'name': u'Water Table Depth',
                                        'pyname': u'water_table_depth',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'water table depth schedule name',
                                       {'name': u'Water Table Depth Schedule Name',
                                        'pyname': u'water_table_depth_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Water Systems',
               'min-fields': 0,
               'name': u'WaterUse:Well',
               'pyname': u'WaterUseWell',
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
    def storage_tank_name(self):
        """field `Storage Tank Name`

        Args:
            value (str): value for IDD Field `Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `storage_tank_name` or None if not set

        """
        return self["Storage Tank Name"]

    @storage_tank_name.setter
    def storage_tank_name(self, value=None):
        """Corresponds to IDD field `Storage Tank Name`"""
        self["Storage Tank Name"] = value

    @property
    def pump_depth(self):
        """field `Pump Depth`

        |  Units: m

        Args:
            value (float): value for IDD Field `Pump Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pump_depth` or None if not set

        """
        return self["Pump Depth"]

    @pump_depth.setter
    def pump_depth(self, value=None):
        """Corresponds to IDD field `Pump Depth`"""
        self["Pump Depth"] = value

    @property
    def pump_rated_flow_rate(self):
        """field `Pump Rated Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Pump Rated Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pump_rated_flow_rate` or None if not set

        """
        return self["Pump Rated Flow Rate"]

    @pump_rated_flow_rate.setter
    def pump_rated_flow_rate(self, value=None):
        """Corresponds to IDD field `Pump Rated Flow Rate`"""
        self["Pump Rated Flow Rate"] = value

    @property
    def pump_rated_head(self):
        """field `Pump Rated Head`

        |  Units: Pa

        Args:
            value (float): value for IDD Field `Pump Rated Head`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pump_rated_head` or None if not set

        """
        return self["Pump Rated Head"]

    @pump_rated_head.setter
    def pump_rated_head(self, value=None):
        """Corresponds to IDD field `Pump Rated Head`"""
        self["Pump Rated Head"] = value

    @property
    def pump_rated_power_consumption(self):
        """field `Pump Rated Power Consumption`

        |  Units: W

        Args:
            value (float): value for IDD Field `Pump Rated Power Consumption`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pump_rated_power_consumption` or None if not set

        """
        return self["Pump Rated Power Consumption"]

    @pump_rated_power_consumption.setter
    def pump_rated_power_consumption(self, value=None):
        """Corresponds to IDD field `Pump Rated Power Consumption`"""
        self["Pump Rated Power Consumption"] = value

    @property
    def pump_efficiency(self):
        """field `Pump Efficiency`

        Args:
            value (float): value for IDD Field `Pump Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pump_efficiency` or None if not set

        """
        return self["Pump Efficiency"]

    @pump_efficiency.setter
    def pump_efficiency(self, value=None):
        """Corresponds to IDD field `Pump Efficiency`"""
        self["Pump Efficiency"] = value

    @property
    def well_recovery_rate(self):
        """field `Well Recovery Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Well Recovery Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `well_recovery_rate` or None if not set

        """
        return self["Well Recovery Rate"]

    @well_recovery_rate.setter
    def well_recovery_rate(self, value=None):
        """Corresponds to IDD field `Well Recovery Rate`"""
        self["Well Recovery Rate"] = value

    @property
    def nominal_well_storage_volume(self):
        """field `Nominal Well Storage Volume`

        |  Units: m3

        Args:
            value (float): value for IDD Field `Nominal Well Storage Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_well_storage_volume` or None if not set

        """
        return self["Nominal Well Storage Volume"]

    @nominal_well_storage_volume.setter
    def nominal_well_storage_volume(self, value=None):
        """Corresponds to IDD field `Nominal Well Storage Volume`"""
        self["Nominal Well Storage Volume"] = value

    @property
    def water_table_depth_mode(self):
        """field `Water Table Depth Mode`

        Args:
            value (str): value for IDD Field `Water Table Depth Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_table_depth_mode` or None if not set

        """
        return self["Water Table Depth Mode"]

    @water_table_depth_mode.setter
    def water_table_depth_mode(self, value=None):
        """Corresponds to IDD field `Water Table Depth Mode`"""
        self["Water Table Depth Mode"] = value

    @property
    def water_table_depth(self):
        """field `Water Table Depth`

        |  Units: m

        Args:
            value (float): value for IDD Field `Water Table Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_table_depth` or None if not set

        """
        return self["Water Table Depth"]

    @water_table_depth.setter
    def water_table_depth(self, value=None):
        """Corresponds to IDD field `Water Table Depth`"""
        self["Water Table Depth"] = value

    @property
    def water_table_depth_schedule_name(self):
        """field `Water Table Depth Schedule Name`

        Args:
            value (str): value for IDD Field `Water Table Depth Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_table_depth_schedule_name` or None if not set

        """
        return self["Water Table Depth Schedule Name"]

    @water_table_depth_schedule_name.setter
    def water_table_depth_schedule_name(self, value=None):
        """Corresponds to IDD field `Water Table Depth Schedule Name`"""
        self["Water Table Depth Schedule Name"] = value




class WaterUseRainCollector(DataObject):

    """ Corresponds to IDD object `WaterUse:RainCollector`
        Used for harvesting rainwater falling on building surfaces. The rainwater is sent to a
        WaterUse:Storage object. In order to use this object it is necessary to also include
        a Site:Precipitation object to describe the rates of rainfall.
    """
    _schema = {'extensible-fields': OrderedDict([(u'collection surface 1 name',
                                                  {'name': u'Collection Surface 1 Name',
                                                   'pyname': u'collection_surface_1_name',
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
                                      (u'storage tank name',
                                       {'name': u'Storage Tank Name',
                                        'pyname': u'storage_tank_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loss factor mode',
                                       {'name': u'Loss Factor Mode',
                                        'pyname': u'loss_factor_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'collection loss factor',
                                       {'name': u'Collection Loss Factor',
                                        'pyname': u'collection_loss_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'collection loss factor schedule name',
                                       {'name': u'Collection Loss Factor Schedule Name',
                                        'pyname': u'collection_loss_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum collection rate',
                                       {'name': u'Maximum Collection Rate',
                                        'pyname': u'maximum_collection_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Water Systems',
               'min-fields': 0,
               'name': u'WaterUse:RainCollector',
               'pyname': u'WaterUseRainCollector',
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
    def storage_tank_name(self):
        """field `Storage Tank Name`

        Args:
            value (str): value for IDD Field `Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `storage_tank_name` or None if not set

        """
        return self["Storage Tank Name"]

    @storage_tank_name.setter
    def storage_tank_name(self, value=None):
        """Corresponds to IDD field `Storage Tank Name`"""
        self["Storage Tank Name"] = value

    @property
    def loss_factor_mode(self):
        """field `Loss Factor Mode`

        Args:
            value (str): value for IDD Field `Loss Factor Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loss_factor_mode` or None if not set

        """
        return self["Loss Factor Mode"]

    @loss_factor_mode.setter
    def loss_factor_mode(self, value=None):
        """Corresponds to IDD field `Loss Factor Mode`"""
        self["Loss Factor Mode"] = value

    @property
    def collection_loss_factor(self):
        """field `Collection Loss Factor`

        |  this is the portion of rain
        |  that is lost in the process of collecting it
        |  the rain collected is one minus this factor

        Args:
            value (float): value for IDD Field `Collection Loss Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `collection_loss_factor` or None if not set

        """
        return self["Collection Loss Factor"]

    @collection_loss_factor.setter
    def collection_loss_factor(self, value=None):
        """Corresponds to IDD field `Collection Loss Factor`"""
        self["Collection Loss Factor"] = value

    @property
    def collection_loss_factor_schedule_name(self):
        """field `Collection Loss Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Collection Loss Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `collection_loss_factor_schedule_name` or None if not set

        """
        return self["Collection Loss Factor Schedule Name"]

    @collection_loss_factor_schedule_name.setter
    def collection_loss_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Collection Loss Factor Schedule Name`"""
        self["Collection Loss Factor Schedule Name"] = value

    @property
    def maximum_collection_rate(self):
        """field `Maximum Collection Rate`

        |  Defaults to unlimited flow.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Maximum Collection Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_collection_rate` or None if not set

        """
        return self["Maximum Collection Rate"]

    @maximum_collection_rate.setter
    def maximum_collection_rate(self, value=None):
        """Corresponds to IDD field `Maximum Collection Rate`"""
        self["Maximum Collection Rate"] = value

    def add_extensible(self,
                       collection_surface_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            collection_surface_1_name (str): value for IDD Field `Collection Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        collection_surface_1_name = self.check_value(
            "Collection Surface 1 Name",
            collection_surface_1_name)
        vals.append(collection_surface_1_name)
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


