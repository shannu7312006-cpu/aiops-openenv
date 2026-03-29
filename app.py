import streamlit as st
from env import AIOpsEnv
from models import Action

st.title("🚀 AIOps OpenEnv Dashboard")

task = st.selectbox("Select Task", ["log_triage", "incident_response", "optimization"])

env = AIOpsEnv(task=task)

if st.button("Run Episode"):
    obs = env.reset()

    logs = []
    healths = []
    rewards = []

    done = False

    while not done:
        # simple rule-based agent for demo
        if "CPU" in obs.log:
            act = "scale_up"
        elif "Memory" in obs.log:
            act = "restart_service"
        else:
            act = "monitor"

        action = Action(action_type=act)

        obs, reward, done, info = env.step(action)

        logs.append(obs.log)
        healths.append(info["health"])
        rewards.append(reward.value)

    st.write("Logs:", logs)
    st.line_chart(healths)
    st.bar_chart(rewards)