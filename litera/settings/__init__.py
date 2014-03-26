import os
from .base import *

if os.environ.get("HEROKU", "").lower() == 'true':
    from .heroku import *

try:
    from .local import *
except ImportError:
    pass
