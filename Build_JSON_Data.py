import json
from Get_Info import Info

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

        data = {
            "data": {
                    "id": self.id, 
                "type": self.datatype,
                "attributes": {
                    "heartbeat_time_gmt": {
                        "current_date_gmt": current_date_gmt,
                        "current_time_gmt": current_time_gmt
                    },
                    "system_information": {
                        "system": system,
                        "name": name,
                        "release": release,
                        "version": version,
                        "machine": machine,
                        "processor": processor
                    },
                    "memory": {
                        "total": mem_total,
                        "available": mem_available,
                        "used": mem_used,
                        "percentage": mem_percentage
                    },
                    "swap": {
                        "total": swap_total,
                        "free": swap_free,
                        "used": swap_used,
                        "percentage": swap_percentage
                    },
                    "cpu_info": {
                        "physical_cores": cpu_physical_cores,
                        "total_cores": cpu_total_cores,
                        "max_frequency": cpu_max_frequency,
                        "min_frequency": cpu_max_frequency,
                        "current_frequency": cpu_current_frequency,
                        "total_cpu_usage": cpu_total_cpu_usage
                    },
                    "boot_time": {
                        "boot_time_local": boot_time_local
                    },
                    "message": "Thump"
                }
            }
        }

        # convert into JSON:
        return json.dumps(data)
