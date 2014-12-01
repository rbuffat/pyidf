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

    def __init__(self):
        """ Init data dictionary object for IDD  `{{ obj.internal_name }}`
        """
        self._data = OrderedDict()
    {%- for field in obj.fields %}
        self._data["{{ field.internal_name }}"] = None
    {%- endfor %}
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        {%- for field in obj.fields %}
        if len(vals[i]) == 0:
            self.{{field.field_name}} = None
        else:
            self.{{field.field_name}} = vals[i]
        i += 1
        if i >= len(vals):
            return
        {%- endfor %}

    {%- for field in obj.fields %}

    @property
    def {{field.field_name}}(self):
        """Get {{ field.field_name }}

        Returns:
            {{ field.attributes.pytype }}: the value of `{{field.field_name}}` or None if not set
        """
        return self._data["{{ field.internal_name }}"]

    @{{field.field_name}}.setter
    def {{field.field_name}}(self, value={%- if field.attributes.default and not field.attributes.pytype == "str" %}{{ field.attributes.default}} {% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %}):
        """  Corresponds to IDD Field `{{field.internal_name}}`

        {%- for comment in field.attributes.note %}
        {{comment}}
        {%- endfor %}
        
        {{ field.attributes }}

        Args:
            value ({{ field.attributes.pytype }} {%- if field.attributes.autocalculatable %} or "Autocalculate" {%- endif %}): value for IDD Field `{{field.internal_name}}`
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
            except ValueError:
                pass

            {%- endif %}
            try:
                value = {{ field.attributes.pytype }}(value)
            except ValueError:
                raise ValueError('value {} need to be of type {{ field.attributes.pytype }} '
                                 'for field `{{field.field_name}}`'.format(value))
            {%- if field.attributes.pytype == "str" %}
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `{{field.field_name}}`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.minimum %}
            if value < {{ field.attributes.minimum }}:
                raise ValueError('value need to be greater or equal {{ field.attributes.minimum }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['minimum>'] %}
            if value <= {{ field.attributes['minimum>'] }}:
                raise ValueError('value need to be greater {{ field.attributes["minimum>"] }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.maximum %}
            if value > {{ field.attributes.maximum }}:
                raise ValueError('value need to be smaller {{ field.attributes.maximum }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['maximum<'] %}
            if value >= {{ field.attributes['maximum<'] }}:
                raise ValueError('value need to be smaller {{ field.attributes["maximum<"] }} '
                                 'for field `{{field.field_name}}`')
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
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `{{field.field_name}}`'.format(value))
            value = vals[value_lower]
            {%- endif %}
        {%- endif %}
        self._data["{{ field.internal_name }}"] = value
    {%- endfor %}

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])
