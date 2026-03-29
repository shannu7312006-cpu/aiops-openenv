def grader_log_triage(log, action):
    if "CPU" in log and action == "scale_up":
        return 1.0
    if "Memory" in log and action == "restart_service":
        return 1.0
    return 0.2


def grader_incident_response(log, action):
    if "API" in log and action == "restart_service":
        return 1.0
    if "Disk" in log and action == "cleanup":
        return 1.0
    return 0.3


def grader_optimization(system_health, action):
    if system_health > 80 and action == "monitor":
        return 1.0
    elif system_health < 50 and action in ["scale_up", "restart_service"]:
        return 0.8
    return 0.4


TASKS = {
    "log_triage": grader_log_triage,
    "incident_response": grader_incident_response,
    "optimization": grader_optimization
}