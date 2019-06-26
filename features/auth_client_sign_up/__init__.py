from aloe import *
import requests
from .. import config, logger
import time


@before.each_feature
def clear(*args):
    time.sleep(2)

    d1 = requests.delete(f"{config.api_uri}/v2/customers/09999999900",
                         headers={"Usertoken": config.admin.user_token})

    d2 = requests.delete(f"{config.api_uri}/v2/customers/09686635566",
                         headers={"Usertoken": config.admin.user_token})

    d3 = requests.delete(f"{config.api_uri}/v2/customers/09000000022",
                         headers={"Usertoken": config.admin.user_token})


@step(r"Client number for signing up is (\d+)")
def get_mobile_number(_, number):
    world.mobile_no = number


@step(r"Checking if the mobile number is invalid")
def check_signin(_):
    r = requests.post(f"{config.api_uri}/caravan/signup_check", json={"cellphone_no": world.mobile_no},
                      headers={"APIToken": config.client.api_token})
    if 'USERToken' in r.headers:
        return True
    world.res = r.json()

    world.sign_up_flag = world.res["user_data"]["signup_flag"]
    logger.info("signup flag for sign up is : %s", world.sign_up_flag)


@step(r"checking sms")
def get_mobile_number(_):
    p = requests.post(f"{config.api_uri}/caravan/signup_check_sms_verification",
                      json={"sms_code": config.client.sms_code, "cellphone_no": world.mobile_no},
                      headers={"APIToken": config.client.api_token})

    world.response = p.json()
    logger.info("response for sms verification is %s", world.response)


@step(r"sign up a new (\S+)")
def check_signin(_,tag):
    if world.sign_up_flag == 0:
        if tag == "user":
            baarbari_status = "false"
        else:
            baarbari_status = "true"


        k = requests.post(f"{config.api_uri}/caravan/user_signup",
                      json={"first_name": "اکانت",
                            "last_name": "تست",
                            "cellphone_no": str(world.mobile_no),
                            "address": "تهران میدان امام",
                            "organization": "ساناگسترسبز",
                            "organization_role": "",
                            "device_type": "ios",
                            "password": "as1234",
                            "password_repeat": "as1234",
                            "website": "http://google.com",
                            "phone": "02144411306",
                            "baarbari":  str(baarbari_status),
                            "push_notif_identifier": "27817127878218712",
                            "region_id": "22"},
                      headers={"APIToken": config.client.api_token})

        logger.error(k.text)

        logger.info("mobile number is %s", world.mobile_no)
        logger.info("baarbari stat %s", baarbari_status)
        logger.info("api token %s", config.client.api_token)




        world.res = k.json()
        logger.info("response for sign up request is %s", world.res)

        success_flag = world.res["success_flag"]
        logger.info("sign up success flag is %s", success_flag)

        verification_flag = world.res["user_data"]["verification_flag"]
        logger.info(" verification flag is %s", verification_flag)

        time.sleep(2)

    # else:
    #     pass


@step(r"success flag for sign up is (\d+)")
def check_response(_, success_flag):
    assert str(world.res["success_flag"]) == success_flag


@step(r"verification flag for sign up is (\S+)")
def check_response(_, ver_flag):
    logger.info("verification flag is : %s", world.res["user_data"]["verification_flag"])
    logger.info("verification flag should be : %s", ver_flag)

    assert str(world.res["user_data"]["verification_flag"]) == ver_flag



@step(r"user role is (\S+)")
def check_user_role(_, role):
    if world.sign_up_flag == 0:


        logger.info("ggggg  %s",world.res["user_data"]['user_role'])
        logger.info("jjjjj %s", role)
        assert world.res["user_data"]['user_role'] == str(role) or world.resp["user_data"]["user_role"] == str(role)
    else:
        pass


@after.all
def clear(*args):
    # time.sleep(10)

    d1 = requests.delete(f"{config.api_uri}/v2/customers/09999999900",
                         headers={"Usertoken": config.admin.user_token})

    d2 = requests.delete(f"{config.api_uri}/v2/customers/09686635566",
                         headers={"Usertoken": config.admin.user_token})

    d3 = requests.delete(f"{config.api_uri}/v2/customers/09000000022",
                         headers={"Usertoken": config.admin.user_token})




