#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import socks
import datetime
from telethon.tl.types import UserStatusOnline
from telethon.tl.types import UserStatusRecently
from telethon.tl.types import UserStatusLastWeek
from telethon.tl.types import UserStatusLastMonth
from telethon.tl.types import UserStatusEmpty

apiSettings = sys.argv[1]
apiSettings = json.loads(apiSettings)
apiID = apiSettings["id"][0]
apiHash = apiSettings["hash"][0]

apiSession = sys.argv[2]
apiSession = json.loads(apiSession)
name = apiSession["name"][0]
areaCode = apiSession["areacode"][0]
phone = apiSession["phone"][0]

sourceGroup = sys.argv[3]
destinationGroup = sys.argv[4]



# Your Telegram API_ID here
tg_api_id = apiID
# Your Telegram API_HASH here
tg_api_hash = apiHash

# Database file
db_file = 'database.db'

# Sessions
sessions = {
    'session_name':
        {
            'name': name,
            'area_code': areaCode,
            'phone': phone,
            'proxy': None,
        },
}

# Filter of UserStatus
# Tips: DO NOT put `UserStatusOffline` in this
filter_user_status_types = [
    UserStatusOnline,
    UserStatusRecently,
    UserStatusLastWeek,
    UserStatusLastMonth,
    UserStatusEmpty,
]

# UserStatusOffline `was_online` limit
# filter_user_status_offline_was_online_min = datetime.datetime.now() - datetime.timedelta(weeks=4)
filter_user_status_offline_was_online_min = None
filter_user_status_offline_was_online_max = None

# if display_name is too long, skip
filter_user_display_name_too_much_words_limit = 25

# user batch amount
rd_pending_users_amount_min = 25
rd_pending_users_amount_max = 35


# Source group list
source_groups = [sourceGroup]

# destination group
destination_group = destinationGroup


# random relax during inviting actions
rd_sleep_min = 10
rd_sleep_max = 30