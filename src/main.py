"""@file        main.py
   @brief       Closed loop motor control main module
   @details     Runs closed loop proportional control step response test
   @author        Clayton Elwell
   @author        Tyler McCue
   @date          January 27, 2022
"""

import encoder_elwell_mccue as enc
import motor_elwell_mccue as moe
import Closed_Loop as control
import pyb
import utime



if __name__ == '__main__':
    ## Driver object for first motor
    motor1 = moe.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    
    motor1.disable()
    
    ## Driver object for second motor
    motor2 = moe.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    motor2.disable()
    
    ## Driver object for first encoder
    enc1 = enc.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    ## Driver object for second encoder
    enc2 = enc.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    
    enc1.set_position(0)
    enc2.set_position(0)
    
    control = control.ClosedLoop(-100, 100, 1, 0, 0)
    
    
    while True:
        x = input()
        if x == "a":
            ref = float(input())
            control.setReference(ref)
        if x == "b":
            new = float(input())
            control.set_Kp(new)
        if x == "c":
            motor1.enable()
            while True:
                #print('here')
                update = enc1.update()
                duty = control.run(update)
                motor1.set_duty_cycle(duty)
                #print(len(control.tArray))
                #print(duty)
                if update >= control.getReference():
                    motor1.disable()
                    motor1.set_duty_cycle(0)
                    control.print_data()
                    enc1.set_position(0)
                    break
        
                
        
        
    
#     
#     control = control.ClosedLoop(-100, 100, .05,16200)
#     
#                           
#     
#     while True:
#         try:
#             
#             
#             
#             update = enc2.update()
#             
#             #if abs(update) >= 16200:
#             #    control.print_data()
#             #    motor1.set_duty_cycle(0)
#             #    break
#             
#             duty = control.duty(update)
#             
#             if duty <= 15:
#                 motor1.set_duty_cycle(0)
#                 control.print_data()
#                 break
#             
#             motor1.set_duty_cycle(duty)
#             
#             
#             utime.sleep_ms(10)
#         
#         
#         except KeyboardInterrupt:
#             motor1.set_duty_cycle(0)
#             #motor2.set_duty_cycle(0)
#             motor1.disable()
#             #motor2.disable()
#             break