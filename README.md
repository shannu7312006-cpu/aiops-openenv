# AIOps Multi-Agent OpenEnv Simulation for Autonomous Incident Management

## Project Description
This project is an OpenEnv-compliant AI environment that simulates real-world IT operations tasks such as log triage, incident response, and system optimization. It enables an autonomous agent to interact with system logs and states, take actions, and optimize performance using a structured reward system.

---

## Problem Statement
Modern IT systems generate large volumes of logs and incidents that require quick diagnosis and resolution. Manual handling is time-consuming and error-prone. This project addresses the need for an intelligent autonomous agent that can analyze logs, respond to incidents, and optimize system performance efficiently.

---

## Solution Overview
The project implements a simulated AIOps environment where an AI agent interacts with system logs and states. It follows the OpenEnv specification and includes:

- Structured observation and action spaces  
- Multi-task environment  
- Reward-based evaluation system  
- Baseline inference using an LLM agent  
- Streamlit dashboard for visualization  

---

## System Architecture

- `env.py` → Core environment logic implementing OpenEnv interface  
- `models.py` → Typed Pydantic models for observation, action, reward  
- `tasks.py` → Definitions of tasks and grader logic  
- `baseline.py` → Baseline LLM agent for evaluation  
- `app.py` → Streamlit dashboard for visualization  
- `openenv.yaml` → Environment configuration metadata  
- `requirements.txt` → Dependencies  
- `Dockerfile` → Containerization setup  

---

## Features

- OpenEnv-compliant environment  
- Real-world AIOps simulation  
- Three tasks with increasing difficulty  
- Programmatic graders for scoring  
- Reward function with partial progress signals  
- Baseline inference script using OpenAI API  
- Streamlit-based interactive dashboard  
- Docker support for deployment  
- Hugging Face Spaces compatible  

---

## Observation and Action Space

**Observation includes:**
- System logs  
- Incident status  
- Resource utilization metrics  

**Actions include:**
- Restart services  
- Scale resources  
- Analyze logs  
- Apply optimizations  

---

## Tasks

1. **log_triage (Easy)**  
   Identify and classify system logs to detect issues.

2. **incident_response (Medium)**  
   Respond to system incidents by taking corrective actions.

3. **optimization (Hard)**  
   Optimize system performance by selecting efficient strategies.

---

## Reward Function

- Rewards are assigned based on task progress  
- Partial rewards are given for intermediate correct actions  
- Penalties are applied for incorrect or inefficient actions  
- Final score is normalized between 0.0 and 1.0  

---

## Baseline Agent

- Uses OpenAI API via environment variable `OPENAI_API_KEY`  
- Interacts with the environment step-by-step  
- Produces reproducible evaluation scores across all tasks  

---

## Installation

```bash
git clone <your-repo-url>
cd <your-project-folder>
pip install -r requirements.txt

---

## ▶️ How to Run

First, install the required dependencies:

```bash
pip install -r requirements.txt
