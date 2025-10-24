# /// script
# dependencies = ["rich"]
# ///
import rich
rich.print("[blue]Hello world")

# `uv run pep_723.py`
# installs rich for only this script (should use this carefully!)
# `python3 pep_723.py` would give package not installed error-- only works with uv run