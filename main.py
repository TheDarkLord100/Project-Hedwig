from speech import Speech
from volume import VolumeModule


def main():
    # speakText("Hello world!")
    speechEngine = Speech()
    # speechEngine.greeting()
    volumeModule = VolumeModule()
    volumeModule.set_volume(69)
    speechEngine.speak("Volume set to 50 percent")
    currentVolume = volumeModule.get_volume()
    speechEngine.speak("Current volume is " + str(currentVolume) + " percent")

    return 0

if __name__ == "__main__":
    main()