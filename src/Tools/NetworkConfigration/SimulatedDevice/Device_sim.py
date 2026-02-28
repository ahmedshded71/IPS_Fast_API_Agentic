from DeviceEnums import DeviceType,RouterConfigStatus


class VirtualRouter:
    def __init__(self):
        self.settings = {
            "ip": "192.168.1.1",
            "dhcp": True,
            "firewall": "off",
            "nat": False
        }
    def show_settings(self):    
        return self.settings






class VirtualSwitch:
    def __init__(self):
        self.settings = {
            "vlan": 10,
            "port_security": True,
            "stp": True,
            "qos": "high"
        }
    def show_settings(self):
        return self.settings




class VirtualFirewall:
    def __init__(self):
        self.settings = {
            "rules": [{"action": "allow", "protocol": "tcp", "port": 80}],
            "default_action": "deny",
            "logging": True,
            "intrusion_detection": True
        }
    def show_settings(self):
        return self.settings
