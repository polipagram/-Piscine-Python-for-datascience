import math
def NULL_not_found(object: any) -> int:

    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
            print(f"Cheese: {object} {type(object)}")
    elif  isinstance(object , int) and object == 0:  
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Empty: {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("type not found")
        return 1
    return 0
#Nothing = None
#Garlic = float("NaN")
#Zero = 0
#Empty = ''
#Fake = False
#NULL_not_found(Nothing)
#NULL_not_found(Garlic)
#NULL_not_found(Zero)
#NULL_not_found(Empty)
#NULL_not_found(Fake)
#print(NULL_not_found("Brian"))


