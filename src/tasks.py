from invoke import task

@task
def start(ctx):
    ctx.run("python3 services/main_service.py")