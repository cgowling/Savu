# Copyright 2014 Diamond Light Source Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. module:: test_runner
   :platform: Unix
   :synopsis: Test runner class for easy testing from the command line

.. moduleauthor:: Mark Basham <scientificsoftware@diamond.ac.uk>

"""

import unittest
import logging

from savu.test.framework_test import FrameworkTest

base_class_name = "savu.plugins.plugin"

if __name__ == "__main__":
    import optparse
    import os
    import sys

    usage = "%prog [options] output_directory"
    version = "%prog 0.1"
    parser = optparse.OptionParser(usage=usage, version=version)
    parser.add_option("-p", "--plugins", dest="plugins",
                      help="plugin names, comma separated. e.g "+
                      "/path/to/base/plugin.name.including.packages" +
                      ",savu.core.plugin",
                      default="savu.plugins.median_filter",
                      type='string')
    (options, args) = parser.parse_args()

    if len(args) is not 1:
        print "output path needs to be specified"
        sys.exit(1)

    if not os.path.exists(args[0]):
        print("path to output directory %s does not exist" % args[0]);
        sys.exit(2)

    logging.basicConfig(filename=os.path.join(args[0],"log.log"),
                        filemode='w',
                        format='%(relativeCreated)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.debug("Files all present and correct")

    suite = unittest.TestSuite()
    ft = FrameworkTest('test_pipeline')
    ft.plugin_list = ','.split(options.plugins)
    logging.debug("Plugin list is %s", str(ft.plugin_list))
    ft.temp_dir = args[0]
    suite.addTest(ft)

    logging.debug("Test suite setup, ready to run")

    unittest.TextTestRunner().run(suite)
