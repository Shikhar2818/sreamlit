import streamlit as st
import math
import time

# Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Function to display the scientific calculator on Home Page
def calculator():
    st.title("✨ Scientific Calculator ✨")
    st.markdown("<h2 style='text-align: center;'>Perform Various Mathematical Operations</h2>", unsafe_allow_html=True)

    # Use Streamlit columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        # Dropdown to select operation
        operation = st.selectbox(
            "Select operation:",
            ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root", "Sine", "Cosine", "Tangent"]
        )
    
    with col2:
        # Create an informative message
        st.info("Choose your operation and enter the numbers to see the result!")

    # Input fields for the calculator
    if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
        num1 = st.number_input("Enter first number:")
        num2 = st.number_input("Enter second number:")
        
    else:
        num1 = st.number_input("Enter the number:")

    # Perform operation based on user selection
    result = None
    progress_bar = st.progress(0.1)#progress is a tool to show the 
    if operation == "Addition":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = add(num1, num2)

    elif operation == "Subtraction":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = subtract(num1, num2)

    elif operation == "Multiplication":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = multiply(num1, num2)

    elif operation == "Division":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = divide(num1, num2)

    elif operation == "Power":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = power(num1, num2)

    elif operation == "Square Root":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = square_root(num1)

    elif operation == "Sine":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = sine(num1)

    elif operation == "Cosine":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = cosine(num1)

    elif operation == "Tangent":
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)
        result = tangent(num1)

    # Display the result with a formatted layout
    if result is not None:
        st.subheader("🔹 Result: 🔹")
        st.markdown(f"{result}", unsafe_allow_html=True)
    
    # Add some space for aesthetics
    st.markdown("<br>", unsafe_allow_html=True)

    # Optional: Add a footer or credits
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>By Team STAR</p>", 
        unsafe_allow_html=True
    )

# Main function to run the app
def main():
    calculator()

# Ensure the script runs correctly
if __name__ == "__main__":
    main()