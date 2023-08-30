from mobly import base_test
from mobly import test_runner
from mobly import asserts
from mobly.controllers import android_device

class SendSmsTest(base_test.BaseTestClass):

  def setup_class(self):
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at least one
    # object is created from this.
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    # Start Mobly Bundled Snippets (MBS).
    self.dut.load_snippet('mbs', android_device.MBS_PACKAGE)

  def test_microphone(self):
    # cheking if microphone is muted or not muted
    self.dut.mbs.setMicrophoneMute(True)
    isMicrophoneMuted = self.dut.mbs.isMicrophoneMute()
    asserts.assert_true(isMicrophoneMuted,"Expected mute but microphone not muted")

    self.dut.mbs.setMicrophoneMute(False)
    isMicrophoneMuted = self.dut.mbs.isMicrophoneMute()
    asserts.assert_false(isMicrophoneMuted,"Expected mute but microphone not muted")

  def test_music(self):
    #checking music is active or not
    music=self.dut.mbs.isMusicActive()
    #self.dut.mbs.isMusicActive()
    self.dut.log.info(music)

  def test_volume(self):
    currentmusicvolume=self.dut.mbs.getMusicVolume()
    maxmusicvolume=self.dut.mbs.getMusicMaxVolume()
    self.dut.log.info('maximum volume = %d',maxmusicvolume)
    self.dut.log.info('current volume= %d',currentmusicvolume)
    alaramvolume=self.dut.mbs.getAlarmVolume()
    self.dut.log.info('current Alaram volume = %d',alaramvolume)



  def teardown_class(self):
    self.dut.mbs.makeToast('Class Teardown')

if __name__ == '__main__':
  test_runner.main()