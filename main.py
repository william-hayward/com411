#output file
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art 
import basics.output.escape_characters as escape_characters

#input file
import basics.input.data_types as data_types
import basics.input.review as input_review
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input

#decisions file - simple decisions
import basics.decisions.simple_decisions.comparison_operator as comparison_operator
import basics.decisions.simple_decisions.counter as counter
import basics.decisions.simple_decisions.if_elif_else as if_elif_else
import basics.decisions.simple_decisions.if_else as if_else
import basics.decisions.simple_decisions.if_ as if_
import basics.decisions.simple_decisions.modulo_operator as modulo_operator

#decisions file - multiple decisions
import basics.decisions.multiple_conditions.and_operator as and_operator
import basics.decisions.multiple_conditions.or_operator as or_operator

#decisions file - nested decisions
import basics.decisions.nested_decisions.nestception as nestception
import basics.decisions.nested_decisions.nested as nested 

#decisions file - review of decisions
import basics.decisions.review as decisions_review

#repetition file - for loops
import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.range_ as range_
import basics.repetitions.for_loop.for_loop_reverse as for_loop_reverse
import basics.repetitions.for_loop.for_loop_simple as for_loop_simple

#repetition file - nested loops
import basics.repetitions.nested_loop.nested_loop_nested as nested_loop_nested
import basics.repetitions.nested_loop.nesting as nesting

#repetition file - while loops 
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers
import basics.repetitions.while_loop.sum100 as sum100
import basics.repetitions.while_loop.while_loop_simple as while_loop_simple
import basics.repetitions.while_loop.while_loop_ascii as while_loop_ascii
import basics.repetitions.while_loop.while_loop_len as while_loop_len 

#functions file 
import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function

#modules file
import basics.modules.guess_the_number as guess_the_number

#lists file
import data.lists.simple_list as simple_list
import data.lists.index_list as index_list
import data.lists.iterate_list as iterate_list
import data.lists.populate_list as populate_list

#tuples file
import data.tuples.simple_tuple as simple_tuple
import data.tuples.function_tuple as function_tuple
import data.tuples.nested_tuple as nested_tuple

#sets file
import data.sets.simple_set as simple_set
import data.sets.set_from_list as set_from_list
import data.sets.sorted_set as sorted_set

#dictionary file
import data.dicts.simple_dict as simple_dict
import data.dicts.nested_dicts as nested_dicts

#file file
import data.files.cwd as cwd
import data.files.read as read
import data.files.write as write
import data.files.generate as generate

#plots file
import visual.plots.simple as csimple
import visual.plots.squares as squares
import visual.plots.path as path
import visual.plots.blockC_dict as Cdict

#subplots folder
import visual.subplots.simple_subplot as simple_subplot

