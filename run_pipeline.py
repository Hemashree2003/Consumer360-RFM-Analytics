import os

print("Starting Consumer360 Analytics Pipeline...\n")

os.system("python Python/rfm.py")
os.system("python Python/cohort.py")
os.system("python Python/basket.py")

print("\nPipeline Executed Successfully!")