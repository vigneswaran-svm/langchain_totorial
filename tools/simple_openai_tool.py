import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.tools import Tool
import re


load_dotenv()
llm= ChatOpenAI(model="gpt-4o-mini")


@tool
def add_numbers(inputs:str) -> dict:
    """
    Adds a list of numbers provided in the input dictionary or extracts numbers from a string.

    Parameters:
    - inputs (str): 
    string, it should contain numbers that can be extracted and summed.

    Returns:
    - dict: A dictionary with a single key "result" containing the sum of the numbers.

    Example Input (Dictionary):
    {"numbers": [10, 20, 30]}

    Example Input (String):
    "Add the numbers 10, 20, and 30."

    Example Output:
    {"result": 60}
    """
    #numbers = [int(x) for x in inputs.replace(",", "").split() if x.isdigit()]
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]

    
    result = sum(numbers)
    return {"result": result}


add_tool=Tool(
        name="AddTool",
        func=add_numbers,
        description="Adds a list of numbers and returns the result.")
print("tool object",add_tool)


print("Name: \n", add_numbers.name)
print("Description: \n", add_numbers.description) 
print("Args: \n", add_numbers.args) 

test_input = "what is the sum between 10, 20 and 30 " 
print(add_numbers.invoke(test_input))  # Example



# Comparing the two approaches
print("Tool Constructor Approach:")

print(f"Has Schema: {hasattr(add_tool, 'args_schema')}")
print("\n")

print("@tool Decorator Approach:")


print(f"Has Schema: {hasattr(add_numbers, 'args_schema')}")
print(f"Args Schema Info: {add_numbers.args}")


