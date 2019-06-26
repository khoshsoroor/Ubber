from aloe import *
import requests
from .. import config, logger
from aloe.tools import guess_types
from datetime import datetime, timedelta
from khayyam import JalaliDate
import time




@step(r"Search order list of admin for status")
def search(s):
    for s in guess_types(s.hashes):
        logger.info("input for s is %s",s)

        cur_to= (datetime.now())
        Shamsi_date_to = str(JalaliDate(cur_to.date()))
        logger.info("shamsi date from: %s", Shamsi_date_to )

        cur_from= (datetime.now())
        Shamsi_date_from = str(JalaliDate(cur_from.date())+ timedelta(days=1))
        logger.info("shamsi date from: %s", Shamsi_date_from)


        dispatch_date_to = (datetime.now() + timedelta(days=1))
        Shamsi_dispatch_date_to = str(JalaliDate(dispatch_date_to.date()))
        logger.info("shamsi date from: %s", Shamsi_dispatch_date_to)


        dispatch_date_from = (datetime.now() + timedelta(days=2))
        Shamsi_dispatch_date_from = str(JalaliDate(dispatch_date_from.date()))
        logger.info("shamsi date from: %s", Shamsi_dispatch_date_from)

        logger.info("ssssss is %s",s['status'])


        p = requests.post(f"{config.api_uri}/caravan/orders_list",
                                      json={
                                          "north_east_lat": "41.20484655708464",
                                          "north_east_lng": "69.72803906249999",
                                          "south_west_lat": "22.706960239893046",
                                          "south_west_lng": "37.64796093749999",
                                          "from_item":"1",
                                          "no_items":"30",
                                          "source_city": "تهران",
                                          "destination_city": "ساری",
                                          "vehicle_type": "joft",
                                          "vehicle_options": "joft:joft_mosaghaf_chadori",
                                          "to_date_submit_order" : str(Shamsi_date_to),
                                          "from_date_submit_order": str(Shamsi_date_from),
                                          "from_date_dispatch_order" : str(Shamsi_dispatch_date_from),
                                          "to_date_dispatch_order": str(Shamsi_dispatch_date_to),
                                          "driver_mobile_no" : "09120213683",
                                          "user_mobile_no" :  "09022012056",
                                          "status" : str(s['status'])
                                      },
                                      headers={"APIToken": config.admin.api_token,
                                               "USERToken": config.admin.user_token})


        world.respon = p.json()
        logger.info("world response FOR P is : %s", world.respon)
        # logger.error("error on orderssss",p.text)


        world.status = p.status_code
        logger.info("status code is: %s", world.status)


@step(r"status is (\d+)")
def search(_,code):

    assert  world.status == code

