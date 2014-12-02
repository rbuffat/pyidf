from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ExteriorLights(object):
    """ Corresponds to IDD object `Exterior:Lights`
        only used for Meter type reporting, does not affect building loads
    """
    internal_name = "Exterior:Lights"
    field_count = 5
    required_fields = ["Name", "Schedule Name", "Design Level"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Exterior:Lights`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level"] = None
        self._data["Control Option"] = None
        self._data["End-Use Subcategory"] = None
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
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_option = None
        else:
            self.control_option = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorLights.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorLights.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorLights.name`')
        self._data["Name"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        units in schedule should be fraction applied to capacity of the exterior lights equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorLights.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorLights.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorLights.schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `Design Level`

        Args:
            value (float): value for IDD Field `Design Level`
                Units: W
                IP-Units: W
                value >= 0.0
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
                                 ' for field `ExteriorLights.design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ExteriorLights.design_level`')
        self._data["Design Level"] = value

    @property
    def control_option(self):
        """Get control_option

        Returns:
            str: the value of `control_option` or None if not set
        """
        return self._data["Control Option"]

    @control_option.setter
    def control_option(self, value=None):
        """  Corresponds to IDD Field `Control Option`
        Astronomical Clock option overrides schedule to turn lights off when sun is up

        Args:
            value (str): value for IDD Field `Control Option`
                Accepted values are:
                      - ScheduleNameOnly
                      - AstronomicalClock
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorLights.control_option`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorLights.control_option`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorLights.control_option`')
            vals = {}
            vals["schedulenameonly"] = "ScheduleNameOnly"
            vals["astronomicalclock"] = "AstronomicalClock"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ExteriorLights.control_option`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ExteriorLights.control_option`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Option"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorLights.enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorLights.enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorLights.enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

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
                    raise ValueError("Required field ExteriorLights:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExteriorLights:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExteriorLights: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExteriorLights: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class ExteriorFuelEquipment(object):
    """ Corresponds to IDD object `Exterior:FuelEquipment`
        only used for Meter type reporting, does not affect building loads
    """
    internal_name = "Exterior:FuelEquipment"
    field_count = 5
    required_fields = ["Name", "Fuel Use Type", "Schedule Name", "Design Level"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Exterior:FuelEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fuel Use Type"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level"] = None
        self._data["End-Use Subcategory"] = None
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
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fuel_use_type = None
        else:
            self.fuel_use_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorFuelEquipment.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorFuelEquipment.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorFuelEquipment.name`')
        self._data["Name"] = value

    @property
    def fuel_use_type(self):
        """Get fuel_use_type

        Returns:
            str: the value of `fuel_use_type` or None if not set
        """
        return self._data["Fuel Use Type"]

    @fuel_use_type.setter
    def fuel_use_type(self, value=None):
        """  Corresponds to IDD Field `Fuel Use Type`

        Args:
            value (str): value for IDD Field `Fuel Use Type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Diesel
                      - Gasoline
                      - Coal
                      - OtherFuel1
                      - OtherFuel2
                      - Steam
                      - DistrictHeating
                      - DistrictCooling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorFuelEquipment.fuel_use_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorFuelEquipment.fuel_use_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorFuelEquipment.fuel_use_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["coal"] = "Coal"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            vals["steam"] = "Steam"
            vals["districtheating"] = "DistrictHeating"
            vals["districtcooling"] = "DistrictCooling"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ExteriorFuelEquipment.fuel_use_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ExteriorFuelEquipment.fuel_use_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fuel Use Type"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        units in schedule should be fraction applied to capacity of the exterior fuel equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorFuelEquipment.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorFuelEquipment.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorFuelEquipment.schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `Design Level`

        Args:
            value (float): value for IDD Field `Design Level`
                Units: W
                IP-Units: W
                value >= 0.0
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
                                 ' for field `ExteriorFuelEquipment.design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ExteriorFuelEquipment.design_level`')
        self._data["Design Level"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorFuelEquipment.enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorFuelEquipment.enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorFuelEquipment.enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

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
                    raise ValueError("Required field ExteriorFuelEquipment:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExteriorFuelEquipment:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExteriorFuelEquipment: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExteriorFuelEquipment: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class ExteriorWaterEquipment(object):
    """ Corresponds to IDD object `Exterior:WaterEquipment`
        only used for Meter type reporting, does not affect building loads
    """
    internal_name = "Exterior:WaterEquipment"
    field_count = 5
    required_fields = ["Name", "Schedule Name", "Design Level"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Exterior:WaterEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fuel Use Type"] = None
        self._data["Schedule Name"] = None
        self._data["Design Level"] = None
        self._data["End-Use Subcategory"] = None
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
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fuel_use_type = None
        else:
            self.fuel_use_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_level = None
        else:
            self.design_level = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorWaterEquipment.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorWaterEquipment.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorWaterEquipment.name`')
        self._data["Name"] = value

    @property
    def fuel_use_type(self):
        """Get fuel_use_type

        Returns:
            str: the value of `fuel_use_type` or None if not set
        """
        return self._data["Fuel Use Type"]

    @fuel_use_type.setter
    def fuel_use_type(self, value="Water"):
        """  Corresponds to IDD Field `Fuel Use Type`

        Args:
            value (str): value for IDD Field `Fuel Use Type`
                Accepted values are:
                      - Water
                Default value: Water
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorWaterEquipment.fuel_use_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorWaterEquipment.fuel_use_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorWaterEquipment.fuel_use_type`')
            vals = {}
            vals["water"] = "Water"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ExteriorWaterEquipment.fuel_use_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ExteriorWaterEquipment.fuel_use_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fuel Use Type"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        units in Schedule should be fraction applied to capacity of the exterior water equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorWaterEquipment.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorWaterEquipment.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorWaterEquipment.schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def design_level(self):
        """Get design_level

        Returns:
            float: the value of `design_level` or None if not set
        """
        return self._data["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """  Corresponds to IDD Field `Design Level`

        Args:
            value (float): value for IDD Field `Design Level`
                Units: m3/s
                value >= 0.0
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
                                 ' for field `ExteriorWaterEquipment.design_level`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ExteriorWaterEquipment.design_level`')
        self._data["Design Level"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ExteriorWaterEquipment.enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ExteriorWaterEquipment.enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ExteriorWaterEquipment.enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

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
                    raise ValueError("Required field ExteriorWaterEquipment:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ExteriorWaterEquipment:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ExteriorWaterEquipment: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ExteriorWaterEquipment: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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