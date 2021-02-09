from time import sleep
def s(text):
	for l in text:
		print("\033[94m"+l, end='', flush=True)
		sleep(0.03)
print("\033[1;32m",end="")
print("Enter Your Text To Scroll-Print:")
print("\033[1;33m", end="")
t = input()
s(t)
