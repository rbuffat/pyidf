import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import OutputPreprocessorMessage
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutputPreprocessorMessage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outputpreprocessormessage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutputPreprocessorMessage()
        # alpha
        var_preprocessor_name = "Preprocessor Name"
        obj.preprocessor_name = var_preprocessor_name
        # alpha
        var_error_severity = "Information"
        obj.error_severity = var_error_severity
        # alpha
        var_message_line_1 = "Message Line 1"
        obj.message_line_1 = var_message_line_1
        # alpha
        var_message_line_2 = "Message Line 2"
        obj.message_line_2 = var_message_line_2
        # alpha
        var_message_line_3 = "Message Line 3"
        obj.message_line_3 = var_message_line_3
        # alpha
        var_message_line_4 = "Message Line 4"
        obj.message_line_4 = var_message_line_4
        # alpha
        var_message_line_5 = "Message Line 5"
        obj.message_line_5 = var_message_line_5
        # alpha
        var_message_line_6 = "Message Line 6"
        obj.message_line_6 = var_message_line_6
        # alpha
        var_message_line_7 = "Message Line 7"
        obj.message_line_7 = var_message_line_7
        # alpha
        var_message_line_8 = "Message Line 8"
        obj.message_line_8 = var_message_line_8
        # alpha
        var_message_line_9 = "Message Line 9"
        obj.message_line_9 = var_message_line_9
        # alpha
        var_message_line_10 = "Message Line 10"
        obj.message_line_10 = var_message_line_10

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outputpreprocessormessages[0].preprocessor_name, var_preprocessor_name)
        self.assertEqual(idf2.outputpreprocessormessages[0].error_severity, var_error_severity)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_1, var_message_line_1)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_2, var_message_line_2)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_3, var_message_line_3)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_4, var_message_line_4)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_5, var_message_line_5)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_6, var_message_line_6)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_7, var_message_line_7)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_8, var_message_line_8)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_9, var_message_line_9)
        self.assertEqual(idf2.outputpreprocessormessages[0].message_line_10, var_message_line_10)