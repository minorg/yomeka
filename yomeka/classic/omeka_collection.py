from datetime import datetime
from typing import NamedTuple, Optional, Tuple

from yomeka.classic.omeka_element_text import OmekaElementText


class OmekaCollection(NamedTuple):
    added: datetime
    element_texts: Tuple[OmekaElementText, ...]
    featured: bool
    id: int
    items_count: int
    modified: datetime
    public: bool
    url: str
    json: Optional[str] = None
