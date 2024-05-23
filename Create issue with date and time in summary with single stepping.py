import requests
from datetime import datetime
 
# Jira base URL and API endpoint for creating issues
base_url = "https://sonashrees.atlassian.net/rest/api/2"
issue_create_endpoint = "/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
auth = ("sonashrees05@gmail.com", "ATATT3xFfGF0ueW4m4vjDol0z-O-7tOUNlR4qgg272GEmJ7gzL9_Seh92qrRHL6dq2eTo1L9hKnFgF-aEuZRNWCVrCoUIoUx8z4huOozTuBfyBLkzzFcOMBpiOkTqcw8i9ZCTuegaPyVLiMGH2E9RI-PrzZTe4R-KCB_PHcYs5amAWssmqaAloc=B369273F")
 
# Function to create an issue with a timestamp in the summary
def create_issue_with_timestamp_in_summary(project_key, summary, description):
    print("Step 1: Starting function create_issue_with_timestamp_in_summary")
   
    # Create a timestamp
    print("Step 2: Creating timestamp")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Timestamp: {timestamp}")
   
    # Include the timestamp in the summary
    print("Step 3: Formatting summary with timestamp")
    summary_with_timestamp = f"Hey {summary} [{timestamp}] is ready"
    print(f"Summary with timestamp: {summary_with_timestamp}")
   
    # Issue data with timestamp in the summary
    print("Step 4: Preparing issue data")
    issue_data = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary_with_timestamp,
            "description": description,
            "issuetype": {
                "name": "Task"  # Change to the appropriate issue type
            }
        }
    }
    print(f"Issue data: {issue_data}")
   
    # URL for creating issue
    print("Step 5: Creating issue URL")
    create_issue_url = base_url + issue_create_endpoint
    print(f"Create issue URL: {create_issue_url}")
   
    # Send POST request to create issue
    print("Step 6: Sending POST request to create issue")
    response = requests.post(create_issue_url, json=issue_data, headers=headers, auth=auth)
    print(f"Response status code: {response.status_code}")
   
    # Check response status
    print("Step 7: Checking response status")
    if response.status_code == 201:
        print("Issue created successfully.")
    else:
        print(f"Failed to create issue: {response.status_code}")
 
# Example usage
project_key = "NW"  # Replace with your project key
summary = "Example issue"
description = "This is an example issue created with a timestamp in the summary."
 
# Create the issue with timestamp in the summary
print("Starting issue creation process")
create_issue_with_timestamp_in_summary(project_key, summary, description)
print("Issue creation process completed")
 