"""
Unit tests for Ableton Live converter functions.
"""
import gzip
from pathlib import Path

import pytest

from ableton_live_git_hooks.als_git.converter import (
    BIN_SUFFIXES,
    XML_SUFFIXES,
    extract_als_to_xml,
    extract_bin_to_xml,
    xml_to_als,
    xml_to_bin,
)

pytestmark = pytest.mark.unit


def test_extract_bin_to_xml_success(tmp_path):
    original = b"<root>data</root>"
    compressed = gzip.compress(original)
    bin_file = tmp_path / f"test{BIN_SUFFIXES[0]}"
    bin_file.write_bytes(compressed)
    xml_file = extract_bin_to_xml(bin_file)
    assert xml_file == bin_file.with_suffix(bin_file.suffix + ".xml")
    assert xml_file.read_bytes() == original


def test_extract_als_to_xml_alias(tmp_path):
    original = b"<alias/>"
    compressed = gzip.compress(original)
    bin_file = tmp_path / f"alias{BIN_SUFFIXES[1]}"
    bin_file.write_bytes(compressed)
    xml_file = extract_als_to_xml(bin_file)
    assert xml_file.exists()
    assert xml_file.read_bytes() == original


def test_extract_bin_to_xml_missing_file():
    missing = Path("nonexistent.als")
    with pytest.raises(ValueError) as exc:
        extract_bin_to_xml(missing)
    assert "File does not exist" in str(exc.value)


def test_extract_bin_to_xml_unsupported_suffix(tmp_path):
    file = tmp_path / "wrong.txt"
    file.write_bytes(gzip.compress(b""))
    with pytest.raises(ValueError) as exc:
        extract_bin_to_xml(file)
    assert "Unsupported Ableton file type" in str(exc.value)


def test_extract_bin_to_xml_decompression_error(tmp_path):
    bin_file = tmp_path / f"bad{BIN_SUFFIXES[0]}"
    bin_file.write_bytes(b"not a gzip")
    with pytest.raises(RuntimeError) as exc:
        extract_bin_to_xml(bin_file)
    assert "Failed to decompress" in str(exc.value)


def test_xml_to_bin_success(tmp_path):
    original = b"<xml/>"
    xml_file = tmp_path / f"doc{XML_SUFFIXES[0]}"
    xml_file.write_bytes(original)
    bin_file = xml_to_bin(xml_file)
    assert bin_file == xml_file.with_suffix("")
    assert gzip.decompress(bin_file.read_bytes()) == original


def test_xml_to_als_alias(tmp_path):
    original = b"<xmlalias/>"
    xml_file = tmp_path / f"xmlalias{XML_SUFFIXES[1]}"
    xml_file.write_bytes(original)
    bin_file = xml_to_als(xml_file)
    assert bin_file.exists()
    assert gzip.decompress(bin_file.read_bytes()) == original


def test_xml_to_bin_missing_file():
    missing = Path("missing.xml")
    with pytest.raises(ValueError) as exc:
        xml_to_bin(missing)
    assert "XML file does not exist" in str(exc.value)


def test_xml_to_bin_unsupported_suffix(tmp_path):
    xml_file = tmp_path / "wrong.xml"
    xml_file.write_bytes(b"")
    with pytest.raises(ValueError) as exc:
        xml_to_bin(xml_file)
    assert "does not look like one of" in str(exc.value)


def test_xml_to_bin_compression_error(tmp_path, monkeypatch):
    original = b"<xmlerror/>"
    xml_file = tmp_path / f"error{XML_SUFFIXES[0]}"
    xml_file.write_bytes(original)
    def fake_compress(data):
        raise OSError("compress failed")

    monkeypatch.setattr(gzip, "compress", fake_compress)
    with pytest.raises(RuntimeError) as exc:
        xml_to_bin(xml_file)
    assert "Failed to compress" in str(exc.value)