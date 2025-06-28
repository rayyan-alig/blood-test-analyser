from crewai import Agent
from tools import BloodTestReportTool, search_tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4')

# Medical Doctor Agent
medical_doctor = Agent(
    role="Medical Doctor",
    goal="Analyze and interpret medical data responsibly based on evidence-based practices.",
    verbose=True,
    memory=True,
    backstory="You are a certified physician providing accurate, safe, and actionable medical advice based on blood test reports and user queries.",
    tools=[BloodTestReportTool.read_data_tool, search_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)

# Nutritionist Agent
nutritionist = Agent(
    role="Nutrition Expert",
    goal="Provide personalized and evidence-based nutritional guidance using blood test data.",
    verbose=True,
    memory=True,
    backstory="You are a licensed nutritionist who recommends safe and effective dietary practices based on medical test reports and known nutritional science.",
    tools=[BloodTestReportTool.read_data_tool, search_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)

# Exercise Specialist Agent
exercise_specialist = Agent(
    role="Fitness and Exercise Planner",
    goal="Create safe and personalized exercise plans considering individual health metrics.",
    verbose=True,
    memory=True,
    backstory="You are a certified fitness trainer and physiologist, crafting fitness routines based on users' physical condition and health reports.",
    tools=[BloodTestReportTool.read_data_tool, search_tool],
    llm=llm,
    max_iter=3,
    max_rpm=2,
    allow_delegation=False
)

# Verifier Agent
verifier = Agent(
    role="Medical File Verifier",
    goal="Check if a document is a valid medical or blood test report and flag irregularities.",
    verbose=True,
    memory=True,
    backstory="You are a data analyst specializing in medical records. You identify if files are blood test reports and flag inconsistencies or errors.",
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=2,
    allow_delegation=False
)
