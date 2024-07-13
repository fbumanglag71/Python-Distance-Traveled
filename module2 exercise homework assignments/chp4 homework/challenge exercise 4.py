## Author: Francisco Bumanglag
## Project: Distance Traveled
## Assignment: Module 2 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 24, 2023


speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

print("Hour\tDistance Traveled")
print("-----------------------")

for hour in range(1, hours + 1):
    distance = speed * hour
    print(hour, "\t", distance)
