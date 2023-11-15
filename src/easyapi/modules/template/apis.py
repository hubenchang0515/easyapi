from application import app
from .constant import module_name

@app.get(f"/{module_name}/")
async def index():
    return {"module": module_name, "path": f"/{module_name}/"}