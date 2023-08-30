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

  def test_sendSms(self):
    phone_num = "+918277598359";
    sms_timeout = 30000

    # get parameter values from test bed
    ffood = self.user_params.get('favorite_food')
    jfood = self.user_params.get('junk_food')


    # invoke sendSms with phone and send message
    self.dut.mbs.setMicrophoneMute(True)
    isMicrophoneMuted = self.dut.mbs.isMicrophoneMute()
    asserts.assert_true(isMicrophoneMuted,"Expected mute but microphone not muted")

    self.dut.mbs.setMicrophoneMute(False)
    isMicrophoneMuted = self.dut.mbs.isMicrophoneMute()
    asserts.assert_false(isMicrophoneMuted,"Expected mute but microphone not muted")

    self.dut.mbs.sendSms(phone_num, jfood)
    self.dut.mbs.sendSms(phone_num, "Send Sms Test")
    self.dut.mbs.sendSms(phone_num, 'Send Sms Test message')

    # Validate if Sms message is recived in 30 secs
    self.dut.mbs.waitForSms(sms_timeout)

  def teardown_class(self):
    self.dut.mbs.makeToast('Class Teardown')

if __name__ == '__main__':
  test_runner.main()