class {{ obj.class_name }}(DataObject):
    """ Corresponds to IDD object `{{ obj.internal_name }}`

    {%- if obj.attributes.memo  %}
    {%- for memo in obj.attributes.memo %}
        {{ memo }}
    {%- endfor %}
    {%- endif %}
    """
    _schema = {{ obj.schema }}


    {%- for field in obj.fields %}

    @property
    def {{field.field_name}}(self):
        """field `{{ field.internal_name }}`
        {% for comment in field.attributes.note %}
        |  {{comment}}
        {%- endfor %}
        {%- if field.attributes.deprecated %}
        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.
        {%- endif %}
        {%- if field.attributes.type == "choice" %}
        |  Accepted values are:
            {%- for k in field.attributes.key %}
        |        - {{ k }}
            {%- endfor %}
            {%- endif %}
        {%- if field.attributes.units %}
        |  Units: {{ field.attributes.units }}
        {%- endif %}
        {%- if field.attributes['ip-units'] %}
        |  IP-Units: {{ field.attributes['ip-units'] }}
        {%- endif %}
        {%- if field.attributes['unitsbasedonfield'] %}
        |  Units are based on field `{{ field.attributes['unitsbasedonfield'] }}`
        {%- endif %}
        {%- if field.attributes.default %}
        |  Default value: {{ field.attributes.default }}
        {%- endif %}
        {%- if field.attributes.minimum %}
        |  value >= {{ field.attributes.minimum }}
        {%- endif %}
        {%- if field.attributes['minimum>'] %}
        |  value > {{ field.attributes['minimum>'] }}
        {%- endif %}
        {%- if field.attributes.maximum %}
        |  value <= {{ field.attributes.maximum }}
        {%- endif %}
        {%- if field.attributes['maximum<'] %}
        |  value < {{ field.attributes['maximum<'] }}
        {%- endif %}
        {%- if field.attributes.missing %}
        |  Missing value: {{ field.attributes.missing }}
        {%- endif %}

        Args:
            value ({{ field.attributes.pytype }}{%- if field.attributes.autocalculatable %} or "Autocalculate"{%- endif %}{%- if field.attributes.autosizable %} or "Autosize"{%- endif %}): value for IDD Field `{{field.internal_name}}`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            {{ field.attributes.pytype }} {%- if field.attributes.autocalculatable %} or "Autocalculate"{%- endif %}{%- if field.attributes.autosizable %} or "Autosize"{%- endif %}: the value of `{{field.field_name}}` or None if not set
        """
        return self["{{ field.internal_name }}"]

    @{{field.field_name}}.setter
    def {{field.field_name}}(self, value={%- if field.attributes.default and not field.attributes.pytype == "str" %}{{ field.attributes.default}}{% elif field.attributes.default and (field.attributes.pytype == "str") %}"{{field.attributes.default}}"{% else %}None{% endif %}):
        """  Corresponds to IDD field `{{field.internal_name}}`

        """
        self["{{ field.internal_name }}"] = value
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
        {{field.field_name}} = self.check_value("{{field.internal_name}}", {{field.field_name}})
        vals.append({{field.field_name}})
        {%- endfor %}
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """ Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values
        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)

    {%- endif %}

