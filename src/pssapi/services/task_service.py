from datetime import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import TaskDesign as _TaskDesign
from .raw import TaskServiceRaw as _TaskServiceRaw


class TaskService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("TaskDesignVersion")
    async def list_all_task_designs(self, client_date_time: _datetime, design_version: int = None) -> _List[_TaskDesign]:
        production_server = await self.get_production_server()
        result = await _TaskServiceRaw.list_all_task_designs_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result
