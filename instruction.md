Parse the Apache-style access log located at `/app/access.log`.

Analyze the traffic and fulfill the following criteria:
1. Generate a valid JSON summary report at `/app/report.json`.
2. The JSON object must contain the key "total_requests": An integer representing the total number of log entries.
3. The JSON object must contain the key "unique_ips": An integer representing the total number of unique client IP addresses.
4. The JSON object must contain the key "top_path": A string representing the most frequently requested path.

You have 120.0 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.