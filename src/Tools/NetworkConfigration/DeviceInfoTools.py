from Schemas import DeviceSchema
from SimulatedDevice import VirtualFirewall,VirtualRouter,VirtualSwitch


class DeviceInfoTools:


    class GeTRouterInfo:

        @staticmethod
        def get_router_info(device_name: str):
            if device_name.lower() == "router":
                router = VirtualRouter()
                return DeviceSchema.RouterConfig(
                    ip=router.show_settings()["ip"],
                dhcp=router.show_settings()["dhcp"],
                firewall=router.show_settings()["firewall"],
                nat=router.show_settings()["nat"]
            ).model_dump()
        
        @staticmethod
        def get_switch_info(device_name: str):
            if device_name.lower() == "switch":
                switch = VirtualSwitch()
                return DeviceSchema.SwitchConfig(
                    vlan=switch.show_settings()["vlan"],
                    port_security=switch.show_settings()["port_security"],
                    nat=switch.show_settings()["nat"]
                ).model_dump()
        
        @staticmethod
        def get_firewall_info(device_name: str):
            if device_name.lower() == "firewall":
                firewall = VirtualFirewall()
                return DeviceSchema.FirewallConfig(
                    rules=firewall.show_settings()["rules"],
                default_action=firewall.show_settings()["default_action"],
                logging=firewall.show_settings()["logging"],
                intrusion_detection=firewall.show_settings()["intrusion_detection"]
            ).model_dump()
        

