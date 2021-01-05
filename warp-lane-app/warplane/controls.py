"""
controls.py

Provides basic classes which represent the individual controls of an audio device.
"""
import abc
from typing import Any, List, Optional, Set, Tuple, Union

import numpy as np

# --- Exceptions


class InvalidSetting(Exception):
    """
    Exception to be raised when a user specifies an invalid setting for a control.
    """

    def __init__(
        self,
        setting,
        valid_settings,
        message="Setting {setting} invalid: valid choices are {valid_settings}",
    ):
        super().__init__(
            message.format(setting=setting, valid_settings=valid_settings)
        )


class DuplicateStates(Exception):
    def __init__(self, states, msg="Duplicate states found in: {states}"):
        super().__init__(msg.format(states=states))


class Descriptor:
    """
    Implements minimal descriptor protocol.
    """

    def __init__(self, name=None, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ControlSpecification(Descriptor):
    """
    Descriptor for marking an attribute of a DeviceControl as an
    essential specification necessary to minimally represent a
    device.
    """

    def __set__(self, instance, value):
        instance._control_specifications.append(self.name)
        super(ControlSpecification, self).__set__(instance, value)


def controlspecs(*specs: str):
    """
    Class decorator for DeviceControl to mark attributes which collectively
    are necessary and sufficient to reconstruct a device's capabilities and
    discard implementation details or state.

    Parameters
    ----------
    specs :
        A tuple of string valued attribute names which are to be marked with
        ControlSpecification. These dynamically build a minimal control json
        representation.
    """

    def decorate(cls):
        for s in specs:
            setattr(cls, s, ControlSpecification(name=s))
        return cls

    return decorate


@controlspecs("name")
class DeviceControl:
    """
    Base class for generic controls for generic audio devices.

    Parameters
    ----------
    name :
        A string name to give this control e.g. "fancy knob 2".

    Attributes
    ----------
    controls :
        A set tracking subclasses of DeviceControl
    """

    controls: Optional[Any] = set()

    def __init__(self, name: str):
        self._control_specifications: List[str] = []
        self.name = name
        # anticipate essential specifications which will be built into json representation
        # of device controls
        self.controls.add(type(self))  # self.__class__)

    @property
    def json(self):
        _j = {s: getattr(self, s) for s in self._control_specifications}
        _j["class"] = self.__class__.__name__
        return _j


class BinarySwitch(DeviceControl):
    """
    Simple representation of a boolean on/off switch.

    Parameters
    ----------
    name :
        A string name to give this switch e.g. "power".
    """

    def __init__(self, name, on: bool = False):
        super(BinarySwitch, self).__init__(name=name)
        self._on = on

    @property
    def on(self) -> bool:
        return self._on

    def toggle(self):
        self._on = not self._on

    def __repr__(self) -> str:
        return f"Switch(name={self.name}, on={self.on})"


@controlspecs("min_val", "max_val")
class BaseDial(DeviceControl, metaclass=abc.ABCMeta):
    """
    Base class for a dial component.
    """

    @abc.abstractmethod
    def __init__(
        self,
        name: str,
        min_val: Union[int, float] = 0,
        max_val: Union[int, float] = 10,
    ):
        super(BaseDial, self).__init__(name=name)
        self.min_val = min_val
        self.max_val = max_val


@controlspecs("step")
class DiscreteDial(BaseDial):
    """
    Simple class representing a dial with settings at discrete intervals.

    Parameters
    ----------
    name :
        The name allocated to this dial.
    min_val :
        The lowest allowed setting.
    max_val :
        The highest allowed setting.
    step :
        The discrete step size between settings on the dial.
    setting :
        The current setting if any.
    default_setting :
        The default setting if any. If not specified, takes the value of min_val.

    Attributes
    ----------
    name :
        The name allocated to this dial.
    min_val :
        The lowest allowed setting.
    max_val :
        The highest allowed setting.
    step :
        The discrete step size between settings on the dial.
    setting :
        The current setting if any.
    default_setting :
        The default setting if any. If not specified, takes the value of min_val.
    valid_settings: :obj:`np.ndarray` of :obj:`int` or :obj:`float`
        An array containing all valid settings (multiples of step) between min_val and max_val.
    """

    def __init__(
        self,
        name: str,
        min_val: Union[int, float] = 0,
        max_val: Union[int, float] = 10,
        step: Union[int, float] = 1,
        setting: Optional[Union[int, float]] = None,
        default_setting: Optional[Union[int, float]] = None,
    ):
        super(DiscreteDial, self).__init__(
            name=name, min_val=min_val, max_val=max_val
        )
        self.step = step
        self.valid_settings = np.arange(
            self.min_val, self.max_val + 1, self.step
        )
        self.default_setting = (
            self.min_val if not default_setting else default_setting
        )
        self.setting = self.default_setting if not setting else setting

    @property
    def setting(self) -> Union[int, float]:
        return self._setting

    @setting.setter
    def setting(self, value: Union[int, float]):
        if value not in self.valid_settings:
            raise InvalidSetting(value, set(self.valid_settings))
        self._setting = value

    def up(self):
        """
        Increments the setting by one step.
        """
        self.setting += self.step

    def down(self):
        """
        Decrements the setting by one step.
        """
        self.setting -= self.step

    def __repr__(self) -> str:
        return (
            f"DiscreteDial(name={self.name}, min_val={self.min_val}, "
            f"max_val={self.max_val}, step={self.step}, setting={self.setting})"
        )


class AnalogueDial(BaseDial):
    """
    Simple class representing a dial with a continuous setting.

    Parameters
    ----------
    name :
        The name allocated to this dial.
    min_val :
        The lowest allowed setting.
    max_val :
        The highest allowed setting.
    setting :
        The current setting if any.
    default_setting :
        The default setting if any. If not specified, takes the value of min_val.

    Attributes
    ----------
    name :
        The name allocated to this dial.
    min_val :
        The lowest allowed setting.
    max_val :
        The highest allowed setting.
    setting :
        The current setting if any.
    default_setting :
        The default setting if any. If not specified, takes the value of min_val.
    """

    def __init__(
        self,
        name: str,
        min_val: Union[int, float] = 0,
        max_val: Union[int, float] = 10,
        setting: Union[int, float] = None,
        default_setting: Optional[Union[int, float]] = None,
    ):
        super(AnalogueDial, self).__init__(
            name=name, min_val=min_val, max_val=max_val
        )
        self.default_setting = (
            self.min_val if not default_setting else default_setting
        )
        self.setting = self.default_setting if not setting else setting

    @property
    def setting(self) -> Union[int, float]:
        return self._setting

    @setting.setter
    def setting(self, value: Union[float, int]):
        if not (value >= self.min_val and value <= self.max_val):
            raise InvalidSetting(value, f"in [{self.min_val}, {self.max_val}]")
        self._setting = value

    def __repr__(self) -> str:
        return (
            f"AnalogueDial(name={self.name}, min_val={self.min_val}, "
            f"max_val={self.max_val}, setting={self.setting})"
        )


@controlspecs("states")
class StateSelector(DeviceControl):
    def __init__(
        self,
        name: str,
        states: Union[List[str], Tuple[str], Set[str]],
        state: Optional[str] = None,
        default_state: Optional[str] = None,
    ):
        super(StateSelector, self).__init__(name=name)
        self.states = tuple(states)
        if len(self.states) != len(set(self.states)):
            raise DuplicateStates(self.states)
        self.default_state = default_state if default_state else self.states[0]
        self.state = self.default_state if not state else state

    def state_index(self, value) -> int:
        return np.where(np.array(self.states) == value)[0][0]

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value):
        if value not in self.states:
            raise InvalidSetting(value, self.states)
        self._state = value

    @property
    def current_state_index(self) -> int:
        return self.state_index(self.state)

    def next_state(self):
        self.state = self.states[self.current_state_index + 1]

    def prev_state(self):
        self.state = self.states[self.current_state_index - 1]

    def __repr__(self):
        return (
            f"Selector(name={self.name}, state='{self.state}', states={self.states}, "
            f"default_state='{self.default_state}')"
        )
