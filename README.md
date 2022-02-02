# Lab2
## ME 405 Lab 2 Repository

Our closed loop controller utilizes position feedback to command our test kit motors
to follow a step response and rotate a flywheel 1 rotation. Our controller utilizes proportional control of the form
*K<sub>P</sub>*(*&theta;<sub>ref</sub>* - *&theta;<sub>meas</sub>*). We implemented a logical statement that disables the
motor once it has completed one full rotation. The figures below display our progression
of tuning our proportional gain, *K<sub>P</sub>*, to improve the step response.


![Kp = 0.0001](kpof.0001.png)
<br>
Figure 1. Step response with input of 1 revolution; *K<sub>P</sub>* = 0.0001. The steady state 
error is small and the response is a ramp function, as expected.

![Kp = 1](kpof1.png)
<br>
Figure 2. Step response with input of 1 revolution; *K<sub>P</sub>* = 1. The steady state 
error is small and the response is a ramp function, as expected.

![Kp = 0.05](kpof.05.png)
<br>
Figure 3. Step response with input of 1 revolution; *K<sub>P</sub>* = 0.05. The steady state 
error is small and the response is a ramp function, as expected.