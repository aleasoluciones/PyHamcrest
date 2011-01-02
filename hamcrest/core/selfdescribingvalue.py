__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.selfdescribing import SelfDescribing


class SelfDescribingValue(SelfDescribing):
    """Wrap any value in a ``SelfDescribingValue`` to satisfy the
    :py:class:`~hamcrest.core.selfdescribing.SelfDescribing` interface.

    """

    def __init__(self, value):
        self.value = value

    def describe_to(self, description):
        """Generates a description of the value."""
        description.append_value(self.value)
