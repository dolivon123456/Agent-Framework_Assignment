import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = "YOUR OPENAI API KEY"

# Use a local model through Ollama (openhermes)
from langchain.llms import Ollama
ollama_llm = Ollama(model="openhermes")

# Define your agents with roles and goals
researcher = Agent(
    role='Researcher',
    goal='Develop ideas for teaching someone new to the subject.',
    backstory="""As a researcher, your task is to explore the subject thoroughly and develop ideas that make it easy for someone new to understand. Your insights will be used by the writer to create educational content.""",
    verbose=True,
    allow_delegation=False,
    tools=[ollama_llm]
)

writer = Agent(
    role='Writer',
    goal='Write educational content based on Researcher’s ideas.',
    backstory="""You are a skilled writer tasked with transforming the researcher's insights into clear and engaging educational content. Your goal is to explain the topic in a way that is accessible to someone new to the subject.""",
    verbose=True,
    allow_delegation=True,
    tools=[ollama_llm]
)

examiner = Agent(
    role='Examiner',
    goal='Craft 2-3 test questions with correct answers based on the educational content.',
    backstory="""As an examiner, your responsibility is to create test questions that assess the reader's understanding of the educational content created by the writer. Craft 2-3 questions with clear and correct answers.""",
    verbose=True,
    allow_delegation=False,
    tools=[ollama_llm]
)

# Create tasks for your agents
task1 = Task(
    description="""Develop ideas for teaching someone new to the subject. Provide detailed insights and concepts that can be used by the writer to create educational content.""",
    agent=researcher
)

task2 = Task(
    description="""Write a piece of text to explain the topic based on the researcher's insights. Ensure the content is clear, engaging, and accessible to someone new to the subject.""",
    agent=writer
)

task3 = Task(
    description="""Craft 2-3 test questions to evaluate understanding of the created text. Include clear and correct answers to assess whether a student has fully understood the content.""",
    agent=examiner
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer, examiner],
    tasks=[task1, task2, task3],
    verbose=2
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
