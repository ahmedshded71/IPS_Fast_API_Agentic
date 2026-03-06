from enum import Enum

class DeviceType(Enum):
    FIREWALL = "FIREWALL"
    ROUTER = "ROUTER"
    SWITCH = "SWITCH"
    PC1 = "PC1"
    PC2 = "PC2"
    CLOUDE = "CLOUDE_PROVIDER"

class DeviceConnectionStatus(Enum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
