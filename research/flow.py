from prefect import task, Flow
from prefect.engine.executors import LocalDaskExecutor
from prefect.environments import LocalEnvironment
from prefect.environments.storage import Docker

from research.example_pkg import things

@task
def run_thing1():
    if things.thing1():
        return True

@task
def run_thing2():
    if things.thing2():
        return True

def main():
    with Flow("test_flow") as flow:
        run_thing1()
        run_thing2()

    flow.environment = LocalEnvironment(executor=LocalDaskExecutor(scheduler="processes"))

    flow.storage = Docker(
        base_image="prefect_logger_repro",
        local_image=True,
        ignore_healthchecks=True,
        registry_url="artifactory.aq.tc/prefect/",
    )
    flow.register(project_name="default")

if __name__ == "__main__":
    main()
