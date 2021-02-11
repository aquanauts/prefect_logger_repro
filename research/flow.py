from prefect import task, Flow
from prefect.executors import LocalDaskExecutor
from prefect.storage import Docker
from prefect.run_configs import DockerRun

from research.example_pkg import things

@task#(log_stdout=True)
def run_thing1():
    if things.thing1():
        return True

@task#(log_stdout=True)
def run_thing2():
    if things.thing2():
        return True

if __name__ == "__main__":
    with Flow("test_flow", executor=LocalDaskExecutor(scheduler="processes")) as flow:
        if run_thing1():
            thing2_var = run_thing2()
    
    flow.storage = Docker(
        base_image="prefect_logger_repro",
        local_image=True,
        build_kwargs={
            "labels" : { "logging_job_name" : "test_flow" }
        },
        ignore_healthchecks=True,
        registry_url="artifactory.aq.tc/prefect/",
    )
    flow.run_config = DockerRun()
    #flow.run()
    flow.register(project_name="default")
