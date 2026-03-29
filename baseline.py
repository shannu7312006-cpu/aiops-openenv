import os
from openai import OpenAI
from env import AIOpsEnv
from models import Action

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

env = AIOpsEnv(task="log_triage")

obs = env.reset()

done = False
total_reward = 0

while not done:
    prompt = f"""
    You are an AIOps agent.

    Log: {obs.log}
    System Health: {obs.system_health}

    Choose one action:
    - scale_up
    - restart_service
    - cleanup
    - monitor

    Return ONLY the action name.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    action_text = response.choices[0].message.content.strip()

    action = Action(action_type=action_text)

    obs, reward, done, info = env.step(action)

    total_reward += reward.value

print("Final Score:", total_reward)