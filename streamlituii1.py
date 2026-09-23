import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊")

st.title("✊ Rock Paper Scissors ✋✌️")

# Initialize scores using session_state
if "human_score" not in st.session_state:
    st.session_state.human_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.subheader(
    f"Score → You: {st.session_state.human_score} | Computer: {st.session_state.comp_score}"
)

# Stop game if someone reaches 5
if st.session_state.human_score == 5:
    st.success("🎉 Congrats! You won the game!")
    st.session_state.game_over = True

elif st.session_state.comp_score == 5:
    st.error("💻 Computer won the game!")
    st.session_state.game_over = True

# Buttons for choices
if not st.session_state.game_over:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("✊ Rock"):
            you = 1
    with col2:
        if st.button("✋ Paper"):
            you = 2
    with col3:
        if st.button("✌️ Scissors"):
            you = 3

    if "you" in locals():
        comp = random.randint(1, 3)

        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        st.write(f"🧠 Computer chose **{choices[comp]}**")

        if (you == 1 and comp == 3) or \
           (you == 2 and comp == 1) or \
           (you == 3 and comp == 2):
            st.session_state.human_score += 1
            st.success("You won this round! 🎉")

        elif you == comp:
            st.info("It's a tie 🤝")

        else:
            st.session_state.comp_score += 1
            st.error("Computer won this round 💻")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.human_score = 0
    st.session_state.comp_score = 0
    st.session_state.game_over = False
