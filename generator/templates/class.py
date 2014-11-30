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

    def __init__(self):
        """ Init data dictionary object for IDD  `{{ obj.internal_name }}`
        """
        self._data = OrderedDict()
    {%- for field in obj.fields %}
        self._data["{{ field.internal_name }}"] = None
    {%- endfor %}

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        {%- for field in obj.fields %}
        if len(vals[i]) == 0:
            self.{{field.field_name}} = None
        else:
            self.{{field.field_name}} = vals[i]
        i += 1
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
    def {{field.field_name}}(self, value={%if field.attributes.default and not field.attributes.pytype == "str" %}{{field.attributes.default}} {% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %}):
        """  Corresponds to IDD Field `{{field.field_name}}`

        {%- for comment in field.attributes.note %}
        {{comment}}
        {%- endfor %}

        Args:
            value ({{ field.attributes.pytype }}): value for IDD Field `{{field.field_name}}`
                {%- if field.attributes.type == "choice" %}
                Accepted values are:
                    {%- for k in field.attributes.key %}
                      - {{ k }}
                    {%- endfor %}
                    {%- endif %}
                {%- if field.attributes.units %}
                Unit: {{ field.attributes.units }}
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
        {%- endif %}
            try:
                value = {{ field.attributes.pytype }}(value)
            except:
                raise ValueError('value {} need to be of type {{ field.attributes.pytype }} '
                                 'for field `{{field.field_name}}`'.format(value))
            {%- if field.attributes.pytype == "str" %}
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
            vals = set()
            {%- for k in field.attributes.key %}
            {%- if field.attributes.pytype == "str" %}
            vals.add("{{k}}")
            {%- else %}
            vals.add({{k}})
            {%- endif %}
            {%- endfor %}
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `{{field.field_name}}`'.format(value))
            {%- endif %}

        self._data["{{ field.internal_name }}"] = value
    {%- endfor %}

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

    def __str__(self):
        out = []
        {%- for field in obj.fields %}
        out.append(self._to_str(self.{{field.field_name}}))
        {%- endfor %}
        return ",".join(out)
