""" Data objects in group "{{ group }}"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())

{% for source in sources %}

{{ source }}

{% endfor %}