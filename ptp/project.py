import sys
import cod3s
import pkg_resources
installed_pkg = {pkg.key for pkg in pkg_resources.working_set}
if 'ipdb' in installed_pkg:
    import ipdb  # noqa: 401


project = cod3s.COD3SProject.from_yaml(
    file_path="project.yaml",
    cls_attr="COD3SProject",
)

# project.system.isimu_start()
# print(project.system.isimu_fireable_transitions())

# project.system.isimu_set_transition()
# print(project.system.isimu_fireable_transitions())

# trans_fired = project.system.isimu_step_forward()
# print(trans_fired)

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
