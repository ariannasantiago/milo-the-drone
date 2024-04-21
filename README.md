## MILO the Drone

This repo containts the source code for our senior design low-cost UAV drone project.

This Modular Intelligent Low-cost Observer (MILO) drone uses a non-stereo camera running YOLO to detect people, then uses a reactive architecture to send control signals via MAVLink to a Pixhawk 6C flight controller to follow the closest person. 

### Work Completed
Rules/comnands: a set of rules to be executed in the following order: Backoff, Follow, Search, NoDetection. The first three assume a closest person detection has been established/selected, the last assumes that no detection has been established and this another is necessary.

Core state machine: What happens when the drone is switched into guided mode (to execute this program). Contains basic state machine logic for operation from ground/before takeoff, after takeoff, while the program is running, and if connection is lost.

Image Processing: Bounding boxes placed around person detections. Confidence levels are placed over each detection.

Project created for 2024 Vanderbilt ECE Senior Design Day by ECE Team 8.
