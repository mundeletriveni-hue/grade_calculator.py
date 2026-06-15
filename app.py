import streamlit as st

st.title("Grade Calculator")

name = st.text_input("Enter Student Name")

marks = st.number_input(
    "Enter Marks (0-100)",
    min_value=0,
    max_value=100
)

if st.button("Calculate Grade"):

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    st.write("Student Name:", name)
    st.write("Marks:", marks)
    st.success(f"Grade: {grade}")
