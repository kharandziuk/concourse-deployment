from invoke import task

@task
def orchestration(c):
    c.run('vagrant up')

@task(orchestration)
def provision(c):
    c.run(f"ansible-playbook -i 10.2.2.25, playbook.yml")
