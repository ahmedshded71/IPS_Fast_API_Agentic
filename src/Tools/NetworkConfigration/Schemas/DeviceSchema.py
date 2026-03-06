from pydantic import BaseModel, Field


class DeviceSchema(BaseModel):

    class RouterConfig(BaseModel):    
        ip: str = Field(..., example="192.168.1.1")
        dhcp: bool = Field(..., example=True)
        firewall: str = Field(..., example="off")
        nat: bool = Field(..., example=False)

    class SwitchConfig(BaseModel):
        vlan: list[dict] = Field(..., example=[{"action": "allow", "protocol": "tcp", "port": 80}])
        port_security: list[dict] = Field(..., example=[{"port": 1, "mac_address": "00:11:22:33:44:55", "action": "deny"}])
        stp: bool = Field(..., example=True)
        qos: bool = Field(..., example=True)

    class FirewallConfig(BaseModel):
        rules: list[dict] = Field(..., example=[{"action": "allow", "protocol": "tcp", "port": 80}])
        default_action: str = Field(..., example="deny")
        logging: bool = Field(..., example=True)
        intrusion_detection: bool = Field(..., example=True)

    class PCConfig(BaseModel):
        ip: str = Field(..., example="192.168.1.2")
        dhcp: bool = Field(..., example=True)
        firewall: str = Field(..., example="on")
        nat: bool = Field(..., example=True)
    
    class CloudProviderConfig(BaseModel):
        cloud_ip_address: str = Field(..., example="192.168.1.100")
        cloud_dhcp: bool = Field(..., example=True)
        cloud_nat: bool = Field(..., example=False)
        cloud_firewall: str = Field(..., example="on")
        bandwidth: int = Field(..., example=1000)
        provider_name: str = Field(..., example="AWS")
        region: str = Field(..., example="us-east-1")
        availability_zone: str = Field(..., example="us-east-1a")
        instance_type: str = Field(..., example="t2.micro")
        cloud_vlans: list[dict] = Field(..., example=[{"id": 10, "name": "VLAN10", "subnet": "0.0.0/24"}])
        cloud_ports: list[dict] = Field(..., example=[{"id": 1, "name": "Port1", "status": "up"}])
        cloud_qos: str = Field(..., example="high")
        cloud_stp: bool = Field(..., example=True)
