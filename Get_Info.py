import time
import psutil
import platform
from datetime import datetime

class Info:

    def Get_GMTDateTime(self):
        return time.strftime("%d %b %Y", time.gmtime()), time.strftime('%H%M', time.gmtime())

    def Get_System_Info(self):
        uname = platform.uname()
        return f"{uname.system}", f"{uname.node}", f"{uname.release}", f"{uname.version}", f"{uname.machine}", f"{uname.processor}"

    def Get_Boottime(self):
        # Boot Time
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        return f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    
    def Get_Memory(self):
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
        # Memory Information
        # get the memory details
        svmem = psutil.virtual_memory()
        total = f"{get_size(svmem.total)}"
        available = f"{get_size(svmem.available)}"
        used = f"{get_size(svmem.used)}"
        percentage = f"{svmem.percent}%"
        return total, available, used, percentage 

    def Get_Swap(self):
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
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        total = f"{get_size(swap.total)}"
        free = f"{get_size(swap.free)}"
        used = f"{get_size(swap.used)}"
        percentage = f"{swap.percent}%"
        return total, free, used, percentage

    def Get_Cpu_Info(self):
        cpufreq = psutil.cpu_freq()
        # number of cores and CPU frequencies
        return psutil.cpu_count(logical=False), psutil.cpu_count(logical=True), f"{cpufreq.max:.2f}Mhz", f"{cpufreq.min:.2f}Mhz", f"{cpufreq.current:.2f}Mhz", f"{psutil.cpu_percent()}%"

"TODO: add disk utilities"
"TODO: add network info"