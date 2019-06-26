from aloe import *
import requests
from .. import config,logger

# this is for driver login


@step(r"Driver number is (\d+)")
def get_mobile_number(_, number):
    world.mobile_no = number


@step(r"Checking the driver login with sms code (\d+)")
def check_signin(_,sms_code):
    world.sms_code = sms_code
    logger.info("sms code is %s", sms_code)
    r = requests.post(f"{config.api_uri}/caravan/sms_verification",
                      json={"cellphone_no": world.mobile_no, "sms_code": world.sms_code},
                      headers={"APIToken": config.driver.api_token})
    world.res = r.json()
    logger.info(" the response is %s", world.res)

    if world.res["success_flag"] ==1:
        if 'token' in world.res["user_data"]:
            world.token = world.res["user_data"]["token"]
            return True


@step(r"success flag is (\d+)")
def check_response(_, success_flag):
    assert str(world.res["success_flag"]) == success_flag