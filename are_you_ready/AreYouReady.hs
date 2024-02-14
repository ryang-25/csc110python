-- Project title: Are You Ready?
-- Roland Yang
-- 2/14/24
-- On my honor, I have neither given nor received unauthorized help on this
-- assignment

{-# LANGUAGE Strict #-}

-- initialize

-- [input prompt] outputs the prompt to stdout and reads an integer from stdin.
input :: String -> IO Int
input prompt = do
  putStr prompt
  putStr " "
  ret <- getLine
  putStrLn ret
  return $ read ret

-- [input_10 prompt] validates the input
input_10 = (validate <$>) . input 
  where
    -- validate that n is within 1 and 10, raising an exception if not
    validate n
      | n < 1 || n > 10 = error "Input must be between 1 and 10"
      | otherwise = n

main = do
  -- input
  importance <- input_10 "Please enter the Importance of the event (from 1 to 10):"
  sleep <- input "Please enter the Hours of sleep you had last night:"
  shots <- input "Please enter the number of Shots of expresso or other stimulants consumed:"
  -- excel hours must be nonzero for the calculation.
  excel <- (\hs -> if hs == 0 then error "Hours must be nonzero!" else hs)
      <$> input "Please enter the number of Hours needed to excel:"
  preparing <- input "Please enter the number of Hours you actually spent preparing:"
  difficulty <- input_10 "Please enter the Difficulty of the subject matter (from 1 to 10):"
  nervousness <- input_10 "Please enter your Level of nervousness (from 1 to 10):"
  -- process
  let numerator = 8*preparing*(sleep+shots)
  let denominator = 3*excel*(difficulty+nervousness+importance)
  let output = fromIntegral numerator / fromIntegral denominator
  -- output
  putStrLn "If your Prepared-ness score is greater that 1, you will be just fine."
  putStr "Your Preparded-ness score is: "
  print output
  -- extra bonus
  if output > 1 then
    putStrLn "GO IN CONFIDENCE"
  else
    putStrLn "YOU NEED MORE PREPARATION"
