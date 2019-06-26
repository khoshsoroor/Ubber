from aloe import *
import requests
from .. import config, logger


@step(r"Admin logs in with email (\S+) and password is (\S+)")
def get_email(_, email,password):
    world.email = email
    world.password = password


@step(r"Checking the admin login")
def check_signin(_):
    q = requests.post(f"{config.api_uri}/caravan/user_login_pass",
                      json={"username": world.email, "passwrd": world.password},
                      headers={"APIToken": config.admin.api_token })
    world.response_admin = q.json()
    logger.info("world response is : %s", world.response_admin)
    logger.info("admin token is : %s", world.response_admin)

    if "user_data" in world.response_admin:
        if "token" in world.response_admin["user_data"]:
            world.token_admin = world.response_admin["user_data"]["token"]
            logger.info("admin token is : %s", world.token_admin)


@step(r"verification flag for admin is (\d+)")
def check_response(_, verification_flag):
    logger.info(world.response_admin["verification_flag"])
    assert str(world.response_admin["verification_flag"]) == verification_flag

