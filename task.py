from crewai import Task
from agents import medical_doctor, nutritionist, exercise_specialist, verifier
from tools import BloodTestReportTool

# Task: Help with Patient Query
help_patients = Task(
    description="Analyze the user's query and provided blood report to identify any relevant medical issues or health conditions. Provide a clear and responsible summary with possible next steps.",
    expected_output="A concise, evidence-based medical summary with recommended actions or follow-up suggestions.",
    agent=medical_doctor,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)

# Task: Nutrition Advice
nutrition_analysis = Task(
    description="Analyze blood markers for nutritional deficiencies or imbalances. Provide personalized and science-backed dietary recommendations.",
    expected_output="A list of dietary suggestions, foods to include or avoid, and optionally supplements backed by credible sources.",
    agent=nutritionist,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)

# Task: Exercise Planning
exercise_planning = Task(
    description="Based on health indicators and blood report, recommend a safe and customized workout routine suitable to the user’s current condition.",
    expected_output="A detailed weekly fitness plan with exercise types, intensity levels, and rest periods tailored to the user's health data.",
    agent=exercise_specialist,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)

# Task: Report Verification
verification = Task(
    description="Verify if the uploaded document is a valid blood test report and identify its relevant components for further analysis.",
    expected_output="A simple status message verifying the document type and summary of what kind of blood data is present.",
    agent=verifier,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)