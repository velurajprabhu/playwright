from behave import *

def generate_token(context):
    res = context.api.post("/auth/credentials", {
        "username": "Admin",
        "password": "admin123"
    })

    assert res.status_code == 200, f"Auth failed: {res.text}"

    token = res.json()["data"]["token"]
    context.api.set_token(token)

@when("employee is created via API")
def step_impl(context):

    generate_token(context)

    payload = {
        "firstName": "APIUser",
        "lastName": "Test"
    }

    res = context.api.post("/pim/employees", payload)
    assert res.status_code == 200, res.text

    data = res.json()["data"]
    context.emp_id = data["empNumber"]
    context.emp_name = data["firstName"]

@then("employee list from API should match UI")
def step_impl(context):

    res = context.api.get("/pim/employees")
    assert res.status_code == 200

    api_names = [e["firstName"] for e in res.json()["data"]]

    ui_names = context.page.locator("div[role='row']").all_inner_texts()

    assert any(name in " ".join(ui_names) for name in api_names), """
❌ API and UI mismatch
"""

@when("leave is applied via API")
def step_impl(context):

    payload = {
        "empNumber": context.emp_id,
        "leaveTypeId": 1,
        "fromDate": "2026-25-03",
        "toDate": "2026-26-03"
    }

    res = context.api.post("/leave/leave-requests", payload)
    assert res.status_code == 200, res.text

    context.leave_id = res.json()["data"]["id"]

@then("leave should be visible in UI")
def step_impl(context):

    context.leave_page.navigate()
    context.leave_page.search_leave()

    assert context.leave_page.is_status_visible("Pending"), """
❌ Leave not visible in UI
"""

@then("leave status should be updated in UI")
def step_impl(context):

    assert context.leave_page.is_status_visible("Approved"), """
❌ Leave not approved in UI
"""

@then("employee should be deleted via API")
def step_impl(context):

    res = context.api.delete(f"/pim/employees/{context.emp_id}")
    assert res.status_code == 200

@then("employee should appear in UI")
def step_impl(context):

    context.pim_page.navigate_to_pim()
    context.pim_page.search_employee(context.emp_name)

    assert context.pim_page.is_employee_present(context.emp_name), f"""
❌ Employee not visible in UI
Name: {context.emp_name}
"""

@when("leave is approved via API")
def step_impl(context):

    res = context.api.put(
        f"/leave/leave-requests/{context.leave_id}",
        {"status": "Approved"}
    )

    assert res.status_code == 200