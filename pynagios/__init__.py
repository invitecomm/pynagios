"""
This package provides all the modules for writing a Nagios plugin
with Python. The package file itself exports the constants used
throughout the library.
"""

from plugin import Plugin, OK, WARNING, CRITICAL, UNKNOWN
from range import Range
from response import Response
from status import Status

__version__ = '0.1.0'
