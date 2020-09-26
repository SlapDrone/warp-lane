import json

import pytest


# example using fixtures
@pytest.fixture(scope="module")  # set up only once
def db():
    print("FIXTURE SETUP")
    db = {"A": ("alice"), "B": ("bob")}
    yield db
    print("FIXTURE TEARDOWN")
    del db


@pytest.mark.parametrize("x1, x2, res", [(1, 1, 2), ("x", "y", "xy")])
def test_dummy(x1, x2, res):
    assert x1 + x2 == res


def test_correct_exc():
    with pytest.raises(ValueError):
        raise ValueError("bla bla")


# pytest built-in fixtures
def test_capsys(capsys):
    print("hello")
    out, err = capsys.readouterr()
    assert "hello" in out


class C:
    """ for monkey patching """

    def do_something(self):
        return 0


def test_monkeypatch(monkeypatch):
    def fake_func(self):
        return 42

    monkeypatch.setattr(C, "do_something", fake_func)
    c = C()
    assert c.do_something() == 42


def read_json(some_file_path):
    with open(some_file_path, "r") as f:
        return json.load(f)


def test_tmpdir(tmpdir):
    "simulate temporary file"
    some_file = tmpdir.join("something.txt")
    some_file.write('{"hello":"world"}')
    result = read_json(str(some_file))
    assert result["hello"] == "world"


@pytest.fixture
def captured_print(capsys):
    print("hello")


def test_fixture_with_fixtures(capsys, captured_print):
    print("more")
    out, err = capsys.readouterr()
    assert out == "hello\nmore\n"


# with fixture
@pytest.mark.parametrize("x1, res", [("A", "alice"), ("B", "bob")])
def test_dummy3(db, res, x1):
    assert db[x1] == res


# --
