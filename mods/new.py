from plugin_abstract import PlugIn

class Times2(PlugIn):
    def __init__(self) -> None:
        super().__init__('Times 2', '0.0.1', "ali")
    
    def process_text(self, text: str) -> str:
        return text * 2
