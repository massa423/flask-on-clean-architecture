class TestUser:
    """
    user APIのテスト
    """

    def test_get_user(self, client):
        """
        正常系
        """

        rv = client.get("/api/v1/users/test-user")
        data = rv.get_json()

        assert data["name"] is None
        assert data["email"] is None
        assert data["created_at"] is None
        assert data["updated_at"] is None

    def test_get_user_with_sample_data(self, client_with_testdata):
        """
        正常系(テストデータあり)
        """

        rv = client_with_testdata.get("/api/v1/users/test-user1")
        data = rv.get_json()

        assert data["name"] == "test-user1"
        assert data["email"] == "test-user1@example.com"
