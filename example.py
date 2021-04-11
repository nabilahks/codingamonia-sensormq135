from mq import*
import sys
import time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ()
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("AMONIA: %g ppm" % (perc["GAS_AMONIA"]))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")
