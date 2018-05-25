import Test.Hspec

data FBType = Same Integer | Fizz deriving (Eq, Show)

fizzBuzz :: Integer -> FBType
fizzBuzz x = x

main = hspec $ do
  describe "FizzBuzz should" $ do
    it "return 1" $
      (fizzBuzz 1) `shouldBe` 1
    it "return Fizz" $
      (fizzBuzz 3) `shouldBe` Fizz
