class Buffer:
    def __init__(self) -> None:
        self.__buffer = []

    @property
    def buffer(self):
        return self.__buffer

    def add(self, text: str):
        self.__buffer.append(text)
