


# import yaml
#
# fs = open("caps.yaml")
# res = yaml.load(fs)
# print(res)


a = {'deviceName': 'MI9','noReset': True}



def hello(**kwargs):
    # if kwargs.keys() is not None:
    #     print("KKKKK")
    print(kwargs)
    a.update(kwargs)
    print(a)


hello()
# hello(monster="good",more="hhah")