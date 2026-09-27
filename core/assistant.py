from datetime import datetime
from modules.system_info import (
    get_hostname,
    get_os_info,
    get_disk_usage,
    get_memory_usage,
    get_uptime,
)


class Nova:
    def __init__(self):
        self.name = "NOVA"
        self.version = "0.1.0"
        self.running = False 

    def start(self): 
        self.running = True 


        print("=" * 50)
        print(f"{self.name} v{self.version}")
        print("Core systems initialized.")
        print("=" * 50)
        print("Type 'help' to display avaiable commands.")

    def process_command(self, command):
        command = command.strip().lower()

        if command == "help":
            return (
                "\nAvailable Commands\n"
                "------------------\n"
                "help      Display avaiable commands\n"
                "status    Display NOVA status\n"
                "system    Display system information\n" 
                "time      Display current system time\n"
                "version   Dispaly NOVA version\n" 
                "exit      Display Shut down NOVA"
            )

        if command == "status":
            return "NOVA core systems operational."

        if command == "system":
            return (
                "\nSystem Information\n"
                "------------------\n"
                f"Hostname: {get_hostname()}\n"
                f"OS: {get_os_info()}\n"
                f"Memory: {get_memory_usage()}\n"
                f"Disk: {get_disk_usage()}\n"
                f"Uptime: {get_uptime()}"
            )


        if command == "time":
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if command == "version":
            return f"{self.name} version {self.version}"

        if command == "exit":
            self.running = False 
            return "Shutting down NOVA"

        return f"Unknown command: {command}" 
