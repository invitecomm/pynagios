# PyNagios

PyNagios is a simple Python library meant to make writing
[Nagios](http://www.nagios.org/) plugins much easier. Nagios
plugins have [quite a few guidelines](http://nagiosplug.sourceforge.net/developer-guidelines.html)
to adhere to, and PyNagios provides helpers to make this
easy.

## Install

To install, simply use `pip` or `easy_install`:

    pip install pynagios

## Features

The core features supported by PyNagios:

  * Parsing command line arguments such that the standard expected
    arguments (such as `-H`, `-w`, `-c`) are accepted.
  * Returning proper POSIX exit code based on status.
  * Parsing Nagios range formats (such as "@10:20", "~:50", "10", etc.)
  * Outputting status and message.
  * Outputting performance data.

## Example

What all these features result in is a concise, simple, and
guidelines-compliant Python-based Nagios plugin:

```python
from pynagios import Plugin, Response

class UserCheck(Plugin):
    """
    Nagios plugin to check how many users are logged into this
    machine.
    """

    def check(self):
        # Get the number of logged in users, for now we hardcode
        users = 27

        # Get the status code for the current number of users
        # given the warning/critical ranges given.
        status = self.status_for_value(users)

        # Build a response and exit
        response = Response(status, "%d users" % users)
        response.set_perf_data("users", users)
        response.set_perf_data("another metric", 27, "MB")
        return response

if __name__ == 'main':
    # Build the plugin instance and run it. This will also parse
    # command line arguments by default.
    UserCheck().check().exit()
```

While the above example subclasses `Plugin`, you're of course welcome
to simply call `Plugin`s methods directly and build a `Response`
yourself.
