"""Python library to read, modify and create EnergyPlus idf files.

Author: Rene Buffat
License: Apache License 2.0

"""

__author__ = "Rene Buffat"
__copyright__ = "Copyright 2014"
__credits__ = []
__license__ = "Apache 2.0"
__version__ = "0.2.0"
__maintainer__ = "Rene Buffat"
__email__ = "buffat@gmail.com"
__status__ = "Development"


class ValidationLevel(object):

    """ Validation levels:
        - no: no validation
        - warn: issue warnings
        - transition: try to transition values to follow specification
        - error: raise exceptions when values are not according specification"""
    no = "no"
    warn = "warm"
    transition = "transition"
    error = "error"

validation_level = ValidationLevel.transition
