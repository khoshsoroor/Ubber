from aloe import *
import requests
from .. import config, logger


@step(r"Search active order list for (\S+) items for (\S*)")
def search_for_item_orders(_, item_no, active_status):
    # for item in status :
    world.item = item_no
    world.status_active = active_status
    # print(world.token)
    print(config.api_uri)
    r = requests.post(f"{config.api_uri}/caravan/active_orders_list",
                      json={"to_items": world.item,
                            "north_east_lat": 62,
                            "north_east_lng": 72,
                            "south_west_lat": 10,
                            "south_west_lng": 30,
                            "load_status": world.status_active,
                            "min_load_weight": 10,
                            "max_load_weight": 10,
                            "source_city": "تهران",
                            "destination_city": "اصفهان",
                            "source_state": "تهران",
                            "destination_state": "اصفهان",
                            "from_item": 0,
                            "from_date_dispatch_order_app": 0,
                            "to_date_dispatch_order_app": 20
                            },
                      headers={"APIToken": config.driver.api_token,
                               "USERToken": world.token})
    world.status = r.status_code
    print(world.status)
    world.res = r.json()


@step(r"success flag is (\d+)")
def check_response(_, success_flag):
    print(world.res)
    assert str(world.res["success_flag"]) == success_flag


@step(r"status is (\d+)")
def check_status(_, status_code):
    assert str(world.status) == status_code


@step(r"Checking the driver login")
def check_signin(_):
    r = requests.post(f"{config.api_uri}/caravan/sms_verification",
                      json={"cellphone_no": world.mobile_no, "sms_code": config.driver.sms_code},
                      headers={"APIToken": config.driver.api_token})
    world.res = r.json()
    if 'token' in world.res["user_data"]:
        world.token = world.res["user_data"]["token"]
