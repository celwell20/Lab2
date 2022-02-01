import serial as s
import matplotlib.pyplot as plt

class UI:
    def __init__(self, com):
        
        self.comnum = com
        
        print(' ____________________________ ')
        print('|                            |')
        print('|  Welcome to the C.T. UI    |')
        print('|  Commands:                 |')
        print('|     a. Set Reference Pos.  |')
        print('|     b. Set Gain            |')
        print('|     c. Run Step Response   |')
        print('|  Enter corresponding letter|')
        print('|         to start           |')
        print('|____________________________|')
        
    
    def run(self, command):
        
        with s.Serial(str(self.comnum), 115200) as port:
            port.write((command+'\r\n').encode('utf-8'))
    
    def read(self):
        
        with s.Serial(str(self.comnum), 115200) as port:
            port.readlines().decode('utf-8')

if __name__ == '__main__':
    user = UI('COM6')
    
    while True:       
        command = input()
        
        if command == 'esc':
            
            print(' ____________________________ ')
            print('|                            |')
            print('|  Welcome to the C.T. UI    |')
            print('|  Commands:                 |')
            print('|     a. Set Reference Pos.  |')
            print('|     b. Set Gain            |')
            print('|     c. Run Step Response   |')
            print('|  Enter corresponding letter|')
            print('|         to start           |')
            print('|____________________________|')
            continue        
        
        if command == 'a':
            user.run(command)  
            
            #with s.Serial('COM6', 115200) as port:
             #   print(port.readline().decode('utf-8'))
                
            ref = input('Please input a new reference position: ')
            #print(ref)
            user.run(ref)
            
            x = s.Serial('COM6', 115200)
            print(x.readline().decode('utf-8'))
            
        elif command == 'b':
            user.run(command)
            kp = input('Please input a new proportional gain: ')
            
            user.run(kp)
            
            x = s.Serial('COM6', 115200)
            print(x.readline().decode('utf-8'))
            
        elif command == 'c':   
                        
            user.run(command)
            
            x = s.Serial('COM6', 115200)
            print(x.readlines().decode('utf-8'))
        
        
        
        
            
            
             
        
