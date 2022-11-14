from plugin_abstract import PlugIn

class Module(PlugIn):
    def __init__(self) -> None:
        super().__init__('Process y', '0.0.1', "ali")
    
    def process_text(self, text: str) -> str:
        return 'y' + text