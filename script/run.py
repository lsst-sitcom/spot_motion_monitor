# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

# This script is meant for running the UI during development. It needs to be
# run in a wrapped environment where the PYTHONPATH points to the
# spot_motion_monitor library.

from spot_motion_monitor.views.main_window import main

main()
