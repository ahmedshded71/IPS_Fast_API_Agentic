from enum import Enum


class DeviceName(Enum):
    ROUTER = "ROUTER"
    SWITCH = "SWITCH"
    FIREWALL = "FIREWALL"
    PC1 = "PC1"
    PC2 = "PC2"
    CLOUD = "CLOUD"

    @classmethod
    def normalize_device_name(cls, device: str):
        if not device:
            return None

        normalized = device.lower().replace("-", "").replace(" ", "")

        for dev in cls:
            if dev.value.lower() == normalized:
                return dev

        return {"massage":DeviceInfoEnums.INITIALIZEDERROR.value}

class DeviceInfoEnums(Enum):
    INITIALIZEDERROR = "DEVICE_NOT_INITIALIZED"
    DEVICEINITIALIZEDNOTFOUND= "DEVICE_NOT_FOUND_OR_NOT_INITIALIZED"
    DEVICECONNECTIONERROR = "DEVICE_CONNECTION_ERROR"
    DEVICEPOSITIONERROR = "DEVICE_POSITION_ERROR"