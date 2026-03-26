def generate_token(api):
    res = api.post("/auth/credentials", {
        "username": "Admin",
        "password": "admin123"
    })
    print("STATUS:", res.status_code)
    print("RESPONSE:", res.text)
    assert res.status_code == 200, f"Auth failed: {res.text}"

    token = res.json()["data"]["token"]
    api.set_token(token)