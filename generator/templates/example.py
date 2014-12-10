import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
{%- for imp in imports %}
from {{ imp[0] }} import {{ imp[1]}}
{%- endfor %}

idf_file_path = r"Exercise1A.idf"


if __name__ == '__main__':

    logging.info("start")
    pyidf.validation_level = ValidationLevel.transition
    idf = IDF()
    {%- for obj in objs %}
    {% set outer_loop = loop %}
    obj{{loop.index}} = {{obj.class}}()
    {%- for field in obj['fields'] %}
    obj{{outer_loop.index}}.{{field[0]}} = {{ field[1] }} 
    {%- endfor %}
    
    {%- for ext in obj['extensible-fields'] %}
    {%- if ext|count > 0 %}
    obj{{outer_loop.index}}.add_extensible({{ext}})
    {%- endif %}
    {%- endfor %}
    idf.add(obj{{outer_loop.index}})
    {% endfor %}

    idf.save(idf_file_path)
