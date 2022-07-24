from item import Item
class Phone(Item):
    # all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        #Call to super function to have access to all atributes/ methods
        super().__init__(name, price, quantity)
        # Run validation to the received arguments
        
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)