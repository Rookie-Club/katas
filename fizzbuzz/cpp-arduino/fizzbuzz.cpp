#include "fizzbuzz.h"
#include <stdio.h>
#include <sstream>

std::string fizzbuzz (int number) {
  std::stringstream ss;
  std::string chaine;

  if (number % 15 == 0) {
    chaine = "FizzBuzz";
  } else if (number % 3 == 0) {
    chaine = "Fizz";
  } else if (number % 5 == 0) {
    chaine = "Buzz";
  } else {
    ss << number;
    chaine = ss.str();
  }

  return chaine;
};

int main (int argc,  char** argv) {

  std::istringstream iss( argv[1] );
  int val;

  if (iss >> val) {

    std::string result;
    result = fizzbuzz(val);
    printf("fizzbuzz %d => %s \n", val, result.c_str());


  }
  return 0;
}
