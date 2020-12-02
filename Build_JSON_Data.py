import json
from Get_Info import Info

class JSON_Data:
    id = 1
    datatype = "heartbeat"

    def __init__(self, id = id):
        self.id = id

    def build_data(self):
        info = Info()
        json_data = {}
        
        # Heartbeat checkin time
        current_date_gmt, current_time_gmt = info.Get_GMTDateTime()
        heartbeat_data = {}
        heartbeat_data['current_date_gmt'] = current_date_gmt
        heartbeat_data['current_time_gmtt'] = current_time_gmt
        
        # System info
        system, name, release, version, machine, processor = info.Get_System_Info()
        sys_data = {}
        sys_data['system'] = system
        sys_data['name'] = name
        sys_data['release'] = release
        sys_data['version'] = version
        sys_data['machine'] = machine
        sys_data['processor'] = processor

        # Memory
        mem_total, mem_available, mem_used, mem_percentage = info.Get_Memory()
        mem_data = {}
        mem_data['total'] = mem_total
        mem_data['available'] = mem_available
        mem_data['used'] = mem_used
        mem_data['percentage'] = mem_percentage

        # Swap
        swap_total, swap_free, swap_used, swap_percentage = info.Get_Swap()
        swap_data = {}
        swap_data['total'] = swap_total
        swap_data['free'] = swap_free
        swap_data['used'] = swap_used
        swap_data['percentage'] = swap_percentage

        #CPU Info
        cpu_physical_cores, cpu_total_cores, cpu_max_frequency, cpu_min_frequency, cpu_current_frequency, cpu_total_cpu_usage = info.Get_Cpu_Info()
        cpu_data = {}
        cpu_data['physical_cores'] = cpu_physical_cores
        cpu_data['total_cores'] = cpu_total_cores
        cpu_data['max_frequency'] = cpu_max_frequency
        cpu_data['min_frequency'] = cpu_min_frequency
        cpu_data['current_frequency'] = cpu_current_frequency
        cpu_data['total_cpu_usage'] = cpu_total_cpu_usage

        # Boot Time
        boot_time_local = info.Get_Boottime()
        boot_data = {}
        boot_data['boot_time_local'] = boot_time_local

        # Disk info
        disk_data = info.Get_Disk_Info()

        # Networking info
        net_info = info.Get_Networking()

        # Create Attributes section
        attributes = {}
        attributes['heartbeat_time_gmt'] = heartbeat_data
        attributes['system_information'] = sys_data 
        attributes['memory'] = mem_data
        attributes['swap'] = swap_data
        attributes['cpu_info'] = cpu_data 
        attributes['boot_time'] = boot_data 
        attributes['disk_data'] = disk_data
        attributes['network_info'] = net_info 
        attributes['message'] = "Thump"

        # Create data section
        data = {}
        data['id'] = self.id
        data['type'] = self.datatype
        data['attributes'] = attributes

        # Create final json object
        json_data['data'] = data

        # convert into JSON:
        return json.dumps(json_data)

test = JSON_Data()
result = test.build_data()
print(result)