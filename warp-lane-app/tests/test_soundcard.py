# import pytest
# import warplane.config as cfg
import warplane.soundcard as sc


def test_get_output_interfaces():
    outputs = sc.get_output_interfaces()
    assert outputs


def test_get_input_interfaces():
    inputs = sc.get_input_interfaces()
    assert inputs


def test_get_interface_metadata():
    for dev in sc.get_output_interfaces():
        assert all(
            k in sc.get_interface_metadata(dev)
            for k in ("name", "channels", "id")
        )
    for dev in sc.get_input_interfaces():
        assert all(
            k in sc.get_interface_metadata(dev)
            for k in ("name", "channels", "id")
        )


def test_get_input_interface():
    inputs = sc.get_input_interfaces()
    sc.get_input_interface(inputs[0].name)


def test_get_output_interface():
    outputs = sc.get_output_interfaces()
    sc.get_output_interface(outputs[0].name)
