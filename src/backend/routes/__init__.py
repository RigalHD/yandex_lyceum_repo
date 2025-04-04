from .auth import routers as auth_routers
from .jobs import routers as jobs_routers
from .departments import routers as departments_routers
from .job_categories import routers as job_categories_routers
from .main_page import router as main_page_router

routers = (
    *auth_routers,
    *jobs_routers,
    *departments_routers,
    *job_categories_routers,
    main_page_router,
)
