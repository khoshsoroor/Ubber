# from aloe import *
# import requests
# from .. import config, logger
# from aloe.tools import guess_types
# from datetime import datetime, timedelta
# from khayyam import JalaliDate
# import time
#
#
#
# @step(r"Add order for raft o bargasht with options like the following:")
# def add_order(s):
#     world.success = []
#     for s in guess_types(s.hashes):
#         # for delta in (3,7,11,14):
#         delta = 8
#         while delta <= 24:
#             cur = (datetime.now() + timedelta(hours=delta))
#             logger.warn(cur)
#             s['dispatch_date'] = str(JalaliDate(cur.date()))
#             s['dispatch_hour'] = cur.time().strftime('%H:%M')
#             logger.info(s['dispatch_date'])
#             logger.info(s['dispatch_hour'])
#
#             r = requests.post(f"{config.api_uri}/caravan/add_order",
#                               json=s,
#                               headers={"APIToken": config.client.api_token, "USERToken": world.token})
#
#             logger.error(r.text)
#             world.res = r.json()
#             time.sleep(0.5)
#             world.status = r.status_code
#             world.success.append(world.res["success_flag"])
#             delta += 4
#
#
#
#
#
# @step(r"Success flag for raft o bargasht order is (\d+)")
# def check_response(_, success_flag):
#     logger.info(world.success)
#     assert all(str(i) == success_flag for i in world.success)
