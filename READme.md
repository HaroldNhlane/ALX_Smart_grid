This project aims to address the challenges of traditional power grids, which suffer from slow failure response, inefficient load distribution, and a lack of real-time monitoring. The solution is an IoT-based smart grid with automated fault detection, priority-based load balancing, and cloud analytics. Key features include real-time sensor monitoring for current and temperature , automated power rerouting using relays , and a web dashboard for remote control.





Problem Statement
Zambia's electricity infrastructure is plagued by frequent and prolonged outages due to its climate-dependent hydropower vulnerability and aging transmission lines. This leads to significant economic losses, with businesses losing an estimated $656 million annually. It also has severe social consequences, including life-threatening equipment failures in hospitals and extended blackouts in schools and rural communities. Technical limitations include a lack of real-time grid health monitoring and a reactive, rather than proactive, maintenance approach.





Objectives
The project has the following specific objectives:

To develop an IoT-based fault detection system that uses current sensors, temperature sensors, and relays to monitor grid health in real-time.

To design a priority-based power distribution algorithm that can assign dynamic load priorities to critical services like hospitals over industries or households.

To build a cloud-based monitoring and control dashboard using platforms like ThingSpeak for real-time data visualization and remote management.

To optimize energy efficiency and reduce costs by minimizing manual intervention and cutting diesel generator dependency by 30%.

Methodology
The project follows an iterative development cycle using an Agile methodology with three main sprints: hardware prototyping, algorithm design, and cloud dashboard deployment. The system architecture is a three-tier model:


Edge Layer (Data Acquisition): This layer consists of IoT nodes (Arduino/Raspberry Pi) and sensors deployed on grid lines to collect real-time data on current, voltage, and temperature.



Middleware Layer (Processing): An OM2M server standardizes communication, and a Python-based priority algorithm aggregates sensor data and triggers automated relay actions during failures. The 


simulate.py script is used to model grid failure scenarios.


Cloud/User Layer (Control & Visualization): This layer uses ThingSpeak and Node-RED to store data, provide real-time grid health monitoring, and enable manual overrides via a web or mobile interface for grid operators.


Tools and Technologies
Category	Tools/Technologies	Purpose
Hardware	Arduino/Raspberry Pi	
Microcontroller for sensor data processing.

ACS712 Current Sensors	
Detects overloads and faults.

DS18B20 Temperature Sensors	
Monitors equipment overheating.

Electromechanical Relays	
Automates power rerouting.

Software	OM2M	
IoT middleware for device interoperability.

ThingSpeak	
Cloud-based data visualization and analytics.

Python (PyFirmata, Pandas)	
Used for algorithm development and data analysis.

simulate.py	Used for simulating data and grid failure scenarios.
Communication	LoRa	
Low-bandwidth, long-range data transmission for rural areas.

Wi-Fi	
High-speed connectivity for urban nodes.


Export to Sheets
Project Budget (for Prototype)
The total estimated budget for the prototype is 

6,525 ZMW.

Category	Item	Unit Cost (ZMW)	Qty	Total (ZMW)
Hardware	Raspberry Pi 4	800	1	
800 

Arduino Nano	250	5	
1,250 

ACS712 Sensors	125	5	
625 

DS18B20 Sensors	80	5	
400 

5V Relays	150	5	
750 

LoRa Modules	600	2	
1,200 

Software	ThingSpeak	0	1	
0 

Miscellaneous	Breadboards/Wires	-	-	
500 

Contingency	-	-	
1,000 


Export to Sheets
Project Timeline (5 Weeks)
The project is a five-week endeavor focused on a prototype deliverable.


Week 1: Purchase all hardware components and assemble a functional hardware testbed.


Week 2: Calibrate current and temperature sensors. Code the priority logic in Python and assemble the sensor nodes and relays.



Week 3: Integrate the Python logic with OM2M/ThingSpeak to create an end-to-end data pipeline.


Week 4: Conduct use case simulations and test scenarios like overloads and drought-induced outages.



Week 5: Deploy the prototype in a pilot site and validate the outage response time. Demonstrate the automated load-shedding and end-to-end data pipeline.



Project Team

STUDENT NAME: Harold Nhlane 

Program Name: Backed Software Engineering 


