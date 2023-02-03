"""Utils module tests."""

from example_pkg_cloos.utils import print_bar, print_foo


def test_print_bar(capsys):
    """Test print_bar()."""
    print_bar()
    captured = capsys.readouterr()
    assert captured.out == "Bar\n"


def test_print_foo(capsys):
    """Test print_foo()."""
    print_foo()
    captured = capsys.readouterr()
    assert captured.out == "Foo\n"
