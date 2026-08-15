class Region():
    """
    Represents a region which snipp can route users to or be routed.
    """
    def __init__(self, json: dict) -> None:
        self.region: str = json["region"]
        """
        The region of it's region
        """
        self.country: str = json["country"]
        """
        The country of it's region
        """
        self.label: str = json["label"]
        """
        The label of it's region
        """