""" Helper methods for pyidf
"""

from collections import OrderedDict
import logging
import re
import six
import pyidf
from pyidf import ValidationLevel

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())


class DataObject(object):

    schema = {}

    def __init__(self):
        """ Init data dictionary object
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None

        self._extdata = []
        self.strict = True

    def add_extensible(self):
        raise NotImplementedError("add_extensible is not implemented for class DataObject")

    def keys(self):
        keys = []
        for field in self.schema['fields'].values():
            keys.append(field['name'])
        for i in range(len(self._extdata)):
            for field in self.schema['extensible-fields'].values():
                keys.append((field['name'], i))
        return keys

    def __setitem__(self, key, value):
        if isinstance(key, six.string_types):
            key_lower = key.lower()
            if key_lower in self.schema['fields']:
                value = self.check_value(key_lower, value)
                self._data[key_lower] = value

        elif isinstance(key, tuple):
            if (not len(key) == 2
                    or not isinstance(key[0], six.string_types) or not isinstance(key[1], int)):
                raise TypeError("{} is not a tuple(str, int) "
                                "with length 2 for object {}".format(str(key),
                                                                     self.schema['pyname']))
            key_name = key[0].lower()
            if key_name not in self.schema['extensible-fields']:
                raise KeyError("{} is not an extensible field "
                               " name for object {}".format(key[0],
                                                            self.schema['pyname']))
            while len(self._extdata) <= key[1]:
                self._extdata.append([None] * len(self.schema['extensible-fields']))

            ind = list(self.schema['extensible-fields'].keys()).index(key_name)
            value = self.check_value(key_name, value)
            self._extdata[key[1]][ind] = value

        elif isinstance(key, int):
            if key < len(self.schema['fields']):
                field_name = self.schema['fields'].keys()[key]
                self[field_name] = value
            else:
                i = key - len(self.schema['fields'])
                group = int(i / len(self.schema['extensible-fields']))
                item = i % len(self.schema['extensible-fields'])
                field_name = self.schema['extensible-fields'].keys()[item]
                self[(field_name, group)] = value

        else:
            raise TypeError("{} not found in {}".format(key,
                                                        self.schema['pyname']))

    def __getitem__(self, key):
        if isinstance(key, six.string_types):
            key_lower = key.lower()
            if key_lower in self.schema['fields']:
                return self._data[key_lower]
            else:
                raise KeyError("{} is not a field name "
                               "for object {}".format(key,
                                                      self.schema['pyname']))

        elif isinstance(key, tuple):
            if (not len(key) == 2
                    or not isinstance(key[0], six.string_types) or not isinstance(key[1], int)):
                raise TypeError("{} is not a tuple(str, int) "
                                "with length 2 for object {}".format(str(key),
                                                                     self.schema['pyname']))
            key_name = key[0].lower()
            if key_name not in self.schema['extensible-fields']:
                raise KeyError("{} is not an extensible field "
                               " name for object {}".format(key[0],
                                                            self.schema['pyname']))

            if len(self._extdata) < key[1]:
                raise IndexError("Only {} extensible values available, key asks for value {}"
                                 " for object {}".format(len(self._extdata),
                                                         key[1],
                                                         self.schema['pyname']))
            key_pos = list(self.schema['extensible-fields'].keys()).index(key_name)
            return self._extdata[key[1]][key_pos]

        elif isinstance(key, int):
            i = key
            if i < len(self._data):
                return self._data.values()[i]
            else:
                i -= len(self._data)

                if i > len(self._extdata) * len(self.schema['extensible-fields']):
                    fields_count = len(self._data) + len(self._extdata) * len(self.schema['extensible-fields'])
                    raise IndexError("Only {} fields available, key asks for index {}"
                                     " for object {}".format(fields_count,
                                                             key,
                                                             self.schema['pyname']))
                else:
                    group = int(i / len(self.schema['extensible-fields']))
                    item = i % len(self.schema['extensible-fields'])
                    return self._extdata[group][item]

        raise TypeError("{} not found in {}".format(key,
                                                    self.schema['pyname']))

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict

        self.clean()

        for i, key in enumerate(self.schema['fields']):
            if i < len(vals) and len(vals[i]) == 0:
                self[key] = None
            elif i < len(vals):
                self[key] = vals[i]
        i = len(self.schema['fields'])
        if len(self.schema['extensible-fields']) > 0:
            while i < len(vals):
                ext_vals = [None] * len(self.schema['extensible-fields'])
                for j, val in enumerate(vals[i:i + len(self.schema['extensible-fields'])]):
                    if len(val) == 0:
                        val = None
                    ext_vals[j] = val
                self.add_extensible(*ext_vals)
                i += len(self.schema['extensible-fields'])

        self.strict = old_strict

    def check_value(self, name, value):
        """ Validates `value` against schema for field with name `name`

        Args:
            name (str): name of field
            value: the value

        Returns:
            value valid for schema

        Raises:
            ValueError: if value not valid for schema
        """

        schema = self.schema
        lower_name = name.lower()
        if lower_name in schema['fields']:
            field = schema['fields'][lower_name]
        elif lower_name in schema['extensible-fields']:
            field = schema['extensible-fields'][lower_name]
        else:
            if pyidf.validation_level == ValidationLevel.error:
                raise ValueError('No field exists with name in data object`{}`'.format(schema['name']))
            else:
                logger.warn('No field exists with name in data object`{}`'.format(schema['name']))
                return value

        # Only cast values to Python types for validation level no
        if pyidf.validation_level == ValidationLevel.no:
            if value is None:
                return value
            try:
                if field['type'] == "alpha":
                    value = str(value)
                elif field['type'] == "integer":
                    value = int(value)
                elif field['type'] == "real":
                    value = float(value)
                else:
                    value = str(value)
            except (TypeError, ValueError):
                    return value
            return value

        if value is not None:

            # Handle autosize and autocalucalte
            if field['autocalculatable'] and not field['type'] == "alpha":
                try:
                    value_lower = str(value).lower()
                    if value_lower == "autocalculate":
                        return "Autocalculate"

                    if pyidf.validation_level == ValidationLevel.transition and "auto" in value_lower:
                        logger.warn('Accept value {} as "Autocalculate" '
                                    'for field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                        return "Autocalculate"

                except ValueError:
                    # No string
                    pass

            if field['autosizable'] and not field['type'] == "alpha":
                try:
                    value_lower = str(value).lower()
                    if value_lower == "autosize":
                        return "Autosize"

                    if pyidf.validation_level == ValidationLevel.transition and "auto" in value_lower:
                        logger.warn('Accept value {} as "Autosize" '
                                     'for field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                        return "Autosize"
                except ValueError:
                    pass

            # test for parametric vars 
            if (isinstance(value, six.string_types) and not field['type'] == "alpha"
                    and '$' in value):
                return value

            # cast input data to appropriate python datatype
            try:
                if field['type'] == "alpha":
                    value = str(value)
                elif field['type'] == "integer":
                    value = int(value)
                elif field['type'] == "real":
                    value = float(value)
                else:
                    value = str(value)
            except (TypeError, ValueError):
                if pyidf.validation_level == ValidationLevel.no:
                    return value

                alt = ""
                if field['autosizable']:
                    alt = " or \"Autosize\""
                if field['autocalculatable']:
                    alt = " or \"Autocalculate\""

                if field['type'] == "integer":
                    if pyidf.validation_level == ValidationLevel.transition:
                        try:
                            conv_value = int(float(value))
                            logger.warn('Cast float {} to int {}, precision may be lost '
                                         'for field `{}.{}`'.format(value,
                                                                    conv_value,
                                                                    schema['pyname'],
                                                                    field['pyname']))
                            value = conv_value

                        except ValueError:
                            logger.warn('value {} need to be of type {}{} '
                                        'for field `{}.{}`'.format(value,
                                                                   field['type'],
                                                                   alt,
                                                                   schema['pyname'],
                                                                   field['pyname']))
                            return value
                else:

                    if pyidf.validation_level == ValidationLevel.error:
                            raise ValueError('value {} need to be of type {}{} '
                                             'for field `{}.{}`'.format(value,
                                                                        field['type'],
                                                                        alt,
                                                                        schema['pyname'],
                                                                        field['pyname']))
                    else:
                            logger.warn('value {} need to be of type {}{} '
                                        'for field `{}.{}`'.format(value,
                                                                   field['type'],
                                                                   alt,
                                                                   schema['pyname'],
                                                                   field['pyname']))

            # Check min / max for non alpha types
            if field['type'] == "alpha":
                if ',' in value:
                    if not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value should not contain a comma '
                                    'for field `{}.{}`'.format(schema['pyname'],
                                                               field['pyname']))
                    else:
                        raise ValueError('value should not contain a comma '
                                         'for field `{}.{}`'.format(schema['pyname'],
                                                                    field['pyname']))

                if '!' in value:
                    if not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value should not contain a ! '
                                    'for field `{}.{}`'.format(schema['pyname'],
                                                               field['pyname']))
                    else:
                        raise ValueError('value should not contain a ! '
                                         'for field `{}.{}`'.format(schema['pyname'],
                                                                    field['pyname']))
            else:

                if 'minimum' in field and value < field['minimum']:
                    if not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value {} need to be greater or equal {} '
                                    'for field `{}.{}`'.format(value,
                                                               field['minimum'],
                                                               schema['pyname'],
                                                               field['pyname']))
                    else:
                        raise ValueError('value {} need to be greater or equal {} '
                                         'for field `{}.{}`'.format(value,
                                                                    field['minimum'],
                                                                    schema['pyname'],
                                                                    field['pyname']))

                if 'minimum>' in field and value <= field['minimum>']:
                    if not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value {} need to be greater  {} '
                                    'for field `{}.{}`'.format(value,
                                                               field['minimum>'],
                                                               schema['pyname'],
                                                               field['pyname']))
                    else:
                        raise ValueError('value {} need to be greater  {} '
                                         'for field `{}.{}`'.format(value,
                                                                    field['minimum>'],
                                                                    schema['pyname'],
                                                                    field['pyname']))

                if 'maximum' in field and value > field['maximum']:
                    if not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value {} need to be smaller or equal  {} '
                                    'for field `{}.{}`'.format(value,
                                                               field['maximum'],
                                                               schema['pyname'],
                                                               field['pyname']))

                    else:
                        raise ValueError('value {} need to be smaller or equal  {} '
                                         'for field `{}.{}`'.format(value,
                                                                    field['maximum'],
                                                                    schema['pyname'],
                                                                    field['pyname']))

                if 'maximum<' in field and value >= field['maximum<']:
                    if not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value {} need to be smaller  {} '
                                    'for field `{}.{}`'.format(value,
                                                               field['maximum<'],
                                                               schema['pyname'],
                                                               field['pyname']))
                    else:
                        raise ValueError('value {} need to be smaller  {} '
                                         'for field `{}.{}`'.format(value,
                                                                    field['maximum<'],
                                                                    schema['pyname'],
                                                                    field['pyname']))
                # Check accepted values for alpha types
            if 'accepted-values' in field:
                vals = {}
                for val in field['accepted-values']:
                    if field['type'] == "alpha":
                        vals[val.lower()] = val
                    else:
                        vals[val] = val

                if field['type'] == "alpha":
                    value_lower = value.lower()
                else:
                    value_lower = value

                if value_lower not in vals:
                    found = False
                    if pyidf.validation_level == ValidationLevel.transition:
                        for key in vals:
                            if key in value_lower or value_lower in key:
                                value = vals[key]
                                found = True
                                break
                        if not found:
                            transition_vals = []
                            value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                            for key in vals:
                                key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                                if key_stripped == value_stripped:
                                    value_lower = key
                                    transition_vals.append(vals[key])
                                    found = True
                            if len(transition_vals) > 1:
                                trans = ", ".join(transition_vals)
                                raise ValueError('value {} is not an accepted value for '
                                                 'field `{}.{}`, multiple accepted values '
                                                 'match: {}'.format(value,
                                                                    schema['pyname'],
                                                                    field['pyname'],
                                                                    trans))
                            elif len(transition_vals) == 1:
                                value = transition_vals[0]
                                logger.warn('change value {} to accepted value {} for '
                                            'field `{}.{}`'.format(value,
                                                                   vals[value_lower],
                                                                   schema['pyname'],
                                                                   field['pyname']))

                    if not found and pyidf.validation_level == ValidationLevel.error:
                        raise ValueError('value {} is not an accepted value for '
                                         'field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                    elif not found and not pyidf.validation_level == ValidationLevel.error:
                        logger.warn('value {} is not an accepted value for '
                                    'field `{}.{}`'.format(value,
                                                           schema['pyname'],
                                                           field['pyname']))

        # value is None
        else:

            # Replace None values for required fields with default values
            if field['required-field'] and 'default' in field:
                if pyidf.validation_level == ValidationLevel.warn:
                    logger.warn('Value is None for required field `{}.{}` '
                                'with default value {}'.format(schema['pyname'],
                                                               field['pyname'],
                                                               field['default']))
                elif pyidf.validation_level == ValidationLevel.error:
                    raise ValueError('Value is None for required field `{}.{}` '
                                     'with default value {}'.format(schema['pyname'],
                                                                    field['pyname'],
                                                                    field['default']))
                elif pyidf.validation_level == ValidationLevel.transition:
                    key = field['name'].lower()
                    if (key in self.schema['fields'] and
                            list(self.schema['fields'].keys()).index(key) < self.schema['min-fields']):
                        logger.warn('Replacing None value for required field `{}.{}` '
                                    'with default value {}'.format(schema['pyname'],
                                                                   field['pyname'],
                                                                   field['default']))
                        value = field['default']

        return value

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
        for key, field in self.schema['fields'].iteritems():
            if field['required-field'] and self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field {}.{} is None".format(self.schema['pyname'],
                                                                           field['pyname']))
                else:
                    logger.warn("Required field {}.{} is None".format(self.schema['pyname'],
                                                                      field['pyname']))

        out_fields = len(self.export(validate=False))
        has_minfields = out_fields >= self.schema['min-fields']
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for {}: {} / {}".format(self.schema['pyname'],
                                                                            out_fields,
                                                                            self.schema['min-fields']))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for {}: {} / {}".format(self.schema['pyname'],
                                                                       out_fields,
                                                                       self.schema['min-fields']))
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

    def export(self, validate=True):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._extdata:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data)
        else:
            maxel = 0
            for i, key in reversed(list(enumerate(self._data.keys()))):
                if self._data[key] is not None:
                    maxel = i + 1
                    break

        maxel = max(maxel, self.schema['min-fields'])

        for key in list(self.schema['fields'].keys())[0:maxel]:
            field = self.schema['fields'][key]
            if validate:
                value = self.check_value(field['name'], self._data[key])
                self._data[key] = value
            unit = ""
            if 'unit' in field:
                unit = "{"+self._to_str(field['unit'])+"}"
            field_txt = "{} {}".format(field['name'], unit)
            out.append((field_txt, self._to_str(self._data[key])))

        for vals in self._extdata:
            for i, key in enumerate(self.schema['extensible-fields']):
                field = self.schema['extensible-fields'][key]
                if validate:
                    value = self.check_value(field['name'], vals[i])
                    vals[i] = value
                unit = ""
                if 'unit' in field:
                    unit = self._to_str(field['unit'])
                field_txt = "{} {}".format(field['name'], unit)
                out.append((field_txt, self._to_str(vals[i])))
        return out

    def extensible_field_index(self, name):
        return list(self.schema['extensible-fields'].keys()).index(name.lower())

    def __str__(self):
        out = self.export(validate=False)
        string = ",".join([self.schema['name']] + [o[1] for o in out])
        if len(string) > 77:
            string = string[:77] + "..."
        return string

    def __iter__(self):
        for val in self._data.values():
            yield val
        for vals in self._extdata:
            for val in vals:
                yield val

    def clean(self):
        """ Deletes all data from dataobject
        """
        for key in self._data:
            self._data[key] = None
        self._extdata = []

    def items(self):
        items = []
        for key, field in self.schema['fields'].iteritems():
            items.append((field['name'], self._data[key]))
        for j, vals in enumerate(self._extdata):
            for i, key in enumerate(self.schema['extensible-fields']):
                field = self.schema['extensible-fields'][key]
                items.append(((field['name'], j), vals[i]))
        return items

    def __len__(self):
        return len(self._data) + len(self._extdata) * len(self.schema['extensible-fields'])


class DONames:
    {%- for obj in objs %}
    {{ obj.class_name }} = "{{ obj.internal_name }}"
    {%- endfor %}
