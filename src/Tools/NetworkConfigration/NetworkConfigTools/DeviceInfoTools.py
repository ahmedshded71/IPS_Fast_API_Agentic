from ..Schemas import DeviceSchema,ConnectionSchema
from ..SimulatedDevice import VirtualFirewall,VirtualRouter,VirtualSwitch ,PC1,PC2,VirtualCloudProvider
from .Enums import DeviceName,DeviceInfoEnums



class DeviceInfoTools:


    class GetDeviceInfo:

        @staticmethod
        def show_Device_settings(device: str):
            try:    
                if device == None:
                    return {"massage": DeviceInfoEnums.INITIALIZEDERROR.value}
                if device.lower() == DeviceName.ROUTER.value.lower():
                    router = VirtualRouter()
                    return DeviceSchema.RouterConfig(
                        **router.show_settings()
                    ).model_dump()
                if device.lower() == DeviceName.SWITCH.value.lower():
                    switch = VirtualSwitch()
                    return DeviceSchema.SwitchConfig(
                        **switch.show_settings()
                    ).model_dump()
                if device.lower() == DeviceName.FIREWALL.value.lower():
                    firewall = VirtualFirewall()
                    return DeviceSchema.FirewallConfig(
                        **firewall.show_settings()
                    ).model_dump()
                if device.lower() == DeviceName.PC1.value.lower():
                    pc1 = PC1()
                    return DeviceSchema.PCConfig(
                        **pc1.show_settings()
                    ).model_dump()
                if device.lower() == DeviceName.PC2.value.lower():
                    pc2 = PC2()
                    return DeviceSchema.PCConfig(
                        **pc2.show_settings()
                    ).model_dump()
                if device.lower() == DeviceName.CLOUD.value.lower():
                    cloud = VirtualCloudProvider()
                    return DeviceSchema.CloudProviderConfig(
                        **cloud.show_settings()
                    ).model_dump()
            except:
                return {"massage": DeviceInfoEnums.DEVICEINITIALIZEDNOTFOUND.value}



    class GetDeviceConnections:

        @staticmethod
        def show_Device_connections(device: str):
            try:    
                if device == None:
                    return {"massage": DeviceInfoEnums.DEVICECONNECTIONERROR.value}
                if device.lower() == DeviceName.ROUTER.value.lower():
                    router = VirtualRouter()
                    return [ConnectionSchema(**conn) for conn in router.connections]
                if device.lower() == DeviceName.SWITCH.value.lower():
                    switch = VirtualSwitch()
                    return [ConnectionSchema(**conn) for conn in switch.connections]
                if device.lower() == DeviceName.FIREWALL.value.lower():
                    firewall = VirtualFirewall()
                    return [ConnectionSchema(**conn) for conn in firewall.connections]
                if device.lower() == DeviceName.PC1.value.lower():
                    pc1 = PC1()
                    return [ConnectionSchema(**conn) for conn in pc1.connections]
                if device.lower() == DeviceName.PC2.value.lower():
                    pc2 = PC2()
                    return [ConnectionSchema(**conn) for conn in pc2.connections]
                if device.lower() == DeviceName.CLOUD.value.lower():
                    cloud = VirtualCloudProvider()
                    return [ConnectionSchema(**conn) for conn in cloud.connections]
            except:
                return {"massage": DeviceInfoEnums.INITIALIZEDERROR.value}

            
    class GetPCInfo:
        @staticmethod
        def get_conection_device(device: str):
            try:    
                if device == None:
                    return {"massage": DeviceInfoEnums.DEVICEPOSITIONERROR.value}
                if device.lower() == DeviceName.ROUTER.value.lower():
                    router = VirtualRouter()
                    return router.position
                if device.lower() == DeviceName.SWITCH.value.lower():
                    switch = VirtualSwitch()
                    return switch.position
                if device.lower() == DeviceName.FIREWALL.value.lower():
                    firewall = VirtualFirewall()
                    return firewall.position
                if device.lower() == DeviceName.PC1.value.lower():
                    pc1 = PC1()
                    return pc1.position
                if device.lower() == DeviceName.PC2.value.lower():
                    pc2 = PC2()
                    return pc2.position
                if device.lower() == DeviceName.CLOUD.value.lower():
                    cloud = VirtualCloudProvider()
                    return cloud.position
            except:
                return {"massage": DeviceInfoEnums.DEVICEPOSITIONERROR.value}
            

            
    class GetSpcialConnection:
        @staticmethod
        def get_conection_device(device: str):
            try:    
                if device == None:
                    return {"massage": DeviceInfoEnums.DEVICECONNECTIONERROR.value}
                if device.lower() == DeviceName.ROUTER.value.lower():
                    router = VirtualRouter()
                    return router.get_conection_device(DeviceName.FIREWALL.value)
                if device.lower() == DeviceName.SWITCH.value.lower():
                    switch = VirtualSwitch()
                    return switch.get_conection_device(DeviceName.ROUTER.value)
                if device.lower() == DeviceName.FIREWALL.value.lower():
                    firewall = VirtualFirewall()
                    return firewall.get_conection_device(DeviceName.ROUTER.value)
                if device.lower() == DeviceName.PC1.value.lower():
                    pc1 = PC1()
                    return pc1.get_conection_device(DeviceName.SWITCH.value)
                if device.lower() == DeviceName.PC2.value.lower():
                    pc2 = PC2()
                    return pc2.get_conection_device(DeviceName.SWITCH.value)
                if device.lower() == DeviceName.CLOUD.value.lower():
                    cloud = VirtualCloudProvider()
                    return cloud.get_conection_device(DeviceName.ROUTER.value)
            except:
                return {"massage": DeviceInfoEnums.DEVICECONNECTIONERROR.value}


    
