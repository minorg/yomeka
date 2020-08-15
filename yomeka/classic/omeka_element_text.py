from typing import NamedTuple

from yomeka.classic.omeka_element import OmekaElement
from yomeka.classic.omeka_element_set import OmekaElementSet


class OmekaElementText(NamedTuple):
    element: OmekaElement
    element_set: OmekaElementSet
    html: bool
    text: str
