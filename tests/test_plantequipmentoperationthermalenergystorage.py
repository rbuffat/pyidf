import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant import PlantEquipmentOperationThermalEnergyStorage

log = logging.getLogger(__name__)

class TestPlantEquipmentOperationThermalEnergyStorage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationthermalenergystorage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationThermalEnergyStorage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_onpeak_schedule = "object-list|On-Peak Schedule"
        obj.onpeak_schedule = var_onpeak_schedule
        # object-list
        var_charging_availability_schedule = "object-list|Charging Availability Schedule"
        obj.charging_availability_schedule = var_charging_availability_schedule
        # real
        var_noncharging_chilled_water_temperature = 4.4
        obj.noncharging_chilled_water_temperature = var_noncharging_chilled_water_temperature
        # real
        var_charging_chilled_water_temperature = 5.5
        obj.charging_chilled_water_temperature = var_charging_chilled_water_temperature
        # alpha
        var_component_1_object_type = "ThermalStorage:Ice:Simple"
        obj.component_1_object_type = var_component_1_object_type
        # object-list
        var_component_1_name = "object-list|Component 1 Name"
        obj.component_1_name = var_component_1_name
        # node
        var_component_1_demand_calculation_node_name = "node|Component 1 Demand Calculation Node Name"
        obj.component_1_demand_calculation_node_name = var_component_1_demand_calculation_node_name
        # node
        var_component_1_setpoint_node_name = "node|Component 1 Setpoint Node Name"
        obj.component_1_setpoint_node_name = var_component_1_setpoint_node_name
        # real
        var_component_1_flow_rate = 10.1
        obj.component_1_flow_rate = var_component_1_flow_rate
        # alpha
        var_component_1_operation_type = "Heating"
        obj.component_1_operation_type = var_component_1_operation_type
        # alpha
        var_component_2_object_type = "ThermalStorage:Ice:Simple"
        obj.component_2_object_type = var_component_2_object_type
        # object-list
        var_component_2_name = "object-list|Component 2 Name"
        obj.component_2_name = var_component_2_name
        # node
        var_component_2_demand_calculation_node_name = "node|Component 2 Demand Calculation Node Name"
        obj.component_2_demand_calculation_node_name = var_component_2_demand_calculation_node_name
        # node
        var_component_2_setpoint_node_name = "node|Component 2 Setpoint Node Name"
        obj.component_2_setpoint_node_name = var_component_2_setpoint_node_name
        # real
        var_component_2_flow_rate = 16.16
        obj.component_2_flow_rate = var_component_2_flow_rate
        # alpha
        var_component_2_operation_type = "Heating"
        obj.component_2_operation_type = var_component_2_operation_type
        # alpha
        var_component_3_object_type = "ThermalStorage:Ice:Simple"
        obj.component_3_object_type = var_component_3_object_type
        # object-list
        var_component_3_name = "object-list|Component 3 Name"
        obj.component_3_name = var_component_3_name
        # node
        var_component_3_demand_calculation_node_name = "node|Component 3 Demand Calculation Node Name"
        obj.component_3_demand_calculation_node_name = var_component_3_demand_calculation_node_name
        # node
        var_component_3_setpoint_node_name = "node|Component 3 Setpoint Node Name"
        obj.component_3_setpoint_node_name = var_component_3_setpoint_node_name
        # real
        var_component_3_flow_rate = 22.22
        obj.component_3_flow_rate = var_component_3_flow_rate
        # alpha
        var_component_3_operation_type = "Heating"
        obj.component_3_operation_type = var_component_3_operation_type
        # alpha
        var_component_4_object_type = "ThermalStorage:Ice:Simple"
        obj.component_4_object_type = var_component_4_object_type
        # object-list
        var_component_4_name = "object-list|Component 4 Name"
        obj.component_4_name = var_component_4_name
        # node
        var_component_4_demand_calculation_node_name = "node|Component 4 Demand Calculation Node Name"
        obj.component_4_demand_calculation_node_name = var_component_4_demand_calculation_node_name
        # node
        var_component_4_setpoint_node_name = "node|Component 4 Setpoint Node Name"
        obj.component_4_setpoint_node_name = var_component_4_setpoint_node_name
        # real
        var_component_4_flow_rate = 28.28
        obj.component_4_flow_rate = var_component_4_flow_rate
        # alpha
        var_component_4_operation_type = "Heating"
        obj.component_4_operation_type = var_component_4_operation_type
        # alpha
        var_component_5_object_type = "ThermalStorage:Ice:Simple"
        obj.component_5_object_type = var_component_5_object_type
        # object-list
        var_component_5_name = "object-list|Component 5 Name"
        obj.component_5_name = var_component_5_name
        # node
        var_component_5_demand_calculation_node_name = "node|Component 5 Demand Calculation Node Name"
        obj.component_5_demand_calculation_node_name = var_component_5_demand_calculation_node_name
        # node
        var_component_5_setpoint_node_name = "node|Component 5 Setpoint Node Name"
        obj.component_5_setpoint_node_name = var_component_5_setpoint_node_name
        # real
        var_component_5_flow_rate = 34.34
        obj.component_5_flow_rate = var_component_5_flow_rate
        # alpha
        var_component_5_operation_type = "Heating"
        obj.component_5_operation_type = var_component_5_operation_type
        # alpha
        var_component_6_object_type = "ThermalStorage:Ice:Simple"
        obj.component_6_object_type = var_component_6_object_type
        # object-list
        var_component_6_name = "object-list|Component 6 Name"
        obj.component_6_name = var_component_6_name
        # node
        var_component_6_demand_calculation_node_name = "node|Component 6 Demand Calculation Node Name"
        obj.component_6_demand_calculation_node_name = var_component_6_demand_calculation_node_name
        # node
        var_component_6_setpoint_node_name = "node|Component 6 Setpoint Node Name"
        obj.component_6_setpoint_node_name = var_component_6_setpoint_node_name
        # real
        var_component_6_flow_rate = 40.4
        obj.component_6_flow_rate = var_component_6_flow_rate
        # alpha
        var_component_6_operation_type = "Heating"
        obj.component_6_operation_type = var_component_6_operation_type
        # alpha
        var_component_7_object_type = "ThermalStorage:Ice:Simple"
        obj.component_7_object_type = var_component_7_object_type
        # object-list
        var_component_7_name = "object-list|Component 7 Name"
        obj.component_7_name = var_component_7_name
        # node
        var_component_7_demand_calculation_node_name = "node|Component 7 Demand Calculation Node Name"
        obj.component_7_demand_calculation_node_name = var_component_7_demand_calculation_node_name
        # node
        var_component_7_setpoint_node_name = "node|Component 7 Setpoint Node Name"
        obj.component_7_setpoint_node_name = var_component_7_setpoint_node_name
        # real
        var_component_7_flow_rate = 46.46
        obj.component_7_flow_rate = var_component_7_flow_rate
        # alpha
        var_component_7_operation_type = "Heating"
        obj.component_7_operation_type = var_component_7_operation_type
        # alpha
        var_component_8_object_type = "ThermalStorage:Ice:Simple"
        obj.component_8_object_type = var_component_8_object_type
        # object-list
        var_component_8_name = "object-list|Component 8 Name"
        obj.component_8_name = var_component_8_name
        # node
        var_component_8_demand_calculation_node_name = "node|Component 8 Demand Calculation Node Name"
        obj.component_8_demand_calculation_node_name = var_component_8_demand_calculation_node_name
        # node
        var_component_8_setpoint_node_name = "node|Component 8 Setpoint Node Name"
        obj.component_8_setpoint_node_name = var_component_8_setpoint_node_name
        # real
        var_component_8_flow_rate = 52.52
        obj.component_8_flow_rate = var_component_8_flow_rate
        # alpha
        var_component_8_operation_type = "Heating"
        obj.component_8_operation_type = var_component_8_operation_type
        # alpha
        var_component_9_object_type = "ThermalStorage:Ice:Simple"
        obj.component_9_object_type = var_component_9_object_type
        # object-list
        var_component_9_name = "object-list|Component 9 Name"
        obj.component_9_name = var_component_9_name
        # node
        var_component_9_demand_calculation_node_name = "node|Component 9 Demand Calculation Node Name"
        obj.component_9_demand_calculation_node_name = var_component_9_demand_calculation_node_name
        # node
        var_component_9_setpoint_node_name = "node|Component 9 Setpoint Node Name"
        obj.component_9_setpoint_node_name = var_component_9_setpoint_node_name
        # real
        var_component_9_flow_rate = 58.58
        obj.component_9_flow_rate = var_component_9_flow_rate
        # alpha
        var_component_9_operation_type = "Heating"
        obj.component_9_operation_type = var_component_9_operation_type
        # alpha
        var_component_10_object_type = "ThermalStorage:Ice:Simple"
        obj.component_10_object_type = var_component_10_object_type
        # object-list
        var_component_10_name = "object-list|Component 10 Name"
        obj.component_10_name = var_component_10_name
        # node
        var_component_10_demand_calculation_node_name = "node|Component 10 Demand Calculation Node Name"
        obj.component_10_demand_calculation_node_name = var_component_10_demand_calculation_node_name
        # node
        var_component_10_setpoint_node_name = "node|Component 10 Setpoint Node Name"
        obj.component_10_setpoint_node_name = var_component_10_setpoint_node_name
        # real
        var_component_10_flow_rate = 64.64
        obj.component_10_flow_rate = var_component_10_flow_rate
        # alpha
        var_component_10_operation_type = "Heating"
        obj.component_10_operation_type = var_component_10_operation_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].name, var_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].onpeak_schedule, var_onpeak_schedule)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].charging_availability_schedule, var_charging_availability_schedule)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].noncharging_chilled_water_temperature, var_noncharging_chilled_water_temperature)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].charging_chilled_water_temperature, var_charging_chilled_water_temperature)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_1_object_type, var_component_1_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_1_name, var_component_1_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_1_demand_calculation_node_name, var_component_1_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_1_setpoint_node_name, var_component_1_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_1_flow_rate, var_component_1_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_1_operation_type, var_component_1_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_2_object_type, var_component_2_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_2_name, var_component_2_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_2_demand_calculation_node_name, var_component_2_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_2_setpoint_node_name, var_component_2_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_2_flow_rate, var_component_2_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_2_operation_type, var_component_2_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_3_object_type, var_component_3_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_3_name, var_component_3_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_3_demand_calculation_node_name, var_component_3_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_3_setpoint_node_name, var_component_3_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_3_flow_rate, var_component_3_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_3_operation_type, var_component_3_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_4_object_type, var_component_4_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_4_name, var_component_4_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_4_demand_calculation_node_name, var_component_4_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_4_setpoint_node_name, var_component_4_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_4_flow_rate, var_component_4_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_4_operation_type, var_component_4_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_5_object_type, var_component_5_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_5_name, var_component_5_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_5_demand_calculation_node_name, var_component_5_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_5_setpoint_node_name, var_component_5_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_5_flow_rate, var_component_5_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_5_operation_type, var_component_5_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_6_object_type, var_component_6_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_6_name, var_component_6_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_6_demand_calculation_node_name, var_component_6_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_6_setpoint_node_name, var_component_6_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_6_flow_rate, var_component_6_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_6_operation_type, var_component_6_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_7_object_type, var_component_7_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_7_name, var_component_7_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_7_demand_calculation_node_name, var_component_7_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_7_setpoint_node_name, var_component_7_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_7_flow_rate, var_component_7_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_7_operation_type, var_component_7_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_8_object_type, var_component_8_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_8_name, var_component_8_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_8_demand_calculation_node_name, var_component_8_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_8_setpoint_node_name, var_component_8_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_8_flow_rate, var_component_8_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_8_operation_type, var_component_8_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_9_object_type, var_component_9_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_9_name, var_component_9_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_9_demand_calculation_node_name, var_component_9_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_9_setpoint_node_name, var_component_9_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_9_flow_rate, var_component_9_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_9_operation_type, var_component_9_operation_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_10_object_type, var_component_10_object_type)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_10_name, var_component_10_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_10_demand_calculation_node_name, var_component_10_demand_calculation_node_name)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_10_setpoint_node_name, var_component_10_setpoint_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_10_flow_rate, var_component_10_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationthermalenergystorages[0].component_10_operation_type, var_component_10_operation_type)