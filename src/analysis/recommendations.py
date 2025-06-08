from typing import Dict, List

def generate_recommendations(insights: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
    """
    Generate improvement recommendations for each bank based on pain points and drivers.
    Returns a dictionary: {bank: [recommendations]}
    """
    recs = {}
    for bank, vals in insights.items():
        recs[bank] = []
        # Suggest addressing pain points
        for pain in vals['painpoints']:
            recs[bank].append(f"Address customer concern: '{pain}' (e.g., improve this area)")
        # Suggest leveraging drivers
        for driver in vals['drivers']:
            recs[bank].append(f"Promote strength: '{driver}' (e.g., highlight in marketing)")
    return recs
