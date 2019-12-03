.. _configuration:

=============
Configuration
=============

In addition to using the configuration menu from within the user interface, the
program provides a mechanism to insert configuration information into the program
on startup. The ``-c`` or ``--config_file`` flag may be passed to the ``smm_ui`` call.
The flag takes a filename corresponding to a YAML configuration file. The following sections
will describe the currently configurable parameters. Each section corresponds to a section
heading in the YAML configuration file.


general
~~~~~~~

This section handles modification to the program's general information and functionality. The following variables are configured under this section.

autorun
  A boolean parameter that allows the program to be started in ROI mode after launch. This parameter can also be set from the command line using the ``-a`` or ``--auto-run`` flag. If the configuration file is read in after program launch, this parameter has no effect.

configVersion
  A string that represents the version of the configuration file being used. The telemetry system places this information in a generated output configuration file. 

saveBufferData
  A boolean parameter that will allow one to automatically save the buffer data upon generation. See :ref:`this section<saveBufferData>` for more details on the generated files.

site
  A string that represents the location of the observations. There is no default site used within the program.

timezone
  A string containing the timezone to use for all date/times within the program. Default is ``UTC``. Supports ``TAI``. To specify other timezones, use the notation supported by the ``pytz`` module.

telemetry
---------

directory
  A string containing the path where the resulting telemetry data is to be stored. This parameter can be overridden from the command line using the ``-t`` or ``--telemetry_dir`` flag.

cleanup
^^^^^^^

directory
  A boolean parameter specifying if the telemetry directory is removed when ROI acquistion is stopped.
  
files
  A boolean parameter specifying if the telemetry files are removed when ROI acquistion is stopped. If ``directory`` is ``true``, setting this parameter to ``false`` has no effect. 

data
~~~~

This section handles modification to the program's data controller. The following variables are configured under this section.

buffer
------

pixelScale
  A decimal parameter that sets the sky scale on the camera CCD in units of arcseconds per pixel. This value will vary depending on the optical path in front of the CCD camera.

size
  An integer parameter that sets the size of the buffer to store the centroid data before performing calculations on a filled buffer. To make the power spectrum distribution calculations effective, the buffer size should be a power of 2 (N^2).

  .. N^2 replace:: N\ :sup:`2`

fullFrame
---------

minimumNumPixels
  An integer parameter that specifies the minimum number of pixels in the found object when calculating the center-of-masses within a CCD frame.

sigmaScale
  A decimal parameter that sets the scale factor for the standard deviation subtraction of a full CCD frame. The scale factor times the standard deviation is then subtracted from the frame.

roiFrame
--------

thresholdFactor
  A decimal parameter that specifies the scale factor for the maximum ADC value from a ROI CCD frame. The scale factor times the max ADC value is then subtracted from the frame.

camera
~~~~~~

full
----

fps
  An integer parameter that sets the frame rate (frames per second) for CCD full frame acquisition. Note: The Gaussian camera does not support frame rates over 40 due to the poisson background generation. For a Vimba camera, consult the appropriate documentation to find the supported range. 

roi
---

fps
  An integer parameter that sets the frame rate (frames per second) for CCD ROI frame acquisition. Note: The Gaussian camera does not support frame rates over 40 due to the frame generation methodology. For a Vimba camera, consult the appropriate documentation to find the supported range. The program has been tested to work with Vimba camera frame rates up to 120 before the CCD plot feature needs to be switched off in order to obtain higher frame rates.

size
  An integer parameter that sets the size of the ROI region in pixels. By the nature of the program, the ROI region is fixed to be a square.

spotOscillation
---------------

This section only applies to a Gaussian camera.

do
  A boolean parameter that determines if the sport oscillation is executed.

x
^

amplitude
  An integer parameter that specifies the amplitude of the oscillation in the x direction. Parameter units are pixels.

frequency
  A decimal parameter that sets the frequency of the oscillation in the x direction. Parameter units are Hz.

y
^

amplitude
  An integer parameter that specifies the amplitude of the oscillation in the y direction. Parameter units are pixels.

frequency
  A decimal parameter that sets the frequency of the oscillation in the y direction. Parameter units are Hz.

Full Example
~~~~~~~~~~~~

This section will show a full example of all items that are configurable based on a configuration saved from the program. The ``camera`` section is for the Gaussian camera. The file passed to the program does not need to contain all of the sections and variables that are shown here.

::

  camera:
    full:
      fps: 24
    roi:
      fps: 40
      size: 50
    spotOscillation:
      do: true
      x:
        amplitude: 10
        frequency: 1.0
      y:
        amplitude: 5
        frequency: 2.0
  data:
    buffer:
      pixelScale: 1.0
      size: 1024
    fullFrame:
      minimumNumPixels: 10
      sigmaScale: 5.0
    roiFrame:
      thresholdFactor: 0.3
  general:
    autorun: false
    configVersion: "1.0.1"
    saveBufferData: false
    site: null
    telemetry:
      cleanup:
        directory: true
        files: true
      directory: null
    timezone: UTC
  plot:
    centroid:
      scatterPlot:
        histograms:
          numBins: 40
      xCentroid:
        autoscaleY: PARTIAL
        maximumY: null
        minimumY: null
      yCentroid:
        autoscaleY: PARTIAL
        maximumY: null
        minimumY: null
    psd:
      waterfall:
        colorMap: viridis
        numBins: 25
      xPSD:
        autoscaleY: true
        maximumY: null
      yPSD:
        autoscaleY: true
        maximumY: null

The following shows the camera section of a Vimba camera configuration.
