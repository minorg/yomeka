from typing import NamedTuple

from yomeka.classic.omeka_classic_element import OmekaClassicElement
from yomeka.classic.omeka_classic_element_set import OmekaClassicElementSet


class OmekaClassicElementText(NamedTuple):
    element: OmekaClassicElement
    element_set: OmekaClassicElementSet
    html: bool
    text: str
