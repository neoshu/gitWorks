
import requests
from plotly import express as px
import time
import json

# set up the url for top stories
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"status_code is {r.status_code}")
top_id_list = r.json() # list with length 500

comments = []
titles = []
url_for_ids = []
result_dict = {}
for id in top_id_list[:10]:
    target_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    item_r = requests.get(target_url)
    # print(f"{id}'s status is {item_r.status_code}")
    item_dict = item_r.json()
    try:
        comment = item_dict["descendants"]
        title = item_dict["title"]
        url_for_id = item_dict["url"]
    except KeyError:
        print(f"The id: {id} has not comments.")
        continue
    else:
        comments.append(comment)
        titles.append(title)
        url_for_ids.append(url_for_id)
    time.sleep(0.2)
"""
result_dict["comments"] = comments
result_dict["titles"] = titles
result_dict["urls"] = url_for_ids

with open("target_file.json", "w") as target_file:
    json.dump(result_dict, target_file)
"""
# make a fig
labels = {"x": "title", "y": "comment"}
# make x axis with links
x_label = []
for i in range(len(titles)):
    content = f"<a href='{url_for_ids[i]}'>{titles[i]}</a>"
    x_label.append(content)

fig = px.bar(x=x_label, y=comments, labels=labels)
fig.show()

"""
import requests
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Function to create a session with retry logic
def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# Set up the URL for top stories
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests_retry_session().get(url)

# Check if the request was successful
if r.status_code != 200:
    print(f"Failed to fetch top stories. Status code: {r.status_code}")
    exit()

print(f"Status code is {r.status_code}")
top_id_list = r.json()  # list with length 500

comments = []
for id in top_id_list:
    target_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    try:
        item_r = requests_retry_session().get(target_url)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        continue

    # Check if the item request was successful
    if item_r.status_code != 200:
        print(f"Failed to fetch item {id}. Status code: {item_r.status_code}")
        continue

    print(f"{id}'s status is {item_r.status_code}")
    item_dict = item_r.json()
    
    try:
        comment = item_dict["descendants"]
    except KeyError:
        continue
    else:
        comments.append(comment)
    
    # Add a delay to avoid hitting the rate limit
    time.sleep(0.1)

print(f"Number of comments collected: {len(comments)}")
"""