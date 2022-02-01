'''@file ui_elwell_mccue.py
   @brief
   @detials
   @author
   @author
   @date
'''

import serial
#import matlibplot


# def __init__(self):
#         '''@brief
#            @details
#         '''
        
        
        

def run():
        '''@brief
           @details
        '''
        
        #command = input()
        
        with serial.Serial('COM6', 115200) as s_port:
            
            s_port.write(input('Do something').encode('UTF-8'))
            
        print(s_port.readline())
            
if __name__ == '__main__':
    
    print('--------------------------------\n'
          '     USER COMMAND INTERFACE     \n'
          '--------------------------------\n'
          'Press a: Set reference position \n'
          'Press b: Set proportional gain \n'
          'Press c: Run step response and plot data \n'
          'Press s: End data collection prematurely\n'
          'Press ESC: Display user interface controls\n'
          '--------------------------------')
            
#     while True:
#         
#         try:
            
    run()
    
    #print(s_port.readline())
    