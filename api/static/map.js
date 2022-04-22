const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 7 });
map.
    locate()
    .on("locationfound", (e) => map.setView(e.latlng, 11))
    .on("locationerror", () => map.setView([37.5664700, 126.9779630], 11));

// To build the marker layer, we ask our endpoint for data asynchronously and extract the properties we want to show in the pop-ups.
async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`
    const response = await fetch(markers_url)
    const geojson = await response.json()
    return geojson
}

async function render_markers() {
    const markers = await load_markers();
    L.geoJSON(markers)
    .bindPopup((layer) => layer.feature.properties.region_name)
    .addTo(map);
}

map.on("moveend", render_markers);