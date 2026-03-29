import random
from models import Observation, Action, Reward
from tasks import TASKS


class AIOpsEnv:
    def __init__(self, task="log_triage"):
        self.task = task
        self.step_count = 0
        self.system_health = 100
        self.current_log = None

    def reset(self):
        self.step_count = 0
        self.system_health = 100
        self.current_log = self._generate_log()
        return self._get_observation()

    def _generate_log(self):
        logs = [
            "CPU usage 99%",
            "Memory leak detected",
            "API failure 500 error",
            "Disk usage high",
            "Network latency spike"
        ]
        return random.choice(logs)

    def _get_observation(self):
        return Observation(
            log=self.current_log,
            system_health=self.system_health,
            step=self.step_count,
            task=self.task
        )

    def step(self, action: Action):
        self.step_count += 1

        grader = TASKS[self.task]

        # task-specific grading
        if self.task in ["log_triage", "incident_response"]:
            score = grader(self.current_log, action.action_type)
        else:
            score = grader(self.system_health, action.action_type)

        # reward shaping
        reward_value = score

        # system dynamics
        if action.action_type == "restart_service":
            self.system_health += 5
        elif action.action_type == "scale_up":
            self.system_health += 3
        elif action.action_type == "cleanup":
            self.system_health += 2
        else:
            self.system_health -= 2

        self.system_health = max(0, min(100, self.system_health))

        done = self.step_count >= 5

        reward = Reward(
            value=reward_value,
            reason="Grader-based + system impact"
        )

        obs = self._get_observation()

        # generate next log
        self.current_log = self._generate_log()

        return obs, reward, done, {"health": self.system_health}

    def state(self):
        return {
            "step": self.step_count,
            "health": self.system_health
        }