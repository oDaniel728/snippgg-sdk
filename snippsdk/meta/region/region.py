class Region():
    def __init__(self, json: dict) -> None:
        self.region: str = json["region"]
        self.country: str = json["country"]
        self.label: str = json["label"]