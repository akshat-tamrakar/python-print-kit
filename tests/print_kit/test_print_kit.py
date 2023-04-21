from print_kit.print_kit import (
    print_success,
    print_colored,
    print_error,
    print_log,
    print_return,
    print_return_info,
)


def test_print_colored(capsys):
    print_colored("Hello, world!", 10)
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
    assert "10" in captured.out


def test_print_error(capsys):
    print_error("Hello, world!", 10)
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
    assert "10" in captured.out


def test_print_log(capsys):
    print_log("Hello, world!", 10)
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
    assert "10" in captured.out


def test_print_success(capsys):
    print_success("Hello, world!", 10)
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
    assert "10" in captured.out


@print_return
def my_function_1(variable):
    return f"hello {variable}"


@print_return_info
def my_function_2(variable):
    return f"hello {variable}"


def test_print_return(capsys):
    output = my_function_1(3)
    captured = capsys.readouterr()
    assert "hello 3" in captured.out
    assert "<- \tmy_function" in captured.out
    assert output == "hello 3"


def test_print_return_info(capsys):
    output = my_function_2(4)
    captured = capsys.readouterr()
    assert "hello 4" in captured.out
    assert "<- \tmy_function" in captured.out
    assert "((4,), {})" in captured.out
    assert output == "hello 4"
