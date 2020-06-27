from typing import Dict


def checkandConvertToFloat(dictionary: Dict, key: str) -> float:
    """
        Check if key exists in the dictionary then
        convert its value into float and return
    """
    convertedValue = 0.0
    try:
        if key in dictionary and dictionary[key] != "False":
            convertedValue = float(dictionary[key].replace(",", "")) 
    except Exception as e:
        print("Exception occured @ checkandConvertToFloat",e)
    finally:  
        return convertedValue


def checkandConvertToStr(dictionary: Dict, key: str) -> str:
    """
        Check if key exists in the dictionary then
        convert its value into String and return
    """
    convertedValue = None
    try:
        if key in dictionary and dictionary[key] != "False":
            convertedValue = str(dictionary[key])
    except Exception as e:
        print("Exception occured @ checkandConvertToStr", e)
    finally:
        return convertedValue

def checkandConvertToBool(dictionary: Dict, key: str) -> bool:
    """
        Check if key exists in the dictionary then
        convert its value into Boolean and return
    """
    convertedValue = False
    try:
        if key in dictionary:
            convertedValue = True if dictionary[key] != "False" else False
    except Exception as e:
        print("Exception occured @ checkandConvertToBool", e)
    finally:
        return convertedValue
