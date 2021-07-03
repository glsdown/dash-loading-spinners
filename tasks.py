import json
from pathlib import Path

import semver
from invoke import task
from termcolor import cprint

HERE = Path(__file__).parent


def normalise_version(version):
    if version.startswith("refs/tags/"):
        version = version.rsplit("/", 1)[1]
    return str(semver.parse_version_info(version))


@task
def update_version(_, version):
    version = normalise_version(version)
    with open(HERE / "package.json", "r") as f:
        package_json = json.load(f)
    package_json["version"] = version
    with open(HERE / "package.json", "w") as f:
        json.dump(package_json, f, indent=2)


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
    make_and_clean_dir("dist")
    make_and_clean_dir("inst")
    make_and_clean_dir("inst/deps")
    make_and_clean_dir("man")
    make_and_clean_dir("R")
    make_and_clean_dir("src", glob="*.jl")


def error(text):
    cprint(text, "red")


def info(text):
    print(text)
