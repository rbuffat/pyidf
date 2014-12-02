from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ComplianceBuilding(object):
    """ Corresponds to IDD object `Compliance:Building`
        Building level inputs related to compliance to building standards, building codes, and beyond energy code programs.
    """
    internal_name = "Compliance:Building"
    field_count = 1
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 1
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Compliance:Building`
        """
        self._data = OrderedDict()
        self._data["Building Rotation for Appendix G"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.building_rotation_for_appendix_g = None
        else:
            self.building_rotation_for_appendix_g = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def building_rotation_for_appendix_g(self):
        """Get building_rotation_for_appendix_g

        Returns:
            float: the value of `building_rotation_for_appendix_g` or None if not set
        """
        return self._data["Building Rotation for Appendix G"]

    @building_rotation_for_appendix_g.setter
    def building_rotation_for_appendix_g(self, value=0.0):
        """  Corresponds to IDD Field `Building Rotation for Appendix G`
        Additional degrees of rotation to be used with the requirement in ASHRAE Standard 90.1 Appendix G
        that states that the baseline building should be rotated in four directions.

        Args:
            value (float): value for IDD Field `Building Rotation for Appendix G`
                Units: deg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ComplianceBuilding.building_rotation_for_appendix_g`'.format(value))
        self._data["Building Rotation for Appendix G"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ComplianceBuilding:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ComplianceBuilding:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ComplianceBuilding: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ComplianceBuilding: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])