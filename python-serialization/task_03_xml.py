#!/usr/bin/python3
"""
XML serialization and deserialization module.
Converts Python dictionaries to XML and back.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to file.
    
    Args:
        dictionary: Python dictionary to serialize
        filename: Output XML filename
    """
    # Create root element
    root = ET.Element("data")
    
    # Add dictionary items as child elements
    for key, value in dictionary.items():
        # Create child element with key as tag name
        child = ET.SubElement(root, key)
        
        # Handle different data types
        if isinstance(value, dict):
            # For nested dictionaries, recursively create sub-elements
            for sub_key, sub_value in value.items():
                sub_child = ET.SubElement(child, sub_key)
                sub_child.text = str(sub_value)
                # Add type attribute for proper deserialization
                sub_child.set('type', type(sub_value).__name__)
        else:
            # Set text content
            child.text = str(value)
            # Add type attribute for proper deserialization
            child.set('type', type(value).__name__)
    
    # Create ElementTree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file back to Python dictionary.
    
    Args:
        filename: XML filename to read from
        
    Returns:
        Python dictionary reconstructed from XML
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Reconstruct dictionary
    result = {}
    
    for child in root:
        # Get the value with proper type conversion
        value = child.text
        
        # Convert to appropriate type based on 'type' attribute
        if 'type' in child.attrib:
            type_name = child.attrib['type']
            
            if type_name == 'int':
                value = int(value)
            elif type_name == 'float':
                value = float(value)
            elif type_name == 'bool':
                value = value.lower() == 'true'
            elif type_name == 'NoneType':
                value = None
            # For nested dictionaries
            elif type_name == 'dict':
                nested_dict = {}
                for sub_child in child:
                    sub_value = sub_child.text
                    if 'type' in sub_child.attrib:
                        sub_type = sub_child.attrib['type']
                        if sub_type == 'int':
                            sub_value = int(sub_value)
                        elif sub_type == 'float':
                            sub_value = float(sub_value)
                        elif sub_type == 'bool':
                            sub_value = sub_value.lower() == 'true'
                        elif sub_type == 'NoneType':
                            sub_value = None
                    nested_dict[sub_child.tag] = sub_value
                value = nested_dict
        
        # Add to result dictionary
        result[child.tag] = value
    
    return result


# Example usage and testing
if __name__ == "__main__":
    # Test with a sample dictionary
    sample_dict = {
        'name': 'John',
        'age': 30,
        'salary': 50000.50,
        'is_student': False,
        'address': {
            'city': 'New York',
            'zipcode': 10001
        },
        'favorite_colors': ['blue', 'green'],
        'spouse': None
    }
    
    print("Original dictionary:")
    print(sample_dict)
    print()
    
    # Serialize to XML
    serialize_to_xml(sample_dict, "data.xml")
    print("Dictionary serialized to 'data.xml'")
    print()
    
    # Deserialize from XML
    reconstructed_dict = deserialize_from_xml("data.xml")
    print("Deserialized dictionary:")
    print(reconstructed_dict)
    print()
    
    # Verify they match
    print("Serialization/Deserialization successful!")
