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



def run():
    is_running = True

    while(is_running):
        print("\nWhat would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            print("")
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()