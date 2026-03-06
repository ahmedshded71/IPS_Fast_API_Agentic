from ..Schemas import DeviceSchema, ConnectionSchema
from ..SimulatedDevice import (
    VirtualFirewall,
    VirtualRouter,
    VirtualSwitch,
    PC1,
    PC2,
    VirtualCloudProvider
)
from .Enums import DeviceName, DeviceInfoEnums

# Mapping between normalized device names (strings) and device classes
DEVICE_CLASS_MAP = {
    "router": VirtualRouter,
    "switch": VirtualSwitch,
    "firewall": VirtualFirewall,
    "pc1": PC1,
    "pc2": PC2,
    "cloud": VirtualCloudProvider,
}


class DeviceInfoTools:

    @staticmethod
    def get_device_instance(device: str):
        """Return an instance of the device class based on normalized device name."""
        device_normalized = device.lower().replace("-", "").replace(" ", "")
        device_class = DEVICE_CLASS_MAP.get(device_normalized)
        if not device_class:
            return None
        return device_class()

    class GetDeviceInfo:

        @staticmethod
        def show_device_settings(device: str) -> dict:
            """Retrieve configuration settings of a device."""
            print(f"[Tool Execution] show_device_settings -> device: {device}")
            try:
                device_instance = DeviceInfoTools.get_device_instance(device)
                if not device_instance:
                    return {
                        "status": "error",
                        "device": device,
                        "error_message": DeviceInfoEnums.DEVICEINITIALIZEDNOTFOUND.value
                    }

                settings = device_instance.show_settings()
                schema_map = {
                    VirtualRouter: DeviceSchema.RouterConfig,
                    VirtualSwitch: DeviceSchema.SwitchConfig,
                    VirtualFirewall: DeviceSchema.FirewallConfig,
                    PC1: DeviceSchema.PCConfig,
                    PC2: DeviceSchema.PCConfig,
                    VirtualCloudProvider: DeviceSchema.CloudProviderConfig,
                }

                schema_class = schema_map.get(type(device_instance))
                if schema_class:
                    settings = schema_class(**settings).model_dump()

                return {
                    "status": "success",
                    "device": device.upper(),
                    "config": settings
                }

            except Exception as e:
                return {
                    "status": "error",
                    "device": device,
                    "error_message": str(e)
                }

    class GetDeviceConnections:

        @staticmethod
        def show_device_connections(device: str) -> dict:
            """Retrieve connections of a device."""
            print(f"[Tool Execution] show_device_connections -> device: {device}")
            try:
                device_instance = DeviceInfoTools.get_device_instance(device)
                if not device_instance:
                    return {
                        "status": "error",
                        "device": device,
                        "error_message": DeviceInfoEnums.DEVICECONNECTIONERROR.value
                    }

                connections = [
                    ConnectionSchema(**conn).model_dump()
                    for conn in device_instance.connections
                ]
                return {
                    "status": "success",
                    "device": device.upper(),
                    "connections": connections
                }

            except Exception as e:
                return {
                    "status": "error",
                    "device": device,
                    "error_message": str(e)
                }

    class GetPCInfo:

        @staticmethod
        def get_device_position(device: str) -> dict:
            """Retrieve the position of a device in the network topology."""
            print(f"[Tool Execution] get_device_position -> device: {device}")
            try:
                device_instance = DeviceInfoTools.get_device_instance(device)
                if not device_instance:
                    return {
                        "status": "error",
                        "device": device,
                        "error_message": DeviceInfoEnums.DEVICEPOSITIONERROR.value
                    }

                return {
                    "status": "success",
                    "device": device.upper(),
                    "position": device_instance.position
                }

            except Exception as e:
                return {
                    "status": "error",
                    "device": device,
                    "error_message": str(e)
                }

    class GetSpcialConnection:

        SPECIAL_CONNECTION_MAP = {
            "router": "firewall",
            "switch": "router",
            "firewall": "router",
            "pc1": "switch",
            "pc2": "switch",
            "cloud": "router",
        }

        @staticmethod
        def get_special_connection(device: str) -> dict:
            """Retrieve the special connection for a device."""
            print(f"[Tool Execution] get_special_connection -> device: {device}")
            try:
                device_normalized = device.lower().replace("-", "").replace(" ", "")
                device_instance = DeviceInfoTools.get_device_instance(device_normalized)
                if not device_instance:
                    return {
                        "status": "error",
                        "device": device,
                        "error_message": DeviceInfoEnums.DEVICEINITIALIZEDNOTFOUND.value
                    }

                target_device = DeviceInfoTools.GetSpcialConnection.SPECIAL_CONNECTION_MAP.get(device_normalized)
                if not target_device:
                    return {
                        "status": "error",
                        "device": device,
                        "error_message": DeviceInfoEnums.DEVICECONNECTIONERROR.value
                    }

                connection_info = device_instance.get_conection_device(target_device)

                return {
                    "status": "success",
                    "device": device.upper(),
                    "target_device": target_device.upper(),
                    "connection": connection_info
                }

            except Exception as e:
                return {
                    "status": "error",
                    "device": device,
                    "error_message": str(e)
                }