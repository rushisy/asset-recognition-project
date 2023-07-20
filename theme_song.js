const l = 'left';
const r = 'right';
console.log('if you\'re going hard enough ${l}, you\'ll find yourself turning ${r}');

displayImage('cars.jpg', 1079, 449)

function displayImage(src, width, height) {
    var img = document.createElement("img");
    img.src = src;
    img.width = width;
    img.height = height;
    document.body.appendChild(img);
   }