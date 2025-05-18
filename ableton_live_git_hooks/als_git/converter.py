import gzip
from pathlib import Path

# --- Supported suffixes -----------------------------------------------------
BIN_SUFFIXES: tuple[str, ...] = (".als", ".alc")  # Ableton binary
XML_SUFFIXES: tuple[str, ...] = tuple(s + ".xml" for s in BIN_SUFFIXES)
# ---------------------------------------------------------------------------

def extract_bin_to_xml(bin_path: Path) -> Path:
    """
    Decompress an Ableton Live binary container (.als **or** .alc) into
    its XML representation, written as "<name>.<ext>.xml".

    Example
    -------
    >>> extract_bin_to_xml(Path("MySong.als"))
    Path("MySong.als.xml")
    >>> extract_bin_to_xml(Path("CoolClip.alc"))
    Path("CoolClip.alc.xml")
    """
    if not bin_path.is_file():
        raise ValueError(f"File does not exist: {bin_path}")

    if bin_path.suffix.lower() not in BIN_SUFFIXES:
        raise ValueError(
            f"Unsupported Ableton file type {bin_path.suffix!r}; "
            f"expected one of {', '.join(BIN_SUFFIXES)}"
        )

    xml_path = bin_path.with_suffix(bin_path.suffix + ".xml")

    try:
        xml_path.write_bytes(gzip.decompress(bin_path.read_bytes()))
        return xml_path
    except OSError as e:
        raise RuntimeError(f"Failed to decompress {bin_path}: {e}") from e

# Backwards-compat shim (old callers used this name)
extract_als_to_xml = extract_bin_to_xml


def xml_to_bin(xml_path: Path) -> Path:
    """
    Re-compress an XML file produced by `extract_bin_to_xml` back to its
    original binary form (.als or .alc).
    """
    if not xml_path.is_file():
        raise ValueError(f"XML file does not exist: {xml_path}")

    # Identify which binary suffix we're restoring
    for suffix in XML_SUFFIXES:
        if xml_path.name.endswith(suffix):
            bin_path = xml_path.with_suffix("")  # strip the trailing ".xml"
            break
    else:
        raise ValueError(f"{xml_path} does not look like one of {XML_SUFFIXES}")

    try:
        bin_path.write_bytes(gzip.compress(xml_path.read_bytes()))
        return bin_path
    except OSError as e:
        raise RuntimeError(f"Failed to compress {xml_path}: {e}") from e

# Backwards-compat shim
xml_to_als = xml_to_bin