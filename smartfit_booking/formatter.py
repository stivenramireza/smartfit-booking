from datetime import datetime

import time

def get_current_date() -> str:
    return datetime.now().strftime("%d/%m/%Y")
    
def convert_24_to_12_hour(time_value: str) -> str:
    t = time.strptime(time_value, "%H:%M")
    return time.strftime("%I:%M %p", t)