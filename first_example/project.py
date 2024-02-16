import sys
import cod3s


project = cod3s.COD3SProject.from_yaml(
    file_path="project.yaml",
    cls_attr="COD3SProject",
)


simu_params = {
    "nb_runs": 10,
    "schedule": [
        {
            "start": 0.0,
            "end": 100.0,
            "nvalues": 5,
        },
    ],
    "time_unit": "seconds",
    "seed": 123331245,
}

project.system.simulate(cod3s.PycMCSimulationParam(**simu_params))

project.system.simulate(cod3s.PycMCSimulationParam(**simu_params))

sys.exit(0)
