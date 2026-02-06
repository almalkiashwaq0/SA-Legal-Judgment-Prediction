import nbformat
from pathlib import Path

# Folder with your notebooks
folder_path = Path(".")

for nb_file in folder_path.glob("*.ipynb"):
    nb = nbformat.read(nb_file, as_version=4)
    
    # If 'widgets' exist but 'state' is missing, add empty 'state'
    if "widgets" in nb.metadata and "state" not in nb.metadata["widgets"]:
        nb.metadata["widgets"]["state"] = {}
        print(f"Fixed {nb_file.name}")
    
    nbformat.write(nb, nb_file)

print("All notebooks are GitHub-ready")
