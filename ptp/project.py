import sys
import cod3s


project = cod3s.COD3SProject.from_yaml(
    file_path="project.yaml",
    cls_attr="COD3SProject",
)


print(project)

sys.exit(0)
