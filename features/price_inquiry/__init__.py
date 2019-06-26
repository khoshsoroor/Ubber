from aloe import *
import requests
from .. import config, logger
from aloe.tools import guess_types
from datetime import datetime, timedelta
from khayyam import JalaliDate
import time
import itertools




@before.each_feature
def clear(*args):
    d = requests.delete((f"{config.api_uri}/v2/customers/09999999900"),
                        headers={"Usertoken": config.admin.user_token})


# price inquiry
@step(r"sign up and log in with username (\d+) and password (\S+)")
def sign_up_new_user(_,num,pas):
    world.mobile = num
    world.password = pas

# check num validation

    r = requests.post(f"{config.api_uri}/caravan/signup_check", json={"cellphone_no": world.mobile},
                      headers={"APIToken": config.client.api_token})
    if 'USERToken' in r.headers:
        return True
    world.response_of_check = r.json()

    world.sign_up_flag = world.response_of_check["user_data"]["signup_flag"]
    logger.info("signup flag for sign up is : %s", world.sign_up_flag)


#enter sms

    p = requests.post(f"{config.api_uri}/caravan/signup_check_sms_verification",
                      json={"sms_code": config.client.sms_code, "cellphone_no": world.mobile},
                      headers={"APIToken": config.client.api_token})

    world.response = p.json()
    logger.info("response for sms verification is %s", world.response)


#sign up a new user

    if world.mobile == "09999999900":
        baarbari_status = "false"
    else:
        baarbari_status = "true"

    k = requests.post(f"{config.api_uri}/caravan/user_signup",
                      json={"first_name": "اکانت",
                            "last_name": "تست",
                            "cellphone_no": world.mobile,
                            "address": "تهران میدان امام",
                            "organization": "ساناگسترسبز",
                            "organization_role": "",
                            "device_type": "ios",
                            "password": "as1234",
                            "password_repeat": world.password,
                            "website": "http://google.com",
                            "phone": "02144411306",
                            "baarbari": baarbari_status,
                            "push_notif_identifier": "27817127878218712",
                            "region_id": "22"},
                      headers={"APIToken": config.client.api_token})

    world.res = k.json()
    logger.info("response for sign up request is %s", world.res)

    world.new_token = world.res["user_data"]["token"]
    logger.info(" world.new_token  is %s", world.new_token)

    success_flag = world.res["success_flag"]
    logger.info("sign up success flag is %s", success_flag)

    verification_flag = world.res["user_data"]["verification_flag"]
    logger.info(" verification flag is %s", verification_flag)


@step(r"get price for options like the following:")
def add_order(s):
    world.price_list = []
    world.order_codes = []
    for s in guess_types(s.hashes):
        cur = (datetime.now() + timedelta(days=3))
        s['dispatch_date'] = str(JalaliDate(cur.date()))
        s['dispatch_hour'] = cur.time().strftime('%H:%M')
        # logger.info(s['dispatch_date'])
        # logger.info(s['dispatch_hour'])
        logger.info("table is %s", s)

        world.source_city = s['source_city']
        logger.info(" sourcy is %s", world.source_city)

        world.destination_city = s['destination_city']
        logger.info(" desty is %s", world.destination_city)

        world.vehicle_type = s['vehicle_type']
        logger.info("vehicle type is: %s", world.vehicle_type)

        world.vehicle_options = s['vehicle_options']
        logger.info("vehicle option is: %s", world.vehicle_options)

        world.weight = s['weight']
        logger.info("weight is: %s", world.weight)

        r = requests.post(f"{config.api_uri}/caravan/price_enquiry",
                          json=s,
                          headers={"APIToken": config.client.api_token, "USERToken": world.new_token})

        # if "USERToken" is in
        world.res = r.json()
        logger.info("world response is : %s", world.res)
        time.sleep(1)
        world.status = r.status_code
        logger.info("status : %s", world.status)
        logger.info("success : %s", world.res['success_flag'])



        if world.res['success_flag'] == 1:
            # logger.info("Response: %s", str(world.res).encode('utf-8'))

            world.predicted_price = world.res['order_data']['predicted_price']
            logger.info("notice: predicted price is : %s", world.predicted_price)
            world.price_list.append(world.predicted_price)

            world.max_price = world.res['order_data']['max_acceptable_price']
            # logger.info("maximum price is : %s", world.max_price)

            world.min_price = world.res['order_data']['min_acceptable_price']
            # logger.info("minimum price is : %s", world.min_price)

            world.response_status = world.res['order_data']['status']
            logger.info("status in response  is : %s", world.response_status)

            world.order_codes.append(world.res['order_data']['tracking_code'])
            logger.info("order code list is : %s", world.order_codes)

            logger.info("price list : %s", world.price_list)


            p = requests.post(f"{config.api_uri}/caravan/orders_list",
                              json={
                                  "north_east_lat": "41.20484655708464",
                                  "north_east_lng": "69.72803906249999",
                                  "south_west_lat": "22.706960239893046",
                                  "south_west_lng": "37.64796093749999",
                                  "no_items": "20",
                                  "source_city": world.source_city,
                                  "destination_city": world.destination_city,
                                  "vehicle_type": world.vehicle_type,
                                  "vehicle_options": world.vehicle_options,
                                  "weight": world.weight
                              },
                              headers={"APIToken": config.admin.api_token,
                                       "USERToken":config.admin.user_token})
            # world.status = p.status_code
            world.respon = p.json()
            logger.info("world response FOR P is : %s", world.respon)
            price_of_last_orders = []
            for i in world.respon['active_orders_list']:
                price_of_last_orders.append(i['price_predict'])
                logger.info("machine learning price is : %s", price_of_last_orders)
            world.second_price_last_orders = []
            for a in price_of_last_orders:
                if a != 0:
                    world.second_price_last_orders.append(a)
                    logger.info("second list is %s:", world.second_price_last_orders)

        else:
          pass


