#define BOOST_TEST_MAIN
#include "fizzbuzz.h"
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_CASE(Cas_des_nombres) {
  BOOST_REQUIRE_EQUAL("1", fizzbuzz(1));
  BOOST_REQUIRE_EQUAL("2", fizzbuzz(2));
}

BOOST_AUTO_TEST_CASE(Cas_du_fizz) {
  BOOST_REQUIRE_EQUAL("Fizz", fizzbuzz(3));
  BOOST_REQUIRE_EQUAL("Fizz", fizzbuzz(6));
}

BOOST_AUTO_TEST_CASE(Cas_du_buzz) {
  BOOST_REQUIRE_EQUAL("Buzz", fizzbuzz(5));
  BOOST_REQUIRE_EQUAL("Buzz", fizzbuzz(10));
}

BOOST_AUTO_TEST_CASE(Cas_du_fizzbuzz) {
  BOOST_REQUIRE_EQUAL("FizzBuzz", fizzbuzz(15));
  BOOST_REQUIRE_EQUAL("FizzBuzz", fizzbuzz(30));
}
