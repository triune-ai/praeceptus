# ---INFO-----------------------------------------------------------------------
"""
Praeceptus
"""


# ---DEPENDENCIES---------------------------------------------------------------
from pathlib import Path


# ------------------------------------------------------------------------------
def usage_guide():
    """
    Temporary utility to fetch the usage guide from the README file. Will be
    removed once the code and the documentation are arrranged.
    """
    path = Path(__file__).parent.parent / "README.md"
    with open(path, "r") as fh:
        readme = fh.read()
    usgsec = readme.split("## Usage")[1]
    usgsec = usgsec.split("## Acknowledgements")[0]
    return usgsec