@step(r"success flag for get price is (\d+)")
def check_response(_, success_flag):
    assert str(world.res["success_flag"]) == success_flag


@step(r"the response should be :")
def get_price(r):
    price_list_should_be = []
    for r in r.hashes:
        price_should_be = r['predicted_price']
        world.tavafogh_Flag = r['tavafoghi_flag']
        world.status_should_be = r['status']
        minprice_should_be = r['min_acceptable_price']
        maxprice_should_be = r['max_acceptable_price']
        # logger.info("predicted price is : %s", world.predicted_price)
        logger.info("price should be : %s", price_should_be)
        price_list_should_be.append(price_should_be)
        world.float_list = [float(i) for i in price_list_should_be]
        logger.info("float list is : %s", world.float_list)

    if world.res['success_flag'] == 1:

        if world.second_price_last_orders != []:
            maximum_price = max(world.second_price_last_orders)
            logger.info("aaaaa %s",maximum_price)

            minimum_price = min(world.second_price_last_orders)
            logger.info("bbbbb %s", minimum_price)

            logger.info("ccccc %s", world.predicted_price)

            assert int(minimum_price) - 120000 < int(world.predicted_price) < int(maximum_price) + 120000
            assert world.response_status == world.status_should_be

        else:
            logger.info("nnnnn : %s", world.float_list)
            for i in range(len(world.price_list)):

                if world.price_list[i] == world.float_list[i]:

                    if world.vehicle_type == "khavar":
                        a= 50000
                    if world.vehicle_type == "tak":
                        a = 100000
                    if world.vehicle_type == "joft":
                        a = 100000
                    if world.vehicle_type == "treili":
                        a = 200000

                    assert (int(world.float_list[i]) - a) < int(world.price_list[i]) < (int(world.float_list[i]) + a)
                    assert world.response_status == world.status_should_be



                if world.tavafogh_Flag == 1:
                    assert world.predicted_price == '0'
                    assert world.max_price == '0'
                    assert world.min_price == '0'
                    assert world.response_status == world.status_should_be




@step(r"status for price inquiry is (\d+)")
def check_status(_, status_code):
    assert str(world.status) == status_code


@after.each_feature
def clear(*args):
    d = requests.delete((f"{config.api_uri}/v2/customers/09999999900"),
                            headers={"Usertoken": config.admin.user_token})

    # time.sleep(10)

    if hasattr(world, 'order_codes'):

        for i in world.order_codes:

            d1 = requests.delete((f"{config.api_uri}/v2/orders/{i}"),
                                headers={"Usertoken": config.admin.user_token})
