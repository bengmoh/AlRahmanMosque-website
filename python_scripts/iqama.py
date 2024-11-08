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
            return add_time(athan, 8, round_to_next_quarter=False) 
        case "Isha":
            return add_time(athan, 15)
        case _:
            return None # handles Sunrise because it has no Iqama


def add_time(athan: str, time: int, round_to_next_quarter: bool=True):
    athan, meridiem = athan.split()
    h, m = athan.split(":") 
    m = int(m)+time
    if m >= 60:
        m -= 60
        h = str((int(h)+1)%12)
    m = str(m)
    if len(m) == 1:
        m = "0"+m
    if round_to_next_quarter:
        h, m = next_quarter(h, m)
    return f"{h}:{m} {meridiem}"


def next_quarter(h: str, m: str):
    if m > "45":
        h, m = str((int(h)+1)%12), "00"
    else:
        m = "00" if m == "00" else "15" if m <= "15" else "30" if m <= "30" else "45"
    return h, m