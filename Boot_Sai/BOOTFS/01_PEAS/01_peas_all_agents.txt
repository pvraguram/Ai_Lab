============================================================
PEAS DESCRIPTION - TASK ENVIRONMENT ANALYSIS FOR AGENTS
============================================================
PEAS = Performance measure, Environment, Actuators, Sensors
 P - how we judge whether the agent is doing well
 E - the world the agent works in
 A - what the agent uses to ACT on the environment
 S - what the agent uses to PERCEIVE the environment
Also state the environment properties: observable, deterministic,
episodic/sequential, static/dynamic, discrete/continuous, single/multi-agent.


============================================================
1. SELF-DRIVING CAR (Automated Taxi)
============================================================
+-------------+---------------------------------------------------------+
| Performance | Safety (no accidents), reach correct destination,       |
|             | minimum travel time, fuel/energy efficiency, obey       |
|             | traffic laws, passenger comfort, maximize profit        |
+-------------+---------------------------------------------------------+
| Environment | Roads, highways, traffic, pedestrians, other vehicles,  |
|             | traffic signals, road signs, weather, passengers,       |
|             | potholes, speed breakers                                |
+-------------+---------------------------------------------------------+
| Actuators   | Steering, accelerator, brake, gear shift, indicators,   |
|             | horn, headlights, wipers, display/speaker for passenger |
+-------------+---------------------------------------------------------+
| Sensors     | Cameras, LIDAR, RADAR, ultrasonic sensors, GPS,         |
|             | speedometer, odometer, accelerometer/IMU, engine        |
|             | sensors, microphone, touchscreen (passenger input)      |
+-------------+---------------------------------------------------------+
Environment type: Partially observable, Stochastic, Sequential,
Dynamic, Continuous, Multi-agent.


============================================================
2. SMART HOME TEMPERATURE CONTROL AGENT (Smart Thermostat)
============================================================
+-------------+---------------------------------------------------------+
| Performance | Keep room at desired temperature (e.g. 22-25 C),        |
|             | minimum energy consumption / electricity bill, user     |
|             | comfort, fast response to changes, few on/off cycles    |
+-------------+---------------------------------------------------------+
| Environment | Rooms of the house, occupants, outside weather,         |
|             | doors/windows, AC, heater, fan, time of day             |
+-------------+---------------------------------------------------------+
| Actuators   | AC / heater ON-OFF switch, temperature set-point        |
|             | control, fan speed control, vents/dampers, mobile app   |
|             | notifications, display                                  |
+-------------+---------------------------------------------------------+
| Sensors     | Temperature sensor (thermistor), humidity sensor,       |
|             | occupancy / motion (PIR) sensor, door/window sensors,   |
|             | clock/timer, outdoor weather data, user input (app)     |
+-------------+---------------------------------------------------------+
Environment type: Partially observable, Stochastic, Sequential,
Dynamic, Continuous, Single-agent.


============================================================
3. MEDICAL DIAGNOSIS SYSTEM
============================================================
+-------------+---------------------------------------------------------+
| Performance | Correct diagnosis (accuracy), patient health/recovery,  |
|             | minimum cost and time, minimum unnecessary tests,       |
|             | low false negatives, avoid lawsuits                     |
+-------------+---------------------------------------------------------+
| Environment | Patient, hospital, doctors, nurses, lab, medical        |
|             | records, pharmacy                                       |
+-------------+---------------------------------------------------------+
| Actuators   | Display of questions, tests, diagnosis, treatments,     |
|             | prescriptions, referrals (screen / printed report)      |
+-------------+---------------------------------------------------------+
| Sensors     | Keyboard / touchscreen for symptoms and answers,        |
|             | lab test results, X-ray / MRI / CT scan images,         |
|             | patient history records, vital-sign monitors            |
+-------------+---------------------------------------------------------+
Environment type: Partially observable, Stochastic, Sequential,
Dynamic, Continuous, Single-agent.


============================================================
4. ANY REAL-WORLD AGENT - extra examples
============================================================
ROBOT VACUUM CLEANER
 P: % floor cleaned, time taken, battery use, no collisions
 E: Rooms, floor, dirt, furniture, walls, charging dock
 A: Wheels/motors, brushes, suction, bumper
 S: Dirt sensor, bump sensor, cliff sensor, camera, battery level

PART-PICKING ROBOT (factory)
 P: % parts placed in correct bin, speed
 E: Conveyor belt, parts, bins
 A: Jointed arm, gripper
 S: Camera, joint angle sensors

ONLINE ENGLISH TUTOR
 P: Student's test score improvement
 E: Students, testing agency
 A: Display of exercises, suggestions, corrections
 S: Keyboard entry, student answers

E-COMMERCE RECOMMENDER
 P: Click-through rate, purchases, customer satisfaction
 E: Website, users, product catalogue
 A: Display of recommended products, emails
 S: Clicks, search queries, purchase history, ratings
