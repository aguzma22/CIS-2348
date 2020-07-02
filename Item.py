class Item:
    def __init__(self, itemId=-1, itemType="", manufacturer="",price=0.0,serviceDate="2020-07-01",condition=""):
        self.itemId=itemId
        self.manufacturer=manufacturer
        self.itemType=itemType
        self.price=price
        self.serviceDate=serviceDate
        self.condition=condition