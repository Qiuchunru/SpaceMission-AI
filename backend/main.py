
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai import analyze_mission, analyze_telemetry


app = FastAPI(
    title="SpaceMission AI",
    description="AI-powered space mission assistant",
    version="1.0"
)


# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class MissionRequest(BaseModel):
    mission: str
    goal: str
    constraints: str



class TelemetryRequest(BaseModel):
    telemetry: str



@app.get("/")
def home():

    return {
        "message":
        "SpaceMission AI API Running"
    }



@app.post("/mission/analyze")
def mission_analysis(
        request: MissionRequest):

    result = analyze_mission(
        request.mission,
        request.goal,
        request.constraints
    )

    return {
        "analysis": result
    }



@app.post("/telemetry/analyze")
def telemetry_analysis(
        request: TelemetryRequest):

    result = analyze_telemetry(
        request.telemetry
    )

    return {
        "analysis": result
    }
