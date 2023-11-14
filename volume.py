from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeModule:

    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))

    def set_volume(self, vol):
        self.volume.SetMasterVolumeLevelScalar((vol / 100), None)

    def get_volume(self):
        return int(round(self.volume.GetMasterVolumeLevelScalar() * 100))
    
    def mute(self, boolMute):
        self.volume.SetMute(boolMute, None)