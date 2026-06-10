"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice basketball skills and compete in interschool games",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["mason@mergington.edu", "lily@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Train for soccer matches and learn teamwork on the field",
        "schedule": "Tuesdays and Fridays, 3:45 PM - 5:15 PM",
        "max_participants": 22,
        "participants": ["evelyn@mergington.edu", "liam@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Improve swim technique and endurance with lap practice",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["henry@mergington.edu", "zoe@mergington.edu"]
    },
    "Yoga Club": {
        "description": "Build strength, flexibility, and mindfulness through yoga",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 25,
        "participants": ["sophia@mergington.edu", "liam@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Explore painting, drawing, and mixed media projects",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["ava@mergington.edu", "noah@mergington.edu"]
    },
    "Photography Club": {
        "description": "Capture images and learn about composition, lighting, and editing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["olivia@mergington.edu", "sophia@mergington.edu"]
    },
    "Creative Writing Workshop": {
        "description": "Write stories, poems, and essays while receiving feedback",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "mason@mergington.edu"]
    },
    "Drama Club": {
        "description": "Develop acting skills and produce school theater performances",
        "schedule": "Fridays, 3:30 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["mia@mergington.edu", "ethan@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Solve advanced math problems and prepare for competitions",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "alex@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific ideas together",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["jack@mergington.edu", "mia@mergington.edu"]
    },
    "Robotics Team": {
        "description": "Design robots and compete in engineering challenges",
        "schedule": "Mondays and Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 16,
        "participants": ["charlotte@mergington.edu", "alex@mergington.edu"]
    },
    "Debate Team": {
        "description": "Practice public speaking and research for debate events",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["charlotte@mergington.edu", "jack@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

# Validate student is not already signed up    if email in activity["participants"]:
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
