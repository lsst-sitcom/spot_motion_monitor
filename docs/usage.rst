========
Usage
========

This package is used as the front-end to a Dome Seeing Monitor. It currently 
does not have any useful module imports. 

To run the user interface, do::

    smm_ui

Command-line help can be acquired by doing::

    smm_ui -h

or::

    smm_ui --help

Telemetry
~~~~~~~~~

When the UI is in the acquiring ROI mode and the first buffer is filled, the system
writes out a file containing information that may be of wider interest. LSST will
leverage this information and place it into their Engineering Facilities Database
when the Dome Seeing Monitor is running. By default, the telemetry files show up in
the current running directory under one called ``dsm_telemetry``. A configuration file
or the command-line can be used to specify an alternate directory. See the :ref:`configuration` 
section for more details. Once the UI is no longer in the acquiring ROI mode, all of the
telemetry files are deleted and the telemetry directory removed.

In the telemetry directory, two types of files will be present. One file called
``dsm_ui_config.yaml`` contains the current configuration of the user interface
at the time the telemetry was started. It contains the following information.

ui_versions
-----------

code
  The current version of the user interface.

config
  The version of a specified configuration file. This is ``null`` if no file is used.

camera
------

name
  This is the general classifier of the camera. Supported names are ``Gaussian`` and
  ``Vimba``

fps
  This is the value for the current frames per second (FPS) setting on the camera.

data
----

buffer_size
  This is the size of the buffer to capture the ROI frame information into.

acquisition_time
  This is the total time it takes to fill a buffer at the above size and FPS


The second file, generally called ``dsm_YYYYMMDD_HHMMSS.dat``, contains the telemetry
information at the time a buffer is filled. The timestamp is the UTC time when
the file was created. The file contains a comma-delimited set of information in the
following order.

  1. The file creation UTC timestamp in ISO format
  #. The UTC time when the first value of the buffer was filled in ISO format
  #. The UTC time when the last value of the buffer was filled in ISO format
  #. The RMS of the centroid in the X direction on the camera in units of arcseconds
  #. The RMS of the centroid in the Y direction on the camera in units of arcseconds

Each time a buffer is filled, a new file is generated.
