from langchain.tools import tool
from typing import List
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from simple_openai_tool import add_numbers

load_dotenv()
llm= ChatOpenAI(model="gpt-4o-mini")

@tool
def add_numbers_with_options(numbers: List[float], absolute: bool = True) -> float:
    """
    Adds a list of numbers provided as input.

    Parameters:
    - numbers (List[float]): A list of numbers to be summed.
    - absolute (bool): If True, use the absolute values of the numbers before summing.

    Returns:
    - float: The total sum of the numbers.
    """
    if absolute:
        numbers = [abs(n) for n in numbers]
    return sum(numbers)

print(f"Args Schema Info 1234: {add_numbers_with_options.args}")
print(f"Args Schema Info 3456: {add_numbers.args}")

print(add_numbers_with_options.invoke({"numbers":[-1.1,-2.1,-3.0],"absolute":False}))
print(add_numbers_with_options.invoke({"numbers":[-1.1,-2.1,-3.0],"absolute":True}))


