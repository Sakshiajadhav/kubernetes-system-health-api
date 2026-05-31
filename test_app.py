import pytest
from app import app

# Setup: Create test client that can send requests to your app
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


class TestReadyEndpoint:
    """Tests for /ready endpoint"""
    
    def test_ready_returns_200(self, client):
        """Test that /ready returns HTTP 200"""
        response = client.get('/ready')
        assert response.status_code == 200


class TestLiveEndpoint:
    """Tests for /live endpoint"""
    
    def test_live_returns_200(self, client):
        """Test that /live returns HTTP 200"""
        response = client.get('/live')
        assert response.status_code == 200
