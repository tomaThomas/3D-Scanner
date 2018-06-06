ArrayList<Point> points;

void setup() {
  size(800, 600, P3D);
  points = new ArrayList<Point>();
  addPoint(0, 0, 0);
  addPoint(10, 112, 42);
  addPoint(23, 62, 32);
  addPoint(34, 84, 45);
}

void draw() {
  background(50);
  camera(0, 0, 0, 0, 0, -1, 0, 1, 0);
  translate(0, 0, -450);
  rotateX((((float)height / 2) - (float)mouseY)/(float)height);
  rotateY((float)mouseX/(float)width*4);


  stroke(255);
  strokeWeight(1);
  noFill();
  box(300);
  strokeWeight(5);
  for(Point p: points){
    p.draw();
  }
}

void clearPoints(){
  points.clear();
}

void addPoint(float x, float y, float z){
  Point p = new Point(x, y, z);
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
