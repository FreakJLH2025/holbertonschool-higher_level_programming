#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                continue
            
            result = a / b
            
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except Exception:
            pass
        finally:
            result_list.append(result)
    
    return result_list
