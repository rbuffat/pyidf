class DataObject:
    {%- for obj in objs %}
    {{ obj.class_name }} = "{{ obj.internal_name }}"
    {%- endfor %}
