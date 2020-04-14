import sys
import logging

sys.path.insert(1, f"{__file__}/../../..")
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# export SLACK_API_TOKEN=xoxb-***
# python3 tests/samples/conversations/open_dm.py

import os
from slack import WebClient

client = WebClient(token=os.environ["SLACK_API_TOKEN"])

all_users = client.users_list(limit=100)["members"]
joinable_only = lambda u: \
    u["id"] != "USLACKBOT" \
    and not u["is_bot"] \
    and not u["is_app_user"] \
    and not u["deleted"] \
    and not u["is_restricted"] \
    and not u["is_ultra_restricted"]
users = filter(joinable_only, all_users)
user_ids = list(map(lambda u: u["id"], users))

response = client.conversations_open(users=user_ids)