from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device
#import sys
#sys.path.append('C:\Users\Sneha.Awaji\Documents\IMS automation\sample_config.yml')

class SendSmsTest(base_test.BaseTestClass):

  def setup_class(self):
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at least one
    # object is created from this.
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    # Start Mobly Bundled Snippets (MBS).
    self.dut.load_snippet('mbs', android_device.MBS_PACKAGE)

  def test_wifi(self):
      #checking the wifi is enabled for 30 secs
      self.dut.mbs.wifiEnable()
      self.dut.mbs.wifiDisable()

  def teardown_class(self):
    self.dut.mbs.makeToast('Class Teardown')

if __name__ == '__main__':
  test_runner.main()