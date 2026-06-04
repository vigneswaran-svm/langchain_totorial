from langgraph.prebuilt import create_react_agent
from zero_shot_reasoning_tool import sum_numbers_from_text
from langchain.tools import tool
from langchain.tools import Tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm= ChatOpenAI(model="gpt-4o-mini")

agent_exec = create_react_agent(
    model=llm, 
    tools=[sum_numbers_from_text])

msgs = agent_exec.invoke({"messages": [("human", "Add the numbers -10, -20, -30")]})

print(msgs["messages"][-1].content)

@tool
def subtract_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string, negates the first number, and successively subtracts 
    the remaining numbers in the list.

    This function is designed to handle input in string format, where numbers are separated 
    by spaces, commas, or other delimiters. It parses the string, extracts valid numeric values, 
    and performs a step-by-step subtraction operation starting with the first number negated.

    Parameters:
    - inputs (str): 
      A string containing numbers to subtract. The string may include spaces, commas, or 
      other delimiters between the numbers.

    Returns:
    - dict: 
      A dictionary containing the key "result" with the calculated difference as its value. 
      If no valid numbers are found in the input string, the result defaults to 0.

    Example Input:
    "100, 20, 10"

    Example Output:
    {"result": -130}

    Notes:
    - Non-numeric characters in the input are ignored.
    - If the input string contains only one valid number, the result will be that number negated.
    - Handles a variety of delimiters (e.g., spaces, commas) but does not validate input formats 
      beyond extracting numeric values.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]

    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Start with the first number negated
    result = -1 * numbers[0]

    # Subtract all subsequent numbers
    for num in numbers[1:]:
        result -= num

    return {"result": result}




@tool
def multiply_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates their product.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the product of the numbers.

    Example Input:
    "2, 3, 4"

    Example Output:
    {"result": 24}

    Notes:
    - If no numbers are found, the result defaults to 1 (neutral element for multiplication).
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]
    print(numbers)

    # If no numbers are found, return 1
    if not numbers:
        return {"result": 1}

    # Calculate the product of the numbers
    result = 1
    for num in numbers:
        result *= num
        print(num)

    return {"result": result}

@tool
def divide_numbers(inputs: str) -> dict:
    """
    Extracts numbers from a string and calculates the result of dividing the first number 
    by the subsequent numbers in sequence.

    Parameters:
    - inputs (str): A string containing numbers separated by spaces, commas, or other delimiters.

    Returns:
    - dict: A dictionary with the key "result" containing the quotient.

    Example Input:
    "100, 5, 2"

    Example Output:
    {"result": 10.0}

    Notes:
    - If no numbers are found, the result defaults to 0.
    - Division by zero will raise an error.
    """
    # Extract numbers from the string
    numbers = [int(num) for num in inputs.replace(",", "").split() if num.isdigit()]


    # If no numbers are found, return 0
    if not numbers:
        return {"result": 0}

    # Calculate the result of dividing the first number by subsequent numbers
    result = numbers[0]
    for num in numbers[1:]:
        result /= num

    return {"result": result}


print("Name: \n", subtract_numbers.name)
print("Description: \n", subtract_numbers.description) 
print("Args: \n", subtract_numbers.args) 

print("Calling Tool Function:")
test_input = "10 20 30 and four a b" 
print(subtract_numbers.invoke(test_input))  # Example

# Testing multiply_tool
multiply_test_input = "2, 3, and four "
multiply_result = multiply_numbers.invoke(multiply_test_input)
print("--- Testing MultiplyTool ---")
print(f"Input: {multiply_test_input}")
print(f"Output: {multiply_result}")


# Testing divide_tool
divide_test_input = "100, 5, two"
divide_result = divide_numbers.invoke(divide_test_input)
print("--- Testing DivideTool ---")
print(f"Input: {divide_test_input}")
print(f"Output: {divide_result}")