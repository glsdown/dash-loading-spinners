import json

from setuptools import setup

with open("package.json") as f:
    package = json.load(f)

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    long_description=description,
    long_description_content_type="text/markdown",
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
