import nbformat
from pathlib import Path

top_folder = Path(".")

for nb_file in top_folder.rglob("*.ipynb"):
    nb = nbformat.read(nb_file, as_version=4)
    

    if "widgets" in nb.metadata:
        del nb.metadata["widgets"]

    for cell in nb.cells:
        if "widgets" in cell.metadata:
            del cell.metadata["widgets"]
        if "outputs" in cell:
            for output in cell.outputs:
                if "metadata" in output and "widgets" in output.metadata:
                    del output.metadata["widgets"]
    
    nbformat.write(nb, nb_file)
    print(f"Cleaned {nb_file}")

print("All notebooks are now GitHub-compatible")
