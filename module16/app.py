
import streamlit as st

def main():
    st.title("Hello World")
    st.button("Click")
    if st.button("Kliko ketu"):
        st.write("Butoni u klikua")
    if st.checkbox("A i ki permi 18 vjet"):
        st.write("po")
    user_input = st.text_input("Enter Text", "Sample")
    st.write("Ti shkruajte:", user_input)
    age = st.number_input("Enter your age", min_value=0, max_value=100)
    st.write(f"Your age is {age}")

if __name__ == "__main__":
    main()