import remotelab
import time
import bb_filter
bb = remotelab.BB()

err_prev = 0
error_sum = 0

interval = 0.004

setpoint_cm = 0
#Control Parameters
kp = 0.2250
ki = 0.0010
kd = 0.1000
feedforward = 750
windup_abs = 30

while True:
    position_analog= bb_filter.filterAnalog(bb.get_position())
    setpoint_analog=(setpoint_cm+25)*80  #(  0 --- 4096 analog value)
    position_cm=(position_analog/80)-25  #(-25 --- 25 cm)
    print(position_cm)
    
    error = setpoint_analog - position_analog
    error_sum += error

    p = error * kp
    i = error_sum * ki
    i = i if -windup_abs <= i <= windup_abs else (i/abs(i))*windup_abs
    d = bb_filter.filterDerivative ((error - err_prev) * kd / interval)

    if abs(error)>10:
    	output = feedforward + p + i + d

    output = output if 500 <= output else 500
    output = output if 1000 >= output else 1000
    bb.set_servo(int(output))
    err_prev = error
    time.sleep(interval)