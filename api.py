import requests
import json


def get_route(api_key, start_lat, start_lng, end_lat, end_lng):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    
    params = {
        'origin': f"{start_lat},{start_lng}",
        'destination': f"{end_lat},{end_lng}",
        'mode': 'driving',
        'language': 'en',
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()

        # Save response to a JSON file for debugging
        with open("route_response.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Response saved to 'route_response.json'")

        if 'routes' in data and data['routes']:
            route = data['routes'][0]
            leg = route['legs'][0]
            distance = leg['distance']['value']
            time = leg['duration']['value']
            
            if 'overview_polyline' in route:
                encoded_points = route['overview_polyline']['points']
                points = decode_polyline(encoded_points)
            else:
                points = None
            
            return distance, time, points
        else:
            print("No route found.")
            return None, None, None
    else:
        print("Error:", response.status_code, response.text)
        return None, None, None

def decode_polyline(encoded):
    points = []
    index = 0
    lat, lng = 0, 0

    while index < len(encoded):
        shift, result = 0, 0
        while True:
            b = ord(encoded[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20:
                break
        dlat = ~(result >> 1) if (result & 1) else (result >> 1)
        lat += dlat

        shift, result = 0, 0
        while True:
            b = ord(encoded[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20:
                break
        dlng = ~(result >> 1) if (result & 1) else (result >> 1)
        lng += dlng

        points.append((lat / 1E5, lng / 1E5))

    return points

def plot_route(api_key, start_lat, start_lng, end_lat, end_lng):
    distance, time, points = get_route(api_key, start_lat, start_lng, end_lat, end_lng)
    return distance, time
   