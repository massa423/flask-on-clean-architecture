class TestTopPage:
    def test_top_page(self, client):

        rv = client.get("/")
        assert b"<title>Top Page</title>" in rv.data
        assert b"<h1>This is a top page</h1>" in rv.data
        assert b'<a href="/signup/index">signup</a>' in rv.data
        assert b'<a href="/redirect">redirect</a>' in rv.data
        assert b'<a href="/index">top</a>' in rv.data


class TestSignUpPage:
    def test_signup_index(self, client):
        rv = client.get("/signup/index")
        assert b"<title>Signup</title>" in rv.data
        assert b"This is a signup page" in rv.data

    def test_signup_confirm(self, client):
        rv = client.post(
            "/signup/confirm",
            data=dict(
                name="test_user",
                password1="password",
                password2="password",
                email="sample@example.com",
            ),
            follow_redirects=True,
        )
        assert b"<title>Signup confirm</title>" in rv.data

    def test_signup_done(self, client):
        rv = client.post(
            "/signup/done",
            data=dict(
                name="test_user",
                password="password",
                email="sample@example.com",
            ),
            follow_redirects=True,
        )
        assert b"<title>Signup done</title>" in rv.data
