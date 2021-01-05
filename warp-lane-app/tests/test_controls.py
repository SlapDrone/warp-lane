import pytest
import warplane.controls as controls


def test_control_specification():
    """
    The ControlSpecifcation descriptor should provide a
    _control_specifications attribute to any DeviceControl
    subclass.
    """

    class D(controls.DeviceControl):
        a = controls.ControlSpecification("a")
        b = controls.ControlSpecification("b")

        def __init__(self, name, a):
            super(D, self).__init__(name=name)
            self.a = a
            self.b = "test"

    d = D("device", 5)
    assert hasattr(d, "_control_specifications")
    assert d._control_specifications == ["name", "a", "b"]
    assert isinstance(D.a, controls.ControlSpecification)


def test_controlspecs():
    """
    The controlspecs class decorator should pre-declare attributes using
    the ControlSpefication descriptor.
    """

    @controls.controlspecs("a")
    class D(controls.DeviceControl):
        def __init__(self, name):
            super(D, self).__init__(name=name)
            self.a = 5
            self.b = "test"

    d = D("device")
    assert d._control_specifications == ["name", "a"]


@pytest.fixture()
def device_control():
    """
    A dummy DeviceControl subclass with one ControlSpecification attribute
    and one other attribute.
    """

    @controls.controlspecs("param")
    class MyControl(controls.DeviceControl):
        def __init__(self, name, param, other_param):
            super(MyControl, self).__init__(name=name)
            self.param = param
            self.other_param = other_param

    mc = MyControl(name="my_control", param=10, other_param="something")
    yield mc
    del mc


class TestDeviceControl:
    """
    DeviceControl objects should have a json dict of their class name along
    with their specific instance name and any ControlSpecification attributes.
    """

    def test_json(self, device_control):
        expected = {"name": "my_control", "param": 10, "class": "MyControl"}
        assert device_control.json == expected


class TestBinarySwitch:
    """
    These should go on and off.
    """

    def test_toggle(self):
        b = controls.BinarySwitch("A switch", on=False)
        b.toggle()
        assert b.on
        b.toggle()
        assert not b.on


class TestBaseDial:
    """
    BaseDial should be abstract
    """

    def test_abstract(self):
        with pytest.raises(TypeError):
            controls.BaseDial("dial_1", 0, 10)


@pytest.fixture()
def discrete_dial():
    """
    A simple DiscreteDial fixture.
    """
    dd = controls.DiscreteDial("mydial", 0, 10, step=1, setting=3)
    yield dd
    del dd


class TestDiscreteDial:
    def test_setting(self, discrete_dial):
        """
        Settings should not be possible outside min and max values
        """
        discrete_dial.setting = 5
        with pytest.raises(controls.InvalidSetting):
            discrete_dial.setting = 11

    def test_up_down(self, discrete_dial):
        """
        Up and down should increment and decrement but respect min/max boundaries.
        """
        discrete_dial.up()
        assert discrete_dial.setting == 4
        discrete_dial.down()
        assert discrete_dial.setting == 3
        with pytest.raises(controls.InvalidSetting):
            for _ in range(10):
                discrete_dial.up()

    def test_invalid(self, discrete_dial):
        """
        Shouldn't be able to instantiate a dial with setting out of range
        """
        with pytest.raises(controls.InvalidSetting):
            controls.DiscreteDial("d", 0, 10, 1, 11)
            discrete_dial.setting = "some string"

    def test_step(self):
        """
        Float steps should be possible and respect up/down.
        """
        dd = controls.DiscreteDial("d", 1, 10, 0.5)
        dd.up()
        assert dd.setting == 1.5
        dd.down()
        assert dd.setting == 1.0


@pytest.fixture()
def analogue_dial():
    ad = controls.AnalogueDial("my_analog_dial", 0.0, 2000.0, 550.0)
    yield ad
    del ad


class TestAnalogueDial:
    def test_setting(self, analogue_dial):
        analogue_dial.setting = 0.0
        analogue_dial.setting = 409.2
        with pytest.raises(controls.InvalidSetting):
            analogue_dial.setting = 2001.034

    def test_invalid(self, analogue_dial):
        with pytest.raises(TypeError):
            controls.AnalogueDial("my_dial", 0.3, "blah", "blork")
            analogue_dial.setting = "a string where it shouldn't be "


@pytest.fixture()
def state_selector():
    ss = controls.StateSelector("my_selector", states=["a", "b", "c"])
    yield ss
    del ss


class TestStateSelector:
    def test_current_state_index(self, state_selector):
        assert state_selector.current_state_index == 0
        state_selector.next_state()
        assert state_selector.current_state_index == 1
        ss2 = controls.StateSelector("ss2", states=list("abc"), state="b")
        assert ss2.current_state_index == 1
        ss3 = controls.StateSelector(
            "ss3", states=list("abc"), default_state="c"
        )
        assert ss3.current_state_index == 2

    def test_set_state(self, state_selector):
        state_selector.state = "b"
        with pytest.raises(controls.InvalidSetting):
            state_selector.state = "d"

    def test_invalid(self):
        with pytest.raises(controls.InvalidSetting):
            controls.StateSelector("blah", states=list("abc"), state="d")
