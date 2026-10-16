import uuid
import datetime as dt

class Project:
    """
    All Trips, outings, etc for settlements
    """
    project_id: str
    project_name: str
    project_created_at: dt.datetime

    def __init__(self, project_id: str = str(uuid.uuid4()).upper(), project_name: str = ""):
        self.project_id = project_id
        self.project_name = project_name
        self.project_created_at = dt.datetime.now(dt.timezone.utc)

    