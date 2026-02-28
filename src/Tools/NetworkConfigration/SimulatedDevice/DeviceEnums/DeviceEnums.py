from enum import Enum

class DeviceType(Enum):
    Firewall = "Firewall"
    Router = "Router"
    Switch = "Switch"

class RouterConfigStatus(Enum):
    Configured = "Configured"
    NotConfigured = "Not Configured"
    IP_changed = "IP Changed"
    NAT_enabled = "NAT Enabled"
    NAT_disabled = "NAT Disabled"
    DHCP_enabled = "DHCP Enabled"
    DHCP_disabled = "DHCP Disabled"
