from .version import __version__
from .Search.linearSearch import lsearch
from .Search.binarySearch import bsearch
from .Search.jumpSearch import jsearch
from .Search.exponentialSearch import esearch

__all__ = [
    'lsearch',
    'bsearch',
    'jsearch',
    'esearch',
]
