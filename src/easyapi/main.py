from application import app, engine, BaseModel
import uvicorn
import os

BaseModel.metadata.create_all(engine)
root_path:str = os.path.split(os.path.realpath(__file__))[0]
modules = os.listdir(f"{root_path}/modules")
for module in modules:
    if not os.path.isdir(f"{root_path}/modules/{module}"):
        continue

    if module == "template":
        continue

    __import__(f"modules.{module}")

def main(**kwargs):
    uvicorn.run("application:app", reload=True)

if __name__ == "__main__":
    main()