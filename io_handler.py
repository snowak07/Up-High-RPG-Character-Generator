class IOHandler():
    def input(self, *, min_value=None, max_value=None, accepted_values=None, descriptions=None, prompt=""):
        raise NotImplementedError("Subclasses must implement this method")

    def output(self, content, file=None) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def inputInt(self, min_value, max_value) -> int:
        raise NotImplementedError("Subclasses must implement this method")

    def inputString(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")