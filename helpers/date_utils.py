from datetime import datetime

def is_future_match(match):
    kickoff = datetime.fromisoformat(match["kickoffDate"])
    return kickoff > datetime.now()

def is_bettable(match):
    return (
        "odds" in match
        and isinstance(match["odds"], dict)
        and all(k in match["odds"] for k in ["home", "draw", "away"])
    )