from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
from typing import List
class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    OPENAI_API_KEY: str
    APP_NAME:str
    APP_VERSION:str
    #router settings
    IP_address: str 
    DHCP: bool
    FIREWALL:str
    NAT: bool


    # Switch settings
    VLANS: List[dict] = [
        {"id": 10, "name": "VLAN10", "subnet": "0.0.0/24"}, 
        {"id": 20, "name": "VLAN20", "subnet": "0.0.0/24"}
    ]
    PORTSECURITY: List[dict] = [
        {"id": 1, "name": "Port1", "status": "up"}, 
        {"id": 2, "name": "Port2", "status": "down"}
    ]
    STP: bool
    QOS: bool

    # firewall settings
    RULES: List[dict] = [
        {"action": "allow", "protocol": "tcp", "port": 80},
        {"action": "deny", "protocol": "udp", "port": 53}
    ]
    DEFAULT_POLICY: str 
    LOGGING: bool
    INTRUSION_DETECTION: bool


    IP_address_PC1: str
    DHCP_PC1: bool
    FIREWALL_PC1: str
    NAT_PC1: bool

    IP_address_PC2: str
    DHCP_PC2: bool
    FIREWALL_PC2: str
    NAT_PC2: bool
    # VirtualCloud Network Configuration
    CLOUD_IP: str
    CLOUD_SUBNET: str
    CLOUD_GATEWAY: str


    # Services
    CLOUD_IP_address: str
    CLOUD_DHCP: bool
    CLOUD_NAT: bool
    CLOUD_FIREWALL: str

    # VLANs inside cloud
    BANDWIDTH: int
    PROVIDER_NAME: str  
    REGION: str
    AVAILABILITY_ZONE: str 
    INSTANCE_TYPE: str 
    CLOUD_VLANS: List[dict] 

    # Ports configuration
    CLOUD_PORTS: List[dict] 

    # QoS and STP
    CLOUD_QOS: str 
    CLOUD_STP: bool 


    model_config = SettingsConfigDict(env_file=".env")

def get_settings():
    return Settings()





