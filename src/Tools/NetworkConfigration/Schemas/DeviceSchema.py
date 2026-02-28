from pydantic import BaseModel, BaseSettings, Field



class DeviceSchema(BaseModel):
    class RouterConfig ( BaseModel):    
        ip: str = Field(..., example="192.168.1.1")
        dhcp: bool = Field(..., example=True)
        firewall: str = Field(..., example="off")
        nat: bool = Field(..., example=False)


    class SwitchConfig ( BaseModel):
        vlan: int = Field(..., example=10)
        port_security: bool = Field(..., example=True)
        stp: bool = Field(..., example=True)
        qos: str = Field(..., example="high")

        
    class FirewallConfig ( BaseModel):
        rules: list = Field(..., example=[{"action": "allow", "protocol": "tcp", "port": 80}])
        default_action: str = Field(..., example="deny")
        logging: bool = Field(..., example=True)
        intrusion_detection: bool = Field(..., example=True)


