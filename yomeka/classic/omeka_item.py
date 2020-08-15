from datetime import datetime
from typing import NamedTuple, Optional, Tuple

from yomeka.classic.omeka_element_text import OmekaElementText
from yomeka.classic.omeka_item_type import OmekaItemType
from yomeka.classic.omeka_tag import OmekaTag


class OmekaItem(NamedTuple):
    added: datetime
    element_texts: Tuple[OmekaElementText, ...]
    featured: bool
    files_count: int
    id: int
    modified: datetime
    public: bool
    tags: Tuple[OmekaTag, ...]
    url: str
    item_type: Optional[OmekaItemType] = None
    json: Optional[str] = None
