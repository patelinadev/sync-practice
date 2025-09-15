from fastapi import APIRouter

# 创建一个临时的、空的router
# 即使我们暂时没有实现任何API，这个文件也需要提供一个router对象
# 以便 api/v1/__init__.py 能够成功导入它。
router = APIRouter(
    prefix="/triangles",
    tags=["Triangles (Not Implemented)"], # 在文档中标记为“未实现”
)

# 未来您可以在这里添加关于三角形的API端点
# @router.post("/draw-isosceles")
# async def draw_isosceles_triangle_endpoint(...):
#     pass
