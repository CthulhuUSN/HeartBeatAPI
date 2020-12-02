import time
import psutil
import platform
from datetime import datetime
import json

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

    def Get_Disk_Info(self):

        data = {}
        count = 0
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
        partitions = psutil.disk_partitions()
        for partition in partitions:
            disk_data = {}
            device = f"{partition.device}"
            mountpoint = f"{partition.mountpoint}"
            partition_type = f"{partition.fstype}"
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            total_size = f"{get_size(partition_usage.total)}"
            partition_used = f"{get_size(partition_usage.used)}"
            free = f"{get_size(partition_usage.free)}"
            partition_usage = f"{partition_usage.percent}%"
            disk_data['device_name'] = device
            disk_data['mountpoint'] = mountpoint
            disk_data['partition_type'] = partition_type
            disk_data['total_size'] = total_size
            disk_data['partition_used'] = partition_used
            disk_data['free_space'] = free
            disk_data['partition_usage'] = partition_usage
            
            data['device{}'.format(count)] = disk_data
            count += 1

        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        read_bytes = f"{get_size(disk_io.read_bytes)}"
        write_bytes = f"{get_size(disk_io.write_bytes)}"
        data['total_read_bytes'] = read_bytes
        data['total_write_bytes'] = write_bytes

        return data

    def Get_Networking(self):

        data = {}
        count = 0
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
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                addr = ""
                netmask = ""
                broadcast = ""
                if str(address.family) == 'AddressFamily.AF_INET':
                    addr =f"{address.address}"
                    netmask = f"  Netmask: {address.netmask}"
                    broadcast = f"{address.broadcast}"
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    addr = f"{address.address}"
                    netmask = f"{address.netmask}"
                    broadcast = f"{address.broadcast}"
                interface_data = {}
                interface_data['interface_name'] = interface_name
                interface_data['ip_address'] = addr 
                interface_data['netmask'] = netmask
                interface_data['broadcast'] = broadcast

                data['interface {}'.format(count)] = interface_data
                count += 1
                
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        total_bytes_sent = f"{get_size(net_io.bytes_sent)}"
        total_bytes_received = f"{get_size(net_io.bytes_recv)}"
        data['total_bytes_sent'] = total_bytes_sent
        data['total_bytes_received'] = total_bytes_received
        return data
