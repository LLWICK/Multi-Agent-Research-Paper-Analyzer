def split_context(parsed_json):
    return {
        "teach": "paper Name - "+parsed_json.Name+ parsed_json.Abstract + parsed_json.Method,
        "math": "paper Name - "+parsed_json.Name+parsed_json.Math,
        "experiment": "paper Name - "+parsed_json.Name+parsed_json.Experiments + parsed_json.Results
    }