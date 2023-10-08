import streamlit as st
import pandas as pd
import time

# Function to simulate user actions with random durations
def simulate_user_actions(num_actions):
    actions = []
    for i in range(num_actions):
        action_duration = round(2 + 3 * i + 2 * (i % 3) * (i % 2), 2)  # Adjust as needed
        actions.append({'Action': f'Action {i+1}', 'Duration': action_duration})
        #time.sleep(action_duration)  # Simulate user taking time for the action
    return pd.DataFrame(actions)

# Streamlit app
def main():
    st.title("Attention Tracker App")

    num_actions = st.slider("Number of Actions", min_value=5, max_value=30, value=10)

    actions_df = simulate_user_actions(num_actions)

    st.subheader("User Actions and Durations")
    st.table(actions_df)

    st.subheader("Graph of Action Durations")
    st.line_chart(actions_df['Duration'])

    inattention_count = 3
    st.info(f"User didn't pay attention {inattention_count} times.")

if __name__ == "__main__":
    main()
