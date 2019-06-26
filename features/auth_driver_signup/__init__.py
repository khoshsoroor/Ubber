from aloe import *
import requests
from .. import config, logger
import time


@before.each_feature
def clear(*args):
    d1 = requests.delete(f"{config.api_uri}/v2/drivers/09999999913",
                         headers={"Usertoken": config.admin.user_token})


@step(r"driver number for signing up is (\d+)")
def get_mobile_number(_, number):
    world.mobile_no = number


@step(r"Checking if the driver mobile number is invalid")
def check_signin(_):
    r = requests.post(f"{config.api_uri}/caravan/driver_signup", json={"cellphone_no": world.mobile_no,
                                                                       "device_type": "web",
                                                                       "push_notif_identifier": "11111111-1111-1111-1111-111111111111"
                                                                       },
                      headers={"APIToken": config.driver.api_token})

    world.res = r.json()
    logger.info("driver sign up : %s", world.res)


    world.sign_up_flag = world.res["success_flag"]
    logger.info("success flag for driver sign up is : %s", world.sign_up_flag)


@step(r"check sms for driver")
def number(_):
    p = requests.post(f"{config.api_uri}/caravan/sms_verification",
                      json={"sms_code": config.driver.sms_code, "cellphone_no": world.mobile_no},
                      headers={"APIToken": config.driver.api_token})

    world.response = p.json()
    logger.info("response for sms verification is %s", world.response)

    world.driver_token = world.response["user_data"]["token"]
    logger.info("driver token is %s", world.driver_token)

    world.success = world.response['success_flag']
    logger.info(" success flag for sms verification is : %s", world.success)


@step(r"sign up driver")
def check_signin(_):
    # if world.success == 1:
        k = requests.post(f"{config.api_uri}/caravan/driver_join",
                          json={"cellphone_no": world.mobile_no,
                                "first_name": "راننده",
                                "last_name": "اکانت تست",
                                "vehicle_options": "joft_bari",
                                "vehicle_type": "joft"},
                          headers={"APIToken": config.driver.api_token, "USERToken": world.driver_token})

        print(k.text)
        world.res = k.json()
        logger.info("response for sign up request is %s", world.res)

        success_flag = world.res["success_flag"]
        logger.info("sign up join success flag is %s", success_flag)


@step(r"success flag for driver sign up is (\d+)")
def check_response(_, success_flag):
    assert str(world.res["success_flag"]) == success_flag


@after.all
def clear(*args):
    # time.sleep(10)

    d1 = requests.delete(f"{config.api_uri}/v2/drivers/09999999913",
                         headers={"Usertoken": config.admin.user_token})


