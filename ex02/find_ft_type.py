def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if obj_type == list:
        print(f"List : {obj_type}")
    elif obj_type == tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type == set:
        print(f"Set : {obj_type}")
    elif obj_type == dict:
        print(f"Dict : {obj_type}")
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")
    return 42

#from find_ft_type import all_thing_is_obj
#ft_list = ["Hello", "tata!"]
#ft_tuple = ("Hello", "toto!")
#ft_set = {"Hello", "tutu!"}
#ft_dict = {"Hello" : "titi!"}
#all_thing_is_obj(ft_list)
#all_thing_is_obj(ft_tuple)
#all_thing_is_obj(ft_set)
#all_thing_is_obj(ft_dict)
#all_thing_is_obj("Brian")
#all_thing_is_obj("Toto")
