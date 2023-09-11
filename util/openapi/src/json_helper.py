import json
from datetime import datetime, date

# copied from
# https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
def _json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat().replace('000+00:00', 'Z')
    raise TypeError ("Type %s not serializable" % type(obj))

def getJson(obj):
    return json.dumps(obj, indent = 2, default=_json_serial)