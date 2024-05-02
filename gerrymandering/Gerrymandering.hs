import Data.List (uncons)
import Data.Maybe (fromJust)

input :: String -> IO String
input prompt = do
  putStr prompt
  putStr " "
  ret <- getLine
  putStrLn ret
  return ret 

chunks [] _ = []
chunks xs n = take n xs : chunks (drop n xs) n

wasted (d, r) = abs d - r

parse = uncurry zip
    . (\(s, ds) -> (s,  chunks ds 3))
    . fromJust 
    . uncons 
    . map words
    . lines

-- This program allows you to search through data about congressional voting districts
-- and determine whether a particular state is gerrymandered.
-- Which state do you want to look up? Arizona
-- Total Wasted Democratic votes: 327852
-- Total Wasted Republican votes: 369697
-- 4738332 eligible voters
-- The Efficiency Gap is 0.9% in favor of the Democrats.
-- The State does not appear to be gerrymandered.
-- 1 of 4


main = do
  putStrLn "This program allows you to search through data about congressional voting districts"
  putStrLn "and determine whether a particular state is gerrymandered."
  state <- input "Which state do you want to look up?"
  return ()