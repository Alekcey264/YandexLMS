def get_spn(toponym_json: dict) -> str:
    bounds = toponym_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]
    lower_corner_x, lower_corner_y = list(map(float, bounds["lowerCorner"].split()))
    upper_corner_x, upper_corner_y = list(map(float, bounds["upperCorner"].split()))
    x_long = str(round(upper_corner_x - lower_corner_x))
    y_long = str(upper_corner_y - lower_corner_y)
    return ",".join([x_long, y_long])