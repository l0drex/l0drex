float circleX;
boolean lr = true;

void setup() {
  size(640, 360);
  circleX = 24/2;
}

void draw () {
  background(50);
  fill(255);
  ellipse(circleX, 180, 24, 24);
  if (lr) {
    circleX += random(0, 10);
  } else {
    circleX -= random(0, 10);
  }
  if (circleX <= 24/2) {
    lr = true;
  } else {
    if (circleX >= 640-24/2) {
      lr = false;
    }
  }
}
