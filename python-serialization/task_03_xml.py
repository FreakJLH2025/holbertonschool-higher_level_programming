#!/usr/bin/python3
"""
Module to serialize a Python dictionary to XML
and deserialize XML back into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to the given filename.
    Returns True if successful, False otherwise.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from the given filename into a Python dictionary.
    Returns the dictionary if successful, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            text = child.text

            # Attempt type conversion: int, bool, fallback to string
            if text is None:
                result[child.tag] = None
            elif text.lower() in ["true", "false"]:
                result[child.tag] = text.lower() == "true"
            else:
                try:
                    result[child.tag] = int(text)
                except ValueError:
                    result[child.tag] = text

        return result
    except Exception:
        return None
