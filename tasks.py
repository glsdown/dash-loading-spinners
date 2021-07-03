from pathlib import Path

from invoke import task
from termcolor import cprint

HERE = Path(__file__).parent


def make_and_clean_dir(dir_, glob="*", ignore=None):
    info(f"Cleaning {dir_}/{glob}")
    (HERE / dir_).mkdir(exist_ok=True)

    ignore = ignore if ignore is not None else []

    for file_ in (HERE / dir_).glob(glob):
        if file_.is_file() and file_.name not in ignore:
            file_.unlink()


def delete_files(files):
    for file_ in files:
        file_ = HERE / file_
        if file_.exists():
            file_.unlink()


@task
def clean(_):
    delete_files(["DESCRIPTION", "NAMESPACE", "Project.toml"])
    make_and_clean_dir("dash_loading_spinners", ignore=["__init__.py"])
    make_and_clean_dir("deps")
    make_and_clean_dir("inst")
    make_and_clean_dir("inst/deps")
    make_and_clean_dir("man")
    make_and_clean_dir("R")
    make_and_clean_dir("src", glob="*.jl")


def error(text):
    cprint(text, "red")


def info(text):
    print(text)
