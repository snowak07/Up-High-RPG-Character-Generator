class IOHandler():
    def input(self, *, min_value=None, max_value=None, accepted_values=None, descriptions=None, prompt="") -> str | int:
        raise NotImplementedError("Subclasses must implement this method")

    def __inputInt(self, min_value, max_value) -> int:
        raise NotImplementedError("Subclasses must implement this method")

    def __inputString(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    def outputFile(self, content, filename) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def output(self, content) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def saveFile(self, content, filename) -> None:
        '''Save file and return file and file location'''
        file_location = f"generated_characters/{filename}.txt"
        write_file = open(file_location, "w")
        print(content, file=write_file)
        write_file.close()

        return file_location