import logging
import time
from datetime import datetime
from zoneinfo import ZoneInfo


logger = logging.getLogger(__name__)
timestamp = time.time()
local_time = datetime.fromtimestamp(timestamp, tz=ZoneInfo("America/Santiago"))
logger.warning(local_time)