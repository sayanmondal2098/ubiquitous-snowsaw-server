import psutil
import platform
from datetime import datetime
import cmd
import os


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


uname = platform.uname()
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)

cpufreq = psutil.cpu_freq()

svmem = psutil.virtual_memory()

swap = psutil.swap_memory()

# for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#     f"Core {i}: {percentage}%",


def return_system_info():
    x = {
        "info : ", "System Information",

        f"System: {uname.system}",
        f"Node Name: {uname.node}",
        f"Release: {uname.release}",
        f"Version: {uname.version}",
        f"Machine: {uname.machine}",
        f"Processor: {uname.processor}",


        # Boot Time
        "Info : ", "Boot Time",

        f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}",


        # let's print CPU information
        "Info : ", "CPU Info",
        # number of cores
        "Physical cores:", psutil.cpu_count(logical=False),
        "Total cores:", psutil.cpu_count(logical=True),
        # CPU frequencies
        f"Max Frequency: {cpufreq.max:.2f}Mhz",
        f"Min Frequency: {cpufreq.min:.2f}Mhz",
        f"Current Frequency: {cpufreq.current:.2f}Mhz",
        # CPU usage
        "CPU Usage Per Core:",

        f"Total CPU Usage: {psutil.cpu_percent()}%",


        # Memory Information
        " Info : ", "Memory Information",
        # get the memory details

        f"Total: {get_size(svmem.total)}",
        f"Available: {get_size(svmem.available)}",
        f"Used: {get_size(svmem.used)}",
        f"Percentage: {svmem.percent}%",
        # get the swap memory details (if exists)

        f"Total: {get_size(swap.total)}",
        f"Free: {get_size(swap.free)}",
        f"Used: {get_size(swap.used)}",
        f"Percentage: {swap.percent}%",


    }
    return x

def test():
    return {"message": "Hello ServiceNow"}


# run some command 
def run_cmd(cmd):
    """
    Runs a command and returns the output.
    """
    p = os.popen(cmd)
    # print (p.buffer.read())
    return p.read()
