from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime, date
import json
import os
from typing import Optional, List

app = FastAPI(title="AI Health Buddy", description="Personal AI assistant for health and phone usage tracking")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data storage file
DATA_FILE = "health_data.json"

# Pydantic models
class JunkFoodEntry(BaseModel):
    date: str
    ate_junk_food: bool
    junk_food_cost: float = 50.0  # Default cost
    notes: Optional[str] = None

class PhoneUsageEntry(BaseModel):
    date: str
    usage_minutes: int
    limit_minutes: int = 180  # Default 3 hours
    notes: Optional[str] = None

class DailySummary(BaseModel):
    date: str
    junk_food_status: bool
    money_saved: float
    phone_usage: int
    phone_limit: int

# Helper functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"junk_food": [], "phone_usage": [], "settings": {"junk_food_cost": 50, "phone_limit": 180}}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# API Routes
@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/manifest.json")
async def manifest():
    return FileResponse("manifest.json")

@app.get("/service-worker.js")
async def service_worker():
    return FileResponse("service-worker.js")

@app.post("/api/junk-food")
async def log_junk_food(entry: JunkFoodEntry):
    data = load_data()
    
    # Check if entry for today already exists
    existing_entries = [e for e in data["junk_food"] if e["date"] == entry.date]
    if existing_entries:
        # Update existing entry
        for e in data["junk_food"]:
            if e["date"] == entry.date:
                e["ate_junk_food"] = entry.ate_junk_food
                e["junk_food_cost"] = entry.junk_food_cost
                e["notes"] = entry.notes
    else:
        # Add new entry
        data["junk_food"].append(entry.model_dump())
    
    save_data(data)
    return {"message": "Junk food entry logged successfully", "entry": entry}

@app.post("/api/phone-usage")
async def log_phone_usage(entry: PhoneUsageEntry):
    data = load_data()
    
    # Check if entry for today already exists
    existing_entries = [e for e in data["phone_usage"] if e["date"] == entry.date]
    if existing_entries:
        # Update existing entry
        for e in data["phone_usage"]:
            if e["date"] == entry.date:
                e["usage_minutes"] = entry.usage_minutes
                e["limit_minutes"] = entry.limit_minutes
                e["notes"] = entry.notes
    else:
        # Add new entry
        data["phone_usage"].append(entry.model_dump())    
    save_data(data)
    return {"message": "Phone usage logged successfully", "entry": entry}

@app.get("/api/summary")
async def get_summary():
    data = load_data()
    
    total_days_tracked = len(data["junk_food"])
    healthy_days = sum(1 for e in data["junk_food"] if not e["ate_junk_food"])
    total_money_saved = sum(e["junk_food_cost"] for e in data["junk_food"] if not e["ate_junk_food"])
    
    # Phone usage stats
    total_phone_entries = len(data["phone_usage"])
    avg_usage = sum(e["usage_minutes"] for e in data["phone_usage"]) / total_phone_entries if total_phone_entries > 0 else 0
    over_limit_days = sum(1 for e in data["phone_usage"] if e["usage_minutes"] > e["limit_minutes"])
    
    return {
        "total_days_tracked": total_days_tracked,
        "healthy_days": healthy_days,
        "junk_food_days": total_days_tracked - healthy_days,
        "total_money_saved": round(total_money_saved, 2),
        "avg_phone_usage": round(avg_usage, 2),
        "over_limit_days": over_limit_days,
        "total_phone_entries": total_phone_entries
    }

@app.get("/api/entries")
async def get_all_entries():
    data = load_data()
    return data

@app.get("/api/today")
async def get_today_status():
    data = load_data()
    today = date.today().isoformat()
    
    junk_food_entry = next((e for e in data["junk_food"] if e["date"] == today), None)
    phone_usage_entry = next((e for e in data["phone_usage"] if e["date"] == today), None)
    
    return {
        "date": today,
        "junk_food": junk_food_entry,
        "phone_usage": phone_usage_entry
    }

@app.get("/api/motivational-quote")
async def get_motivational_quote():
    quotes = [
        "Your body is a temple. Keep it pure and clean.",
        "Small progress is still progress!",
        "Every healthy choice brings you closer to your goals.",
        "You are stronger than your cravings!",
        "Focus on progress, not perfection.",
        "Time spent offline is time well spent on yourself.",
        "Digital detox leads to mental clarity.",
        "Your future self will thank you for today's choices."
    ]
    import random
    return {"quote": random.choice(quotes)}



@app.get("/api/monthly-stats")
async def get_monthly_stats(year: int = None, month: int = None):
    from datetime import datetime
    data = load_data()
    
    # Use current month if not specified
    if year is None or month is None:
        now = datetime.now()
        year = now.year
        month = now.month
    
    month_str = f"{year}-{month:02d}"
    
    # Filter entries for the specific month
    junk_food_month = [e for e in data["junk_food"] if e["date"].startswith(month_str)]
    phone_usage_month = [e for e in data["phone_usage"] if e["date"].startswith(month_str)]
    
    # Calculate monthly stats
    total_days = len(junk_food_month)
    junk_food_days = sum(1 for e in junk_food_month if e["ate_junk_food"])
    healthy_days = total_days - junk_food_days
    money_saved = sum(e["junk_food_cost"] for e in junk_food_month if not e["ate_junk_food"])
    
    # Phone usage stats
    total_phone_days = len(phone_usage_month)
    avg_phone_usage = sum(e["usage_minutes"] for e in phone_usage_month) / total_phone_days if total_phone_days > 0 else 0
    over_limit_days = sum(1 for e in phone_usage_month if e["usage_minutes"] > e["limit_minutes"])
    
    return {
        "year": year,
        "month": month,
        "total_days_tracked": total_days,
        "junk_food_days": junk_food_days,
        "healthy_days": healthy_days,
        "money_saved": round(money_saved, 2),
        "avg_phone_usage": round(avg_phone_usage, 2),
        "over_limit_days": over_limit_days,
        "total_phone_days": total_phone_days
    }

@app.get("/api/daily-report")
async def get_daily_report(date_str: str = None):
    from datetime import date as dt_date
    data = load_data()
    
    # Use today if not specified
    if date_str is None:
        date_str = dt_date.today().isoformat()
    
    junk_food_entry = next((e for e in data["junk_food"] if e["date"] == date_str), None)
    phone_usage_entry = next((e for e in data["phone_usage"] if e["date"] == date_str), None)
    
    report = {
        "date": date_str,
        "junk_food_logged": junk_food_entry is not None,
        "phone_usage_logged": phone_usage_entry is not None,
    }
    
    if junk_food_entry:
        report["ate_junk_food"] = junk_food_entry["ate_junk_food"]
        report["junk_food_cost"] = junk_food_entry["junk_food_cost"]
        report["money_saved"] = 0 if junk_food_entry["ate_junk_food"] else junk_food_entry["junk_food_cost"]
        report["junk_food_notes"] = junk_food_entry.get("notes", "")
    
    if phone_usage_entry:
        report["usage_minutes"] = phone_usage_entry["usage_minutes"]
        report["limit_minutes"] = phone_usage_entry["limit_minutes"]
        report["over_limit"] = phone_usage_entry["usage_minutes"] > phone_usage_entry["limit_minutes"]
        report["phone_notes"] = phone_usage_entry.get("notes", "")
    
    return report
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
