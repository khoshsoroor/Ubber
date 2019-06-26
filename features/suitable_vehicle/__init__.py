from aloe import *
import requests
from .. import config, logger
from aloe.tools import guess_types


@step(r"Checking the suitable vehicle for")
def vehicle(v):
    world.vehicle_type = []

    logger.info("guesstype %s", guess_types(v.hashes))
    for v in guess_types(v.hashes):
        r = requests.post(f"{config.api_uri}/caravan/suitable_vehicle",
                          json=v,
                          headers={"APIToken": config.client.api_token, "USERToken": world.token})

        world.vehicle_response = r.json()
        # logger.debug("Response for suitable vehicle is: %s", world.vehicle_response)

        world.vehicle_type = list(world.vehicle_response["vehicle_models"].keys())
        # logger.info("response for vehicle type is: %s", world.vehicle_type)

        world.vehicle_options = list(world.vehicle_response["vehicle_options"].values())
        # logger.info("response for option is: %s", world.vehicle_options)
        world.vehicle_options_final = []
        for x in world.vehicle_options:
            final_option = list(x.keys())
            # logger.info("final option list is : %s", final_option)

            for item in final_option:
                if item != '':
                    world.vehicle_options_final.append(item)
                    # logger.info("final append list is : %s", world.vehicle_options_final)


@step(r"the vehicle type should be:")
def vehicle_type(t):
    world.vehicle_type_should_be = []
    for t in guess_types(t.hashes):
        world.vehicle_type_should_be.append(t)
        # logger.info("the vehicle  should be: %s", world.vehicle_type_should_be)

    for x in world.vehicle_type_should_be:
        final_vehicle_list = list(x.values())
        # logger.info("final sort is : %s", final_vehicle_list)

    assert world.vehicle_type == final_vehicle_list


@step(r"success flag for suitable vehicle is (\d+)")
def check_flag(_, success_flag):
    logger.info(world.vehicle_response["success_flag"])
    assert str(world.vehicle_response["success_flag"]) == success_flag


@step(r"the vehicle options should be:")
def get_options(n):
    world.options_should_be = []

    for n in guess_types(n.hashes):
        world.options_should_be.append(n)
        # logger.info("the vehicle option should be: %s", world.options_should_be)
        for x in world.options_should_be:
            final_vehicle_option = list(x.values())
            # logger.info("final sort is : %s", final_vehicle_option)
            final_list = []
            for item in final_vehicle_option:
                if item != '':
                    final_list.append(item)
                    # logger.info("final list is : %s", final_list)
    assert final_list == world.vehicle_options_final


@step(r"Checking the suitable dimensions for:")
def vehicle(d):
    for d in guess_types(d.hashes):
        r = requests.post(f"{config.api_uri}/caravan/suitable_vehicle",
                          json=d,
                          headers={"APIToken": config.client.api_token, "USERToken": world.token})
        # logger.info("d is: %s", d)

        world.vehicle_response = r.json()
        # logger.debug("Response for suitable vehicle is: %s", world.vehicle_response)

        world.vehicle_dimension = list(world.vehicle_response["truck_dimensions"].values())
        logger.info("truck dimensions are : %s", world.vehicle_dimension)

        world.weight_in_list = d['weight_load']
        # logger.info("the weight in list is : %s", world.weight_in_list)
        world.length_in_list = d['length_load']
        # logger.info("the length in list is : %s", world.length_in_list)
        world.width_in_list = d['width_load']
        world.height_in_list = d['height_load']

        world.length_list = []
        world.width_list = []
        world.height_list = []
        for i in world.vehicle_dimension:
            for m in i['length']:
                world.length_list.append(float(m))
            # logger.info("length list is %s", world.length_list)

            for n in i['width']:
                world.width_list.append(float(n))
            # logger.info("width list is %s", world.width_list)

            for p in i['height']:
                world.height_list.append(float(p))
            # logger.info("height list is %s", world.height_list)


@step(r"the allowed dimensions is calculating")
def check_num(_):
    main_length_list = ['2.1', '4', '5.6', '5.7', '5.8', '6', '6.1', '6.2', '6.3', '7', '8.5', '6', '8.5', '9', '12',
                   '12.2', '12.4', '12.5', '12.6', '13', '13.2', '13.6', '5', '6', '6.3', '6.4', '6.65', '6.7', '6.8',
                   '7', '7.2', '7.5', '8', '12', '12.2', '13', '3.6', '4', '4.1', '4.2', '4.3', '4.4', '4.5', '4.55',
                   '4.6', '4.7', '4.75', '4.8', '4.9', '5', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8',
                   '5.9', '6', '6.1', '6.2', '6.8', '7']
    main_width_list = ['2.2', '2.25', '2.28', '2.3', '2.35', '2.4', '2.5', '2.6', '2', '2.3', '2.4', '2.45', '2.5', '2.55',
                  '2.6', '2.2', '2.3', '2.35', '2.4', '2.45', '2.5', '2.55', '2.6', '2.7', '3', '1.8', '1.9', '1.95',
                  '2', '2.05', '2.07', '2.1', '2.15', '2.2', '2.25', '2.3', '2.35', '2.6', '2.8']
    main_height_list = ['1.25', '1.7', '1.8', '2', '2.2', '2.5', '2.6', '2.7', '2.8', '1.3', '1.5', '1.8', '1.45', '2',
                   '2.6', '2.65', '2.7', '2.8', '2.9', '3', '3.2', '1.2', '1.3', '1.5', '1.6', '1.8', '2', '2.2',
                   '2.4', '2.48', '2.5', '3', '1', '1.1', '1.75', '1.8', '2', '2.2', '2.22', '2.4', '2.5', '2.6',
                   '2.65', '2.7', '2.75', '2.8', '3']

    l = [float(h) for h in main_length_list]
    # logger.info("l is : %s", l)

    w = [float(t) for t in main_width_list]
    # logger.info("w is : %s", w)

    h = [float(e) for e in main_height_list]
    # logger.info("h is : %s", h)

    world.filtered_length = list(filter(lambda x: x >= float(world.length_in_list), l))
    # logger.info(" filtered length is : %s", world.filtered_length)

    world.filtered_width = list(filter(lambda x: x >= float(world.width_in_list), w))
    # logger.info(" filtered width is : %s", world.filtered_width)

    world.filtered_height = list(filter(lambda x: x >= float(world.height_in_list), h))
    # logger.info(" filtered height is : %s", world.filtered_height)


    assert world.filtered_length == world.length_list
    assert world.filtered_width == world.width_list
    assert world.filtered_height == world.height_list
