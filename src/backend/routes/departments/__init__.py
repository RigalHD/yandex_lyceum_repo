from .departments_create import router as departments_create_router
from .departments_update import router as departments_update_router
from .departments_delete import router as departments_delete_router
from .departments_retrieve import router as departments_retrieve_router

routers = (
    departments_create_router,
    departments_update_router,
    departments_delete_router,
    departments_retrieve_router,
)
