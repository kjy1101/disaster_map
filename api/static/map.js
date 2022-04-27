const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 7 });
map.
    locate()
    .on("locationfound", (e) => map.setView([36, 127.5], 1))
    .on("locationerror", () => map.setView([36, 127.5], 11));

// To build the marker layer, we ask our endpoint for data asynchronously and extract the properties we want to show in the pop-ups.
async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`
    const response = await fetch(markers_url)
    const geojson = await response.json()
    return geojson
}
//.bindPopup((layer) => markers.feature.properties.name)

async function render_markers() {
    const markers = await load_markers();
    L.geoJSON(markers, {
        onEachFeature : function (feature, layer) {
            layer.bindPopup("<img src='https://upload.wikimedia.org/wikipedia/ko/9/9e/%ED%8A%B8%EC%9C%84%ED%84%B0_%EB%A1%9C%EA%B3%A0_%282012%29.svg' style='width:20px;'><p style='display:flow-root;'><span style='float:left;font-weight:700'>@"+feature.properties.tweet[0].user+"</span><span style='float:right;color:gray;'>"+feature.properties.tweet[0].time+"</span></p><p>"+feature.properties.region_name+" - "+feature.properties.tweet[0].disaster_tag+"</p><p>"+feature.properties.tweet[0].text+"</p>");
        }
    }).addTo(map);
}

map.on("moveend", render_markers);