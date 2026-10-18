from modules.network_info import get_ip_addresses, get_default_gateway
from config.settings import NOVA_NAME, NOVA_VERSION
from datetime import datetime
from modules.system_info import (
    get_hostname,
    get_os_info,
    get_disk_usage,
    get_memory_usage,
    get_uptime,
)
from modules.network_info import (
    get_ip_addresses,
    get_default_gateway,
    get_interfaces,
    get_hostname,
    get_fqdn,
    resolve_hostname
)
from core.logger import logger

class Nova:
    def __init__(self):
        self.name = NOVA_NAME
        self.version = NOVA_VERSION
        self.running = False
        self.commands = {
            "help": self.command_help,
            "status": self.command_status,
            "system": self.command_system,
            "network": self.command_network,
            "time": self.command_time,
            "version": self.command_version,
            "exit": self.command_exit,
}

    def command_network(self):
        addresses = get_ip_addresses()
        gateway =  get_default_gateway()
        interfaces = get_interfaces()
        hostname = get_hostname()
        fqdn = get_fqdn() 

        address_text = "\n".join(addresses)
        interface_text = "\n".join(interfaces)

        return (
            "\nNetwork Information\n"
            "---------------------\n"
            f"Hostname: {hostname}\n"
            f"FQDN: {fqdn}\n"
            f"{address_text}\n"
            f"Default Gateway: {gateway}"
            "\nInterfaces\n"
            "------------\n"
            f"{interface_text}"
        )

    def command_help(self):
        return (
            "\nAvailable Commands\n" 
            "--------------------\n"
            "help     Display available commands\n"
            "status   Display NOVA status\n"
            "system   Display information\n"
            "network  Display local network information\n"
            "time     Display current system time\n"
            "version  Dispaly NOVA version\n"
            "exit     Shut down NOVA"
            "resolve Resolve a hostname to an IPV4 address\n"
        )
    def command_system(self):
        return (
            "\nSystem Information\n"
            "-------------------\n"
           f"Hostname: {get_hostname()}\n"
           f"OS: {get_os_info()}\n"
           f"Memory: {get_memory_usage()}\n"
           f"Disk: {get_disk_usage()}\n"
           f"Uptime: {get_uptime()}"
        )
    def start(self): 
        self.running = True 
        logger.info("NOVA started")

        print("=" * 50)
        print(f"{self.name} v{self.version}")
        print("Core systems initialized.")
        print("=" * 50)
        print("Type 'help' to display avaiable commands.")

    def command_status(self):
        return "NOVA core systems operational."

    def command_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def command_version(self):
        return f"{self.name} version {self.version}"
    def command_exit(self):
        logger.info("NOVA shutting down")
        self.running = False
        return "Shutting down Nova."

    def process_command(self, command):
        command = command.strip()

        logger.info(f"Command received: {command}")
        parts = command.split(maxsplit=1)
        command_name = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else None

        if command_name == "resolve":
            if argument:
                return self.command_resolve(argument) 
            return "Usage: resolve <hostname>"
        command_function = self.commands.get(command_name)

        if command_function:
            return command_function()

        return f"Unknown command: {command}" 

    def command_resolve(self, hostname):
        return f"{hostname} -> {resolve_hostname(hostname)}"
