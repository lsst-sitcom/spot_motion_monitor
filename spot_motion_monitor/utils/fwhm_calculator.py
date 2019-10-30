#------------------------------------------------------------------------------
# Copyright (c) 2019 LSST Systems Engineering
# Distributed under the MIT License. See LICENSE for more information.
#------------------------------------------------------------------------------
import numpy as np

__all__ = ['fwhm_calculator']

def fwhm_calculator(frame, cx, cy):
    """Calculate the 2D Full-Width Half-Maximum for the given frame.

    Parameters
    ----------
    frame : `np.array`
        The frame information.
    cx : int
        The x pixel index to look along.
    cy : int
        The y pixel index to look along.

    Returns
    -------
    float
        The 2D FWHM.
    """
    def getFWHM1D(p):
        """Calculate the 1D Full-Width Half-Maximum.

        Parameters
        ----------
        p : `np.array`
            The axial slice for calculating FWHM.

        Returns
        -------
        float
            The 1D FWHM.
        """
        hm = np.max(p) / 2
        n = len(p)
        i1 = np.argmax(p > hm)
        i2 = n - np.argmax(p[::-1] > hm) - 1
        fwhm = i2 - i1 + 1 + (p[i1] - hm) / (p[i1] - p[i1 - 1]) + (p[i2] - hm) / (p[i2] - p[i2 + 1])
        return fwhm

    fwhmX = getFWHM1D(frame[cy, :])
    fwhmY = getFWHM1D(frame[:, cx])

    return (fwhmX + fwhmY) / 2
