import serial as s
import matplotlib.pyplot as plt
import time

class UI:
    def __init__(self, com):
        
        self.comnum = com
        
        print(' ____________________________ ')
        print('|                            |')
        print('|  Welcome to the C.T. UI    |')
        print('|  Commands:                 |')
        print('|     A. Set Reference Pos.  |')
        print('|     B. Set Gain            |')
        print('|     C. Run Step Response   |')
        print('|  Enter corresponding letter|')
        print('|         to start           |')
        print('|____________________________|')
        print('\n')
        
    
    
    def run(self, command):
        
        with s.Serial(str(self.comnum), 115200) as port:
            port.write((command+"\r\n").encode('utf-8'))
    
    def read(self):
        #flag = True
        x = [] #preallocating some lists for future storage
        y = []
        with s.Serial(str(self.comnum), 115200) as port:
            #time.sleep(5)
            while True:
                try:
                    data = port.readline().decode('utf-8')
                    
                    cooked = [idx for idx in data.replace('\r\n', '').split(',')]
                    #fried = [idx for idx in cooked]
                    #print(cooked[0])
                        
                    xtemp = float(cooked[0]) # converting first index to float
                    ytemp = float(cooked[1]) # converting second index to float
                    x.append(xtemp) #adding first index to x list
                    y.append(ytemp) #adding second index to ylist
                    print(y)
                except:
                    break
        #print('here')
            
                    
        plt.figure()
        plt.plot(x, y)
        plt.xlabel('Time, [sec]')
        plt.ylabel('Angular position [deg]')
        plt.title('1 Revolution Step Response - Position versus time with Kp = 0.05')
        plt.show()
        
        x = []
        y = []
            
                
                # cooking = [idx for idx in data.strip().split('\n')]  # splitting based on the carriage return
                # #print(cooking)
                
                # for i in range(len(cooking)-2):  # splits the commas in each list index, converts each list index into its own list
            
                # try:
                #     cooked = [idx for idx in cooking[i].split(',')]
                #     print(cooked)
                #     xtemp = float(cooked[0]) # converting first index to float
                #     ytemp = float(cooked[1]) # converting second index to float
                #     x.append(xtemp) #adding first index to x list
                #     y.append(ytemp) #adding second index to ylist
                
                # except:
                #    continue
                
                
           
                
   #             print(x)
    #            if x == 'Setting position value':
     #               flag = False
                    
                    
if __name__ == '__main__':
    
    
    user = UI('COM6')
    while True:
        c = 0
        
        c = input("Enter Command: ")
        #print(user.read())
        user.run(c)
        if c == "a":
            com = input("Please set reference position: ")
            user.run(com)
        elif c == "b":
            com = input("Please set a controller gain: ")
            user.run(com)
        elif c == 'c':
            user.read()
            #print('here')
            
            
            
        
