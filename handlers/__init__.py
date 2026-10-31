from aiogram import Router
from .start import router as start_router
from .add_task import router as add_task_router
from .list_tasks import router as list_tasks_router
from .stats import router as stats_router

router = Router()
router.include_router(start_router)
router.include_router(add_task_router)
router.include_router(list_tasks_router)
router.include_router(stats_router)