from calendar import month
from datetime import datetime, timedelta, timezone
import google.cloud.logging
from google.oauth2 import service_account

cred = service_account.Credentials.from_service_account_file(
    'D:/VIIT/B.Tech/Major Project/CloudAgnosticMultiAgent/Test/TestGCPLogging/config/fourth-carport-468820-q0-4d7085bacfb3.json'
)

client = google.cloud.logging.Client(credentials=cred)

# Format timestamps to RFC 3339 standard (YYYY-MM-DDTHH:MM:SSZ)
# This prevents potential parsing errors by the API.
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(days=365)

start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
end_time_str = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')

filter_str = f'timestamp >= "{start_time_str}" AND timestamp <= "{end_time_str}"'
print(filter_str)

# Example usage:
for entry in client.list_entries(filter_=filter_str):
    print(entry.payload)