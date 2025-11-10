import streamlit as st

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by 0"
        else:
            return num1 / num2
    else:
        return "Invalid Operator"

# Streamlit UI
st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

operator = st.selectbox("Select an operator", ['+', '-', '*', '/'])

if st.button("Calculate"):
    result = calculator(num1, num2, operator)
    st.success(f"Result: {num1} {operator} {num2} = {result}")
