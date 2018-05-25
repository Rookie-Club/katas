import Data.Maybe (fromMaybe)

fizzBuzz :: Integer -> String
fizzBuzz n = fromMaybe (show n) $ fizz n `mappend` buzz n
  where fizz = maybeWord 3 "Fizz"
        buzz = maybeWord 5 "Buzz"

maybeWord :: Integer -> String -> Integer -> Maybe String
maybeWord divisor word n
  | n `mod` divisor == 0 = Just word
  | otherwise = Nothing


main = fizzBuzz 3
