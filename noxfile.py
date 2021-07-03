import nox

nox.options.sessions = ["lint"]

SOURCES = [
    "docs",
    "dash_loading_spinners/__init__.py",
    "examples/usage.py",
    "noxfile.py",
    "setup.py",
    "tasks.py",
]


@nox.session()
def lint(session):
    session.install("black", "flake8", "isort")
    session.run("black", "--check", *SOURCES)
    session.run("flake8", *SOURCES)
    session.run("isort", "--check", *SOURCES)


@nox.session(name="format")
def format_(session):
    session.install("black", "isort")
    session.run("black", *SOURCES)
    session.run("isort", *SOURCES)


# @nox.session(python=["2.7", "3.5", "3.6", "3.7", "3.8", "3.9"])
# def test(session):
#     session.install("pytest")
#     session.install("dash[testing]")
#     session.install(".")
#     session.run("pytest", "--headless", "tests")
