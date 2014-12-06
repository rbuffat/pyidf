import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant import PlantEquipmentOperationSchemes

log = logging.getLogger(__name__)

class TestPlantEquipmentOperationSchemes(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationschemes(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationSchemes()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_scheme_1_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_1_object_type = var_control_scheme_1_object_type
        # object-list
        var_control_scheme_1_name = "object-list|Control Scheme 1 Name"
        obj.control_scheme_1_name = var_control_scheme_1_name
        # object-list
        var_control_scheme_1_schedule_name = "object-list|Control Scheme 1 Schedule Name"
        obj.control_scheme_1_schedule_name = var_control_scheme_1_schedule_name
        # alpha
        var_control_scheme_2_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_2_object_type = var_control_scheme_2_object_type
        # object-list
        var_control_scheme_2_name = "object-list|Control Scheme 2 Name"
        obj.control_scheme_2_name = var_control_scheme_2_name
        # object-list
        var_control_scheme_2_schedule_name = "object-list|Control Scheme 2 Schedule Name"
        obj.control_scheme_2_schedule_name = var_control_scheme_2_schedule_name
        # alpha
        var_control_scheme_3_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_3_object_type = var_control_scheme_3_object_type
        # object-list
        var_control_scheme_3_name = "object-list|Control Scheme 3 Name"
        obj.control_scheme_3_name = var_control_scheme_3_name
        # object-list
        var_control_scheme_3_schedule_name = "object-list|Control Scheme 3 Schedule Name"
        obj.control_scheme_3_schedule_name = var_control_scheme_3_schedule_name
        # alpha
        var_control_scheme_4_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_4_object_type = var_control_scheme_4_object_type
        # object-list
        var_control_scheme_4_name = "object-list|Control Scheme 4 Name"
        obj.control_scheme_4_name = var_control_scheme_4_name
        # object-list
        var_control_scheme_4_schedule_name = "object-list|Control Scheme 4 Schedule Name"
        obj.control_scheme_4_schedule_name = var_control_scheme_4_schedule_name
        # alpha
        var_control_scheme_5_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_5_object_type = var_control_scheme_5_object_type
        # object-list
        var_control_scheme_5_name = "object-list|Control Scheme 5 Name"
        obj.control_scheme_5_name = var_control_scheme_5_name
        # object-list
        var_control_scheme_5_schedule_name = "object-list|Control Scheme 5 Schedule Name"
        obj.control_scheme_5_schedule_name = var_control_scheme_5_schedule_name
        # alpha
        var_control_scheme_6_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_6_object_type = var_control_scheme_6_object_type
        # object-list
        var_control_scheme_6_name = "object-list|Control Scheme 6 Name"
        obj.control_scheme_6_name = var_control_scheme_6_name
        # object-list
        var_control_scheme_6_schedule_name = "object-list|Control Scheme 6 Schedule Name"
        obj.control_scheme_6_schedule_name = var_control_scheme_6_schedule_name
        # alpha
        var_control_scheme_7_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_7_object_type = var_control_scheme_7_object_type
        # object-list
        var_control_scheme_7_name = "object-list|Control Scheme 7 Name"
        obj.control_scheme_7_name = var_control_scheme_7_name
        # object-list
        var_control_scheme_7_schedule_name = "object-list|Control Scheme 7 Schedule Name"
        obj.control_scheme_7_schedule_name = var_control_scheme_7_schedule_name
        # alpha
        var_control_scheme_8_object_type = "PlantEquipmentOperation:CoolingLoad"
        obj.control_scheme_8_object_type = var_control_scheme_8_object_type
        # object-list
        var_control_scheme_8_name = "object-list|Control Scheme 8 Name"
        obj.control_scheme_8_name = var_control_scheme_8_name
        # object-list
        var_control_scheme_8_schedule_name = "object-list|Control Scheme 8 Schedule Name"
        obj.control_scheme_8_schedule_name = var_control_scheme_8_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].name, var_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_1_object_type, var_control_scheme_1_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_1_name, var_control_scheme_1_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_1_schedule_name, var_control_scheme_1_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_2_object_type, var_control_scheme_2_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_2_name, var_control_scheme_2_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_2_schedule_name, var_control_scheme_2_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_3_object_type, var_control_scheme_3_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_3_name, var_control_scheme_3_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_3_schedule_name, var_control_scheme_3_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_4_object_type, var_control_scheme_4_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_4_name, var_control_scheme_4_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_4_schedule_name, var_control_scheme_4_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_5_object_type, var_control_scheme_5_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_5_name, var_control_scheme_5_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_5_schedule_name, var_control_scheme_5_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_6_object_type, var_control_scheme_6_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_6_name, var_control_scheme_6_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_6_schedule_name, var_control_scheme_6_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_7_object_type, var_control_scheme_7_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_7_name, var_control_scheme_7_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_7_schedule_name, var_control_scheme_7_schedule_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_8_object_type, var_control_scheme_8_object_type)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_8_name, var_control_scheme_8_name)
        self.assertEqual(idf2.plantequipmentoperationschemess[0].control_scheme_8_schedule_name, var_control_scheme_8_schedule_name)