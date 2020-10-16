import platform, os

# print(os.name())  # Work for nix

uname = platform.uname()

def getSystemInfo(uname):
    print("="*40, "System Information", "="*40)
    # uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    # return (uname)

getSystemInfo(uname)

print(uname.node)