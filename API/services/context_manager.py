def split_context(parsed_json):
    return {
        "teach": parsed_json["Abstract"] + parsed_json["Method"],
        "math": parsed_json["Math"],
        "experiment": parsed_json["Experiments"] + parsed_json["Results"]
    }