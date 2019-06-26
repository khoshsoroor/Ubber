from aloe import *
import requests
from .. import config, logger
from aloe.tools import guess_types
from datetime import datetime, timedelta
from khayyam import JalaliDate
import time



@step(r"An order is added by following options:")
def add_order(s):
    world.order_price = []
    for s in guess_types(s.hashes):
        cur = (datetime.now() + timedelta(days=1))
        s['dispatch_date'] = str(JalaliDate(cur.date()))
        s['dispatch_hour'] = cur.time().strftime('%H:%M')
        logger.info(s['dispatch_date'])
        logger.info(s['dispatch_hour'])

        r = requests.post(f"{config.api_uri}/caravan/add_order",
                          json=s,
                          headers={"APIToken": config.client.api_token, "USERToken": world.token})
        logger.error(r.text)
        world.res = r.json()
        time.sleep(1)

        logger.info("Response: %s", str(world.res).encode('utf-8'))

        world.status = r.status_code

        world.order_price.append(world.res['order_data']['price'])

        logger.info(world.order_price)


@step(r"The price is :")
def show_price(m):
    final_price = []
    for m in guess_types(m.hashes):
        final_price.append(m)
        logger.debug(final_price)

    price_value = [x.get('price') for x in final_price[0:5]]
    float_list = [float(i) for i in price_value]
    logger.debug(float_list)
    final_list = [str(a) for a in float_list]
    logger.debug(final_list)

    assert final_list == world.order_price
