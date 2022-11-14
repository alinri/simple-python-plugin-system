from abc import ABC, abstractmethod

class PlugIn(ABC):
    def __init__(self, name: str, version: str, auther: str,) -> None:
        self.name = name
        self.version = version
        self.auther = auther
    
    @abstractmethod
    def process_text(text: str) -> str:
        raise NotImplementedError