import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.user_defined_hvac_and_plant_component_models import PlantEquipmentOperationUserDefined

log = logging.getLogger(__name__)

class TestPlantEquipmentOperationUserDefined(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationuserdefined(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationUserDefined()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_main_model_program_calling_manager_name = "object-list|Main Model Program Calling Manager Name"
        obj.main_model_program_calling_manager_name = var_main_model_program_calling_manager_name
        # object-list
        var_initialization_program_calling_manager_name = "object-list|Initialization Program Calling Manager Name"
        obj.initialization_program_calling_manager_name = var_initialization_program_calling_manager_name
        # alpha
        var_equipment_1_object_type = "Equipment 1 Object Type"
        obj.equipment_1_object_type = var_equipment_1_object_type
        # alpha
        var_equipment_1_name = "Equipment 1 Name"
        obj.equipment_1_name = var_equipment_1_name
        # alpha
        var_equipment_2_object_type = "Equipment 2 Object Type"
        obj.equipment_2_object_type = var_equipment_2_object_type
        # alpha
        var_equipment_2_name = "Equipment 2 Name"
        obj.equipment_2_name = var_equipment_2_name
        # alpha
        var_equipment_3_object_type = "Equipment 3 Object Type"
        obj.equipment_3_object_type = var_equipment_3_object_type
        # alpha
        var_equipment_3_name = "Equipment 3 Name"
        obj.equipment_3_name = var_equipment_3_name
        # alpha
        var_equipment_4_object_type = "Equipment 4 Object Type"
        obj.equipment_4_object_type = var_equipment_4_object_type
        # alpha
        var_equipment_4_name = "Equipment 4 Name"
        obj.equipment_4_name = var_equipment_4_name
        # alpha
        var_equipment_5_object_type = "Equipment 5 Object Type"
        obj.equipment_5_object_type = var_equipment_5_object_type
        # alpha
        var_equipment_5_name = "Equipment 5 Name"
        obj.equipment_5_name = var_equipment_5_name
        # alpha
        var_equipment_6_object_type = "Equipment 6 Object Type"
        obj.equipment_6_object_type = var_equipment_6_object_type
        # alpha
        var_equipment_6_name = "Equipment 6 Name"
        obj.equipment_6_name = var_equipment_6_name
        # alpha
        var_equipment_7_object_type = "Equipment 7 Object Type"
        obj.equipment_7_object_type = var_equipment_7_object_type
        # alpha
        var_equipment_7_name = "Equipment 7 Name"
        obj.equipment_7_name = var_equipment_7_name
        # alpha
        var_equipment_8_object_type = "Equipment 8 Object Type"
        obj.equipment_8_object_type = var_equipment_8_object_type
        # alpha
        var_equipment_8_name = "Equipment 8 Name"
        obj.equipment_8_name = var_equipment_8_name
        # alpha
        var_equipment_9_object_type = "Equipment 9 Object Type"
        obj.equipment_9_object_type = var_equipment_9_object_type
        # alpha
        var_equipment_9_name = "Equipment 9 Name"
        obj.equipment_9_name = var_equipment_9_name
        # alpha
        var_equipment_10_object_type = "Equipment 10 Object Type"
        obj.equipment_10_object_type = var_equipment_10_object_type
        # alpha
        var_equipment_10_name = "Equipment 10 Name"
        obj.equipment_10_name = var_equipment_10_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].name, var_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].main_model_program_calling_manager_name, var_main_model_program_calling_manager_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].initialization_program_calling_manager_name, var_initialization_program_calling_manager_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_1_object_type, var_equipment_1_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_1_name, var_equipment_1_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_2_object_type, var_equipment_2_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_2_name, var_equipment_2_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_3_object_type, var_equipment_3_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_3_name, var_equipment_3_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_4_object_type, var_equipment_4_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_4_name, var_equipment_4_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_5_object_type, var_equipment_5_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_5_name, var_equipment_5_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_6_object_type, var_equipment_6_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_6_name, var_equipment_6_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_7_object_type, var_equipment_7_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_7_name, var_equipment_7_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_8_object_type, var_equipment_8_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_8_name, var_equipment_8_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_9_object_type, var_equipment_9_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_9_name, var_equipment_9_name)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_10_object_type, var_equipment_10_object_type)
        self.assertEqual(idf2.plantequipmentoperationuserdefineds[0].equipment_10_name, var_equipment_10_name)