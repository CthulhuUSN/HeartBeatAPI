import json
from Get_Info import Info
from SFTM_Utilities import get_deviceID

class JSON_Data:
    id = 1
    datatype = "heartbeat"

    def __init__(self, id = id):
        self.id = id

    def build_data(self):
        info = Info()
        # Heartbeat checkin time
        current_date_gmt, current_time_gmt = info.Get_GMTDateTime()
        # System info
        system, name, release, version, machine, processor = info.Get_System_Info()
        # Memory
        mem_total, mem_available, mem_used, mem_percentage = info.Get_Memory()
        # Swap
        swap_total, swap_free, swap_used, swap_percentage = info.Get_Swap()
        #CPU Info
        cpu_physical_cores, cpu_total_cores, cpu_max_frequency, cpu_min_frequency, cpu_current_frequency, cpu_total_cpu_usage = info.Get_Cpu_Info()
        # Boot Time
        boot_time_local = info.Get_Boottime()
        # Disk info
        disk_data = info.Get_Disk_Info()
        # Networking info
        net_info = info.Get_Networking()

        data = {
            "deviceID": get_deviceID(),
            "currentDateGMT": current_date_gmt,
            "currentTimeGMT": current_time_gmt,
            "system": system,
            "name": name,
            "release": release,
            "version": version,
            "processor": processor,
            "totalMemory": mem_total,
            "availableMemory": mem_available,
            "usedMemory": mem_used,
            "totalSwap": swap_total,
            "freeSwap": swap_free,
            "usedSwap": swap_used,
            "swapPercentage": swap_percentage,
            "physicalCores": cpu_physical_cores,
            "totalCores": cpu_total_cores,
            "maxFrequency": cpu_max_frequency,
            "minFrequency": cpu_min_frequency,
            "currentFrequency": cpu_current_frequency,
            "totalCPUUsage": cpu_total_cpu_usage,
            "bootTimeLocal": boot_time_local,
            "diskData": disk_data,
            "networkData": net_info,
            "message": "Thump"

        }

        # convert into JSON:
        return json.dumps(data)
