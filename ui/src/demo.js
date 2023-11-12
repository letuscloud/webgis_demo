
class CarMarker {
  constructor(map, carIcon) {
    this.map = map;

    this.realRouteLine = L.polyline([], {
        weight: 4,
        color: "Red"
    }).addTo(map);

    this.decorator = L.polylineDecorator(this.realRouteLine, {
      patterns: [{
          repeat: 50,
          symbol: L.Symbol.arrowHead({
              pixelSize: 5,
              headAngle: 75,
              polygon: false,
              pathOptions: {
                  stroke: true,
                  weight: 2,
                  color: '#FFFFFF'
              }
          })
      }]
  }).addTo(map);

    this.animatedMarker = L.animatedMarker( {

      interval: 200, // 默认为100mm
      iconOptions: carIcon
  }).addTo(map)

  }

  update_route_line(latlng) {
    this.realRouteLine.addLatLng(latlng)
    this.decorator.setPaths(this.realRouteLine);
}

  update_pos(lat, lng) {
    this.animatedMarker.update_pos(lat, lng);
    this.update_route_line({
              lat: lat,
              lng: lng
          })

  }

  set_line_color(color) {
    this.realRouteLine.setStyle({color:color});
  }

  set_line_weight(weight) {
    this.realRouteLine.setStyle({weight:weight});
  }

  set_icon_size(width, height) {
    var icon_option = this.animatedMarker.options.iconOptions.options;
    icon_option.iconSize = [width, height];
    this.animatedMarker.resetIcon();
  }

};



var car_list = {}
function update_new_pos(car_id, lat, lng, creator) {
  var car;
  if (car_id in car_list) {
    car = car_list[car_id];
  } else {

    car = creator();
    car_list[car_id] = car;
  }
  car.update_pos(lat, lng);
}

function update_line_color(color) {
  for (var car_id in car_list) {
    var car = car_list[car_id];
    car.set_line_color(color);
  }
}

function update_line_weight(weight) {
  for (var car_id in car_list) {
    var car = car_list[car_id];
    car.set_line_weight(weight);
  }
}

function update_icon_size(width, height) {
  for (var car_id in car_list) {
    var car = car_list[car_id];
    car.set_icon_size(width, height);
  }
}
