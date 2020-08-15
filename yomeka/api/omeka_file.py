from datetime import datetime
from typing import NamedTuple, Optional, Tuple

from yomeka.api.omeka_element_text import OmekaElementText
from yomeka.api.omeka_file_urls import OmekaFileUrls


class OmekaFile(NamedTuple):
    added: datetime
    authentication: str
    element_texts: Tuple[OmekaElementText, ...]
    file_urls: OmekaFileUrls
    has_derivative_image: bool
    id: int
    item_id: int
    mime_type: str
    modified: datetime
    original_filename: str
    size: int
    stored: bool
    type_os: str
    url: str
    json: Optional[str] = None
