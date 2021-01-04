"""
device.py

Provides basic classes to represent an individual audio device.
"""
from typing import Dict, List, Optional, Set, Tuple, Union

from warplane.controls import DeviceControl

# --- Exceptions


class InvalidControl(Exception):
    def __init__(
        self,
        control,
        msg: str = "Device control: {control} invalid. Valid options are: {valid_controls}",
    ):
        valid_controls = set(c.__name__ for c in DeviceControl.controls)
        super().__init__(
            msg.format(control=control, valid_controls=valid_controls)
        )


class DuplicateControls(Exception):
    def __init__(self, control, msg="Duplicate control {control} found."):
        super().__init__(msg.format(control=control))


class ControlNotFound(Exception):
    def __init__(self, control, msg="Control {control} not found on device."):
        super().__init__(msg.format(control=control))


# --- main device class


class AudioDevice:
    """
    A simple class representing an audio device as a named collection of I/O channels
    and controls.

    Provides a minimal json representation of itself as a property.

    Parameters
    ----------

    name :
        The name given to the device
    inputs :
        The input channels either as a total number e.g. 6, an iterable of
        numbers e.g. [0, 1, 2], or a mapping {0 : 'left_input', 1 : 'right_input'}
    outputs :
        As with inputs.
    controls:
        A list, tuple or set of DeviceControl objects.
    """

    def __init__(
        self,
        name: str,
        inputs: Union[Dict[int, str], Tuple[int], List[int], Set[int], int],
        outputs: Union[Dict[int, str], Tuple[int], List[int], Set[int], int],
        controls: Optional[
            Union[
                List[DeviceControl],
                Tuple[DeviceControl],
                Set[DeviceControl],
            ]
        ] = None,
    ):
        self.name = name
        self.inputs = (
            inputs
            if isinstance(inputs, dict)
            else self._assign_keys("input", inputs)
        )
        self.outputs = (
            outputs
            if isinstance(outputs, dict)
            else self._assign_keys("output", inputs)
        )
        if not controls:
            controls = set()
        self.controls = set(controls)

    @property
    def controls(self):
        return self._controls

    @controls.setter
    def controls(self, value):
        self._check_controls(value)
        self._controls = value

    def get_control(self, key):
        try:
            return self.control_dict[key]
        except KeyError as e:
            raise ControlNotFound(key) from e

    @property
    def control_dict(self):
        return {c.name: c for c in self.controls}

    def add_control(self, control: DeviceControl):
        cs = self.controls.copy()
        cs.add(control)
        self.controls = cs

    def remove_control(self, control: Union[DeviceControl, str]):
        if isinstance(control, str):
            control = self.get_control(control)
        self.controls.pop(control)

    def _assign_keys(self, prefix, values):
        if isinstance(values, int):
            values = tuple(range(values))
        return {v: f"{prefix}_{v}" for v in values}

    def _check_controls(self, controls):
        names = set()
        for c in controls:
            if not isinstance(c, DeviceControl):
                raise InvalidControl(c)
            if c.name in names:
                raise DuplicateControls(c)
            names.add(c.name)

    def __repr__(self):
        return f"AudioDevice(inputs={self.inputs}, outputs={self.outputs}, controls={self.controls})"

    @property
    def json(self):
        return {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "controls": [c.json for c in self.controls],
        }
