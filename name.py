"""Remove 'e' from below dictionary."""

d = {"key2":99,"key3":["sameer","ameer","adi",1],"key":"sadfxev"}


def replace_e(string):
    if 'e' in string:
        return string.replace('e','')
    else:
        return string

update_key_value = {}

#items property of dict, it gives back tuple of key,value pair. ie "key":"value", (key,value)
#Note: tuples can be unpacked.
#isinstance is a function which checks the type of instance is similar with your given datatype or not
#--if given instance is same as your given instan then its true, else its false.
for k,v in d.items():
    if isinstance(v,str):
        """replace_e is a funtion which takes string as argument are replace e with ''."""
        update_key_value[k] = replace_e(string=v)
    elif isinstance(v,list):
        list_values = []
        for s in v:
            if isinstance(s,str):
                list_values.append(replace_e(string=s))
            else:
                list_values.append(s)
        update_key_value[k] = list_values
    else:
        update_key_value[k] = v
d = update_key_value.copy()
print(d)


