### README.md (Documentation File)

```markdown
# Agent Framework Assignment

This repository contains the code for an agent framework designed to generate questions and answers on a specific topic using the CrewAI agent frameworks in Python.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Install required packages using the following command:

  ```bash
  pip install -r requirements.txt
  ```

### Configuration

1. Replace "YOUR OPENAI API KEY" in the code with your actual OpenAI API key.

2. Adjust other configuration parameters as needed based on your assignment requirements.

## Usage

Run the main script to initiate the agent workflow:

```bash
python writer.py
```

## Agents and Tasks

- **Researcher:** Develops ideas for teaching someone new to the subject.
- **Writer:** Writes educational content based on the Researcher’s ideas.
- **Examiner:** Crafts 2-3 test questions with correct answers based on the educational content.

## Models Used

- Ollama's "openhermes" model with a maximum of 7 billion parameters.

## Results

The agents collaborate to generate educational content and test questions based on the specified roles and goals.

```

### requirements.txt (Requirements File)
```
crewai==0.1.0
langchain==0.1.0
```
