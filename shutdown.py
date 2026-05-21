import os
import time

shutdown_after_minutes = int(input("Enter shutdown time in minutes: "))

seconds = shutdown_after_minutes * 60

print(f"System will shutdown in {shutdown_after_minutes} minutes")

time.sleep(seconds)

os.system("shutdown /s /t 1")
