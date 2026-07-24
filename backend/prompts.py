
"""
SpaceMission AI Prompt Templates

Contains prompt definitions used for
IBM Granite / Large Language Model interaction.
"""


def build_mission_prompt(
        mission,
        goal,
        constraints
):


    prompt = f"""
You are an AI assistant specialized in
space mission planning.


Analyze the following mission information.


Mission Target:

{mission}


Mission Goal:

{goal}


Mission Constraints:

{constraints}



Provide:

1. Mission planning suggestions
2. Possible risks
3. Resource optimization strategies
4. Safety recommendations



Your answer should be clear and useful
for aerospace engineers.
"""


    return prompt





def build_telemetry_prompt(
        telemetry
):


    prompt = f"""
You are an AI spacecraft monitoring assistant.


Analyze the following spacecraft telemetry data.


Telemetry:

{telemetry}



Identify:

1. Possible anomalies
2. System risks
3. Recommended actions
4. Mission impact



Provide a concise engineering report.
"""


    return prompt
