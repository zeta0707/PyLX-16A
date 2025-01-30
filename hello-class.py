from lx16a import *
import time
import myconfig

SERIAL_PORT = '/dev/buslinker2'
LX16A.initialize(SERIAL_PORT, 0.1)
Tfactor = 25        #value to LX16A time
T1Factor = 0.3      #300ms more wait

#assume -120~120 => 0~240
def a2c(angle):
    return angle + 120.0

class Joint:
    def __init__(self, id):
        self.id = id
        #class with torque enable
        self.servo = LX16A(id, 0)
        self.servo.set_angle_limits(0, 240)
        self.prev_pos = -1

    def move_to(self, pos):
        self.prev_pos = pos
        try:
            self.servo.move(pos, time=500)
        except:
            pass

    def get_pos(self):
        try:
            angle  = self.servo.get_physical_angle() 
            self.prev_pos = angle
            return self.prev_pos
        except:
            return None
     
    def set_offset(self, deviation):
        #with permanent
        self.servo.set_angle_offset(deviation, True)

    def get_offset(self):
        try:
            #read with poll_hardware
            return self.servo.get_angle_offset(True)
        except:
            return None  


servo1 = Joint(1)
servo2 = Joint(2)
servo3 = Joint(3)
servo4 = Joint(4)
servo5 = Joint(5)
servo6 = Joint(6)

#check home operation
while True:
    print("Start Home")
    val = a2c(myconfig.GRIPPER_OPEN)
    servo6.move_to(val)
    time.sleep(1)
    angle = servo6.get_pos()
    print('Gr:',val, angle)

    val = a2c(myconfig.MOTOR4_HOME + 15.0)
    servo4.move_to(val)
    time.sleep(1)
    angle = servo4.get_pos() 
    print('M4:',val, angle)

    val = a2c(myconfig.MOTOR3_HOME - 10.0)
    servo3.move_to(val)
    time.sleep(1)
    angle = servo3.get_pos() 
    print('M3:',val, angle)

    val = a2c(myconfig.MOTOR2_HOME + 10.0)
    servo2.move_to(val)
    time.sleep(1)
    angle = servo2.get_pos() 
    print('M2:',val, angle)

    val = a2c(myconfig.MOTOR4_HOME)
    servo4.move_to(val)
    time.sleep(1)
    angle = servo4.get_pos() 
    print('M4:',val, angle)

    val = a2c(myconfig.MOTOR5_HOME)
    servo5.move_to(val)
    time.sleep(1)
    angle = servo5.get_pos() 
    print('M5:',val, angle)

    val = a2c(myconfig.MOTOR3_HOME)
    servo3.move_to(val)
    time.sleep(1)
    angle = servo3.get_pos() 
    print('M3:',val, angle)

    val = a2c(myconfig.MOTOR2_HOME)
    servo2.move_to(val)
    time.sleep(1)
    angle = servo2.get_pos() 
    print('M2:',val, angle)

    val = a2c(myconfig.MOTOR1_HOME)
    servo1.move_to(val)
    time.sleep(1)
    angle = servo1.get_pos() 
    print('M1:',val, angle)

    print("Done Home")