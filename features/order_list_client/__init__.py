from aloe import *
import requests
from .. import config,logger

# this is for client order lists


@step(r"Search for order list for (\S+) items for (\S*)")
def search_for_item(_, item_no, status):
    world.item = item_no
    print(world.token)
    r = requests.post(f"{config.api_uri}/caravan/my_orders",
                      json={"no_items": world.item, "status": status},
                      headers={"APIToken": config.client.api_token,
                               "USERToken": world.token})
    world.status = r.status_code
    print(world.status)
    logger.error(r.text)

    world.res = r.json()



@step(r"success flag is (\d+)")
def check_response(_, success_flag):
    print(world.res)
    assert str(world.res["success_flag"]) == success_flag


@step(r"status is (\d+)")
def check_status(_, status_code):
    assert str(world.status) == status_code


@step(r"login with username (\S+) and password (\S*)")
def username_password(_, user_name, password):
    r = requests.post(f"{config.api_uri}/caravan/user_login_pass",
                      json={'username': user_name, "passwrd": password, "device_type": "web",
                            "push_notif_identifier": "alaki"},
                      headers={"APIToken": config.client.api_token})
    res = r.json()
    world.token = res["user_data"]["token"]
