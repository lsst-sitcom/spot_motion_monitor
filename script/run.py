#------------------------------------------------------------------------------
# Copyright (c) 2018 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------

# This script is meant for running the UI during development. It needs to be
# run in a wrapped environment where the PYTHONPATH points to the
# spot_motion_monitor library.

from spot_motion_monitor.views.main_window import main

main()
