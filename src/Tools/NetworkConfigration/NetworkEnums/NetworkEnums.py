from enum import Enum


class NetworkConfigrationTools(str, Enum):
    DEVICE_INFO = "device_info"
    NETWORK_TOPOLOGY = "network_topology"
    TRAFFIC_ANALYSIS = "traffic_analysis"
    SECURITY_ASSESSMENT = "security_assessment"
    CONFIGURATION_MANAGEMENT = "configuration_management"
    PERFORMANCE_MONITORING = "performance_monitoring"
    ALERTING_AND_LOGGING = "alerting_and_logging"
    VULNERABILITY_SCANNING = "vulnerability_scanning"
    PATCH_MANAGEMENT = "patch_management"
    BACKUP_AND_RECOVERY = "backup_and_recovery"
    