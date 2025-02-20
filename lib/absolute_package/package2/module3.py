from ..subpackage1.module6 import function6 # type: ignore

def function3():
    return "Function 3 from module3"

print(function6())  # Expected Output: "Function 6 from module6"
