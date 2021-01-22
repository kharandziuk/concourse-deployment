from invoke import task
from pathlib import Path

ROOT_DIR = Path()


@task
def format(c):
    c.run("pre-commit install")
    c.run("pre-commit run --all-files")


@task
def orchestration(c):
    c.run("vagrant up")


@task
def provision(c):
    SSH_KEY = (
        ROOT_DIR / ".vagrant" / "machines" / "server" / "virtualbox" / "private_key"
    )
    c.run(
        f"ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i 10.2.2.25,  --user=vagrant --key-file {SSH_KEY} playbook.yml"
    )


@task
def deploy(c):
    orchestration(c)
    provision(c)
