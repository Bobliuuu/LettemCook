import streamlit as st
import pandas as pd
import time
import redis

# Function to simulate user actions with random durations
def simulate_user_actions():
    actions = []
    actions.append({'Action': 'Linear Algebra', 'Duration': 3})
    actions.append({'Action': 'Break', 'Duration': 5})
    actions.append({'Action': 'CS Assignment', 'Duration': 2})
    return pd.DataFrame(actions)

# Streamlit app
def main():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    st.title("StudySnitch Analytics")

    actions_df = simulate_user_actions()

    st.subheader("User Actions and Durations")
    st.table(actions_df)

    st.subheader("Graph of Action Durations")
    st.line_chart(actions_df['Duration'])

    inattention_count = print(r.get('bad'))
    st.info(f"User didn't pay attention {inattention_count} times.")

if __name__ == "__main__":
    main()
