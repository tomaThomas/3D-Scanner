ArrayList<Point> points;

boolean pressed = false;

float rotX = 0;
float rotY = 0;

void setup() {
  size(1000, 600, P3D);
  points = new ArrayList<Point>();
}

void draw() {

  if(pressed){
    float lock = 3.14159 / 2.0
    rotY -= (float)(mouseX-pmouseX) / 200.0;
    rotX += (float)(mouseY-pmouseY) / 200.0;
    if(rotX > lock)rotX = lock;
    if(rotX < -lock)rotX = -lock;
  }

  background(50);
  camera(0, 0, 0, 0, 0, -1, 0, -1, 0);
  translate(0, 0, -450);
  rotateX(rotX);
  rotateY(rotY);

  stroke(255);
  strokeWeight(1);
  noFill();
  box(300);
  strokeWeight(2);
  for(Point p: points){
    p.draw();
  }
}

void mousePressed(){
    pressed=true;
}

void mouseReleased(){
    pressed=false;
}

void clearPoints(){
  points.clear();
}

void addPoint(float x, float y, float z){
  Point p = new Point(x, y-150, z);
  points.add(p);
}

class Point {
  float x, y, z;
  Point(float x, float y, float z) { 
    this.x=x; 
    this.y=y;
    this.z=z;
  }
  void draw() {
    stroke(0, 0, 255);
    point(x, y, z);
  }
}
