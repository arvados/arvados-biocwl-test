from biocwltest import helpers
from biocwltest.basic import basic_arvados_test
from biocwltest.cwl_runner import run_cwl, run_cwl_arvados
from biocwltest.arvados_connection import find_process_in_new_project


biocwltest_testing_uuid = "arind-j7d0g-u7rja16z572ldb8"


def test_load_file():
    assert type(helpers.load_file("./examples/example_pipeline.cwl")) == list


def test_create_input_yml():
    helpers.create_input_yml(
        {
            "metaInfoFile": {
                "class": "File",
                "location": "keep:b05083d7db79c2e4e211dbef369e98a7+76/sampleList_E-MTAB-8208.txt",
            },
            "fastqCollection": {
                "class": "File",
                "location": "keep:00780063929dcd34186ae2394505202d+422439",
            }
        }
    )

# def test_create_input_yml_empty():
#     helpers.create_input_yml()


def test_run_cwl(): # 
    run_cwl("components/single_step/single_step.cwl", {"name": "example.txt"})



def test_run_cwl_arvados():
    run_cwl_arvados(
        "./components/single_step/single_step.cwl",
        {"name": "example.txt"},
        "arind-j7d0g-u7rja16z572ldb8",
        "Name"
        )


def test_find_process_in_new_project():
    # Just check how does it work
    assert type(find_process_in_new_project(biocwltest_testing_uuid)).__name__ == 'Process'


# Example how to run this tests on some pipeline
def test_basic_arvados_test():
    assert basic_arvados_test(
        biocwltest_testing_uuid,
        "Example test",
        "components/single_step/single_step.cwl",
        {
            "name": "example.txt"
            }
        ) == []
    
def test_single_step():
    run = basic_arvados_test(
        biocwltest_testing_uuid,
        "Example test",
        "components/single_step/single_step.cwl",
        {
            "name": "example.txt"
            }
            )
    
    
