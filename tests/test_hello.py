from src import Hello


def test_write():
    hello: Hello = Hello()
    result: bool = hello.write()

    assert result, 'Print failed'
