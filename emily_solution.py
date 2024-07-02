import requests

response = requests.get("https://coderbyte.com/api/challenges/json/wizard-list")
all_data = response.json()



def remove_empty_data(data):
    if isinstance(data, dict):
        cleaned_dict = {key: value for key, value in sorted(data.items()) if value != None and value != ""}
        for key in ["enemies", "friends"]:
            if key in cleaned_dict and isinstance(cleaned_dict[key], list):
                non_empty_keys = [item for item in cleaned_dict[key] if item != ""]
                if non_empty_keys and isinstance(non_empty_keys[0], dict):
                    non_empty_keys = [dict(sorted(enemy.items())) for enemy in non_empty_keys]
                    cleaned_dict[key] = sorted(non_empty_keys, key=lambda x:x.get("name", ""))
                else:
                    cleaned_dict[key] = sorted(non_empty_keys)
            if not cleaned_dict[key]:
                del cleaned_dict[key]
        if "wand" in cleaned_dict and isinstance(cleaned_dict["wand"], dict):
            cleaned_dict["wand"] = {k:v for k,v in sorted(cleaned_dict['wand'].items())}
        return cleaned_dict
    elif isinstance(data, list):
        cleaned_list = [remove_empty_data(item) for item in data]
        return [item for item in sorted(cleaned_list) if item or item == 0]
    else:
        return data
    
for person in all_data:
    print("PERSON: ", remove_empty_data(person))