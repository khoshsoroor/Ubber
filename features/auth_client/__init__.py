from aloe import *
import requests
from .. import config,logger


@step(r"Client number is (\d+)")
def get_mobile_number(_, number):
    world.mobile_no = number


@step(r"Checking the mobile number")
def check_signin(_):
    r = requests.post(f"{config.api_uri}/caravan/signup_check", json={"cellphone_no": world.mobile_no},
                      headers={"APIToken": config.client.api_token})
    if 'USERToken' in r.headers:
        return True
    world.res = r.json()


@step(r"sign up flag is (\d+)")
def check_response(_, signup_flag):
    assert str(world.res["user_data"]["signup_flag"]) == signup_flag


@step(r"Client password is (\S+)")
def get_password(_, password):
    world.password = password


@step(r"Checking the password for USERToken")
def check_password(_):
    r = requests.post(f"{config.api_uri}/caravan/user_login_pass",
                      json={'username': world.mobile_no, "passwrd": world.password, "device_type": "web",
                            "push_notif_identifier": "alaki"},
                      headers={"APIToken": config.client.api_token})
    print(config.client.api_token)
    print(config.api_uri)
    if 'USERToken' in r.headers:
        return True
    world.res = r.json()
    print(world.res)


@step(r"verification_flag is (\d+)")
def check_response(_, verification_flag):

    assert str(world.res["verification_flag"]) == verification_flag
    logger.info("verification flag is %s", world.res["verification_flag"])





@step(r"Client ID is (\S+)")
def ID_email(_, email):
    world.email = email


@step(r"Checking the login")
def check_password(_):
    e = requests.post(f"{config.api_uri}/caravan/user_login_pass",
                      json={'username': world.email, "passwrd": world.password, "device_type": "web",
                            "push_notif_identifier": "alaki"},
                      headers={"APIToken": config.client.api_token})
    world.email_res = e.json()

    if "user_data" in world.response_admin:
        if 'token' in world.email_res["user_data"]:
            world.token = world.email_res["user_data"]["token"]
            return True

@step(r"verification_flag for email is (\d+)")
def check_response(_, verification_flag):
    assert str(world.email_res["verification_flag"]) == verification_flag

@step(r"user role should be (\S+)")
def check_role(_,role):
    world.role = role
    if world.res["verification_flag"] == 1:
        logger.info("response is : %s", world.res["user_data"]["user_role"])
        logger.info("response role is : %s", world.role)

        assert str(world.res["user_data"]["user_role"])== world.role



@step(r"login with username and pass")
def username_password(_):
    r = requests.post(f"{config.api_uri}/caravan/user_login_pass",
                      json={'username': world.mobile_no, "passwrd": world.password, "device_type": "web",
                            "push_notif_identifier": "alaki"},
                      headers={"APIToken": config.client.api_token})
    res = r.json()
    world.token = res["user_data"]["token"]
