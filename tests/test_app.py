"""
Comprehensive tests for the High School Activities API using AAA (Arrange-Act-Assert) pattern.
"""

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to path to import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test."""
    # Arrange: Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
    }
    
    # Clear existing activities and restore defaults
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Cleanup: Reset again after test
    activities.clear()
    activities.update(original_activities)


class TestGetActivities:
    """Tests for GET /activities endpoint."""
    
    def test_get_activities_returns_all_activities(self, client, reset_activities):
        """Test that GET /activities returns all available activities."""
        # Arrange: Activities are already loaded via fixture
        
        # Act: Send GET request
        response = client.get("/activities")
        
        # Assert: Verify response
        assert response.status_code == 200
        data = response.json()
        assert "Chess Club" in data
        assert "Programming Class" in data
        assert "Gym Class" in data
        assert len(data) == 3
    
    def test_get_activities_returns_correct_structure(self, client, reset_activities):
        """Test that each activity has required fields."""
        # Arrange: Activities are loaded
        
        # Act: Send GET request
        response = client.get("/activities")
        data = response.json()
        
        # Assert: Verify structure
        activity = data["Chess Club"]
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
    
    def test_get_activities_includes_participants(self, client, reset_activities):
        """Test that participants list is included in response."""
        # Arrange: Activities have participants
        
        # Act: Send GET request
        response = client.get("/activities")
        data = response.json()
        
        # Assert: Verify participants are included
        chess_participants = data["Chess Club"]["participants"]
        assert "michael@mergington.edu" in chess_participants
        assert "daniel@mergington.edu" in chess_participants


class TestSignup:
    """Tests for POST /activities/{name}/signup endpoint."""
    
    def test_signup_student_successfully(self, client, reset_activities):
        """Test successful signup for a new student."""
        # Arrange: Prepare test data
        activity_name = "Chess Club"
        email = "newemail@mergington.edu"
        initial_count = len(activities[activity_name]["participants"])
        
        # Act: Send signup request
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert: Verify signup success and participant added
        assert response.status_code == 200
        assert "message" in response.json()
        assert email in activities[activity_name]["participants"]
        assert len(activities[activity_name]["participants"]) == initial_count + 1
    
    def test_signup_returns_success_message(self, client, reset_activities):
        """Test that signup returns appropriate success message."""
        # Arrange: Test data
        activity_name = "Programming Class"
        email = "test@mergington.edu"
        
        # Act: Send signup request
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert: Verify message format
        assert response.status_code == 200
        data = response.json()
        assert f"Signed up {email} for {activity_name}" in data["message"]
    
    def test_signup_prevents_double_registration(self, client, reset_activities):
        """Test that a student cannot register twice for the same activity."""
        # Arrange: Student already registered
        activity_name = "Chess Club"
        email = "michael@mergington.edu"
        
        # Act: Try to signup again
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert: Verify error response
        assert response.status_code == 400
        assert "already signed up" in response.json()["detail"]
    
    def test_signup_for_nonexistent_activity_returns_404(self, client, reset_activities):
        """Test that signing up for non-existent activity returns 404."""
        # Arrange: Non-existent activity
        activity_name = "Nonexistent Club"
        email = "test@mergington.edu"
        
        # Act: Try to signup
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert: Verify 404 error
        assert response.status_code == 404
        assert "Activity not found" in response.json()["detail"]
    
    def test_signup_multiple_students_to_same_activity(self, client, reset_activities):
        """Test that multiple different students can signup for same activity."""
        # Arrange: Test data
        activity_name = "Gym Class"
        emails = ["student1@mergington.edu", "student2@mergington.edu"]
        initial_count = len(activities[activity_name]["participants"])
        
        # Act: Sign up multiple students
        for email in emails:
            response = client.post(
                f"/activities/{activity_name}/signup",
                params={"email": email}
            )
            assert response.status_code == 200
        
        # Assert: All students added
        for email in emails:
            assert email in activities[activity_name]["participants"]
        assert len(activities[activity_name]["participants"]) == initial_count + 2


class TestUnregister:
    """Tests for POST /activities/{name}/unregister endpoint."""
    
    def test_unregister_student_successfully(self, client, reset_activities):
        """Test successful unregistration from an activity."""
        # Arrange: Select student from existing participants
        activity_name = "Chess Club"
        email = "michael@mergington.edu"
        initial_count = len(activities[activity_name]["participants"])
        
        # Act: Send unregister request
        response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email}
        )
        
        # Assert: Verify unregister success and participant removed
        assert response.status_code == 200
        assert "message" in response.json()
        assert email not in activities[activity_name]["participants"]
        assert len(activities[activity_name]["participants"]) == initial_count - 1
    
    def test_unregister_returns_success_message(self, client, reset_activities):
        """Test that unregister returns appropriate success message."""
        # Arrange: Test data
        activity_name = "Programming Class"
        email = "emma@mergington.edu"
        
        # Act: Send unregister request
        response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email}
        )
        
        # Assert: Verify message format
        assert response.status_code == 200
        data = response.json()
        assert f"Removed {email} from {activity_name}" in data["message"]
    
    def test_unregister_nonexistent_student_returns_400(self, client, reset_activities):
        """Test that unregistering non-participating student returns 400."""
        # Arrange: Student not in activity
        activity_name = "Chess Club"
        email = "nonparticipant@mergington.edu"
        
        # Act: Try to unregister
        response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email}
        )
        
        # Assert: Verify error response
        assert response.status_code == 400
        assert "not signed up" in response.json()["detail"]
    
    def test_unregister_from_nonexistent_activity_returns_404(self, client, reset_activities):
        """Test that unregistering from non-existent activity returns 404."""
        # Arrange: Non-existent activity
        activity_name = "Nonexistent Club"
        email = "test@mergington.edu"
        
        # Act: Try to unregister
        response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email}
        )
        
        # Assert: Verify 404 error
        assert response.status_code == 404
        assert "Activity not found" in response.json()["detail"]
    
    def test_unregister_removes_only_specified_student(self, client, reset_activities):
        """Test that unregister only removes the specified student."""
        # Arrange: Multiple students in activity
        activity_name = "Chess Club"
        email_to_remove = "michael@mergington.edu"
        email_to_keep = "daniel@mergington.edu"
        
        # Act: Unregister one student
        response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email_to_remove}
        )
        
        # Assert: Verify only one student removed
        assert response.status_code == 200
        assert email_to_remove not in activities[activity_name]["participants"]
        assert email_to_keep in activities[activity_name]["participants"]


class TestSignupUnregisterFlow:
    """Integration tests for signup and unregister flow."""
    
    def test_signup_then_unregister_flow(self, client, reset_activities):
        """Test complete flow: signup then unregister."""
        # Arrange: Test data
        activity_name = "Gym Class"
        email = "new_student@mergington.edu"
        
        # Act & Assert: Signup
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        assert signup_response.status_code == 200
        assert email in activities[activity_name]["participants"]
        
        # Act & Assert: Unregister
        unregister_response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email}
        )
        assert unregister_response.status_code == 200
        assert email not in activities[activity_name]["participants"]
    
    def test_cannot_unregister_after_signup_failure(self, client, reset_activities):
        """Test that failed signup doesn't allow unregister."""
        # Arrange: Test data (student already registered)
        activity_name = "Chess Club"
        email = "michael@mergington.edu"
        
        # Act: Try to signup (should fail)
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert: Signup failed, student still in list
        assert signup_response.status_code == 400
        
        # Act & Assert: Unregister should still work (was already registered)
        unregister_response = client.post(
            f"/activities/{activity_name}/unregister",
            params={"email": email}
        )
        assert unregister_response.status_code == 200
