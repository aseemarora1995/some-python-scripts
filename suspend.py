import subprocess
import time

def suspend():
	dur = int(raw_input('time(minutes): '))
	for minutes in range(dur):
		print 'suspending system in %d minute(s)...'% (dur-minutes)
		time.sleep(60)

	args = ["systemctl", "suspend"]
	subprocess.call(args)

if __name__ == "__main__":
	suspend()