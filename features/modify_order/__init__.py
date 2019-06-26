from aloe import *
import requests
from .. import config, logger
from aloe.tools import guess_types
from datetime import datetime, timedelta
from khayyam import JalaliDate
import time


@step(r"an order is added by following options to modify later:")
def add_order(s):
    world.track_codes = []
    for s in guess_types(s.hashes):
        cur = (datetime.now() + timedelta(days=1))
        s['dispatch_date'] = str(JalaliDate(cur.date()))
        s['dispatch_hour'] = cur.time().strftime('%H:%M')
        logger.info(s['dispatch_date'])
        logger.info(s['dispatch_hour'])

        world.description = s['description']
        logger.info("description log is : %s", world.description)
        if world.description == 'ویرایش سفارش':
            world.list_1 = s
            logger.info("ssss %s:", world.list_1)

        # get price and order code

        r = requests.post(f"{config.api_uri}/caravan/price_enquiry",
                          json=s,
                          headers={"APIToken": config.client.api_token, "USERToken": world.token})

        logger.error(r.text)
        world.res = r.json()
        logger.info("Response: %s", str(world.res).encode('utf-8'))

        time.sleep(1)

        world.status = r.status_code

        s['order_code'] = world.res['order_data']['tracking_code']
        logger.info(" ssss %s", s['order_code'])

        s['price'] = world.res['order_data']['predicted_price']

        # main_code= world.res['order_data']['tracking_code']
        # main_price = world.res['order_data']['predicted_price']
        # s['price']
        #

        world.track_codes.append(world.res['order_data']['tracking_code'])
        logger.info("tracking code groups : %s", world.track_codes)

        logger.info(" s is : %s", s)

        k = requests.put(f"{config.api_uri}/caravan/modify_order",
                         json=s,
                         headers={"APIToken": config.client.api_token, "USERToken": world.token})

        response_of_add = k.json()
        logger.info("response for add order is : %s", response_of_add)

        if world.description == "ویرایش سفارش":
            world.new_code = response_of_add['order_data']['tracking_code']
            logger.info("the unique order code is: %s", world.new_code)

        time.sleep(0.5)


@step(r"modify order with options like the following:")
def add_order(m):
    if world.description == "ویرایش سفارش":

        for m in guess_types(m.hashes):
            cur = (datetime.now() + timedelta(days=2))
            m['dispatch_date'] = str(JalaliDate(cur.date()))
            m['dispatch_hour'] = cur.time().strftime('%H:%M')
            logger.info(m['dispatch_date'])
            logger.info(m['dispatch_hour'])
            m['order_code'] = world.new_code
            world.list_2 = m
            logger.info("mmm: %s", world.list_2)

            world.description_check = m["description"]
            logger.info("description check after modifying is : %s", world.description_check)

            p = requests.put(f"{config.api_uri}/caravan/modify_order",
                             json=m,
                             headers={"APIToken": config.client.api_token, "USERToken": world.token})

            logger.error(p.text)

            world.response_for_edit = p.json()
            time.sleep(0.5)

            logger.info("Response after edit is: %s", world.response_for_edit)

            print(str(world.response_for_edit))
            world.status = p.status_code

            world.order_codes = world.response_for_edit['order_data']['tracking_code']
            logger.info("world order code is %s: ", world.order_codes)

    else:
        # assert not hasattr(world, 'list_2')
        pass


@step(r"check modifying")
def check_modifying(_):
    if hasattr(world, 'list_2'):
        final_assertion = []
        for i in world.list_1:
            if world.list_1[i] != world.list_2[i]:
                final_assertion.append(i)

        logger.info("final assertation list is %s", final_assertion)

        logger.info("order code in add %s", world.new_code)
        logger.info("order code in edit %s", world.order_codes)

        assert world.description_check in final_assertion
        assert world.new_code == world.order_codes


    else:
        pass


@step(r"Success flag for modify is (\d+)")
def check_response(_, success_flag):
    assert str(world.res["success_flag"]) == success_flag


@step(r"status is (\d+)")
def check_status(_, status_code):
    assert str(world.status) == status_code


@after.each_feature
def clear(*args):
    time.sleep(10)
    if hasattr(world, 'track_codes'):
        for i in world.track_codes:
            logger.info("iiiiii %s", i)
            d1 = requests.delete((f"{config.api_uri}/v2/orders/{i}"),
                                 headers={"X-User-Id": "test@gmail.com"})
