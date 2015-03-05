# -*- coding: utf-8 -*-
"""
obspy.core.util - Various utilities for ObsPy
=============================================

.. note:: Please import all utilities within your custom applications from this
    module rather than from any sub module, e.g.

    >>> from obspy.core.util import AttribDict  # good

    instead of

    >>> from obspy.core.util.attribdict import AttribDict  # bad

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA

# import order matters - NamedTemporaryFile must be one of the first!
from obspy.core.util.attribdict import AttribDict
from obspy.core.util.base import (ALL_MODULES, DEFAULT_MODULES,
                                  NATIVE_BYTEORDER, NETWORK_MODULES,
                                  NamedTemporaryFile, _readFromPlugin,
                                  createEmptyDataChunk, getExampleFile,
                                  getMatplotlibVersion, getScriptDirName)
from obspy.core.util.decorator import (deprecated, deprecated_keywords, skip,
                                       skipIf, uncompressFile)
from obspy.core.util.geodetics import (FlinnEngdahl, calcVincentyInverse,
                                       degrees2kilometers, gps2DistAzimuth,
                                       kilometer2degrees, locations2degrees)
from obspy.core.util.misc import (BAND_CODE, CatchOutput, complexifyString,
                                  guessDelta, loadtxt, scoreatpercentile,
                                  toIntOrZero)
from obspy.core.util.obspy_types import (ComplexWithUncertainties, Enum,
                                         FloatWithUncertainties)
from obspy.core.util.testing import add_doctests, add_unittests
from obspy.core.util.version import get_git_version as _getVersionString
