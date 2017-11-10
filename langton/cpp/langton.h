
class Point {
  public:
    int x;
    int y;

    Point(int x, int y) {
      this->x = x;
      this->y = y;
    };
};

class Ant {
  public:
    Point position() {
      Point position = Point(0, 0);
      return position;
    };
};
