from statistics import mean, stdev
from os.path import isfile
from os import rename, remove

test_results = {
  "CopyMatrix5000": [],
  "CopyMatrix7000": [],
  "CopyMatrix9000": [],
  "LookAndSay40": [],
  "LookAndSay45": [],
  "LookAndSay48": [],
  "CountUniqueWordsBible": [],
  "CountUniqueWordsBook1": [],
  "CountUniqueWordsPlrabn12": [],
  "CountUniqueWordsWorld192": [],
  "IterativeFib25": [],
  "RecursiveFib25": [],
  "IterativeFib35": [],
  "RecursiveFib35": [],
  "IterativeFib45": [],
  "RecursiveFib45": [],
  "MatrixMultiplication1500": [],
  "MatrixMultiplication1750": [],
  "MatrixMultiplication2000": [],
  "BeliefPropagation250": [],
  "BeliefPropagation500": [],
  "BeliefPropagation1000": [],
  "MarkovChain5000": [],
  "MarkovChain10000": [],
  "MarkovChain15000": [],
  "LaplaceJacobi100": [],
  "LaplaceJacobi150": [],
  "LaplaceJacobi200": [],
  "Quadrature50": [],
  "Quadrature75": [],
  "Quadrature100": [],
  "EvaluateFunctions80000": [],
  "EvaluateFunctions90000": [],
  "EvaluateFunctions100000": [],
  "PerniciousNumbers": [],
  "MunchausenNumbers": [],
}

test_from_to = {
  "CopyMatrix5000": "copy_matrix_5000",
  "CopyMatrix7000": "copy_matrix_7000",
  "CopyMatrix9000": "copy_matrix_9000",
  "LookAndSay40": "look_and_say_sequence_40",
  "LookAndSay45": "look_and_say_sequence_45",
  "LookAndSay48": "look_and_say_sequence_48",
  "CountUniqueWordsBible": "count_words_bible",
  "CountUniqueWordsBook1": "count_words_book1",
  "CountUniqueWordsPlrabn12": "count_words_plrabn12",
  "CountUniqueWordsWorld192": "count_words_world192",
  "IterativeFib25": "iterative_fibonacci_25",
  "RecursiveFib25": "recursive_fibonacci_25",
  "IterativeFib35": "iterative_fibonacci_35",
  "RecursiveFib35": "recursive_fibonacci_35",
  "IterativeFib45": "iterative_fibonacci_45",
  "RecursiveFib45": "recursive_fibonacci_45",
  "MatrixMultiplication1500": "matrix_multiplication_1500",
  "MatrixMultiplication1750": "matrix_multiplication_1750",
  "MatrixMultiplication2000": "matrix_multiplication_2000",
  "BeliefPropagation250": "belief_propagation_250",
  "BeliefPropagation500": "belief_propagation_500",
  "BeliefPropagation1000": "belief_propagation_1000",
  "MarkovChain5000": "markov_chain_function_5000",
  "MarkovChain10000": "markov_chain_function_10000",
  "MarkovChain15000": "markov_chain_function_15000",
  "LaplaceJacobi100": "iterative_solver_100",
  "LaplaceJacobi150": "iterative_solver_150",
  "LaplaceJacobi200": "iterative_solver_200",
  "Quadrature50": "compute_quadrature_50",
  "Quadrature75": "compute_quadrature_75",
  "Quadrature100": "compute_quadrature_100",
  "EvaluateFunctions80000": "evaluate_functions_80000",
  "EvaluateFunctions90000": "evaluate_functions_90000",
  "EvaluateFunctions100000": "evaluate_functions_100000",
  "PerniciousNumbers": "find_pernicious_numbers_100000",
  "MunchausenNumbers": "find_munchausen_numbers_0",
  #""" "VectorCopy": "vector_copy_500", # Unimplemented
  #"LookAndSay": "look_and_say_sequence_40",
  #"CountWordsDictionary": "count_words_dictionary_bible.txt", # Unimplemented
  #"CountUniqueWords": "count_words_set_bible.txt",
  # "IterativeFib": "iterative_fibonacci_25",
  # "RecursiveFib": "recursive_fibonacci_25",
  # "MatrixMultiplication": "matrix_multiplication_2000",
  # "BeliefPropagation": "belief_propagation_1000",
  # "MarkovChain": "markov_chain_function_15000",
  # "ComputFFT": "compute_FFT", # Unimplemented
  # "LaplaceJacobi": "loop_solver_200",
  # "VectorizedSolver": "vectorized_solver_200", # Unimplemented
  # "Quadrature": "compute_quadrature_10",
  # "EvaluateFunctions": "evaluate_functions_100000",
  # "MunchausenNumbers": None,
  # "PerniciousNumbers": None, """
}

if __name__ == "__main__":
  # Read log
  with open("java-results-log.txt", "r+") as log:
    for line in log:
      test, result = line.split(" ")
      result = result.replace(",",".")
      if test in test_results.keys():
        test_results[test].append(float(result))
  # Rename log outpus as backup
  if isfile("java-results-log-bk.txt"):
    remove("java-results-log-bk.txt")
  rename("java-results-log.txt", "java-results-log-bk.txt")
  # Obtain statistics for results read
  test_stats = { 
    test: [mean(results), min(results), max(results), stdev(results)] 
    for test, results in test_results.items() if results}
  # Transform stats data to standatd output
  test_stats = { 
    new_name: (test_stats[old_name] if old_name in test_stats.keys() else ['', '', '', ''] ) 
    for old_name, new_name in test_from_to.items() if new_name }
  # Write stats to csv
  with open("results-environment-java.csv", "w+") as csv:
    # Write header
    csv.write("function name,avg time,min time,max time,std dev\n")
    # Write lines
    for test, results in test_stats.items():
      avg, minimum, maximum, dev = tuple(results)
      csv.write(f'{test},{avg},{minimum},{maximum},{dev}\n')