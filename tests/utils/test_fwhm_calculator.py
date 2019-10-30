#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np
import pytest

from spot_motion_monitor.utils import fwhm_calculator

class TestFwhmCalculator:

    def test_calculation(self):
        np.random.seed(4000)
        x, y = np.meshgrid(np.arange(50), np.arange(50))
        x0 = 30
        y0 = 15
        sigma = 5
        z = 10 * np.exp(-((x - x0)**2 + (y - y0)**2) / 2 / sigma)
        z += np.random.uniform(size=2500).reshape(50, 50)

        fwhm = fwhm_calculator(z, x0, y0)
        assert fwhm == pytest.approx(5.58, rel=1e-2)
