// https://www.codewars.com/kata/52532cc8e9ea83b89b000008
for (var property in this) {
    if (this.hasOwnProperty(property)) {
        if (property.substring(0, 4) == "boom") {
          Bomb.CutTheWire(this[property])
        }
    }
}
