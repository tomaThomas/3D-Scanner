void setup() {
  size(640, 360, P3D);
}

void draw() {
  background(0);
  camera(mouseX, height/2, (height/2) / tan(PI/6), mouseX, height/2, 0, 0, 1, 0);
  translate(width/2, height/2, -100);
  rotateY((float)mouseY/(float)height*4);
  stroke(255);
  noFill();
  box(200);
  for(float y = -1.0f; y <= 1.0f; y += 0.2){
    for(int a = 0; a < 3.14159 * 2; a += 3.14159 / 6){
      float r = sqrt(1 - y * y) * 50.0;
      point(sin(a) * r, y * 50, cos(a) * r);
    }
  }
}


