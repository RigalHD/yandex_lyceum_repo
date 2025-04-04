from .jobs_create import router as jobs_create_router
from .jobs_update import router as jobs_update_router
from .jobs_delete import router as jobs_delete_router

routers = (
    jobs_create_router,
    jobs_update_router,
    jobs_delete_router,
)
