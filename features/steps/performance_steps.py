from behave import *
from pages.pim_page import PimPage

@then("dashboard should load within 3 seconds using browser metrics")
def step_impl(context):

    perf = context.page.evaluate("window.performance.timing")

    load_time = (perf["loadEventEnd"] - perf["navigationStart"]) / 1000

    print(f"⏱ Dashboard Load (Browser API): {load_time:.2f}s")

    assert load_time < 3, f"""
❌ Dashboard too slow
Expected: < 3s
Actual: {load_time:.2f}s
"""

@when("user navigates to employee list with performance tracking")
def step_impl(context):
    context.page.evaluate("""
    () => performance.mark('pim-start')
    """)
    context.pim_page.navigate_to_pim()
    context.page.locator("div[role='row']").first.wait_for()
    context.page.evaluate("""
    () => {
        performance.mark('pim-end');

        if (performance.getEntriesByName('pim-start').length > 0) {
            performance.measure('pim-load', 'pim-start', 'pim-end');
        }
    }
    """)
    duration = context.page.evaluate("""
    () => {
        const entry = performance.getEntriesByName('pim-load')[0];
        return entry ? entry.duration : -1;
    }
    """)

    assert duration != -1, "❌ Performance mark not created"
    #
    # context.pim_page.navigate_to_pim()
    # context.page.locator("div[role='row']").first.wait_for()
    # context.page.evaluate("performance.mark('pim-end')")
    # context.page.evaluate("performance.measure('pim-load', 'pim-start', 'pim-end')")

@then("employee list should load within 3 seconds using browser metrics")
def step_impl(context):

    duration = context.page.evaluate("""
    () => performance.getEntriesByName('pim-load')[0].duration
    """)

    load_time = duration / 1000

    print(f"⏱ Employee List Load (SPA): {load_time:.2f}s")

    assert load_time < 3, f"""
❌ Employee list too slow
Expected: < 3s
Actual: {load_time:.2f}s
"""

@when("user creates employee with browser performance tracking")
def step_impl(context):

    # 🔥 Ensure correct navigation FIRST
    context.pim_page.navigate_to_pim()
    context.pim_page.click_add_employee()

    # Wait for form to be ready
    context.page.locator("input[name='firstName']").wait_for()

    # Clear previous performance entries
    context.page.evaluate("performance.clearResourceTimings()")

    # Start mark
    context.page.evaluate("performance.mark('emp-start')")

    # Perform action
    context.pim_page.add_employee("PerfUser", "Test")

    # Wait for success
    context.page.locator("text=Successfully Saved").wait_for()

    # End mark
    context.page.evaluate("performance.mark('emp-end')")

@then("employee creation should complete within 2 seconds using browser metrics")
def step_impl(context):

    data = context.page.evaluate("""
    () => {
        const resources = performance.getEntriesByType('resource');

        // Find employee API call
        const api = resources.find(r => r.name.includes('/pim/employees'));

        if (!api) return null;

        return {
            duration: api.duration,
            startTime: api.startTime,
            responseEnd: api.responseEnd
        };
    }
    """)

    assert data is not None, "❌ Employee API call not captured"

    duration = data["duration"] / 1000

    print(f"⏱ Create Employee (Browser API): {duration:.2f}s")

    assert duration < 2, f"""
❌ Create employee too slow
Expected: < 2s
Actual: {duration:.2f}s
"""