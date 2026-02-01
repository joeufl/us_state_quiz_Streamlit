import random
import pandas as pd
import streamlit as st

all_states = pd.read_csv("./data/50_states.csv")
# st.write(all_states)

# select random state
if "answer" not in st.session_state:
    st.session_state.answer = random.choice(all_states["state"])
if "guess_count" not in st.session_state:
    st.session_state.guess_count = 0
if "current_guesses" not in st.session_state:
    st.session_state.current_guesses = []
if "finished" not in st.session_state:
    st.session_state.finished = False
# additional items to add to session state

st.set_page_config(page_title="Geography Guessing Quiz", page_icon="🗺️")

st.title("🗺️ Geography Guessing Quiz (US States)")
st.caption("Guess the hidden state.")

with st.form("State Guess"):
    guess = st.selectbox("Guess a state:", all_states["state"])
    submit = st.form_submit_button()

if submit:
    if guess == st.session_state.answer:
        st.session_state.guess_count += 1
        st.write(f"You got it in {st.session_state.guess_count} tries!")
        st.session_state.finished = True
    elif st.session_state.finished == False and guess not in st.session_state.current_guesses:
        st.session_state.guess_count += 1
        st.session_state.current_guesses.append(guess)
    elif st.session_state.finished == False and guess in st.session_state.current_guesses:
        st.write("You already guessed this state.")
    submit = False

with st.sidebar:
    st.write("DEBUG answer:", st.session_state.answer)
    st.metric("Total Guesses", st.session_state.guess_count)
    if st.button("Reset"):
        st.session_state.clear()
        st.rerun(scope="app")