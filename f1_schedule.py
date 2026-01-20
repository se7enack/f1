import requests

def get_f1_schedule(year=2026):
    url = f"https://api.openf1.org/v1/meetings?year={year}"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()

    meetings = resp.json()

    schedule = []
    for i, m in enumerate(meetings, start=1):
        schedule.append({
            "round": i,
            "name": m.get("meeting_name"),
            "start": m.get("date_start")[:10],
            "end": m.get("date_end")[:10],
            "location": m.get("location"),
            "country": m.get("country_name"),
            "circuit": m.get("circuit_short_name"),
        })

    return schedule
