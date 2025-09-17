from .square_api import router as square_router
from .triangle_api import router as triangle_router
from .trapezoid_api import router as trapezoid_router
from .diamond_api import router as diamond_router

all_routers = [
    square_router,
    triangle_router,
    trapezoid_router,
    diamond_router,
]