#runs everything in the basics file
def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        print("")
        simple_message.run()
    elif (response == "multiline_message"):
        print("")
        multiline_message.run()
    elif (response == "ascii_art"):
        print("")
        ascii_art.run()
    elif (response == "escape_characters"):
        print("")
        escape_characters.run()
    elif (response == "data_types"):
        print("")
        data_types.run()
    elif (response == "input_review"):
        print("")
        input_review.run()
    elif (response == "string_operators"):
        print("")
        string_operators.run()
    elif (response == "user_input"):
        print("")
        user_input.run()
    elif (response == "comparison_operator"):
        print("")
        comparison_operator.run()
    elif (response == "counter"):
        print("")
        counter.run()
    elif (response == "if_elif_else"):
        print("")
        if_elif_else.run()
    elif (response == "if_else"):
        print("")
        if_else.run()
    elif (response == "if_"):
        print("")
        if_.run()
    elif (response == "modulo_operator"):
        print("")
        modulo_operator.run()
    elif (response == "and_operator"):
        print("")
        and_operator.run()
    elif (response == "or_operator"):
        print("")
        or_operator.run()
    elif (response == "nestception"):
        print("")
        nestception.run()
    elif (response == "nested"):
        print("")
        nested.run()
    elif (response == "decisions_review"):
        print("")
        decisions_review.run()
    elif (response == "characters"):
        print("")
        characters.run()
    elif (response == "count_down"):
        print("")
        count_down.run()
    elif (response == "membership_operators"):
        print("")
        membership_operators.run()
    elif (response == "range_"):
        print("")
        range_.run()
    elif (response == "for_loop_reverse"):
        print("")
        for_loop_reverse.run()
    elif (response == "for_loop_simple"):
        print("")
        for_loop_simple.run()
    elif (response == "nested_loop_nested"):
        print("")
        nested_loop_nested.run()
    elif (response == "nesting"):
        print("")
        nesting.run()
    elif (response == "count"):
        print("")
        count.run()
    elif (response == "factorial"):
        print("")
        factorial.run()
    elif (response == "sum_user_numbers"):
        print("")
        sum_user_numbers.run()
    elif (response == "sum100"):
        print("")
        sum100.run()
    elif (response == "while_loop_simple"):
        print("")
        while_loop_simple.run()
    elif (response == "while_loop_ascii"):
        print("")
        while_loop_ascii.run()
    elif (response == "while_loop_len"):
        print("")
        while_loop_len.run()
    elif (response == "ascii_character"):
        print("")
        ascii_character.run()
    elif (response == "ascii_code"):
        print("")
        ascii_code.run()
    elif (response == "function_calls"):
        print("")
        function_calls.run()
    elif (response == "function_with_loop"):
        print("")
        function_with_loop.run()
    elif (response == "function_with_nesting"):
        print("")
        function_with_nesting.run()
    elif (response == "function_with_parameter"):
        print("")
        function_with_parameter.run()
    elif (response == "function_with_parameters"):
        print("")
        function_with_parameters.run()
    elif (response == "multiple_functions"):
        print("")
        multiple_functions.run()
    elif (response == "return_values"):
        print("")
        return_values.run()
    elif (response == "simple_function"):
        print("")
        simple_function.run()
    elif (response == "guess_the_number"):
        print("")
        guess_the_number.run()
    

def run_block_b():
  print("Which program in 'Block B: Data' do you wish to run?")
  response = input()
  if (response == "simple_list"):
      print("")
      simple_list.run()
  elif (response == "index_list"):
      print("")
      index_list.run()
  elif (response == "iterate_list"):
      print("")
      iterate_list.run()
  elif (response == "populate_list"):
      print("")
      populate_list.run()
  elif (response == "simple_tuple"):
      print("")
      simple_tuple.run()
  elif (response == "function_tuple"):
      print("")
      function_tuple.run()
  elif (response == "nested_tuple"):
      print("")
      nested_tuple.run()
  elif (response == "simple_set"):
      print("")
      simple_set.run()
  elif (response == "set_from_list"):
      print("")
      set_from_list.run()
  elif (response == "sorted_set"):
      print("")
      sorted_set.run()
  elif (response == "simple_dict"):
      print("")
      simple_dict.run()
  elif (response == "nested_dicts"):
      print("")
      nested_dicts.run()
  elif (response == "cwd"):
      print("")
      cwd.run()
  elif (response == "read"):
      print("")
      read.run()
  elif (response == "write"):
      print("")
      write.run()
  elif (response == "generate"):
      print("")
      generate.run()

def run_block_c():
  print("Which program in 'Block C: Visual' do you wish to run?")
  response = input()
  if (response == "csimple"):
      print("")
      csimple.run()
  elif (response == "squares"):
      print("")
      squares.run()
  elif (response == "path"):
      print("")
      path.run()
  elif (response == "Cdict"):
      print("")
      Cdict.run()
  elif (response == "simple_subplot"):
      print("")
      simple_subplot.run()

def run():
    is_running = True

    while(is_running):
        print("\nWhat would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[b] Run 'Block B: Data' programs")
        print("[c] Run 'Block C: Visual' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            print("")
            run_block_a()
        elif (response == "b"):
            print("")
            run_block_b()
        elif (response == "c"):
            print("")
            run_block_c()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()