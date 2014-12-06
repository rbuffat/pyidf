import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant import PlantEquipmentOperationComponentSetpoint

log = logging.getLogger(__name__)

class TestPlantEquipmentOperationComponentSetpoint(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationcomponentsetpoint(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationComponentSetpoint()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_equipment_1_object_type = "Equipment 1 Object Type"
        obj.equipment_1_object_type = var_equipment_1_object_type
        # alpha
        var_equipment_1_name = "Equipment 1 Name"
        obj.equipment_1_name = var_equipment_1_name
        # node
        var_demand_calculation_1_node_name = "node|Demand Calculation 1 Node Name"
        obj.demand_calculation_1_node_name = var_demand_calculation_1_node_name
        # node
        var_setpoint_1_node_name = "node|Setpoint 1 Node Name"
        obj.setpoint_1_node_name = var_setpoint_1_node_name
        # real
        var_component_1_flow_rate = 6.6
        obj.component_1_flow_rate = var_component_1_flow_rate
        # alpha
        var_operation_1_type = "Heating"
        obj.operation_1_type = var_operation_1_type
        # alpha
        var_equipment_2_object_type = "Equipment 2 Object Type"
        obj.equipment_2_object_type = var_equipment_2_object_type
        # alpha
        var_equipment_2_name = "Equipment 2 Name"
        obj.equipment_2_name = var_equipment_2_name
        # node
        var_demand_calculation_2_node_name = "node|Demand Calculation 2 Node Name"
        obj.demand_calculation_2_node_name = var_demand_calculation_2_node_name
        # node
        var_setpoint_2_node_name = "node|Setpoint 2 Node Name"
        obj.setpoint_2_node_name = var_setpoint_2_node_name
        # real
        var_component_2_flow_rate = 12.12
        obj.component_2_flow_rate = var_component_2_flow_rate
        # alpha
        var_operation_2_type = "Heating"
        obj.operation_2_type = var_operation_2_type
        # alpha
        var_equipment_3_object_type = "Equipment 3 Object Type"
        obj.equipment_3_object_type = var_equipment_3_object_type
        # alpha
        var_equipment_3_name = "Equipment 3 Name"
        obj.equipment_3_name = var_equipment_3_name
        # node
        var_demand_calculation_3_node_name = "node|Demand Calculation 3 Node Name"
        obj.demand_calculation_3_node_name = var_demand_calculation_3_node_name
        # node
        var_setpoint_3_node_name = "node|Setpoint 3 Node Name"
        obj.setpoint_3_node_name = var_setpoint_3_node_name
        # real
        var_component_3_flow_rate = 18.18
        obj.component_3_flow_rate = var_component_3_flow_rate
        # alpha
        var_operation_3_type = "Heating"
        obj.operation_3_type = var_operation_3_type
        # alpha
        var_equipment_4_object_type = "Equipment 4 Object Type"
        obj.equipment_4_object_type = var_equipment_4_object_type
        # alpha
        var_equipment_4_name = "Equipment 4 Name"
        obj.equipment_4_name = var_equipment_4_name
        # node
        var_demand_calculation_4_node_name = "node|Demand Calculation 4 Node Name"
        obj.demand_calculation_4_node_name = var_demand_calculation_4_node_name
        # node
        var_setpoint_4_node_name = "node|Setpoint 4 Node Name"
        obj.setpoint_4_node_name = var_setpoint_4_node_name
        # real
        var_component_4_flow_rate = 24.24
        obj.component_4_flow_rate = var_component_4_flow_rate
        # alpha
        var_operation_4_type = "Heating"
        obj.operation_4_type = var_operation_4_type
        # alpha
        var_equipment_5_object_type = "Equipment 5 Object Type"
        obj.equipment_5_object_type = var_equipment_5_object_type
        # alpha
        var_equipment_5_name = "Equipment 5 Name"
        obj.equipment_5_name = var_equipment_5_name
        # node
        var_demand_calculation_5_node_name = "node|Demand Calculation 5 Node Name"
        obj.demand_calculation_5_node_name = var_demand_calculation_5_node_name
        # node
        var_setpoint_5_node_name = "node|Setpoint 5 Node Name"
        obj.setpoint_5_node_name = var_setpoint_5_node_name
        # real
        var_component_5_flow_rate = 30.3
        obj.component_5_flow_rate = var_component_5_flow_rate
        # alpha
        var_operation_5_type = "Heating"
        obj.operation_5_type = var_operation_5_type
        # alpha
        var_equipment_6_object_type = "Equipment 6 Object Type"
        obj.equipment_6_object_type = var_equipment_6_object_type
        # alpha
        var_equipment_6_name = "Equipment 6 Name"
        obj.equipment_6_name = var_equipment_6_name
        # node
        var_demand_calculation_6_node_name = "node|Demand Calculation 6 Node Name"
        obj.demand_calculation_6_node_name = var_demand_calculation_6_node_name
        # node
        var_setpoint_6_node_name = "node|Setpoint 6 Node Name"
        obj.setpoint_6_node_name = var_setpoint_6_node_name
        # real
        var_component_6_flow_rate = 36.36
        obj.component_6_flow_rate = var_component_6_flow_rate
        # alpha
        var_operation_6_type = "Heating"
        obj.operation_6_type = var_operation_6_type
        # alpha
        var_equipment_7_object_type = "Equipment 7 Object Type"
        obj.equipment_7_object_type = var_equipment_7_object_type
        # alpha
        var_equipment_7_name = "Equipment 7 Name"
        obj.equipment_7_name = var_equipment_7_name
        # node
        var_demand_calculation_7_node_name = "node|Demand Calculation 7 Node Name"
        obj.demand_calculation_7_node_name = var_demand_calculation_7_node_name
        # node
        var_setpoint_7_node_name = "node|Setpoint 7 Node Name"
        obj.setpoint_7_node_name = var_setpoint_7_node_name
        # real
        var_component_7_flow_rate = 42.42
        obj.component_7_flow_rate = var_component_7_flow_rate
        # alpha
        var_operation_7_type = "Heating"
        obj.operation_7_type = var_operation_7_type
        # alpha
        var_equipment_8_object_type = "Equipment 8 Object Type"
        obj.equipment_8_object_type = var_equipment_8_object_type
        # alpha
        var_equipment_8_name = "Equipment 8 Name"
        obj.equipment_8_name = var_equipment_8_name
        # node
        var_demand_calculation_8_node_name = "node|Demand Calculation 8 Node Name"
        obj.demand_calculation_8_node_name = var_demand_calculation_8_node_name
        # node
        var_setpoint_8_node_name = "node|Setpoint 8 Node Name"
        obj.setpoint_8_node_name = var_setpoint_8_node_name
        # real
        var_component_8_flow_rate = 48.48
        obj.component_8_flow_rate = var_component_8_flow_rate
        # alpha
        var_operation_8_type = "Heating"
        obj.operation_8_type = var_operation_8_type
        # alpha
        var_equipment_9_object_type = "Equipment 9 Object Type"
        obj.equipment_9_object_type = var_equipment_9_object_type
        # alpha
        var_equipment_9_name = "Equipment 9 Name"
        obj.equipment_9_name = var_equipment_9_name
        # node
        var_demand_calculation_9_node_name = "node|Demand Calculation 9 Node Name"
        obj.demand_calculation_9_node_name = var_demand_calculation_9_node_name
        # node
        var_setpoint_9_node_name = "node|Setpoint 9 Node Name"
        obj.setpoint_9_node_name = var_setpoint_9_node_name
        # real
        var_component_9_flow_rate = 54.54
        obj.component_9_flow_rate = var_component_9_flow_rate
        # alpha
        var_operation_9_type = "Heating"
        obj.operation_9_type = var_operation_9_type
        # alpha
        var_equipment_10_object_type = "Equipment 10 Object Type"
        obj.equipment_10_object_type = var_equipment_10_object_type
        # alpha
        var_equipment_10_name = "Equipment 10 Name"
        obj.equipment_10_name = var_equipment_10_name
        # node
        var_demand_calculation_10_node_name = "node|Demand Calculation 10 Node Name"
        obj.demand_calculation_10_node_name = var_demand_calculation_10_node_name
        # node
        var_setpoint_10_node_name = "node|Setpoint 10 Node Name"
        obj.setpoint_10_node_name = var_setpoint_10_node_name
        # real
        var_component_10_flow_rate = 60.6
        obj.component_10_flow_rate = var_component_10_flow_rate
        # alpha
        var_operation_10_type = "Heating"
        obj.operation_10_type = var_operation_10_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].name, var_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_1_object_type, var_equipment_1_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_1_name, var_equipment_1_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_1_node_name, var_demand_calculation_1_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_1_node_name, var_setpoint_1_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_1_flow_rate, var_component_1_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_1_type, var_operation_1_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_2_object_type, var_equipment_2_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_2_name, var_equipment_2_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_2_node_name, var_demand_calculation_2_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_2_node_name, var_setpoint_2_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_2_flow_rate, var_component_2_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_2_type, var_operation_2_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_3_object_type, var_equipment_3_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_3_name, var_equipment_3_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_3_node_name, var_demand_calculation_3_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_3_node_name, var_setpoint_3_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_3_flow_rate, var_component_3_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_3_type, var_operation_3_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_4_object_type, var_equipment_4_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_4_name, var_equipment_4_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_4_node_name, var_demand_calculation_4_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_4_node_name, var_setpoint_4_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_4_flow_rate, var_component_4_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_4_type, var_operation_4_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_5_object_type, var_equipment_5_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_5_name, var_equipment_5_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_5_node_name, var_demand_calculation_5_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_5_node_name, var_setpoint_5_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_5_flow_rate, var_component_5_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_5_type, var_operation_5_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_6_object_type, var_equipment_6_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_6_name, var_equipment_6_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_6_node_name, var_demand_calculation_6_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_6_node_name, var_setpoint_6_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_6_flow_rate, var_component_6_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_6_type, var_operation_6_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_7_object_type, var_equipment_7_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_7_name, var_equipment_7_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_7_node_name, var_demand_calculation_7_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_7_node_name, var_setpoint_7_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_7_flow_rate, var_component_7_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_7_type, var_operation_7_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_8_object_type, var_equipment_8_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_8_name, var_equipment_8_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_8_node_name, var_demand_calculation_8_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_8_node_name, var_setpoint_8_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_8_flow_rate, var_component_8_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_8_type, var_operation_8_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_9_object_type, var_equipment_9_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_9_name, var_equipment_9_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_9_node_name, var_demand_calculation_9_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_9_node_name, var_setpoint_9_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_9_flow_rate, var_component_9_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_9_type, var_operation_9_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_10_object_type, var_equipment_10_object_type)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].equipment_10_name, var_equipment_10_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].demand_calculation_10_node_name, var_demand_calculation_10_node_name)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].setpoint_10_node_name, var_setpoint_10_node_name)
        self.assertAlmostEqual(idf2.plantequipmentoperationcomponentsetpoints[0].component_10_flow_rate, var_component_10_flow_rate)
        self.assertEqual(idf2.plantequipmentoperationcomponentsetpoints[0].operation_10_type, var_operation_10_type)