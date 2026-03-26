def assert_response_time(response, threshold, name):
    timing = response.timing

    duration = (timing["responseEnd"] - timing["startTime"]) / 1000

    print(f"⏱ {name}: {duration:.2f}s")

    assert duration < threshold, f"""
❌ Performance threshold breached
Step: {name}
Expected: < {threshold}s
Actual: {duration:.2f}s
"""