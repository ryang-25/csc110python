


-- [input prompt] outputs the prompt to stdout and reads an integer from stdin.
input :: String -> IO Float
input prompt = do
  putStr prompt
  putStr " "
  ret <- getLine
  putStrLn ret
  return $ read ret

-- sumSquares can be a fold or implemented with recursion
sumSquares n = foldr (\acc i -> acc + 2^i) 0 [0..n]

main = do
  putStrLn "THE CHESSBOARD PROBLEM"
  squares <- input "What is the total number of squares on the gameboard?"
  volume <- input "What is the volume of a single grain of rice (in cubic mm)?"
  mass <- input "What is the mass of a single grain of rice (in mg)?"
  packign <- input "What is the fraction of air gaps (%age of voids)?"
  area <- input "What is the total surface area of South Carolina (in square miles)?"

  let rice = sumSquares $ round squares
  let rice_volume = 1

  let rice_volume = rice_volume * 35.315

  putStrLn ""
  putStrLn ("The total number of grains of rice for a gameboard of " ++ show squares ++ " is " ++ show rice ++ " grains.")





  return ()

