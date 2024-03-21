import json
import folium

# Define a dictionary with category icons
category_icons = {
    11049: "https://maps.gstatic.com/mapfiles/ms2/micons/blue-dot.png",
    13002: "https://maps.gstatic.com/mapfiles/ms2/micons/orange-dot.png",
    17124: "https://maps.gstatic.com/mapfiles/ms2/micons/green-dot.png",
}

def create_marker(place):
    popup = folium.Popup(f"<b>{place['name']}</b><br>"
                         f"Category: {place['categories'][0]['name']}<br>"
                         f"Address: {place['location']['formatted_address']}",
                         parse_html=True)

    icon_url = category_icons.get(place['categories'][0]['id'])

    if icon_url:
        marker_icon = folium.features.CustomIcon(icon_url, icon_size=(30, 30))
    else:
        marker_icon = None

    return folium.Marker(location=(place["geocodes"]["main"]["latitude"],
                                  place["geocodes"]["main"]["longitude"]),
                          popup=popup, icon=marker_icon)

# Load the JSON data
with open("foursqure_response.json", "r") as file:
    data = json.load(file)

# Create a new Folium map centered at the center of the data
map = folium.Map([12.96821, 77.59459], zoom_start=13)

# Add markers for every place in the data to the map
for place in data["results"]:
    map.add_child(create_marker(place))

# Save the map into a HTML file
map.save("map.html")