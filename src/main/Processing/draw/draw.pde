void setup() {
  size(500, 400);
  background(#000000); //oder clear();
}

color strokecolor = #000000;

void draw() {  
  stroke(#222233);
  fill(#ff0000);
  ellipse(30, 30, 50, 50);
  fill(#00ff00);
  ellipse(30, 95, 50, 50);
  fill(#0000ff);
  ellipse(30, 160, 50, 50);
  //rect(75,50, 150, 100);
  stroke(strokecolor);
  line(pmouseX, pmouseY, mouseX, mouseY);
}

void mousePressed() {
  background(#000000);
  if (5<mouseX & mouseX<55) {
    println("Check");
    if (5<mouseY & mouseY<55) {
      strokecolor = #ff0000;
      println("Red");
    } else {
      if (70<mouseY & mouseY<120) {
        strokecolor = #00ff00;
        println("Green");
      } else {
        if (135<mouseY & mouseY<185) {
          strokecolor = #0000ff;
          println("Blue");
        }
      }
    }
  } else {
    println("-");
    strokecolor = #000000;
  }
}
