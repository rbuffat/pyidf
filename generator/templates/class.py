class {{ obj.class_name }}(object):
    """ Corresponds to IDD object `{{ obj.internal_name }}`

    {%- if obj.attributes.memo  %}
    {%- for memo in obj.attributes.memo %}
        {{ memo }}
    {%- endfor %}
    {%- endif %}
    """
    internal_name = "{{ obj.internal_name }}"
    field_count = {{ obj.fields|count }}
    required_fields = [{{required_fields}}]
    extensible_fields = {{obj.extensible_fields|count}}
    {%- if obj.attributes['format'] %}
    format = {% filter lower %}"{{obj.attributes.format}}"{% endfilter %}
    {%- else %}
    format = None
    {%- endif %}
    {%- if obj.attributes['min-fields'] %}
    min_fields = {{obj.attributes['min-fields']}}
    {%- else %}
    min_fields = 0
    {%- endif %}
    {%- if obj.extensible_fields|count > 0 %}
    extensible_keys = [{{extensible_keys}}]
    {%- else %}
    extensible_keys = []
    {%- endif %}

    def __init__(self):
        """ Init data dictionary object for IDD  `{{ obj.internal_name }}`
        """
        self._data = OrderedDict()
    {%- for field in obj.fields %}
        self._data["{{ field.internal_name }}"] = None
    {%- endfor %}
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
        {%- for field in obj.fields %}
        if i < len(vals) and len(vals[i]) == 0:
            self.{{field.field_name}} = None
        elif i < len(vals):
            self.{{field.field_name}} = vals[i]
        i += 1
        {%- endfor %}

        {%- if obj.extensible_fields|count > 0 %}
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        {%- endif %}

        {%- for field in obj.fields %}
        {%- if field.attributes["required-field"] and field.attributes.default %}
        if not strict and self.{{field.field_name}} is None:
            value = {%- if field.attributes.default and not field.attributes.pytype == "str" %}{{ field.attributes.default}}{% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %}
            self.{{field.field_name}} = value
            logger.warn('No value present for required  field `{{obj.class_name}}.{{field.field_name}}, '
                        'using default value {}`'.format(value))

        elif strict and self.{{field.field_name}} is None:
            raise ValueError('No value present for required field `{{obj.class_name}}.{{field.field_name}}')

        {%- elif field.attributes["required-field"] and not field.attributes.default %}
        if not strict and self.{{field.field_name}} is None:
            logger.warn('No value present for required  field `{{obj.class_name}}.{{field.field_name}}')

        elif strict and self.{{field.field_name}} is None:
            raise ValueError('No value present for required  field `{{obj.class_name}}.{{field.field_name}}')
        {%- endif %}
        {%- endfor %}


        self.strict = old_strict

    {%- for field in obj.fields %}

    @property
    def {{field.field_name}}(self):
        """Get {{ field.field_name }}

        Returns:
            {{ field.attributes.pytype }}: the value of `{{field.field_name}}` or None if not set
        """
        return self._data["{{ field.internal_name }}"]

    @{{field.field_name}}.setter
    def {{field.field_name}}(self, value={%- if field.attributes.default and not field.attributes.pytype == "str" %}{{ field.attributes.default}}{% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %}):
        """  Corresponds to IDD Field `{{field.internal_name}}`

        {%- if field.attributes.deprecated %}
        This field is not really used and will be deleted from the object.
        The required information is gotten internally or
        not needed by the program.
        {%- endif %}

        {%- for comment in field.attributes.note %}
        {{comment}}
        {%- endfor %}

        Args:
            value ({{ field.attributes.pytype }}{%- if field.attributes.autocalculatable %} or "Autocalculate"{%- endif %}{%- if field.attributes.autosizable %} or "Autosize"{%- endif %}): value for IDD Field `{{field.internal_name}}`
                {%- if field.attributes.type == "choice" %}
                Accepted values are:
                    {%- for k in field.attributes.key %}
                      - {{ k }}
                    {%- endfor %}
                    {%- endif %}
                {%- if field.attributes.units %}
                Units: {{ field.attributes.units }}
                {%- endif %}
                {%- if field.attributes['ip-units'] %}
                IP-Units: {{ field.attributes['ip-units'] }}
                {%- endif %}
                {%- if field.attributes['unitsbasedonfield'] %}
                Units are based on field `{{ field.attributes['unitsbasedonfield'] }}`
                {%- endif %}
                {%- if field.attributes.default %}
                Default value: {{ field.attributes.default }}
                {%- endif %}
                {%- if field.attributes.minimum %}
                value >= {{ field.attributes.minimum }}
                {%- endif %}
                {%- if field.attributes['minimum>'] %}
                value > {{ field.attributes['minimum>'] }}
                {%- endif %}
                {%- if field.attributes.maximum %}
                value <= {{ field.attributes.maximum }}
                {%- endif %}
                {%- if field.attributes['maximum<'] %}
                value < {{ field.attributes['maximum<'] }}
                {%- endif %}
                {%- if field.attributes.missing %}
                Missing value: {{ field.attributes.missing }}
                {%- endif %}
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        {%- if field.attributes|length > 0  %}
        if value is not None:
            {%- if field.attributes.autocalculatable and not field.attributes.pytype == "alpha" %}
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["{{ field.internal_name }}"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                    self._data["{{ field.internal_name }}"] = "Autocalculate"
                    return
            except ValueError:
                pass

            {%- endif %}
            {%- if field.attributes.autosizable and not field.attributes.pytype == "alpha" %}
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["{{ field.internal_name }}"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                    self._data["{{ field.internal_name }}"] = "Autosize"
                    return
            except ValueError:
                pass

            {%- endif %}
            try:
                value = {{ field.attributes.pytype }}(value)
            except ValueError:
                {%- if field.attributes.type == "integer" %}
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type {{ field.attributes.pytype }} '
                                         'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                {%- else %}
                raise ValueError('value {} need to be of type {{ field.attributes.pytype }} {%- if field.attributes.autocalculatable %} or "Autocalculate"{%- endif %}{%- if field.attributes.autosizable %} or "Autosize"{%- endif %}'
                                 ' for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                {%- endif %}
            {%- if field.attributes.pytype == "str" %}
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.minimum %}
            if value < {{ field.attributes.minimum }}:
                raise ValueError('value need to be greater or equal {{ field.attributes.minimum }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['minimum>'] %}
            if value <= {{ field.attributes['minimum>'] }}:
                raise ValueError('value need to be greater {{ field.attributes["minimum>"] }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.maximum %}
            if value > {{ field.attributes.maximum }}:
                raise ValueError('value need to be smaller {{ field.attributes.maximum }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['maximum<'] %}
            if value >= {{ field.attributes['maximum<'] }}:
                raise ValueError('value need to be smaller {{ field.attributes["maximum<"] }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.type == "choice" %}
            vals = {}
            {%- for k in field.attributes.key %}
            {%- if field.attributes.pytype == "str" %}
            vals[{% filter lower %}"{{k}}"{% endfilter %}] = "{{k}}"
            {%- else %}
            vals.add({{k}})
            {%- endif %}
            {%- endfor %}
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
                                     'field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `{{obj.class_name}}.{{field.field_name}}`'.format(value, vals[value_lower]))
            value = vals[value_lower]
            {%- endif %}
        {%- endif %}
        self._data["{{ field.internal_name }}"] = value
    {%- endfor %}

    {%- if obj.extensible_fields|count > 0 %}

    def add_extensible(self,
                       {%- for field in obj.extensible_fields %}
                       {{field.field_name}}={%- if field.attributes.default and not field.attributes.pytype == "str" %}{{ field.attributes.default}}{% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %},
                       {%- endfor %}
                       ):
        """ Add values for extensible fields

        Args:
            {%- for field in obj.extensible_fields %}

            {{field.field_name}} ({{ field.attributes.pytype }}{%- if field.attributes.autocalculatable %} or "Autocalculate"{%- endif %}{%- if field.attributes.autosizable %} or "Autosize"{%- endif %}): value for IDD Field `{{field.internal_name}}`
                {%- if field.attributes.type == "choice" %}
                Accepted values are:
                    {%- for k in field.attributes.key %}
                      - {{ k }}
                    {%- endfor %}
                    {%- endif %}
                {%- if field.attributes.units %}
                Units: {{ field.attributes.units }}
                {%- endif %}
                {%- if field.attributes['ip-units'] %}
                IP-Units: {{ field.attributes['ip-units'] }}
                {%- endif %}
                {%- if field.attributes['unitsbasedonfield'] %}
                Units are based on field `{{ field.attributes['unitsbasedonfield'] }}`
                {%- endif %}
                {%- if field.attributes.default %}
                Default value: {{ field.attributes.default }}
                {%- endif %}
                {%- if field.attributes.minimum %}
                value >= {{ field.attributes.minimum }}
                {%- endif %}
                {%- if field.attributes['minimum>'] %}
                value > {{ field.attributes['minimum>'] }}
                {%- endif %}
                {%- if field.attributes.maximum %}
                value <= {{ field.attributes.maximum }}
                {%- endif %}
                {%- if field.attributes['maximum<'] %}
                value < {{ field.attributes['maximum<'] }}
                {%- endif %}
                {%- if field.attributes.missing %}
                Missing value: {{ field.attributes.missing }}
                {%- endif %}
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            {%- endfor %}
        """
        vals = []
        {%- for field in obj.extensible_fields %}
        vals.append(self._check_{{field.field_name}}({{field.field_name}}))
        {%- endfor %}
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    {%- endif %}

    {%- for field in obj.extensible_fields %}

    def _check_{{field.field_name}}(self, value):
        """ Validates falue of field `{{field.internal_name}}`
        """
        {%- if field.attributes|length > 0  %}
        if value is not None:
            {%- if field.attributes.autocalculatable and not field.attributes.pytype == "alpha" %}
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["{{ field.internal_name }}"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                    self._data["{{ field.internal_name }}"] = "Autocalculate"
                    return
            except ValueError:
                pass

            {%- endif %}
            {%- if field.attributes.autosizable and not field.attributes.pytype == "alpha" %}
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["{{ field.internal_name }}"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                    self._data["{{ field.internal_name }}"] = "Autosize"
                    return
            except ValueError:
                pass

            {%- endif %}
            try:
                value = {{ field.attributes.pytype }}(value)
            except ValueError:
                {%- if field.attributes.type == "integer" %}
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type {{ field.attributes.pytype }} '
                                         'for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                {%- else %}
                raise ValueError('value {} need to be of type {{ field.attributes.pytype }} {%- if field.attributes.autocalculatable %} or "Autocalculate"{%- endif %}{%- if field.attributes.autosizable %} or "Autosize"{%- endif %}'
                                 ' for field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                {%- endif %}
            {%- if field.attributes.pytype == "str" %}
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.minimum %}
            if value < {{ field.attributes.minimum }}:
                raise ValueError('value need to be greater or equal {{ field.attributes.minimum }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['minimum>'] %}
            if value <= {{ field.attributes['minimum>'] }}:
                raise ValueError('value need to be greater {{ field.attributes["minimum>"] }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.maximum %}
            if value > {{ field.attributes.maximum }}:
                raise ValueError('value need to be smaller {{ field.attributes.maximum }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['maximum<'] %}
            if value >= {{ field.attributes['maximum<'] }}:
                raise ValueError('value need to be smaller {{ field.attributes["maximum<"] }} '
                                 'for field `{{obj.class_name}}.{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.type == "choice" %}
            vals = {}
            {%- for k in field.attributes.key %}
            {%- if field.attributes.pytype == "str" %}
            vals[{% filter lower %}"{{k}}"{% endfilter %}] = "{{k}}"
            {%- else %}
            vals.add({{k}})
            {%- endif %}
            {%- endfor %}
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
                                     'field `{{obj.class_name}}.{{field.field_name}}`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `{{obj.class_name}}.{{field.field_name}}`'.format(value, vals[value_lower]))
            value = vals[value_lower]
            {%- endif %}
        {%- endif %}
        return value

    {%- endfor %}

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
                    raise ValueError("Required field {{ obj.class_name }}:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field {{ obj.class_name }}:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for {{ obj.class_name }}: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for {{ obj.class_name }}: {} / {}".format(out_fields,
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
            maxel = 0
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                if self._data[key] is not None:
                    maxel = i + 1
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
        out = self.export()
        string = ",".join([self.internal_name] + [o[1] for o in out])
        if len(string) > 77:
            string = string[:77] + "..."
        return string

    def __getitem__(self, val):
        self._data[val]

    def __iter__(self):
        for val in self._data.values():
            yield val

