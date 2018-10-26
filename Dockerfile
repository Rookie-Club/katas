FROM haskell

RUN cabal update && cabal install hspec

WORKDIR /app

COPY . /app

CMD ["runghc", "FizzBuzz.hs"]
