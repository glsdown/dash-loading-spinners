import json

from setuptools import setup

with open("package.json") as f:
    package = json.load(f)

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    description=package.get("description", package_name),
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
    url="https://dash-loading-spinners.herokuapp.com/",
    project_urls={
        "Bug Reports": package["bugs"]["url"],
        "Source": "https://github.com/glsdown/dash-loading-spinners",
    },
    license=package["license"],
    install_requires=["dash"],
    classifiers=[
        "Framework :: Dash",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
