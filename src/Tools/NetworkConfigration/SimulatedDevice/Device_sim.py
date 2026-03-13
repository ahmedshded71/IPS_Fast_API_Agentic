from .DeviceEnums import DeviceType,DeviceConnectionStatus
from ..Schemas.DeviceSchema import DeviceSchema



class VirtualCloudProvider:
    config = None
    settings = {}

    @classmethod
    def initialize(cls, config):
        cls.config = config
        cls.settings = {
            "cloud_ip_address": cls.config.CLOUD_IP_address,
            "cloud_dhcp": cls.config.CLOUD_DHCP,
            "cloud_nat": cls.config.CLOUD_NAT,
            "cloud_firewall": cls.config.CLOUD_FIREWALL,
            "bandwidth": cls.config.BANDWIDTH,
            "provider_name": cls.config.PROVIDER_NAME,
            "region": cls.config.REGION,
            "availability_zone": cls.config.AVAILABILITY_ZONE,
            "instance_type": cls.config.INSTANCE_TYPE,
            "cloud_vlans": cls.config.CLOUD_VLANS,
            "cloud_ports": cls.config.CLOUD_PORTS,
            "cloud_qos": cls.config.CLOUD_QOS,
            "cloud_stp": cls.config.CLOUD_STP,
        }
        cls.position = (0, 5)  
        cls.connections = [
            {"device": DeviceType.ROUTER.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.FIREWALL.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.SWITCH.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.PC1.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.PC2.value, "status": DeviceConnectionStatus.DISCONNECTED.value}
        ]    
    @classmethod
    def show_settings(cls):
        if cls.settings is None:
            raise ValueError("Cloud not initialized")
        return DeviceSchema.CloudProviderConfig(**cls.settings)
    
    @classmethod
    def get_conection_device(cls, device_name):
        for connection in cls.connections:
            if connection["device"] == device_name:
                connection["status"] = DeviceConnectionStatus.CONNECTED.value
                return f"{device_name} connected to Cloud"
        return f"{device_name} not found in Cloud connections"
    





class VirtualFirewall:
    config = None
    settings = {}

    @classmethod
    def initialize(cls, config):
        cls.config = config
        cls.settings = {
            "rules": cls.config.RULES,
            "default_action": cls.config.DEFAULT_POLICY,
            "logging": cls.config.LOGGING,
            "intrusion_detection": cls.config.INTRUSION_DETECTION
        }
        cls.position = (0, 4)
        cls.connections = [
            {"device": DeviceType.ROUTER.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.CLOUD.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.PC1.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.PC2.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.SWITCH.value, "status": DeviceConnectionStatus.DISCONNECTED.value}] 

    @classmethod
    def show_settings(cls):
        if cls.settings is None:
            raise ValueError("Firewall not initialized")
        return DeviceSchema.FirewallConfig(**cls.settings)
    @classmethod
    def get_conection_device(cls, device_name):
        for connection in cls.connections:
            if connection["device"] == device_name:
                connection["status"] = DeviceConnectionStatus.CONNECTED.value
                return f"{device_name} connected to Firewall"
        return f"{device_name} not found in Firewall connections"

class VirtualRouter:
    config = None
    settings = {}
    

    @classmethod
    def initialize(cls, config):
        cls.config = config
        cls.settings = {
            "ip": cls.config.IP_address,
            "dhcp": cls.config.DHCP,
            "nat": cls.config.NAT,
            "firewall": cls.config.FIREWALL
        }
        cls.position = (0, 3)  
        cls.connections = [
            {"device": DeviceType.SWITCH.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.CLOUD.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.FIREWALL.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.PC1.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.PC2.value, "status": DeviceConnectionStatus.DISCONNECTED.value}
        ]    
    @classmethod
    def show_settings(cls):
        if cls.settings is None:
            raise ValueError("Router not initialized")
        return DeviceSchema.RouterConfig(**cls.settings)
    
    @classmethod
    def get_conection_device(cls, device_name):
        for connection in cls.connections:
            if connection["device"] == device_name:
                connection["status"] = DeviceConnectionStatus.CONNECTED.value
                return f"{device_name} connected to Router"
        return f"{device_name} not found in Router connections"
    




class VirtualSwitch:
    config = None
    settings = {}

    @classmethod
    def initialize(cls, config):
        cls.config = config
        cls.settings = {
            "vlan": cls.config.VLANS,
            "port_security": cls.config.PORTSECURITY,
            "stp": cls.config.STP,
            "qos": cls.config.QOS
        }
        cls.position = (0, 2)  
        cls.connections = [
            {"device": DeviceType.FIREWALL.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.CLOUD.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.ROUTER.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.PC1.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.PC2.value, "status": DeviceConnectionStatus.CONNECTED.value}
        ] 

    @classmethod
    def show_settings(cls):
        if cls.settings is None:
            raise ValueError("Switch not initialized")
        return DeviceSchema.SwitchConfig(**cls.settings)
    @classmethod
    def get_conection_device(cls, device_name):
        for connection in cls.connections:
            if connection["device"] == device_name:
                connection["status"] = DeviceConnectionStatus.CONNECTED.value
                return f"{device_name} connected to Switch"
        return f"{device_name} not found in Switch connections"


class PC1:
    config= None
    settings = {}

    @classmethod
    def initialize(cls, config):
        cls.config = config
        cls.settings = {
            "ip": cls.config.IP_address_PC1,
            "dhcp": cls.config.DHCP_PC1,
            "firewall": cls.config.FIREWALL_PC1,
            "nat": cls.config.NAT_PC1
        }
        cls.position = (-1, 1)
        cls.connections = [
            {"device": DeviceType.ROUTER.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.CLOUD.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.FIREWALL.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.SWITCH.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.PC2.value, "status": DeviceConnectionStatus.DISCONNECTED.value}
        ]  

    @classmethod
    def show_settings(cls):
        if cls.settings is None:
            raise ValueError("PC1 not initialized")
        return DeviceSchema.PCConfig(**cls.settings)
    
    @classmethod
    def get_conection_device(cls, device_name):
        for connection in cls.connections:
            if connection["device"] == device_name:
                connection["status"] = DeviceConnectionStatus.CONNECTED.value
                return f"{device_name} connected to PC1"
        return f"{device_name} not found in PC1 connections"

class PC2:
    config= None
    settings = {}

    @classmethod
    def initialize(cls, config):
        cls.config = config
        cls.settings = {
            "ip": cls.config.IP_address_PC2,
            "dhcp": cls.config.DHCP_PC2,
            "firewall": cls.config.FIREWALL_PC2,
            "nat": cls.config.NAT_PC2
        }
        cls.position = (1, 1)
        cls.connections = [
            {"device": DeviceType.ROUTER.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.CLOUD.value, "status": DeviceConnectionStatus.DISCONNECTED.value},
            {"device": DeviceType.FIREWALL.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.SWITCH.value, "status": DeviceConnectionStatus.CONNECTED.value},
            {"device": DeviceType.PC1.value, "status": DeviceConnectionStatus.DISCONNECTED.value}
        ]  

    @classmethod
    def show_settings(cls):
        if cls.settings is None:
            raise ValueError("PC2 not initialized")
        return DeviceSchema.PCConfig(**cls.settings)
    @classmethod
    def get_conection_device(cls, device_name):
        for connection in cls.connections:
            if connection["device"] == device_name:
                connection["status"] = DeviceConnectionStatus.CONNECTED.value
                return f"{device_name} connected to PC2"
        return f"{device_name} not found in PC2 connections"


