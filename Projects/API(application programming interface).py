# fixme --> API is method or a bridge that connect user to external service and provide
# fixme--> in the formate of json so json is just a dta format transfer by the external service to user

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")  # this is the ISS location current
print(response.status_code)

# todo HTTP status code--> 1xx means Hold on, 2xx means Here you go(success),
#  todo -->3xx means Go away, 4xx means you screwed up, 5xx means I screwed up