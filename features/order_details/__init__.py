from aloe import *
import requests
from .. import config, logger , REFERENCE_DATE_DATE
from datetime import datetime, timedelta
from khayyam import JalaliDate
from aloe.tools import guess_types
import time

def calculate_ms(end_date,begin_date):
   elapsed = (end_date-begin_date).total_seconds()
   return int(1000*elapsed)


@step(r"add an order")
def add_order(_):
    cur = (datetime.now() + timedelta(days=1))
    world.shamsi_date = str(JalaliDate(cur.date()))
    world.shamsi_hour = cur.time().strftime('%H:%M')
    logger.info("Shamsi date is: %s", world.shamsi_date)
    logger.info("Shamsi hour is: %s", world.shamsi_hour)
    logger.info("token is : %s", world.token)
    r = requests.post(f"{config.api_uri}/caravan/add_order",
                      json={
                          "weight": 5.0,
                          "price": 150000,
                          "source_city": "تهران",
                          "destination_city": "ساری",
                          "sender_phone": "09965555555",
                          "receiver_phone": "02144411306",
                          "source_address": "خیابان اول کوچه دوم",
                          "destination_address": " میدون دست چپ",
                          "dispatch_date": str(world.shamsi_date),
                          "vehicle_type": "joft",
                          "load_type": "بار صنعتی",
                          "vehicle_options": "joft:hichkodam",
                          "dispatch_hour": str(world.shamsi_hour),
                          "load_value": 10000000,
                          "description": "بار تست جزییات",
                          "sender_name": "علی",
                          "receiver_name": "اصغری",
                          "payment_type": "sender",
                          "sender_company": "سانا",
                          "receiver_company": "سانا گستر",
                          "package_options": "falleh",
                          "length": 0.0,
                          "width": 1.0,
                          "height": 1.0,
                          "baarnameh": "yes",
                          "unload_option": "day",
                          "sender_mobile_phone": "09022012056",
                          "announce_type": "mydrivers",
                          "source_region_id": "22",
                          "address_id_source": "1069",
                          "address_id_destination": "1070",
                          "destination_region_id": "16",
                          "surplus_costs": "3000.0"},
                      headers={"APIToken": config.client.api_token,
                               "USERToken": world.token})
    world.status = r.status_code
    print(world.status)
    world.res = r.json()
    world.status_detail = r.status_code

    world.order_code = world.res["order_data"]["tracking_code"]
    logger.warn("order code is : %s", world.order_code)
    world.dispatch_date_ms = calculate_ms(cur.date(), REFERENCE_DATE_DATE)


@step(r"get order details")


