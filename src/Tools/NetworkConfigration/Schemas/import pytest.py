import pytest
from unittest.mock import Mock, patch, MagicMock
from .DeviceInfoTools import DeviceInfoTools

class TestDeviceInfoTools:
    """Tests for DeviceInfoTools class"""

    def test_get_device_instance_router(self):
        """Test get_device_instance returns normalized device name for router"""
        result = DeviceInfoTools.get_device_instance("Router")
        assert result == "router"

    def test_get_device_instance_with_spaces_and_hyphens(self):
        """Test get_device_instance normalizes spaces and hyphens"""
        result = DeviceInfoTools.get_device_instance("Virtual-Router")
        assert result == "virtualrouter"

    def test_get_device_instance_cloud(self):
        """Test get_device_instance for cloud provider"""
        result = DeviceInfoTools.get_device_instance("Cloud")
        assert result == "cloud"


class TestGetDeviceInfo:
    """Tests for GetDeviceInfo nested class"""

    @patch('DeviceInfoTools.DEVICE_CLASS_MAP')
    def test_show_device_settings_success(self, mock_device_map):
        """Test show_device_settings returns success with valid device"""
        mock_device_class = Mock()
        mock_device_class.show_settings.return_value = {
            "ip": "192.168.1.1",
            "dhcp": True,
            "nat": True,
            "firewall": True
        }
        mock_device_map.__getitem__.return_value = mock_device_class

        result = DeviceInfoTools.GetDeviceInfo.show_device_settings("router")

        assert result["status"] == "success"
        assert result["device"] == "ROUTER"
        assert "config" in result

    def test_show_device_settings_invalid_device(self):
        """Test show_device_settings handles invalid device gracefully"""
        result = DeviceInfoTools.GetDeviceInfo.show_device_settings("")
        assert result["status"] == "error"
        assert "error_message" in result

    @patch('DeviceInfoTools.DEVICE_CLASS_MAP')
    def test_show_device_settings_exception(self, mock_device_map):
        """Test show_device_settings handles exceptions"""
        mock_device_map.__getitem__.side_effect = KeyError("Device not found")

        result = DeviceInfoTools.GetDeviceInfo.show_device_settings("invalid")

        assert result["status"] == "error"
        assert "error_message" in result


class TestGetDeviceConnections:
    """Tests for GetDeviceConnections nested class"""

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_show_device_connections_success(self, mock_get_instance):
        """Test show_device_connections returns connections for valid device"""
        mock_device = Mock()
        mock_device.connections = [
            {"device": "switch", "status": "connected"},
            {"device": "firewall", "status": "connected"}
        ]
        mock_get_instance.return_value = mock_device

        result = DeviceInfoTools.GetDeviceConnections.show_device_connections("router")

        assert result["status"] == "success"
        assert result["device"] == "ROUTER"
        assert "connections" in result

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_show_device_connections_invalid_device(self, mock_get_instance):
        """Test show_device_connections handles invalid device"""
        mock_get_instance.return_value = None

        result = DeviceInfoTools.GetDeviceConnections.show_device_connections("invalid")

        assert result["status"] == "error"
        assert "error_message" in result

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_show_device_connections_exception(self, mock_get_instance):
        """Test show_device_connections handles exceptions"""
        mock_get_instance.side_effect = Exception("Connection error")

        result = DeviceInfoTools.GetDeviceConnections.show_device_connections("router")

        assert result["status"] == "error"
        assert "error_message" in result


class TestGetPCInfo:
    """Tests for GetPCInfo nested class"""

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_get_device_position_success(self, mock_get_instance):
        """Test get_device_position returns position for valid device"""
        mock_device = Mock()
        mock_device.position = (0, 1)
        mock_get_instance.return_value = mock_device

        result = DeviceInfoTools.GetPCInfo.get_device_position("pc1")

        assert result["status"] == "success"
        assert result["device"] == "PC1"
        assert result["position"] == (0, 1)

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_get_device_position_invalid_device(self, mock_get_instance):
        """Test get_device_position handles invalid device"""
        mock_get_instance.return_value = None

        result = DeviceInfoTools.GetPCInfo.get_device_position("invalid")

        assert result["status"] == "error"
        assert "error_message" in result

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_get_device_position_exception(self, mock_get_instance):
        """Test get_device_position handles exceptions"""
        mock_get_instance.side_effect = Exception("Position error")

        result = DeviceInfoTools.GetPCInfo.get_device_position("pc1")

        assert result["status"] == "error"
        assert "error_message" in result


class TestGetSpecialConnection:
    """Tests for GetSpcialConnection nested class"""

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_get_special_connection_success(self, mock_get_instance):
        """Test get_special_connection returns connection info"""
        mock_device = Mock()
        mock_device.get_conection_device.return_value = "firewall connected to router"
        mock_get_instance.return_value = mock_device

        result = DeviceInfoTools.GetSpcialConnection.get_special_connection("router")

        assert result["status"] == "success"
        assert result["device"] == "ROUTER"
        assert result["target_device"] == "FIREWALL"
        assert "connection" in result

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_get_special_connection_invalid_device(self, mock_get_instance):
        """Test get_special_connection handles invalid device"""
        mock_get_instance.return_value = None

        result = DeviceInfoTools.GetSpcialConnection.get_special_connection("invalid")

        assert result["status"] == "error"
        assert "error_message" in result

    def test_get_special_connection_unsupported_target(self):
        """Test get_special_connection with unsupported device"""
        result = DeviceInfoTools.GetSpcialConnection.get_special_connection("unsupported-device")

        assert result["status"] == "error"
        assert "error_message" in result

    @patch('DeviceInfoTools.DeviceInfoTools.get_device_instance')
    def test_get_special_connection_exception(self, mock_get_instance):
        """Test get_special_connection handles exceptions"""
        mock_get_instance.side_effect = Exception("Connection error")

        result = DeviceInfoTools.GetSpcialConnection.get_special_connection("router")

        assert result["status"] == "error"
        assert "error_message" in result