""" Data objects in group "Compliance Objects"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ComplianceBuilding(DataObject):

    """ Corresponds to IDD object `Compliance:Building`
        Building level inputs related to compliance to building standards, building codes, and beyond energy code programs.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'building rotation for appendix g',
                                       {'name': u'Building Rotation for Appendix G',
                                        'pyname': u'building_rotation_for_appendix_g',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'})]),
               'format': None,
               'group': u'Compliance Objects',
               'min-fields': 1,
               'name': u'Compliance:Building',
               'pyname': u'ComplianceBuilding',
               'required-object': False,
               'unique-object': True}

    @property
    def building_rotation_for_appendix_g(self):
        """field `Building Rotation for Appendix G`

        |  Additional degrees of rotation to be used with the requirement in ASHRAE Standard 90.1 Appendix G
        |  that states that the baseline building should be rotated in four directions.
        |  Units: deg

        Args:
            value (float): value for IDD Field `Building Rotation for Appendix G`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `building_rotation_for_appendix_g` or None if not set

        """
        return self["Building Rotation for Appendix G"]

    @building_rotation_for_appendix_g.setter
    def building_rotation_for_appendix_g(self, value=None):
        """Corresponds to IDD field `Building Rotation for Appendix G`"""
        self["Building Rotation for Appendix G"] = value