def check_order_detail(n):
    m = requests.post(f"{config.api_uri}/caravan/order_details",
                      json={"order_code": world.order_code},
                      headers={"APIToken": config.client.api_token, "USERToken": world.token})
    world.response = m.json()
    logger.info("response for order detail is : %s", world.response)

    world.order_detail = world.response["order_details"]
    logger.info("order detail is : %s", world.order_detail)

    creation= datetime.now()
    world.shamsi_creation_date = str(JalaliDate(creation.date()))
    world.shamsi_creation_hour = creation.time().strftime('%H:%M')


    world.response_should_be = {"sender_name": "علی",
                                "baarnameh_options_persian": "بارنامه",
                                "vehicle_options": "joft:hichkodam",
                                "source_lng": "51.3239120054",
                                "cancellation_date_ms": 0.0,
                                "destination_address": " میدون دست چپ",
                                "sender_mobile_phone": "09022012056",
                                "delivery_date_ms": 0,
                                "baarnameh_photo": "",
                                "packaging_type_english": "falleh",
                                "driver_score_no_jobs": 0.0,
                                "destination_address_title": None,
                                "postpone_order": False,
                                "baarbari_name": "",
                                "address_id_destination": "1070",
                                "source_lat": "35.7451231463",
                                "order_code": str(world.order_code),
                                "source_address_person_name": None,
                                "baarnameh": "yes",
                                "unload_option": "day",
                                "driver_income": 150000.0,
                                "surplus_costs": 0.0,
                                "receiver_company": "سانا گستر",
                                "delivery_date": "",
                                "destination_region_id": "16",
                                "weight": 5.0,
                                "source_address_phone": "09965555555",
                                "dispatch_date": str(world.shamsi_date),
                                "creation_date": str(world.shamsi_creation_date),
                                "baarnameh_type": "baarnameh",
                                "vehicle_options_farsi": "فرقی نمی کند",
                                "driver_status": "",
                                "receiver_mobile_phone": "09022012056",
                                "source_region_id": "22",
                                "source_city": "تهران",
                                "destination_address_person_name": None,
                                "driver_cellphone": "",
                                "destination_region_name": "ساری",
                                "sender_phone": "09965555555",
                                "transportation_cost": 150000.0,
                                "status_farsi": "منتظر پیدا شدن راننده",
                                "assignment_date": "",
                                "discount": 0.0,
                                "destination_neighborhood": "ساری",
                                "source_neighborhood" : "تهران",
                                "number_plate": "",
                                "receiver_score": 0.0,
                                "source_address_mobile_no": "09022012056",
                                "cancellation_date": "",
                                "length": 0.0,
                                "assignment_date_ms": 0,
                                "destination_address_company_name": None,
                                "receiver_name": "اصغری",
                                "sender_company": "سانا",
                                "destination_lng": "53.0586328",
                                "dispatch_date_ms": float(world.dispatch_date_ms) ,
                                "height": 1.0,
                                "source_region_coordinate": {'lat': '35.7451231463', 'lng': '51.3239120054'},
                                "packaging_type_farsi": "فله",
                                "sender_score_no_jobs": 0,
                                "driver_photo": "",
                                "dispatch_hour": str(world.shamsi_hour),
                                "address_id_source": "1069",
                                "receiver_score_no_jobs": 0.0,
                                "destination_city": "ساری",
                                "width": 1.0,
                                "driver_status_farsi": "",
                                "source_address_company_name": None,
                                "transport_price": 150000.0,
                                "receiver_phone": "09965555555",
                                "order_credit": 0.0,
                                "cancellation_reason_comment": "",
                                "volume": 0.0,
                                "baarnameh_options": "baarnameh",
                                "destination_address_phone": "09965555555",
                                "load_value": 10000000.0,
                                "destination_region_coordinate": {'lat': '36.5658729', 'lng': '53.0586328'},
                                "pickup_date_ms": 0,
                                "payment_type": "sender",
                                "pickup_date": "",
                                "less_4_hours_left": 0,
                                "packaging_type": "فله",
                                "payment_type_farsi": "پیش\u200cکرایه",
                                "destination_address_mobile_no": "09022012056",
                                "vehicle_type_farsi": "جفت",
                                "source_address": "خیابان اول کوچه دوم",
                                "status": "registered",
                                "description": "بار تست جزییات",
                                "destination_lat": "36.5658729",
                                "load_type": "بار صنعتی",
                                "source_region_name": "تهران",
                                "driver_score": 0.0,
                                "vehicle_type": "joft",
                                "source_address_title": None,
                                "sender_score": 0.0,
                                "driver_name": "",
                                "vehicle_suspension_type": "",
                                "cancellation_reason": "",
                                "payment_status":"منتظر تایید" ,
                                "payment_method": "",
                                "payment_flag": False,
                                "online_payment_link_msg": "با احترام لینک پرداخت بار بار صنعتی  از تهران  به ساری به مبلغ 150000 خدمت شما ارسال گردید.",
                                "source_state": "تهران",
                                "destination_state" : "مازندران",
                                "delivery_confirmation_code":"" ,
                                "payment_status_english":"pending" ,
                                "online_payment_link": f"http://dev.ubaar.ir/landing/pay_order#{world.order_code}",
                                "driver_id": "",
                                "order_id": "",
                                "importance" : "regular",
                                "is_modified" :False,
                                "bearing": None
                                }



@step(r"check the order detail")
def check_order(_):
    a=[]
    for i in world.response_should_be:
        if i not in world.order_detail:
            a.append(i)


    for i in a:

        logger.info("iiiii key %s", i.key)
        if i.key == "order_id":
             del world.response_should_be["order_id"]
             del world.order_detail["order_id"]




        assert world.order_detail == world.response_should_be

        logger.info("new response should be: %s",world.response_should_be)
        logger.info("new response detail is: %s",world.order_detail)


@step(r"success flag for order detail is (\d+)")
def check_status(_, status_flag):
    assert str(world.res["success_flag"]) == status_flag


@step(r"the status code for detail should be (\d+)")
def check_status_code(_, stat):
    logger.info("stat is %s",stat)
    logger.info("status code of detail is %s", world.status_detail)
    assert int(stat) == int(world.status_detail)


