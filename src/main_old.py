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
#import serial



tick2deg = (256/360)*16

if __name__ == '__main__':
    ## Driver object for first motor
    motor1 = moe.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    
    motor1.enable()
    
    ## Driver object for second motor
    motor2 = moe.MotorDriver(pyb.Pin.cpu.C1, pyb.Pin.cpu.A0, pyb.Pin.cpu.A1, 5)
    motor2.enable()
    
    ## Driver object for first encoder
    enc1 = enc.EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    ## Driver object for second encoder
    enc2 = enc.EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    
    enc1.set_position(0)
    enc2.set_position(0)
    
    #control = control.ClosedLoop(-100, 100, .05,16200)
    
    
    
#     while True:
#         try:
#             
#             if CommReader.any():
#                 
#                 command = CommReader.read(1)
#                 CommReader.read()
#                 
#             if command == b'\a':
#                 
#                 control.set_setpoint(input('Please input a new reference position'))
#             
#             elif command == b'\b':
#                 
#                 control.set_Kp(input('Please input a new proportional gain'))
#                 
#             elif command == b'\c':
#                 
#                 update = enc2.update
#                 
#                 if duty <= 15:
#                     motor1.set_duty_cycle(0)
#                     control.print_data()
#                     break
            #if command = 'b\x1b':
                    
            
           
            #update = enc2.update()
            
            #if abs(update) >= 16200:
            #    control.print_data()
            #    motor1.set_duty_cycle(0)
            #    break
            
            #duty = control.duty(update)
            
            #if duty <= 15:
            #   motor1.set_duty_cycle(0)
            #    control.print_data()
            #    break
            
            #motor1.set_duty_cycle(duty)
            
            
            #utime.sleep_ms(10)
        
        
#         except KeyboardInterrupt:
#             motor1.set_duty_cycle(0)
#             #motor2.set_duty_cycle(0)
#             motor1.disable()
#             #motor2.disable()
#             break
    
    
