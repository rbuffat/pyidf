import os
import tempfile
import unittest
import pyidf
from pyidf.thermal_zones_and_surfaces import WindowPropertyShadingControl
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestWindowPropertyShadingControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowpropertyshadingcontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowPropertyShadingControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_shading_type = "InteriorShade"
        obj.shading_type = var_shading_type
        # object-list
        var_construction_with_shading_name = "object-list|Construction with Shading Name"
        obj.construction_with_shading_name = var_construction_with_shading_name
        # alpha
        var_shading_control_type = "AlwaysOn"
        obj.shading_control_type = var_shading_control_type
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_setpoint = 6.6
        obj.setpoint = var_setpoint
        # alpha
        var_shading_control_is_scheduled = "No"
        obj.shading_control_is_scheduled = var_shading_control_is_scheduled
        # alpha
        var_glare_control_is_active = "No"
        obj.glare_control_is_active = var_glare_control_is_active
        # object-list
        var_shading_device_material_name = "object-list|Shading Device Material Name"
        obj.shading_device_material_name = var_shading_device_material_name
        # alpha
        var_type_of_slat_angle_control_for_blinds = "FixedSlatAngle"
        obj.type_of_slat_angle_control_for_blinds = var_type_of_slat_angle_control_for_blinds
        # object-list
        var_slat_angle_schedule_name = "object-list|Slat Angle Schedule Name"
        obj.slat_angle_schedule_name = var_slat_angle_schedule_name
        # real
        var_setpoint_2 = 12.12
        obj.setpoint_2 = var_setpoint_2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].name, var_name)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].shading_type, var_shading_type)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].construction_with_shading_name, var_construction_with_shading_name)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].shading_control_type, var_shading_control_type)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.windowpropertyshadingcontrols[0].setpoint, var_setpoint)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].shading_control_is_scheduled, var_shading_control_is_scheduled)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].glare_control_is_active, var_glare_control_is_active)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].shading_device_material_name, var_shading_device_material_name)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].type_of_slat_angle_control_for_blinds, var_type_of_slat_angle_control_for_blinds)
        self.assertEqual(idf2.windowpropertyshadingcontrols[0].slat_angle_schedule_name, var_slat_angle_schedule_name)
        self.assertAlmostEqual(idf2.windowpropertyshadingcontrols[0].setpoint_2, var_setpoint_2)