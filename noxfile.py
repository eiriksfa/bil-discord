"""Noxfile."""
import tempfile

import nox
from nox.sessions import Session


locations = "src", "tests", "noxfile.py"
package = "bil_discord"
nox.options.sessions = "lint", "tests", "safety", "mypy", "xdoctest"


def install_with_constraints(session, *args, **kwargs):
    """Install virtual env with constraints.

    Args:
        session: nox session
        *args: args
        **kwargs: kwargs
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python="3.8")
def black(session):
    """Run black.

    Args:
        session: nox session
    """
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python=["3.8"])
def tests(session):
    """Run pytests.

    Args:
        session: nox session
    """
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)


@nox.session(python=["3.8"])
def lint(session):
    """Run linter.

    Args:
        session: nox session
    """
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-annotations",
        "flake8-import-order",
        "flake8-docstrings",
        "darglint",
        "flake8-bandit",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def mypy(session) -> None:
    """Run mypy.

    Args:
        session: nox session
    """
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


@nox.session(python=["3.8"])
def xdoctest(session: Session) -> None:
    """Run xdoctests.

    Args:
        session: nox session
    """
    args = session.posargs or ["all"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "xdoctest")
    session.run("python", "-m", "xdoctest", package, *args)


@nox.session(python="3.8")
def safety(session):
    """Run safety.

    Args:
        session: nox session
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
