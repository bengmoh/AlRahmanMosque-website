from typing import Dict, Tuple, Optional
import csv 

def iqama(prayer: str, athan: str) -> str:
    """return iqama time given prayer and athan time"""
    match prayer:
        case "Fajr":
            return add_time(athan, 15) # iqama after at least 15 minutes from the athan
        case "Dhuhr":
            return add_time(athan, 15) 
        case "Asr":
            return add_time(athan, 15) 
        case "Maghrib":
            return add_time(athan, 5, round_to_quarter=False) 
        case "Isha":
            return add_time(athan, 15)
        case _:
            return None # handles Sunrise because it has no Iqama


def add_time(athan: str, time: int, round_to_quarter: bool=True):
    athan, meridiem = athan.split()
    h, m = athan.split(":") 
    m = int(m)+time
    
    while m >= 60: # for adding time
        m -= 60
        h = str((int(h)+1)%12)
        
    while m < 0: # for subtracting time (time < 0)
        m += 60
        h = str((int(h)-1)%12)
        
    m = str(m)
    if len(m) == 1:
        m = "0"+m
    if round_to_quarter:
        h, m = quarter(h, m)
    return f"{h}:{m} {meridiem}"


def quarter(h: str, m: str):
    if m > "45":
        h, m = str((int(h)+1)%12), "00"
    else:
        m = "00" if m == "00" else "15" if m <= "15" else "30" if m <= "30" else "45"
    return h, m


def compare_iqama_times(today_file: str, tomorrow_file: str) -> Optional[Dict[str, Tuple[str, str]]]:
    """
    Compare today's and tomorrow's prayer times to detect changes.
    Returns a dictionary of changes with prayer name as key and (old_time, new_time) as value.
    """
    def read_times(file_path: str) -> dict:
        times = {}
        try:
            with open(file_path) as f:
                reader = csv.reader(f)
                for row in reader:
                    prayer, _, iqama = row
                    times[prayer] = iqama
        except FileNotFoundError:
            return {}
        return times

    today_times = read_times(today_file)
    tomorrow_times = read_times(tomorrow_file)
    
    if not today_times or not tomorrow_times:
        return None

    changes = {}
    for prayer in today_times:
        if prayer in tomorrow_times and today_times[prayer] != tomorrow_times[prayer]:
            changes[prayer] = (today_times[prayer], tomorrow_times[prayer])
    
    return changes if changes else None