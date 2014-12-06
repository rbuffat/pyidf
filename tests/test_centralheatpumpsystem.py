import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import CentralHeatPumpSystem

log = logging.getLogger(__name__)

class TestCentralHeatPumpSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_centralheatpumpsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CentralHeatPumpSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_method = "SmartMixing"
        obj.control_method = var_control_method
        # alpha
        var_cooling_loop_inlet_node_name = "Cooling Loop Inlet Node Name"
        obj.cooling_loop_inlet_node_name = var_cooling_loop_inlet_node_name
        # alpha
        var_cooling_loop_outlet_node_name = "Cooling Loop Outlet Node Name"
        obj.cooling_loop_outlet_node_name = var_cooling_loop_outlet_node_name
        # alpha
        var_source_loop_inlet_node_name = "Source Loop Inlet Node Name"
        obj.source_loop_inlet_node_name = var_source_loop_inlet_node_name
        # alpha
        var_source_loop_outlet_node_name = "Source Loop Outlet Node Name"
        obj.source_loop_outlet_node_name = var_source_loop_outlet_node_name
        # alpha
        var_heating_loop_inlet_node_name = "Heating Loop Inlet Node Name"
        obj.heating_loop_inlet_node_name = var_heating_loop_inlet_node_name
        # alpha
        var_heating_loop_outlet_node_name = "Heating Loop Outlet Node Name"
        obj.heating_loop_outlet_node_name = var_heating_loop_outlet_node_name
        # real
        var_ancillary_power = 0.0
        obj.ancillary_power = var_ancillary_power
        # object-list
        var_ancillary_operation_schedule_name = "object-list|Ancillary Operation Schedule Name"
        obj.ancillary_operation_schedule_name = var_ancillary_operation_schedule_name
        # alpha
        var_chiller_heater_modules_performance_component_object_type_1 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_1 = var_chiller_heater_modules_performance_component_object_type_1
        # object-list
        var_chiller_heater_modules_performance_component_name_1 = "object-list|Chiller Heater Modules Performance Component Name 1"
        obj.chiller_heater_modules_performance_component_name_1 = var_chiller_heater_modules_performance_component_name_1
        # object-list
        var_chiller_heater_modules_control_schedule_name_1 = "object-list|Chiller Heater Modules Control Schedule Name 1"
        obj.chiller_heater_modules_control_schedule_name_1 = var_chiller_heater_modules_control_schedule_name_1
        # integer
        var_number_of_chiller_heater_modules_1 = 1
        obj.number_of_chiller_heater_modules_1 = var_number_of_chiller_heater_modules_1
        # alpha
        var_chiller_heater_modules_performance_component_object_type_2 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_2 = var_chiller_heater_modules_performance_component_object_type_2
        # object-list
        var_chiller_heater_modules_performance_component_name_2 = "object-list|Chiller Heater Modules Performance Component Name 2"
        obj.chiller_heater_modules_performance_component_name_2 = var_chiller_heater_modules_performance_component_name_2
        # object-list
        var_chiller_heater_modules_control_schedule_name_2 = "object-list|Chiller Heater Modules Control Schedule Name 2"
        obj.chiller_heater_modules_control_schedule_name_2 = var_chiller_heater_modules_control_schedule_name_2
        # integer
        var_number_of_chiller_heater_modules_2 = 1
        obj.number_of_chiller_heater_modules_2 = var_number_of_chiller_heater_modules_2
        # alpha
        var_chiller_heater_performance_component_object_type_3 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_performance_component_object_type_3 = var_chiller_heater_performance_component_object_type_3
        # object-list
        var_chiller_heater_performance_component_name_3 = "object-list|Chiller Heater Performance Component Name 3"
        obj.chiller_heater_performance_component_name_3 = var_chiller_heater_performance_component_name_3
        # object-list
        var_chiller_heater_modules_control_schedule_name_3 = "object-list|Chiller Heater Modules Control Schedule Name 3"
        obj.chiller_heater_modules_control_schedule_name_3 = var_chiller_heater_modules_control_schedule_name_3
        # integer
        var_number_of_chiller_heater_modules_3 = 1
        obj.number_of_chiller_heater_modules_3 = var_number_of_chiller_heater_modules_3
        # alpha
        var_chiller_heater_modules_performance_component_object_type_4 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_4 = var_chiller_heater_modules_performance_component_object_type_4
        # object-list
        var_chiller_heater_modules_performance_component_name_4 = "object-list|Chiller Heater Modules Performance Component Name 4"
        obj.chiller_heater_modules_performance_component_name_4 = var_chiller_heater_modules_performance_component_name_4
        # object-list
        var_chiller_heater_modules_control_schedule_name_4 = "object-list|Chiller Heater Modules Control Schedule Name 4"
        obj.chiller_heater_modules_control_schedule_name_4 = var_chiller_heater_modules_control_schedule_name_4
        # integer
        var_number_of_chiller_heater_modules_4 = 1
        obj.number_of_chiller_heater_modules_4 = var_number_of_chiller_heater_modules_4
        # alpha
        var_chiller_heater_modules_performance_component_object_type_5 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_5 = var_chiller_heater_modules_performance_component_object_type_5
        # object-list
        var_chiller_heater_models_performance_component_name_5 = "object-list|Chiller Heater Models Performance Component Name 5"
        obj.chiller_heater_models_performance_component_name_5 = var_chiller_heater_models_performance_component_name_5
        # object-list
        var_chiller_heater_modules_control_schedule_name_5 = "object-list|Chiller Heater Modules Control Schedule Name 5"
        obj.chiller_heater_modules_control_schedule_name_5 = var_chiller_heater_modules_control_schedule_name_5
        # integer
        var_number_of_chiller_heater_modules_5 = 1
        obj.number_of_chiller_heater_modules_5 = var_number_of_chiller_heater_modules_5
        # alpha
        var_chiller_heater_modules_performance_component_object_type_6 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_6 = var_chiller_heater_modules_performance_component_object_type_6
        # object-list
        var_chiller_heater_modules_performance_component_name_6 = "object-list|Chiller Heater Modules Performance Component Name 6"
        obj.chiller_heater_modules_performance_component_name_6 = var_chiller_heater_modules_performance_component_name_6
        # object-list
        var_chiller_heater_modules_control_schedule_name_6 = "object-list|Chiller Heater Modules Control Schedule Name 6"
        obj.chiller_heater_modules_control_schedule_name_6 = var_chiller_heater_modules_control_schedule_name_6
        # integer
        var_number_of_chiller_heater_modules_6 = 1
        obj.number_of_chiller_heater_modules_6 = var_number_of_chiller_heater_modules_6
        # alpha
        var_chiller_heater_modules_performance_component_object_type_7 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_7 = var_chiller_heater_modules_performance_component_object_type_7
        # object-list
        var_chiller_heater_modules_performance_component_name_7 = "object-list|Chiller Heater Modules Performance Component Name 7"
        obj.chiller_heater_modules_performance_component_name_7 = var_chiller_heater_modules_performance_component_name_7
        # object-list
        var_chiller_heater_modules_control_schedule_name_7 = "object-list|Chiller Heater Modules Control Schedule Name 7"
        obj.chiller_heater_modules_control_schedule_name_7 = var_chiller_heater_modules_control_schedule_name_7
        # integer
        var_number_of_chiller_heater_modules_7 = 1
        obj.number_of_chiller_heater_modules_7 = var_number_of_chiller_heater_modules_7
        # alpha
        var_chiller_heater_modules_performance_component_object_type_8 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_8 = var_chiller_heater_modules_performance_component_object_type_8
        # object-list
        var_chiller_heater_modules_performance_component_name_8 = "object-list|Chiller Heater Modules Performance Component Name 8"
        obj.chiller_heater_modules_performance_component_name_8 = var_chiller_heater_modules_performance_component_name_8
        # object-list
        var_chiller_heater_modules_control_schedule_name_8 = "object-list|Chiller Heater Modules Control Schedule Name 8"
        obj.chiller_heater_modules_control_schedule_name_8 = var_chiller_heater_modules_control_schedule_name_8
        # integer
        var_number_of_chiller_heater_modules_8 = 1
        obj.number_of_chiller_heater_modules_8 = var_number_of_chiller_heater_modules_8
        # alpha
        var_chiller_heater_modules_performance_component_object_type_9 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_9 = var_chiller_heater_modules_performance_component_object_type_9
        # object-list
        var_chiller_heater_modules_performance_component_name_9 = "object-list|Chiller Heater Modules Performance Component Name 9"
        obj.chiller_heater_modules_performance_component_name_9 = var_chiller_heater_modules_performance_component_name_9
        # object-list
        var_chiller_heater_modules_control_schedule_name_9 = "object-list|Chiller Heater Modules Control Schedule Name 9"
        obj.chiller_heater_modules_control_schedule_name_9 = var_chiller_heater_modules_control_schedule_name_9
        # integer
        var_number_of_chiller_heater_modules_9 = 1
        obj.number_of_chiller_heater_modules_9 = var_number_of_chiller_heater_modules_9
        # alpha
        var_chiller_heater_modules_performance_component_object_type_10 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_10 = var_chiller_heater_modules_performance_component_object_type_10
        # object-list
        var_chiller_heater_modules_performance_component_name_10 = "object-list|Chiller Heater Modules Performance Component Name 10"
        obj.chiller_heater_modules_performance_component_name_10 = var_chiller_heater_modules_performance_component_name_10
        # object-list
        var_chiller_heater_modules_control_schedule_name_10 = "object-list|Chiller Heater Modules Control Schedule Name 10"
        obj.chiller_heater_modules_control_schedule_name_10 = var_chiller_heater_modules_control_schedule_name_10
        # integer
        var_number_of_chiller_heater_modules_10 = 1
        obj.number_of_chiller_heater_modules_10 = var_number_of_chiller_heater_modules_10
        # alpha
        var_chiller_heater_modules_performance_component_object_type_11 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_11 = var_chiller_heater_modules_performance_component_object_type_11
        # object-list
        var_chiller_heater_modules_performance_component_name_11 = "object-list|Chiller Heater Modules Performance Component Name 11"
        obj.chiller_heater_modules_performance_component_name_11 = var_chiller_heater_modules_performance_component_name_11
        # object-list
        var_chiller_heater_module_control_schedule_name_11 = "object-list|Chiller Heater Module Control Schedule Name 11"
        obj.chiller_heater_module_control_schedule_name_11 = var_chiller_heater_module_control_schedule_name_11
        # integer
        var_number_of_chiller_heater_modules_11 = 1
        obj.number_of_chiller_heater_modules_11 = var_number_of_chiller_heater_modules_11
        # alpha
        var_chiller_heater_modules_performance_component_object_type_12 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_12 = var_chiller_heater_modules_performance_component_object_type_12
        # object-list
        var_chiller_heater_modules_performance_component_name_12 = "object-list|Chiller Heater Modules Performance Component Name 12"
        obj.chiller_heater_modules_performance_component_name_12 = var_chiller_heater_modules_performance_component_name_12
        # object-list
        var_chiller_heater_modules_control_schedule_name_12 = "object-list|Chiller Heater Modules Control Schedule Name 12"
        obj.chiller_heater_modules_control_schedule_name_12 = var_chiller_heater_modules_control_schedule_name_12
        # integer
        var_number_of_chiller_heater_modules_12 = 1
        obj.number_of_chiller_heater_modules_12 = var_number_of_chiller_heater_modules_12
        # alpha
        var_chiller_heater_modules_performance_component_object_type_13 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_13 = var_chiller_heater_modules_performance_component_object_type_13
        # object-list
        var_chiller_heater_modules_performance_component_name_13 = "object-list|Chiller Heater Modules Performance Component Name 13"
        obj.chiller_heater_modules_performance_component_name_13 = var_chiller_heater_modules_performance_component_name_13
        # object-list
        var_chiller_heater_modules_control_schedule_name_13 = "object-list|Chiller Heater Modules Control Schedule Name 13"
        obj.chiller_heater_modules_control_schedule_name_13 = var_chiller_heater_modules_control_schedule_name_13
        # integer
        var_number_of_chiller_heater_modules_13 = 1
        obj.number_of_chiller_heater_modules_13 = var_number_of_chiller_heater_modules_13
        # alpha
        var_chiller_heater_modules_performance_component_object_type_14 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_14 = var_chiller_heater_modules_performance_component_object_type_14
        # object-list
        var_chiller_heater_modules_performance_component_name_14 = "object-list|Chiller Heater Modules Performance Component Name 14"
        obj.chiller_heater_modules_performance_component_name_14 = var_chiller_heater_modules_performance_component_name_14
        # object-list
        var_chiller_heater_modules_control_schedule_name_14 = "object-list|Chiller Heater Modules Control Schedule Name 14"
        obj.chiller_heater_modules_control_schedule_name_14 = var_chiller_heater_modules_control_schedule_name_14
        # integer
        var_number_of_chiller_heater_modules_14 = 1
        obj.number_of_chiller_heater_modules_14 = var_number_of_chiller_heater_modules_14
        # alpha
        var_chiller_heater_modules_performance_component_object_type_15 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_15 = var_chiller_heater_modules_performance_component_object_type_15
        # object-list
        var_chiller_heater_modules_performance_component_name_15 = "object-list|Chiller Heater Modules Performance Component Name 15"
        obj.chiller_heater_modules_performance_component_name_15 = var_chiller_heater_modules_performance_component_name_15
        # object-list
        var_chiller_heater_modules_control_schedule_name_15 = "object-list|Chiller Heater Modules Control Schedule Name 15"
        obj.chiller_heater_modules_control_schedule_name_15 = var_chiller_heater_modules_control_schedule_name_15
        # integer
        var_number_of_chiller_heater_modules_15 = 1
        obj.number_of_chiller_heater_modules_15 = var_number_of_chiller_heater_modules_15
        # alpha
        var_chiller_heater_modules_performance_component_object_type_16 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_16 = var_chiller_heater_modules_performance_component_object_type_16
        # object-list
        var_chiller_heater_modules_performance_component_name_16 = "object-list|Chiller Heater Modules Performance Component Name 16"
        obj.chiller_heater_modules_performance_component_name_16 = var_chiller_heater_modules_performance_component_name_16
        # object-list
        var_chiller_heater_modules_control_schedule_name_16 = "object-list|Chiller Heater Modules Control Schedule Name 16"
        obj.chiller_heater_modules_control_schedule_name_16 = var_chiller_heater_modules_control_schedule_name_16
        # integer
        var_number_of_chiller_heater_modules_16 = 1
        obj.number_of_chiller_heater_modules_16 = var_number_of_chiller_heater_modules_16
        # alpha
        var_chiller_heater_modules_performance_component_object_type_17 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_17 = var_chiller_heater_modules_performance_component_object_type_17
        # object-list
        var_chiller_heater_modules_performance_component_name_17 = "object-list|Chiller Heater Modules Performance Component Name 17"
        obj.chiller_heater_modules_performance_component_name_17 = var_chiller_heater_modules_performance_component_name_17
        # object-list
        var_chiller_heater_modules_control_schedule_name_17 = "object-list|Chiller Heater Modules Control Schedule Name 17"
        obj.chiller_heater_modules_control_schedule_name_17 = var_chiller_heater_modules_control_schedule_name_17
        # integer
        var_number_of_chiller_heater_modules_17 = 1
        obj.number_of_chiller_heater_modules_17 = var_number_of_chiller_heater_modules_17
        # alpha
        var_chiller_heater_modules_performance_component_object_type_18 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_18 = var_chiller_heater_modules_performance_component_object_type_18
        # object-list
        var_chiller_heater_modules_performance_component_name_18 = "object-list|Chiller Heater Modules Performance Component Name 18"
        obj.chiller_heater_modules_performance_component_name_18 = var_chiller_heater_modules_performance_component_name_18
        # object-list
        var_chiller_heater_modules_control_control_schedule_name_18 = "object-list|Chiller Heater Modules Control Control Schedule Name 18"
        obj.chiller_heater_modules_control_control_schedule_name_18 = var_chiller_heater_modules_control_control_schedule_name_18
        # integer
        var_number_of_chiller_heater_modules_18 = 1
        obj.number_of_chiller_heater_modules_18 = var_number_of_chiller_heater_modules_18
        # alpha
        var_chiller_heater_modules_performance_component_object_type_19 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_19 = var_chiller_heater_modules_performance_component_object_type_19
        # object-list
        var_chiller_heater_modules_performance_component_name_19 = "object-list|Chiller Heater Modules Performance Component Name 19"
        obj.chiller_heater_modules_performance_component_name_19 = var_chiller_heater_modules_performance_component_name_19
        # object-list
        var_chiller_heater_modules_control_schedule_name_19 = "object-list|Chiller Heater Modules Control Schedule Name 19"
        obj.chiller_heater_modules_control_schedule_name_19 = var_chiller_heater_modules_control_schedule_name_19
        # integer
        var_number_of_chiller_heater_modules_19 = 1
        obj.number_of_chiller_heater_modules_19 = var_number_of_chiller_heater_modules_19
        # alpha
        var_chiller_heater_modules_performance_component_object_type_20 = "ChillerHeaterPerformance:Electric:EIR"
        obj.chiller_heater_modules_performance_component_object_type_20 = var_chiller_heater_modules_performance_component_object_type_20
        # object-list
        var_chiller_heater_modules_performance_component_name_20 = "object-list|Chiller Heater Modules Performance Component Name 20"
        obj.chiller_heater_modules_performance_component_name_20 = var_chiller_heater_modules_performance_component_name_20
        # object-list
        var_chiller_heater_modules_control_schedule_name_20 = "object-list|Chiller Heater Modules Control Schedule Name 20"
        obj.chiller_heater_modules_control_schedule_name_20 = var_chiller_heater_modules_control_schedule_name_20
        # integer
        var_number_of_chiller_heater_modules_20 = 1
        obj.number_of_chiller_heater_modules_20 = var_number_of_chiller_heater_modules_20

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.centralheatpumpsystems[0].name, var_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].control_method, var_control_method)
        self.assertEqual(idf2.centralheatpumpsystems[0].cooling_loop_inlet_node_name, var_cooling_loop_inlet_node_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].cooling_loop_outlet_node_name, var_cooling_loop_outlet_node_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].source_loop_inlet_node_name, var_source_loop_inlet_node_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].source_loop_outlet_node_name, var_source_loop_outlet_node_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].heating_loop_inlet_node_name, var_heating_loop_inlet_node_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].heating_loop_outlet_node_name, var_heating_loop_outlet_node_name)
        self.assertAlmostEqual(idf2.centralheatpumpsystems[0].ancillary_power, var_ancillary_power)
        self.assertEqual(idf2.centralheatpumpsystems[0].ancillary_operation_schedule_name, var_ancillary_operation_schedule_name)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_1, var_chiller_heater_modules_performance_component_object_type_1)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_1, var_chiller_heater_modules_performance_component_name_1)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_1, var_chiller_heater_modules_control_schedule_name_1)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_1, var_number_of_chiller_heater_modules_1)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_2, var_chiller_heater_modules_performance_component_object_type_2)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_2, var_chiller_heater_modules_performance_component_name_2)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_2, var_chiller_heater_modules_control_schedule_name_2)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_2, var_number_of_chiller_heater_modules_2)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_performance_component_object_type_3, var_chiller_heater_performance_component_object_type_3)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_performance_component_name_3, var_chiller_heater_performance_component_name_3)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_3, var_chiller_heater_modules_control_schedule_name_3)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_3, var_number_of_chiller_heater_modules_3)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_4, var_chiller_heater_modules_performance_component_object_type_4)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_4, var_chiller_heater_modules_performance_component_name_4)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_4, var_chiller_heater_modules_control_schedule_name_4)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_4, var_number_of_chiller_heater_modules_4)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_5, var_chiller_heater_modules_performance_component_object_type_5)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_models_performance_component_name_5, var_chiller_heater_models_performance_component_name_5)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_5, var_chiller_heater_modules_control_schedule_name_5)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_5, var_number_of_chiller_heater_modules_5)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_6, var_chiller_heater_modules_performance_component_object_type_6)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_6, var_chiller_heater_modules_performance_component_name_6)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_6, var_chiller_heater_modules_control_schedule_name_6)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_6, var_number_of_chiller_heater_modules_6)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_7, var_chiller_heater_modules_performance_component_object_type_7)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_7, var_chiller_heater_modules_performance_component_name_7)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_7, var_chiller_heater_modules_control_schedule_name_7)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_7, var_number_of_chiller_heater_modules_7)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_8, var_chiller_heater_modules_performance_component_object_type_8)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_8, var_chiller_heater_modules_performance_component_name_8)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_8, var_chiller_heater_modules_control_schedule_name_8)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_8, var_number_of_chiller_heater_modules_8)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_9, var_chiller_heater_modules_performance_component_object_type_9)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_9, var_chiller_heater_modules_performance_component_name_9)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_9, var_chiller_heater_modules_control_schedule_name_9)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_9, var_number_of_chiller_heater_modules_9)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_10, var_chiller_heater_modules_performance_component_object_type_10)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_10, var_chiller_heater_modules_performance_component_name_10)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_10, var_chiller_heater_modules_control_schedule_name_10)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_10, var_number_of_chiller_heater_modules_10)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_11, var_chiller_heater_modules_performance_component_object_type_11)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_11, var_chiller_heater_modules_performance_component_name_11)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_module_control_schedule_name_11, var_chiller_heater_module_control_schedule_name_11)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_11, var_number_of_chiller_heater_modules_11)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_12, var_chiller_heater_modules_performance_component_object_type_12)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_12, var_chiller_heater_modules_performance_component_name_12)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_12, var_chiller_heater_modules_control_schedule_name_12)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_12, var_number_of_chiller_heater_modules_12)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_13, var_chiller_heater_modules_performance_component_object_type_13)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_13, var_chiller_heater_modules_performance_component_name_13)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_13, var_chiller_heater_modules_control_schedule_name_13)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_13, var_number_of_chiller_heater_modules_13)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_14, var_chiller_heater_modules_performance_component_object_type_14)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_14, var_chiller_heater_modules_performance_component_name_14)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_14, var_chiller_heater_modules_control_schedule_name_14)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_14, var_number_of_chiller_heater_modules_14)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_15, var_chiller_heater_modules_performance_component_object_type_15)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_15, var_chiller_heater_modules_performance_component_name_15)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_15, var_chiller_heater_modules_control_schedule_name_15)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_15, var_number_of_chiller_heater_modules_15)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_16, var_chiller_heater_modules_performance_component_object_type_16)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_16, var_chiller_heater_modules_performance_component_name_16)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_16, var_chiller_heater_modules_control_schedule_name_16)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_16, var_number_of_chiller_heater_modules_16)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_17, var_chiller_heater_modules_performance_component_object_type_17)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_17, var_chiller_heater_modules_performance_component_name_17)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_17, var_chiller_heater_modules_control_schedule_name_17)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_17, var_number_of_chiller_heater_modules_17)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_18, var_chiller_heater_modules_performance_component_object_type_18)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_18, var_chiller_heater_modules_performance_component_name_18)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_control_schedule_name_18, var_chiller_heater_modules_control_control_schedule_name_18)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_18, var_number_of_chiller_heater_modules_18)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_19, var_chiller_heater_modules_performance_component_object_type_19)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_19, var_chiller_heater_modules_performance_component_name_19)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_19, var_chiller_heater_modules_control_schedule_name_19)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_19, var_number_of_chiller_heater_modules_19)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_object_type_20, var_chiller_heater_modules_performance_component_object_type_20)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_performance_component_name_20, var_chiller_heater_modules_performance_component_name_20)
        self.assertEqual(idf2.centralheatpumpsystems[0].chiller_heater_modules_control_schedule_name_20, var_chiller_heater_modules_control_schedule_name_20)
        self.assertEqual(idf2.centralheatpumpsystems[0].number_of_chiller_heater_modules_20, var_number_of_chiller_heater_modules_20)