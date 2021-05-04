#CrashDash by redev
import os, ctypes, sys

try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
if is_admin == 0 :
    sys.exit("You need to run this script as root/admin.")

commands = ["--help", "--crash", "--gui", "--credits"]

def crash1():
    #os.system("bash :(){ :|:& };:")
    while True: os.fork()

def crash2():
    #os.system("bash :(){ :|:& };:")
    os.system("sudo echo c > /proc/sysrq-trigger")

def crash3():
    os.system("mkdir /tmp/kpanic")
    file1 = open('/tmp/kpanic/kpanic.c', 'w')
    L = ['#include <linux/kernel.h>\n', '#include <linux/module.h>\n', 'MODULE_LICENSE("GPL");static int8_t* message = "buffer overrun at 0x4ba4c73e73acce54";int init_module(void){panic(message);return 0;}']
    file1.writelines(L)
    file1.close()
    file1 = open('/tmp/kpanic/Makefile', 'w')
    L = ['obj-m += kpanic.o\n', 'all:\n', '\tmake -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules']
    file1.writelines(L)
    file1.close()
    os.system("cd /tmp/kpanic && make")
    os.system("sudo insmod /tmp/kpanic/kpanic.ko")

def crash4():
    sys.exit()

for commandList in commands:
    try:
        bool(sys.argv[1])
    except:
        sys.exit("redev's CrashDash\nCommand List:\n\t--help - This message\n\t--crash {crash type} - Selects the crash type the script will use")
    if sys.argv[1] not in commands:
        sys.exit(sys.argv[1] + " is not a command. To get a command list, run 'python3 crashdash.py --help'.")

if "--help" in sys.argv[1]:
    try:
        bool(sys.argv[2])
    except:
        sys.exit("redev's CrashDash\nCommand List:\n\t--help - This message\n\t--crash {crash type} - Selects the crash type the script will use\n--credits - Shows the credits of this script.\n --gui - Runs a graphical user interface version of the script.")
    if sys.argv[2] == "gui":
        sys.exit("redev's CrashDash\npython3 crashdash.py --gui\nRuns a graphical user interface version of the script.")
    elif sys.argv[2] == "help":
        sys.exit("redev's CrashDash\npython3 crashdash.py --help\nShows the command list.")
    elif sys.argv[2] == "crash":
        sys.exit("redev's CrashDash\npython3 crashdash.py --crash {crash type}\nPossible crash types:\n\tforkbomb - Spawns a ton of processes. May freeze, crash, or rarely do nothing at all (depending on the computer's configuration).\n\tkpanic - Sends a signal to the system to crash and kernel panic\n\tkpanicmod - Quickly compiles a kernel module and loads it (not permanently) that kernel panics the system.")
    elif sys.argv[2] == "credits":
        sys.exit("redev's CrashDash\npython3 crashdash.py --credits\nShows the credits of this script.")
elif "--gui" in sys.argv[1]:
    try:
        import tkinter as tk
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()
        button = tk.Button(
            text="Fork Bomb",
            width=25,
            height=5,
            bg="black",
            fg="red",
            command=crash1)
        button2 = tk.Button(
            text="Direct Kernel Crash",
            width=25,
            height=5,
            bg="black",
            fg="red",
            command=crash2)
        button3 = tk.Button(
            text="Kernel Crash (Kernel Module)",
            width=25,
            height=5,
            bg="black",
            fg="red",
            command=crash3)
        button4 = tk.Button(
            text="Exit",
            width=25,
            height=5,
            bg="black",
            fg="red",
            command=crash4)
        button.pack(side=tk.LEFT)
        button2.pack(side=tk.LEFT)
        button3.pack(side=tk.RIGHT)
        button4.pack(side=tk.RIGHT)
        root.title("redev's CrashDash")
        photo = tk.PhotoImage(file = "icon.png")
        root.iconphoto(False, photo)
        root.mainloop()
    except:
        sys.exit("Unable to connect to display. Cannot continue.")
elif "--crash" in sys.argv[1]:
    try:
        bool(sys.argv[2])
    except:
        sys.exit("There were no arguments passed. Try running 'python3 crashdash.py --help crash'.")
    if sys.argv[2] == "forkbomb":
        crash1()
    elif sys.argv[2] == "kpanic":
        crash2()
    elif sys.argv[2] == "kpanicmod":
        crash3()
    else:
        sys.exit(sys.argv[2] + " is not a crash type. Try running 'python3 crashdash.py --help crash'.")
elif "--credits" in sys.argv[1]:
    sys.exit("This script was made by redev (reoccurdev#0021 on Discord) and can be found on their GitHub repository.\nTHEY TAKE NO LIABILITY FOR WHAT YOU DO WITH THIS SCRIPT.")
