from aloe import *
import requests
from .. import config, logger


@step(r"Search for driver order list for (\S+) items for (\S*)")
def search_for_item(_, item_no, driver_status):
    world.item = item_no
    world.status_order = driver_status
    r = requests.post(f"{config.api_uri}/caravan/my_orders_mobile",
                      json={"no_items": world.item, "status": world.status_order},
                      headers={"APIToken": config.driver.api_token, "USERToken": world.token})

    world.status = r.status_code
    world.res = r.json()
    print(world.res)


@step(r"success flag is (\d+)")
def check_response(_, success_flag):
    print(world.res)
    assert str(world.res["success_flag"]) == success_flag


@step(r"status is (\d+)")
def check_status(_, status_code):
    assert str(world.status) == status_code


@step(r"Driver number is (\d+)")
def get_mobile_number(_, number):
    world.mobile_no = number


@step(r"Checking the driver login")
def check_signin(_):
    r = requests.post(f"{config.api_uri}/caravan/sms_verification",
                      json={"cellphone_no": world.mobile_no, "sms_code": config.driver.sms_code},
                      headers={"APIToken": config.driver.api_token})
    world.res = r.json()
    logger.debug(world.res)
    if 'token' in world.res["user_data"]:
        world.token = world.res["user_data"]["token"]
        # return True
