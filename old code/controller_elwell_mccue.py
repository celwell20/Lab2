"""@file       controller_elwell_mccue.py
   @brief      Closed loop controller with methods to set an arbitary duty cycle.
   @details    The controller calculates the difference between a reference and measured velocity to determine the error.
               The Kp gain, time difference, and error magnitude are used to calculate and return a motor duty cycle.
   @author     Clayton Elwell
   @author     Tyler McCue
   @date       February 3, 2022
"""

import array
import utime

tick2deg = (360/256)/16/2

class ClosedLoop():
    '''@brief
       @details
       
    '''
    
    def __init__(self, satLimitLow, satLimitHigh, initKp, setpoint):
        '''@brief   Constructs a closed loop controller
           @details Sets saturations limits and in initial Kp gain.
        '''
        ## Start time attribute
        self.t0 = utime.ticks_ms()
       
        ## Attribute associated with the Kp controller Gain
        self.Kp = initKp
        ## Lower saturation limit value, -100
        self.satLimitLow = satLimitLow
        ## Upper saturation limit value, 100
        self.satLimitHigh = satLimitHigh
        # Sum of the errors
        #self.error_sum = 0
        ## Previous error value
        self.last_error = 0
        
        ## Reference setpoint attribute
        self.setpoint = setpoint
        
        ## Time array
        self.tArray = array.array('f',[])
        
        ## Position array attribute
        self.pArray = array.array('f',[])
        
    def duty(self, measure):
        '''@brief    Computes and returns the actuation value based on the measured and referenced values
           @details  Uses the setpoint and measured velocities to determine the error. The velocities are determined in the
                     hardware task.
           @param    measure  The measured velocity
           @return   The duty cycle which is calculated with the run() method.
        '''
        
        current_time = utime.ticks_ms() - self.t0
        
        self.tArray.append(current_time)
        self.pArray.append(measure)
        
        error = self.setpoint - measure
        
        #self.error_sum += (self.last_error + error) * deltat * .5
        
        #error_delta = (error - self.last_error) / deltat
        
        self.last_error = error
        
        
        duty = self.Kp*error
        #print(duty)
        return self.run(duty)
        
    def run(self, duty):
        '''@brief    Calculates the new saturation limit.
           @details  Determines if the duty is too large, compared to what is calculated in the duty() method.
           @param    duty New duty cycle determined by duty() method
           @return   The new saturation limit.
        '''
                
        if duty >= self.satLimitHigh:
            
            return self.satLimitHigh
            
        elif duty <= self.satLimitLow:
            
            return self.satLimitLow
        
        else:
            return duty
        #return self.actuation    
        
        
    def get_Kp(self):
        '''@brief    Method that returns the value of the proportional motor gain
           @return   The current value of the proportional gain
        '''
        return self.Kp
        
    def get_setpoint(self):
        '''@brief    Method that returns the value of the setpoint
           @return   The current value of the setpoint
        '''
        return self.setpoint
    
    
    def set_Kp(self, input_Kp):
        '''@brief    Method that changes the value of the proportional motor gain
           @param    input_Kp New proportional gain value
        '''
        self.Kp = input_Kp
        
    def set_setpoint(self, new_setpoint):
        '''@brief Method that changes the controller setpoint
           @param new_setpoint New setpoint value
        '''
        self.setpoint = new_setpoint
        
    def print_data(self):
        '''@brief Prints the collected position and time data in two columns.

        '''
        print('Time [sec], Position [deg]')
        for i in range(len(self.tArray)):
            print('{:}, {:}'.format(self.tArray[i], self.pArray[i]*tick2deg))
           
    def send_data(self):
        
        return [self.tArray, self.pArray]
        
        

