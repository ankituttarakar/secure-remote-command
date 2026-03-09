import datetime

def log_event(message):
    with open("audit_log.txt", "a") as f:
        time = datetime.datetime.now()
        f.write(f"[{time}] {message}\n")