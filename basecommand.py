class BaseCommand:
    """
    Base command class. Every command should inherit from this class
    """

    def handle(self) -> None | NotImplementedError :
        """
        Main method for handling command logic
        """
        raise NotImplementedError(
            "This method should be redefined in child class"
        )
