import socket
import subprocess


def get_ip_addresses():
    result = subprocess.run(
        ["ip", "-4", "-o", "addr", "show"],
        capture_output=True,
        text=True,
        check=True,
    )

    addresses = []

    for line in result.stdout.splitlines():
        parts = line.split()

        interface = parts[1]
        address = parts[3].split("/")[0]

        if interface != "lo":
            addresses.append(f"{interface}: {address}")

    return addresses


def get_default_gateway():
    result = subprocess.run(
        ["ip", "route", "show", "default"],
        capture_output=True,
        text=True,
        check=True,
    )

    parts = result.stdout.split()

    if "via" in parts:
        gateway_index = parts.index("via") + 1
        return parts[gateway_index]

    return "Not found"

def get_interfaces():
    result = subprocess.run(
        ["ip", "-o", "link", "show"],
        capture_output=True,
        text=True,
        check=True,
    )

    interfaces = []

    for line in result.stdout.splitlines():
        parts = line.split()

        interface = parts[1].rstrip(":")
        state = "UNKNOWN"
        mac_address = "N/A"

        if "state" in parts:
            state_index = parts.index("state") + 1
            state = parts[state_index]

        if "link/ether" in parts:
            mac_index = parts.index("link/ether") + 1
            mac_address = parts[mac_index]

        if interface != "lo":
            interfaces.append(
                f"{interface}: state={state}, mac={mac_address}"
            )

    return interfaces




