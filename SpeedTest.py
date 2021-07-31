import speedtest
import time
from imutils.video import FPS
import argparse
import imutils

static_back = None
motion_list = [None, None]
time = []

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	            help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	            help="Whether or not frames should be displayed")
args = vars(ap.parse_args())
fps = FPS().start()

s = speedtest.Speedtest()

print("Testing...\n")

downloadSpeed = s.download() / 1048576
uploadSpeed = s.upload() / 1048576
pingResult = round(s.results.ping)

print(f"Download Speed: {downloadSpeed:.2f} Mbps")
print(f"Upload Speed: {uploadSpeed:.2f} Mbps")
print(f"Ping: {pingResult} ms")

fps.update()
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
