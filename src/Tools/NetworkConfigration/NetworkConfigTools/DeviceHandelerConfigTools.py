from ..Schemas import DeviceSchema
from ..SimulatedDevice import VirtualFirewall,VirtualRouter,VirtualSwitch

class DeviceHandelerConfigTools:

    
    class ChangeDeviceConfig:

        class ChangeRouterConfig:
            @staticmethod
            def show_settings(router: VirtualRouter):
                return router.settings

            @staticmethod
            def change_ip(router: VirtualRouter, new_ip):
                router.settings["ip"] = new_ip
                return {"status": "IP changed", "ip": router.settings["ip"]}
            @staticmethod
            def enable_dhcp(router: VirtualRouter):
                router.settings["dhcp"] = True
                return {"status": "DHCP enabled"}
            @staticmethod
            def disable_dhcp(router: VirtualRouter):
                router.settings["dhcp"] = False
                return {"status": "DHCP disabled"}
            @staticmethod
            def enable_nat(router: VirtualRouter):
                router.settings["nat"] = True
                return {"status": "NAT enabled"}
            @staticmethod
            def disable_nat(router: VirtualRouter):
                router.settings["nat"] = False
                return {"status": "NAT disabled"}


        class ChangeSwitchConfig:
            @staticmethod
            def show_settings(switch: VirtualSwitch):
                return switch.settings

            @staticmethod
            def change_vlan(switch: VirtualSwitch, new_vlan):
                switch.settings["vlan"] = new_vlan
                return {"status": "VLAN changed", "vlan": switch.settings["vlan"]}
            @staticmethod
            def enable_port_security(switch: VirtualSwitch):
                switch.settings["port_security"] = True
                return {"status": "Port Security enabled"}
            @staticmethod
            def disable_port_security(switch: VirtualSwitch):
                switch.settings["port_security"] = False
                return {"status": "Port Security disabled"}
            @staticmethod
            def enable_nat(switch: VirtualSwitch):
                switch.settings["nat"] = True
                return {"status": "NAT enabled"}
            @staticmethod
            def disable_nat(switch: VirtualSwitch):
                switch.settings["nat"] = False
                return {"status": "NAT disabled"}
        
        class ChangeFirewallConfig:
            @staticmethod
            def show_settings(firewall: VirtualFirewall):
                return firewall.settings

            @staticmethod
            def add_rule(firewall: VirtualFirewall, rule):
                firewall.settings["rules"].append(rule)
                return {"status": "Rule added", "rules": firewall.settings["rules"]}
            @staticmethod
            def remove_rule(firewall: VirtualFirewall, rule):
                if rule in firewall.settings["rules"]:
                    firewall.settings["rules"].remove(rule)
                    return {"status": "Rule removed", "rules": firewall.settings["rules"]}
                return {"status": "Rule not found"}
            @staticmethod
            def set_default_action(firewall: VirtualFirewall, action):
                firewall.settings["default_action"] = action
                return {"status": "Default action set", "default_action": firewall.settings["default_action"]}

        
