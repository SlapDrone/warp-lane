"""
audio_interface.py

Provides methods for identifying and using connected audio interfaces (audio input/outputs)
"""
from typing import Any, Dict, List, Optional

import soundcard as sc

# --- Exceptions


class NoInputInterfaces(Exception):
    def __init__(self, message="No input interfaces detected!"):
        super().__init__(message)


class NoOutputInterfaces(Exception):
    def __init__(self, message="No output interfaces detected!"):
        super().__init__(message)


class OutputInterfaceNotFound(Exception):
    def __init__(
        self, device, message="Selected output interface {device} not found!"
    ):
        self.device = device
        self.message = message
        super().__init__(self.message.format(device=self.device))


class InputInterfaceNotFound(Exception):
    def __init__(
        self, device, message="Selected input interface {device} not found!"
    ):
        self.device = device
        self.message = message
        super().__init__(self.message.format(device=self.device))


# --- Find and acquire objects allowing control over connected audio interfaces


def get_output_interfaces() -> List[Any]:
    """
    Returns a list of audio output devices connected to the computer.

    These are currently _Speaker objects provided by SoundCard which give a
    unified wrapper for underlying OS-dependent audio libraries such as
    PulseAudio on Linux.
    """
    return sc.all_speakers()


def get_input_interfaces() -> List[Any]:
    """
    Returns a list of audio input devices connected to the computer.

    These are currently _Microphone objects provided by SoundCard which give a
    unified wrapper for underlying OS-dependent audio libraries such as
    PulseAudio on Linux.
    """
    return sc.all_microphones()


def get_interface_metadata(
    device, attrs: List[str] = ["name", "channels", "id"]
) -> Dict[str, Any]:
    """
    Returns a dictionary of a select subset of the attributes of a connected
    input or output device.
    """
    return {a: getattr(device, a) for a in attrs}


def display_interfaces(
    devices: List[Any],
    display_attrs: List[str] = ["name", "channels"],
    tag: Optional[str] = None,
):
    """
    Prints an overview of the selected devices' properties.
    """
    for d in devices:
        print("-" * 80)
        print(f"| {tag + ' ' if tag else ''}Device: {d}")
        print("-" * 80)
        attrs = get_interface_metadata(d)
        for a in display_attrs:
            print(f"| {a}: {attrs[a]}")
        print("-" * 80)
        print()


def display_input_interfaces(attrs: List[str] = ["name", "channels", "id"]):
    """
    Identifies all connected audio input devices and prints an overview
    of their properties.
    """
    devices = get_input_interfaces()
    if not devices:
        raise NoInputInterfaces
    display_interfaces(devices, display_attrs=attrs, tag="Input")


def display_output_interfaces(attrs: List[str] = ["name", "channels", "id"]):
    """
    Identifies all connected audio output devices and prints an overview
    of their properties.
    """
    devices = get_output_interfaces()
    if not devices:
        raise NoOutputInterfaces
    display_interfaces(devices, display_attrs=attrs, tag="Output")


def get_input_interface(device_name: str):
    """
    Gets the input device object matching the provided name.
    """
    try:
        return sc.get_microphone(device_name)
    except IndexError as ie:
        raise InputInterfaceNotFound(device_name) from ie


def get_output_interface(device_name: str):
    """
    Gets the output device object matching the provided name.
    """
    try:
        return sc.get_speaker(device_name)
    except IndexError as ie:
        raise OutputInterfaceNotFound(device_name) from ie
