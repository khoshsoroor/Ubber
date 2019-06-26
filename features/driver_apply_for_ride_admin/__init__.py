from aloe import *
import requests
from .. import config, logger
from aloe.tools import guess_types
from datetime import datetime, timedelta
from khayyam import JalaliDate
import time


@step(r"an order is added by following options for applying driver")
def add_order(s):

    world.list_of_status=[]

    for s in guess_types(s.hashes):
        cur = (datetime.now() + timedelta(days=1))
        s['dispatch_date'] = str(JalaliDate(cur.date()))
        s['dispatch_hour'] = cur.time().strftime('%H:%M')
        logger.info(s['dispatch_date'])
        logger.info(s['dispatch_hour'])
        logger.info(" sssssss is : %s", s)


        r = requests.post(f"{config.api_uri}/caravan/add_order/",
                          json=s,
                          headers={"APIToken": config.client.api_token, "USERToken": world.token})

        world.res = r.json()
        logger.info("Response: %s", str(world.res).encode('utf-8'))

        world.status = r.status_code


        world.track_code = world.res['order_data']['tracking_code']
        logger.info("tracking code groups : %s", world.track_code)

        logger.info(" s is : %s", s)

        world.list_of_status.append(world.res['order_data']['status'])
        logger.info("wwwwwwww list of status of orders is %s", world.list_of_status)
        time.sleep(1)

time.sleep(1)


@step(r"a driver is assigned to order with number (\d+)")
def assign_driver(_, num):
    p = requests.post(f"{config.api_uri}/caravan/apply_for_ride",
                      json={
                          "driver_cellphone" : num ,
                          "order_code" :  world.track_code
                      },
                      headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})

    logger.error(p.text)

    res_for_driver = p.json()

    logger.info("response for driver assign : %s", res_for_driver)

    world.order_status = res_for_driver ["order_data"]["status"]
    logger.info("response for status: %s",world.order_status)

time.sleep(0.5)


@step(r"status should be (\S+)")
def check_modifying(_,stat_1):
    assert stat_1 == world.order_status




@step(r"turn the status back to (\S+)")
def turn_stat(_,new_stat):

    t = requests.post(f"{config.api_uri}/caravan/order_status_update",
                      json={
                          "new_status": new_stat ,
                          "order_code": world.track_code
                      },
                      headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})

    logger.error(t.text)

    response_turn_status = t.json()
    logger.info("response for turn status bach is %s",response_turn_status)

    statuscode_turnstatus = t.status_code
    logger.info("status code for turn status bach is %s",statuscode_turnstatus)





@step(r"A new driver is sign up with number (\d+)")
def sign_up_driver(_,driver_num):
    k = requests.post(f"{config.api_uri}/caravan/driver_join",
                      json={"cellphone_no": driver_num,
                            "first_name": "راننده",
                            "last_name": "اکانت تست",
                            "vehicle_options": "treili_transit_chadori",
                            "vehicle_suspension_type": "fanari",
                            "vehicle_type": "treili"},
                      headers={"APIToken": config.admin.api_token, "USERToken": config.admin.user_token})

time.sleep(0.5)




@step(r"call for order detail")


def check_detail(_):

    p = requests.post(f"{config.api_uri}/caravan/order_details",
                      json={"order_code": world.track_code},
                      headers={"APIToken": config.client.api_token, "USERToken": world.token})

    world.detail = p.json()
    logger.info("response for order detail is : %s", world.detail)

    world.order_detail = world.detail["order_details"]
    logger.info("order detail is : %s", world.order_detail)

time.sleep(0.5)



@step(r" the driver is deleted")
def clear_driver(*args):


    d1 = requests.delete(f"{config.api_uri}/v2/drivers/09999999915",
                         headers={"Usertoken": config.admin.user_token})


time.sleep(0.5)

