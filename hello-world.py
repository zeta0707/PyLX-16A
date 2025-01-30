from lx16a import *
import time
import myconfig

SERIAL_PORT = '/dev/buslinker2'
LX16A.initialize(SERIAL_PORT, 0.1)

#assume -120~120 => 0~240
def a2c(angle):
    return angle + 120.0

try:
    servo1 = LX16A(1, 0)
    servo2 = LX16A(2, 0)
    servo3 = LX16A(3, 0)
    servo4 = LX16A(4, 0)
    servo5 = LX16A(5, 0)
    servo6 = LX16A(6, 0)
    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

#check home operation
while True:
    print("Start Home")
    val = a2c(myconfig.GRIPPER_OPEN)
    servo6.move(val, time=500)
    time.sleep(1)
    angle = servo6.get_physical_angle() 
    print('Gr:',val, angle)

    val = a2c(myconfig.MOTOR4_HOME + 15.0)
    servo4.move(val, time=500)
    time.sleep(1)
    angle = servo4.get_physical_angle() 
    print('M4:',val, angle)

    val = a2c(myconfig.MOTOR3_HOME - 10.0)
    servo3.move(val, time=500)
    time.sleep(1)
    angle = servo3.get_physical_angle() 
    print('M3:',val, angle)

    val = a2c(myconfig.MOTOR2_HOME + 10.0)
    servo2.move(val, time=500)
    time.sleep(1)
    angle = servo2.get_physical_angle() 
    print('M2:',val, angle)

    val = a2c(myconfig.MOTOR4_HOME )
    servo4.move(val, time=500)
    time.sleep(1)
    angle = servo4.get_physical_angle() 
    print('M4:',val, angle)

    val = a2c(myconfig.MOTOR5_HOME )
    servo5.move(val, time=500)
    time.sleep(1)
    angle = servo5.get_physical_angle() 
    print('M5:',val, angle)

    val = a2c(myconfig.MOTOR3_HOME)
    servo3.move(val, time=500)
    time.sleep(1)
    angle = servo3.get_physical_angle() 
    print('M3:',val, angle)

    val = a2c(myconfig.MOTOR2_HOME)
    servo2.move(val, time=500)
    time.sleep(1)
    angle = servo2.get_physical_angle() 
    print('M2:',val, angle)

    val = a2c(myconfig.MOTOR1_HOME)
    servo1.move(val, time=500)
    time.sleep(1)
    angle = servo1.get_physical_angle() 
    print('M1:',val, angle)

    print("Done Home")