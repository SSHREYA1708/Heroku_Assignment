import streamlit as st


st.write("""
# Whether the given number is even or odd
""")

#Get Input
st.header('User Input Parameters')


def user_input_features():
    num = st.number_input("Number",step=1)
    if(num%2==0):
        return f'The number {num} is an even number.'
    else:
        return f'The number {num} is an odd number.'

result=user_input_features()

st.subheader('Result')
st.write(result)
