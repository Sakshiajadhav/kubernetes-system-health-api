import pytest
from unittest.mock import patch
from app import app, get_system_metrics


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


class TestHealthEndpoint:
    """Tests for /health endpoint"""
    
    def test_health_returns_200(self, client):
        """Test that /health returns HTTP 200"""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_returns_json(self, client):
        """Test that /health returns JSON data"""
        response = client.get('/health')
        data = response.get_json()
        assert isinstance(data, dict)
    
    def test_health_has_required_fields(self, client):
        """Test that /health has cpu, memory, disk, status"""
        response = client.get('/health')
        data = response.get_json()
        assert 'cpu' in data
        assert 'memory' in data
        assert 'disk' in data
        assert 'status' in data
    
    def test_health_status_is_valid(self, client):
        """Test that status is either 'healthy' or 'unhealthy'"""
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] in ['healthy', 'unhealthy']


class TestMetricsEndpoint:
    """Tests for /metrics endpoint"""
    
    def test_metrics_returns_200(self, client):
        """Test that /metrics returns HTTP 200"""
        response = client.get('/metrics')
        assert response.status_code == 200

    def test_metrics_has_threshold_values(self, client):
        """Test that /metrics returns configured threshold values"""
        response = client.get('/metrics')
        data = response.get_json()

        assert 'cpu_threshold' in data
        assert 'memory_threshold' in data
        assert 'disk_threshold' in data


class TestReadyEndpoint:
    """Tests for /ready endpoint"""
    
    def test_ready_returns_200(self, client):
        """Test that /ready returns HTTP 200"""
        response = client.get('/ready')
        assert response.status_code == 200

    def test_ready_returns_expected_response(self, client):
        """Test that /ready returns expected JSON response"""
        response = client.get('/ready')
        data = response.get_json()

        assert data == {"ready": True}


class TestLiveEndpoint:
    """Tests for /live endpoint"""
    
    def test_live_returns_200(self, client):
        """Test that /live returns HTTP 200"""
        response = client.get('/live')
        assert response.status_code == 200

    def test_live_returns_expected_response(self, client):
        """Test that /live returns expected JSON response"""
        response = client.get('/live')
        data = response.get_json()

        assert data == {"alive": True}


class TestSystemMetrics:
    """Tests for system metric status calculation"""

    @patch('app.psutil.disk_usage')
    @patch('app.psutil.virtual_memory')
    @patch('app.psutil.cpu_percent')
    def test_get_system_metrics_returns_healthy_when_under_threshold(
        self, mock_cpu, mock_memory, mock_disk
    ):
        """Test health status is healthy when all metrics are below thresholds"""
        mock_cpu.return_value = 10
        mock_memory.return_value.percent = 20
        mock_disk.return_value.percent = 30

        data = get_system_metrics()

        assert data["status"] == "healthy"

    @patch('app.psutil.disk_usage')
    @patch('app.psutil.virtual_memory')
    @patch('app.psutil.cpu_percent')
    def test_get_system_metrics_returns_unhealthy_when_over_threshold(
        self, mock_cpu, mock_memory, mock_disk
    ):
        """Test health status is unhealthy when CPU crosses threshold"""
        mock_cpu.return_value = 95
        mock_memory.return_value.percent = 20
        mock_disk.return_value.percent = 30

        data = get_system_metrics()

        assert data["status"] == "unhealthy"