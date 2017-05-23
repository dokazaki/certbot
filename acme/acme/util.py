"""ACME utilities."""
import six
MYPY = False
if MYPY:
    from typing import Callable, Any  # pylint: disable=unused-import


def map_keys(dikt, func):
    # type: (dict, Callable[[Any], Any]) -> dict
    """Map dictionary keys."""
    return dict((func(key), value) for key, value in six.iteritems(dikt))
