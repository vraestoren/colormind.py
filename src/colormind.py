from requests import Session

class ColorMind:
    def __init__(self) -> None:
        self.api = "http://colormind.io"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
        }
    
    def get_random_color_palette(self, model: str = "default") -> dict:
        data = {
            "model": model
        }
        return self.session.post(
            f"{self.api}/api/", data=data).json()
    
    def get_color_suggestions(
            self, 
            input: list,
            model: str = "default") -> dict:
        data = {
            "input": input,
            "model": model
        }
        return self.session.post(
            f"{self.api}/api/", data=data).json()
    
    def get_models(self) -> dict:
        return self.session.get(f"{self.api}/list/").json()
