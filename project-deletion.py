from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

# The Project ID (for example, `foo-bar-123`).
# Required.
project_id = 'test-273120'  # TODO: Update placeholder value.

request = service.projects().delete(projectId=project_id)
request.execute()
