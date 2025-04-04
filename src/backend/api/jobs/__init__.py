from .jobs_retrieve import router as jobs_retrieve_router
from .jobs_create import router as jobs_create_router

routers = (jobs_retrieve_router, jobs_create_router,)
