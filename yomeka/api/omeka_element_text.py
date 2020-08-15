from typing import NamedTuple

from yomeka.api.omeka_element import OmekaElement
from yomeka.api.omeka_element_set import OmekaElementSet


class OmekaElementText(NamedTuple):
    element: OmekaElement
    element_set: OmekaElementSet
    html: bool
    text: str
