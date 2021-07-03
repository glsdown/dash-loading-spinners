import json

from setuptools import setup

with open("package.json") as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    packages=[package_name],
    include_package_data=True,
    package_data={
        "dash_loading_spinners": [
            "dash_loading_spinners.min.js",
            "dash_loading_spinners.min.js.map",
            "metadata.json",
            "package-info.json",
        ]
    },
    license=package["license"],
    description=package.get("description", package_name),
    install_requires=["dash"],
    classifiers=[
        "Framework :: Dash",
    ],
)
