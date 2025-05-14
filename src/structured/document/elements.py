from __future__ import annotations
import abc
import enum

class ElementType(enum.StrEnum):
    DOCUMENT = "document"
    TEXT = "text"
    IMAGE = "image"
    PARAGRAPH = "paragraph"
    TABLE = "table"
    LIST = "list"
    HEADER = "header"
    FOOTER = "footer"
    TOC = "table of contents"
    PAGE_BREAK = "page break"
    LINK = "link"
    SECTION = "section"

class Element(abc.ABC):
    text: str
    type: ElementType
    children: list[Element]
    parent: Element | None

    def __str__(self):
        return self.text
    
    def __repr__(self):
        return f"{self.type}: {self.text}"