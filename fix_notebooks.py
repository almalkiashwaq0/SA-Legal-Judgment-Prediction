import nbformat
from pathlib import Path


top_folder = Path(".") 

for nb_file in top_folder.rglob("*.ipynb"):
    nb = nbformat.read(nb_file, as_version=4)
    
    # Add missing 'state' key if 'widgets' exist
    if "widgets" in nb.metadata and "state" not in nb.metadata["widgets"]:
        nb.metadata["widgets"]["state"] = {}
        print(f"Fixed {nb_file}")

    # Save the notebook
    nbformat.write(nb, nb_file)

print("All notebooks (including subfolders) are fixed!")
