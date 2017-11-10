#define BOOST_TEST_MAIN
#include <boost/test/unit_test.hpp>
#include "langton.h"

BOOST_AUTO_TEST_CASE(position_initial_de_la_fourmi) {
  Ant ant;
  BOOST_REQUIRE_EQUAL(0, ant.position().x);
  BOOST_REQUIRE_EQUAL(0, ant.position().y);
}
