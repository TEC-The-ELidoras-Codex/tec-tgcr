import os
import sys

# Ensure the project's src/ folder is on sys.path so tests can import the package
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
# Also add repository root so imports that use the literal `src.*` package path
# (some tests import `src.tec_tgcr...`) will resolve correctly.
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
