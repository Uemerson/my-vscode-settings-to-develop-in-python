class Hello:
    __message: str

    def hello(self) -> None:
        pass

    def some_function(self) -> None: ...


class HelloPython(Hello):
    def __init__(self, message):
        self.__message = message

    def hello(self) -> None:
        print(self.__message)


if __name__ == "__main__":
    hello_python = HelloPython("Hello Python ❤")
    hello_python.hello()
    some_string = """
                    Indentation in multiline strings should not be touched.
                    Only actual code should be reindented. """
