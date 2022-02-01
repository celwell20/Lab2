"""@file        main.py
   @brief       Closed loop motor control main module
   @details     Runs closed loop proportional control step response test
   @author        Clayton Elwell
   @author        Tyler McCue
   @date          January 27, 2022
"""

import encoder_elwell_mccue as enc
import motor_elwell_mccue as moe
import controller_elwell_mccue as control
import pyb
import utime

if __name__ == '__main__':
    flag = True
    ## Driver object for first motor
    motor1 = moe.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    
    ## Driver object for second motor
    #motor2 = moe.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    #motor2.enable()
    
    ## Driver object for first encoder
    #enc1 = enc.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    ## Driver object for second encoder
    enc2 = enc.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    
    #enc1.set_position(0)
    enc2.set_position(0)
    
    control = control.ClosedLoop(-100, 100, .05,0)
    
    while True:
        
        try:
            
            x = input()
            
            if x == 'a':
                
                ref = input().decode('utf-8')
                print(ref)
                control.set_setpoint(float(ref))
                
                #print('New setpoint: ' + float(ref))
            
            if x == 'b':
                
                kp = input().decode('utf-8')
    
                control.set_Kp(float(kp))
                
                print('New proportional gain: ' + float(kp))
                
            if x == 'c':
                print('Running step response, and printing collected data after response completion')
                
                while flag == True:
                
                    motor1.enable()
                    update = enc2.update()
            
                    if abs(update) >= control.get_setpoint():
                        motor1.set_duty_cycle(0)
                        motor1.disable()
                        control.print_data()
                        flag = False
                        
                    duty = control.duty(update)
            
#                     if duty <= 15:
#                         motor1.set_duty_cycle(0)
#                         motor1.disable
#                         control.print_data()
#                         flag = False
                    motor1.set_duty_cycle(duty)
                    
        except KeyboardInterrupt:
            motor1.set_duty_cycle(0)
            motor1.disable()
            break