#!/bin/python3

# John Choi - jchoi16@student.cscc.edu / choi.1655@osu.edu
# Speed Sensor Lab, Camera Calibration Technique Calculation Script

import numpy

# ========================================
# GLOBAL
# ========================================
placements = [13.75, 14.675, 15.6, 16.9, 18.2, 19.65, 21.1, 23]  # placements in inches of corresponding frame
TIME_BETWEEN_FRAMES = 0.067  # unit: seconds
X_VAL = 43.25  # unit: inches


# ========================================
# FUNCTIONS
# ========================================

def calculate_frame_velocity():
    velocity_num = 2
    for i in range(len(placements) - 1):
        velocity = (placements[i + 1] - placements[i]) / TIME_BETWEEN_FRAMES
        velocity_meters_per_sec = velocity / 39.37
        print(
            "Vframe%d: %f inches per second, %f meters per second" % (velocity_num, velocity, velocity_meters_per_sec))
        velocity_num += 1


def calculate_velocity_at_sensor(frames, placement):
    x = numpy.array(frames)
    y = numpy.array(placement)
    m, b = numpy.polyfit(x, y, 1)
    v_sensor = m * X_VAL + b
    print("V at sensor: %f in/s" % v_sensor)


# ========================================
# MAIN
# ========================================

# Question 1a
print("Problem 1a...\n")
calculate_frame_velocity()

print("\nProblem 1b...\n")
trimmed_placements = placements[1:]
calculate_velocity_at_sensor([2, 3, 4, 5, 6, 7, 8], trimmed_placements)
