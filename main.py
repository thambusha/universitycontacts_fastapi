from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Simulated database
university_contacts = {
    "harvard university": {
        "phone": "+1 617-495-1000",
        "email": "info@harvard.edu",
        "website": "https://www.harvard.edu"
    },
    "stanford university": {
        "phone": "+1 650-723-2300",
        "email": "info@stanford.edu",
        "website": "https://www.stanford.edu"
    },
    "university of oxford": {
        "phone": "+44 1865 270000",
        "email": "information.office@admin.ox.ac.uk",
        "website": "https://www.ox.ac.uk"
    }
}

@app.get("/university")
def get_university_contact(name: str):
    name = name.lower()
    contact = university_contacts.get(name)
    if contact:
        return {"university": name.title(), "contact": contact}
    return {"error": "University not found"}
