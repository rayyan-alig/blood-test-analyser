## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools import tool
from langchain_community.document_loaders import PDFLoader

## Creating custom pdf reader tool
class BloodTestReportTool:
    
    @tool("Read data from blood test report PDF")
    def read_data_tool(self, path='data/sample.pdf'):
        """Read blood report PDF from the provided path and return the full report as string"""
        docs = PDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content

            # Remove extra newlines
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"

        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool:

    @tool("Analyze nutrition based on blood report")
    def analyze_nutrition_tool(self, blood_report_data: str):
        """Analyze the blood report and provide nutritional insights"""
        processed_data = blood_report_data.replace("  ", " ")  # Remove extra spaces

        # Placeholder logic
        return "Nutritional recommendations will be generated based on detailed report parsing."

## Creating Exercise Planning Tool
class ExerciseTool:

    @tool("Create an exercise plan based on blood report")
    def create_exercise_plan_tool(self, blood_report_data: str):
        """Create an exercise plan based on the blood report"""
        # Placeholder logic
        return "Exercise recommendations will be generated based on the patient’s health condition."
