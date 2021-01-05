import pytest
import warplane.controls as controls
import warplane.device as device


@pytest.fixture()
def audio_device():
    ad = device.AudioDevice(
        name="my_device",
        inputs=[0, 1],
        outputs=[0, 1],
        controls={
            controls.BinarySwitch("my_switch"),
            controls.DiscreteDial(
                "my_discrete_dial", min_val=0, max_val=20, step=0.5
            ),
            controls.AnalogueDial(
                "analogue_dial",
                min_val=-50.0,
                max_val=50.0,
                default_setting=0.0,
            ),
            controls.StateSelector(
                "effect_selector",
                states={"clean", "distorted", "echo", "reverb"},
            ),
        },
    )
    yield ad
    del ad


class TestAudioDevice:
    def test_inputs_and_outputs(self):
        ad = device.AudioDevice("my fancy box", inputs=[0, 1], outputs=[4, 5])
        assert ad.inputs == {0: "input_0", 1: "input_1"}
        ad2 = device.AudioDevice("my fancy box 2", inputs=5, outputs=8)
        assert len(ad2.inputs) == 5 and len(ad2.outputs) == 8

    def test_controls(self, audio_device):
        for c in audio_device.controls:
            assert isinstance(c, controls.DeviceControl)
        # use control methods from device object
        c = audio_device.get_control("my_switch")
        c.toggle()
        c2 = audio_device.get_control("analogue_dial")
        c2.setting = 14.1
        with pytest.raises(device.ControlNotFound):
            audio_device.get_control("not there")

    def test_add_control(self, audio_device):
        class C(controls.DeviceControl):
            pass

        c = C(name="blah")
        audio_device.add_control(c)
        audio_device.get_control("blah")
        with pytest.raises(device.DuplicateControls):
            audio_device.add_control(C("my_switch"))
        with pytest.raises(device.InvalidControl):
            audio_device.add_control("fork")

    def test_remove_control(self, audio_device):
        audio_device.remove_control("my_switch")
        assert "my_switch" not in audio_device.control_dict
        with pytest.raises(device.ControlNotFound):
            audio_device.remove_control("fork")

    def test_json(self, audio_device):
        assert all(
            c.json in audio_device.json["controls"]
            for c in audio_device.controls
        )
