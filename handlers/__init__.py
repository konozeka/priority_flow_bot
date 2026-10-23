from aiogram import Router
from .start import router as start_router
from .add_task import router as add_task_router

router = Router()
router.include_router(start_router)
router.include_router(add_task_router)