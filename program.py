def GetElementsArray(array: list) -> list:
    result = []
    for elem in array:
        if len(elem) < 4:
            result.append(elem)
    return result
    
    
print(GetElementsArray(["hello", "2", "world", ":-)"]))
print(GetElementsArray(["1234", "1567", "-2", "computer science"]))
print(GetElementsArray(["Russia", "Denmark", "Kazan"]))