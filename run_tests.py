import os
import unittest

from utils.appium_utils import get_platform_config

# Get the platform from an environment variable
platform = os.environ.get('PLATFORM', 'android')

# Load the platform-specific configuration file
platform_config = get_platform_config(platform)

# Set up the test cases
if platform == 'android':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests/android', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
elif platform == 'ios':
    # TODO: Set up test cases for iOS platform
    pass
else:
    raise ValueError(f"Invalid platform specified: {platform}")

# Run the tests
try:
    runner.run(test_suite)
except:
    raise Exception('Ooops')
