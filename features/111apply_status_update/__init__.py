# from aloe import *
# import requests
# from .. import config, logger
# from aloe.tools import guess_types
# from datetime import datetime, timedelta
# from khayyam import JalaliDate
# import time
#
# # @before.each_feature
# # def clear(*arg):
# #     d1 = requests.delete(f"{config.api_uri}/v2/customers/09999999900",
# #                          headers={"Usertoken": config.admin.user_token})
# #
#
#
# @step(r"sign up a new client user with (\d+)")
# def sign_up(_,client_num):
#
#     world.mobile_no= client_num
#
#     r = requests.post(f"{config.api_uri}/caravan/signup_check", json={"cellphone_no": world.mobile_no},
#                       headers={"APIToken": config.client.api_token})
#
#
#
#
#     p = requests.post(f"{config.api_uri}/caravan/signup_check_sms_verification",
#                       json={"sms_code": config.client.sms_code, "cellphone_no": world.mobile_no},
#                       headers={"APIToken": config.client.api_token})
#
#
#
#     k = requests.post(f"{config.api_uri}/caravan/user_signup",
#                   json={"first_name": "اکانت",
#                         "last_name": "تست",
#                         "cellphone_no": world.mobile_no,
#                         "address": "تهران میدان امام",
#                         "organization": "ساناگسترسبز",
#                         "organization_role": "",
#                         "device_type": "ios",
#                         "password": "as1234",
#                         "password_repeat": "as1234",
#                         "website": "http://google.com",
#                         "phone": "02144411306",
#                         "baarbari": "false",
#                         "push_notif_identifier": "27817127878218712",
#                         "region_id": "22"},
#                   headers={"APIToken": config.client.api_token})
#
#
#     response_final = k.json()
#     logger.info("final response for sign up is %s",response_final)
#
#
#     world.token = response_final["user_data"]["token"]
#     logger.info("user tokrn is %s", world.token)
#
# time.sleep(0.5)
#
#
#
# @step(r"an order is added by following options for applying driver")
# def add_order(s):
#
#     world.list_of_status=[]
#     world.tracking =[]
#
#     for s in guess_types(s.hashes):
#         cur = (datetime.now() + timedelta(days=1))
#         s['dispatch_date'] = str(JalaliDate(cur.date()))
#         s['dispatch_hour'] = cur.time().strftime('%H:%M')
#         logger.info(s['dispatch_date'])
#         logger.info(s['dispatch_hour'])
#
#
#         r = requests.post(f"{config.api_uri}/caravan/add_order",
#                           json=s,
#                           headers={"APIToken": config.client.api_token, "USERToken": world.token})
#
#         world.res = r.json()
#         logger.error(r.text)
#         logger.info("Response: %s", str(world.res).encode('utf-8'))
#         logger.info("Response: %s", world.res)
#
#         world.status = r.status_code
#
#
#         world.track_code = world.res['order_data']['tracking_code']
#         logger.info("tracking code groups : %s", world.track_code)
#
#
#
#         world.list_of_status.append(world.res['order_data']['status'])
#         logger.info("wwwwwwww list of status of orders is %s", world.list_of_status)
#
#
#         world.tracking.append( world.track_code)
#         logger.info("list of added order is %s",world.tracking)
#
#         time.sleep(1)
#
#
#
# @step(r"a driver is assigned to order with number (\d+)")
# def assign_driver(_, num):
#     time.sleep(1)
#
#     p = requests.post(f"{config.api_uri}/caravan/apply_for_ride",
#                       json={
#                           "driver_cellphone" : num ,
#                           "order_code" :  world.track_code
#                       },
#                       headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})
#
#     logger.error(p.text)
#
#     res_for_driver = p.json()
#     logger.info("response for driver assign : %s", res_for_driver)
#
#     world.order_status = res_for_driver ["order_data"]["status"]
#     logger.info("response for status: %s",world.order_status)
#
# time.sleep(1)
#
#
#
# @step(r"the status after add order should be:")
# def status_check(m):
#     order_new_status = []
#     for m in guess_types(m.hashes):
#         logger.info("status mmmm is : %s", m)
#         order_new_status.append(m["status"])
#         logger.info("status list of second : %s", order_new_status)
#         logger.info(" world list of status %s", world.list_of_status)
#
#
#
#     assert  (order_new_status ==  world.list_of_status)
#
#
#
# @step(r"turn the status back to (\S+)")
# def turn_stat(_,new_stat):
#
#     p = requests.post(f"{config.api_uri}/caravan/order_status_update",
#                       json={
#                           "new_status": new_stat ,
#                           "order_code": world.track_code
#                       },
#                       headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})
#
#
#
#
# @step(r"change the status to:")
# def change_stat(k):
#
#     world.status_code_list = []
#     for k in guess_types(k.hashes):
#         logger.info("change in status %s", str(k['status']))
#         logger.info("order code in changing is %s",world.track_code)
#         p = requests.post(f"{config.api_uri}/caravan/order_status_update",
#                           json={
#                               "new_status":str(k['status']),
#                               "order_code": world.track_code
#                           },
#                           headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})
#
#         world.response_for_status_changing =p.json()
#         logger.info("response of changing status is : %s", world.response_for_status_changing)
#
#         world.status_1 = p.status_code
#         logger.info("1111status code is %s", world.status_1 )
#         world.status_code_list.append(world.status)
#
#     logger.info("status of this order is %s",world.status_code_list)
#
#
#
#
#
#
#
# @step(r"update the status by modify_order to:")
# def update_stat(k):
#
#     world.status_code_list = []
#     for k in guess_types(k.hashes):
#         logger.info("order code in changing is %s",world.track_code)
#         logger.info("order status is %s",str(k['status']))
#
#
#         c = requests.put(f"{config.api_uri}/caravan/modify_order",
#                           json={
#                               "status": str(k['status']),
#                               "order_code": world.track_code,
#                               "address_id_destination": "1407",
#                               "address_id_source": "1406"
#                           },
#                           headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})
#
#         world.response_for_status_update =c.json()
#         logger.info("response of changing status is : %s", world.response_for_status_update)
#
#         world.status_2 = c.status_code
#         logger.info("status code is %s", world.status_2 )
#         world.status_code_list.append(world.status_2)
#
# time.sleep(0.5)
#
#
#
# @step(r"order status code is")
# def check_status_code(h):
#     status_code_list_should_be = []
#     for h in guess_types(h.hashes):
#         logger.info("hhhhhhhh %s", h)
#         status_code_list_should_be.append(h['code'])
#
#         logger.info("status_code_list_should_be %s", status_code_list_should_be)
#         logger.info("world.status_code_list %s", world.status_code_list)
#
#     logger.info("the final list of status_code_list_should_be %s", status_code_list_should_be)
#     assert status_code_list_should_be == world.status_code_list
#
#
#
#
#
# @step(r"upload a new baarnameh")
# def upload_barnameh(t):
#
#
#
#     files = {'baarnameh_photo':  open('/Users/Mazdak Badakhshan/Documents/ubaar_test/baarnameh.jpg','rb')}
#
#     t = requests.post(f"{config.api_uri}/caravan/order_barnameh_photo/",
#                       files=files,
#                       headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token, 'ORDERID':  world.track_code})
#     logger.info("body: %s", t.text)
#     response_baarnameh = t.json()
#     logger.info("response for baarname is %s", response_baarnameh)
#
#     m = requests.post(f"{config.api_uri}/caravan/0order_details",
#                       json={"order_code": world.track_code},
#                       headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})
#     response_detail = m.json()
#     logger.info("response for order detail is : %s", response_detail)
#
#     world.status_barnameh = response_detail['0order_details']['status']
#     logger.info(" response of order detail after uploading barname: %s", world.status_barnameh)
#
# time.sleep(0.5)
#
#
#
# @step(r"the status after add barnameh should be:")
# def upload_barnameh(j):
#     # order_new_status = []
#     for j in guess_types(j.hashes):
#         logger.info("status jjjjjj is : %s", j)
#         # order_new_status.append(j["status"])
#         # logger.info("status list of second : %s", order_new_status)
#         logger.info("status list of second : %s", j["status"])
#
#
#
#     assert world.status_barnameh == j["status"]
#
#
# time.sleep(1)
#
#
#
# @step(r"delete the number of new client")
# def clear_client(*args):
#     d1 = requests.delete(f"{config.api_uri}/v2/customers/09999999900",
#                          headers={"Usertoken": config.admin.user_token})
#
#     if hasattr(world, 'track_codes'):
#         for i in world.track_codes:
#             logger.info("iiiiii %s", i)
#             d1 = requests.delete((f"{config.api_uri}/v2/orders/{i}"),
#                                  headers={"UserToken": config.admin.user_token})
#
#
# @step(r"the status code for status update should be (\d+)")
# def check_stat2(_,stat3):
#
#     logger.info("stat 3 %s",stat3)
#     logger.info("stat order  %s",world.status_1)
#
#
#     assert world.status ==  stat3