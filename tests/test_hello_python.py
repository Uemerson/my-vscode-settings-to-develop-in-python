from src.hello_python import HelloPython


def test_hello_python():
    hello_python = HelloPython("any_message")
    assert hello_python.hello() is None
