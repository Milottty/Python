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
    message = st.text_area("Enter a message:")
    st.write(f"You message: {message}")
    choices = st.radio("Pick one", ["Choice 1 ","Choice 2 ","Choice 3"])
    st.write(f"You choice: {choices}")
    if st.button("Success"):
        st.success("Operation was successful")
    try:
        1/0
    except Exception as e:
        st.exception(e)

if __name__ == "__main__":
    main()