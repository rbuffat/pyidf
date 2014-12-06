import os
import tempfile
import unittest
import pyidf
from pyidf.advanced_construction import SurfacePropertySolarIncidentInside
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSurfacePropertySolarIncidentInside(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_surfacepropertysolarincidentinside(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SurfacePropertySolarIncidentInside()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_inside_surface_incident_sun_solar_radiation_schedule_name = "object-list|Inside Surface Incident Sun Solar Radiation Schedule Name"
        obj.inside_surface_incident_sun_solar_radiation_schedule_name = var_inside_surface_incident_sun_solar_radiation_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.surfacepropertysolarincidentinsides[0].name, var_name)
        self.assertEqual(idf2.surfacepropertysolarincidentinsides[0].surface_name, var_surface_name)
        self.assertEqual(idf2.surfacepropertysolarincidentinsides[0].construction_name, var_construction_name)
        self.assertEqual(idf2.surfacepropertysolarincidentinsides[0].inside_surface_incident_sun_solar_radiation_schedule_name, var_inside_surface_incident_sun_solar_radiation_schedule_name)