from .job_categories_create import router as job_categories_create_router
from .job_categories_update import router as job_categories_update_router
from .job_categories_delete import router as job_categories_delete_router

routers = (
    job_categories_create_router,
    job_categories_update_router,
    job_categories_delete_router,
)
