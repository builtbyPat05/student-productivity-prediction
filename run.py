"""Execute the complete evaluation in a fresh kernel and save notebook outputs."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager

root = Path(__file__).resolve().parent
path = root / "student_performance.ipynb"
notebook = nbformat.read(path, as_version=4)
manager = KernelManager(kernel_name="python3")
manager.kernel_spec.argv[0] = sys.executable
try:
    NotebookClient(
        notebook,
        km=manager,
        timeout=180,
        resources={"metadata": {"path": str(root)}},
    ).execute()
    nbformat.write(notebook, path)
finally:
    if manager.has_kernel:
        manager.shutdown_kernel(now=True)
print((root / "results" / "summary.json").read_text())
