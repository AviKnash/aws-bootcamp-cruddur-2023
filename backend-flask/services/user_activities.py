from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class UserActivities:
  @staticmethod
  def run(user_handle):
      # segment = xray_recorder.begin_segment('user_activities')
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      if user_handle is None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
          'created_at': (now - timedelta(days=1)).isoformat(),
          'expires_at': (now + timedelta(days=31)).isoformat()
        }]
        model['data'] = results

      # X_RAY ----------------------------------
      # metadata = {
      #   "now": now.isoformat(),
      #   "results-size": len(model['data']) if model['data'] else 0
      # }
      # subsegment = xray_recorder.begin_subsegment('mock-data')
      # subsegment.put_metadata('key', metadata, 'namespace')

      return model
