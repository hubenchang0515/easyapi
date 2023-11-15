import sys
import os
import argparse
import shutil

def main(**kwargs):
    source_path:str = os.path.realpath(os.path.dirname(__file__))
    working_path:str = os.path.realpath(os.getcwd())

    parser = argparse.ArgumentParser(description="EasyAPI Manager")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--project", action="store_true", help="create project")
    group.add_argument("-m", "--module", action="store_true", help="add module")
    parser.add_argument("name")

    args = parser.parse_args()

    if args.name is None:
        parser.print_help()
        quit()

    if not args.project and not args.module:
        parser.print_help()
        quit()

    if args.project:
        project_path:str = os.path.join(working_path, args.name)
        if os.path.exists(project_path):
            print(f"Project path '{project_path}' is exists", file=sys.stderr)
            quit()

        shutil.copytree(os.path.join(source_path, "application"), os.path.join(project_path, "application"))
        os.mkdir(os.path.join(project_path, "modules"))
        os.mkdir(os.path.join(project_path, "static"))
        shutil.copyfile(os.path.join(source_path, "main.py"), os.path.join(project_path, "main.py"))

    if args.module:
        module_path:str = os.path.join(working_path, "modules", args.name)
        if os.path.exists(module_path):
            print(f"Module path '{module_path}' is exists", file=sys.stderr)
            quit()

        shutil.copytree(os.path.join(source_path, "modules", "template"), module_path)

if __name__ == "__main__":
    main()