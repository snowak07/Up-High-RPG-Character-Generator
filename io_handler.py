class IOHandler():
    def input(self, *, min_value=None, max_value=None, accepted_values=None, descriptions=None, prompt="") -> str | int:
        raise NotImplementedError("Subclasses must implement this method")

    def __inputInt(self, min_value, max_value) -> int:
        raise NotImplementedError("Subclasses must implement this method")

    def __inputString(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def output(self, content, file=None) -> None:
        raise NotImplementedError("Subclasses must implement this method")