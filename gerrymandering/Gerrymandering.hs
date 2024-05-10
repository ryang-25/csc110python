import Control.Monad (join)
import Data.Bifunctor (bimap, second)
import Data.List (find, uncons)
import Data.Maybe (fromJust)
import Debug.Trace (traceShowId)

input :: String -> IO String
input prompt = do
  putStr prompt
  putStr " "
  ret <- getLine
  putStrLn ret
  return ret

uncons' = fromJust . uncons

doubleMap = join bimap

absDiff a b = abs $ a - b

chunks [] _ = []
chunks xs n = take n xs : chunks (drop n xs) n

votes :: [String] -> (String, (Int, Int))
votes = second (\vs -> let [a, b] = map read vs in (a, b)) . uncons'

split str = case break (== ',') str of
  (a, ',' : b) -> a : split b
  (a, "") -> [a]

parse =
  map
    ( second (map votes . flip chunks 3)
        . uncons'
        . split
    )
    . lines

realCeil n = floor n + 1

anyIsEven :: [(String, (Int, Int))] -> Bool
anyIsEven = any (\(a, b) -> (a + b) `rem` 2 /= 0) . map snd

-- calculate the average, and if n - a < 0 then n
-- else n - a
-- max n-a and 0
-- then min o and
-- if n - a < 0 < n
-- and if 0 < n - a < n

wasted (a, b) = doubleMap (\n -> if n - avg < 0 then n else n - avg) (a, b)
  where
    avg = (+ 1) $ floor $ fromIntegral (a + b) / 2

-- WHNF
efficiencyGap s tot = ((,) (win s) $ gap s)
  where
    gap (a, b) = (* 100) $ (/) (fromIntegral $ abs $ a - b) $ fromIntegral tot
    win (a, b) = if a < b then "Democrats" else "Republicans"

doubleSum :: [(Int, Int)] -> (Int, Int)
doubleSum = foldr (\(acc, bcc) (a, b) -> (,) (a + acc) (b + bcc)) (0, 0)

canGerryMander (_ : _ : _ : _) = True
canGerryMander _ = False

efficiencyStr percent party = "The Efficiency Gap is " ++ "1"

-- Just (doubleMap sum $ unzip $ map wasted $ snd $ unzip ds)

-- doubleMap sum $ map wasted $ snd $ unzip ds

-- gerrymandered = id

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
  contents <- readFile "districts.txt"
  state <- input "Which state do you want to look up?"
  let parsed = parse contents
  let districts = snd $ fromJust $ find ((== state) . fst) parsed
  let votes = map snd districts
  let total = let (d, r) = doubleSum votes in d + r
  let wasted_districts = map wasted votes
  let able = canGerryMander wasted_districts
  let wasted_votes = doubleSum wasted_districts
  let gap = efficiencyGap wasted_votes total
  print $ (++) "Total Wasted Democratic votes: " $ show $ fst wasted_votes
  print $ (++) "Total Wasted Republican votes: " $ show $ snd wasted_votes
  if canGerryMander wasted_districts
    then
      print gap
    else print "There are an insufficient number of districts to calculate an Efficiency Gap."
  -- if gap > 7 then print "hello" else return ()

  -- let u = map (map (second wasted)) $ map snd parsed
  -- let u = map anyIsEven $ map snd parsed
  -- print u
  return ()