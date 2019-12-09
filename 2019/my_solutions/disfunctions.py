###############################################################################
### pthon imports                                                           ###
###############################################################################



import pandas as pd
import numpy as np

# Functionize testing

def test_target_check(df, target_col='target', test_col='test', result_col='result'):
    df[result_col] = df[test_col] == df[target_col]
    return len(df[result_col]) == sum(df[result_col])


# Day 1 Functions

def fuel_calc(mass):
    return (mass // 3) - 2


def fuel_counter_upper(df, mass_col='mass', fuel_col='fuel', test_id='p1'):
    df[fuel_col] = df[mass_col].apply(lambda x: fuel_calc(x))
    return df[fuel_col].sum()


def fuel_recalc(fuel):
    refuel = fuel
    new_fuel = fuel
    while refuel > 8:
        refuel = max(0, fuel_calc(refuel))
        new_fuel += refuel
    return new_fuel


def fuel_topper_offer(df, fuel_col='fuel', refuel_col='refuel'):
    df[refuel_col] = df[fuel_col].apply(lambda x: fuel_recalc(x))
    return df[refuel_col].sum()


# Day 2 Functions

def run_opcode_step(code_list, start_pos, show_it=False):
    run_code = code_list[start_pos]
    max_pos = len(code_list)
    var1_pos = code_list[min(start_pos + 1, max_pos-1)]
    var1 = code_list[var1_pos]
    var2_pos = code_list[min(start_pos + 2, max_pos-1)]
    var2 = code_list[var2_pos]
    answer_pos = code_list[min(start_pos + 3, max_pos-1)]
    # if show_it:
    #     print(f'run_code: {run_code}, var1: {var1}, var2: {var2}:, answer_pos: {answer_pos}')
    prev_value = code_list[answer_pos]
    if run_code == 99:
        if show_it:
            print(f'End of code at step {start_pos}')
        return 0
    if run_code == 1:
        result = var1 + var2
    elif run_code == 2:
         result = var1 * var2
    else:
        print(f'ERROR FOUND at step {start_pos}')
        return -1
    code_list[answer_pos] = result
    if show_it:
        print(f'Position {answer_pos} changed to {result}')
    return 1


def opcode_step_through(start_codes, show_it=False):
    code_list = start_codes.copy()
#     if show_it:
#         print(code_list)
    on_pos = 0
    max_pos = len(code_list)
    go_code = 1
    steps = 0
    while go_code > 0:
        to_pos = min(on_pos + 4, max_pos-1)
        if code_list[on_pos] == 99:
            go_code = 0
#             if show_it:
#                 print('Result:', code_list)
            continue
        if show_it:
#             print(on_pos, to_pos)
            print(f'Position {on_pos}:') 
            print(code_list[on_pos:to_pos])
        go_code = run_opcode_step(code_list, on_pos, show_it=show_it)
#         if show_it:
#             print(f'Position {on_pos}:', code_list[on_pos:to_pos])
#             print('Go Code =', go_code)
        on_pos = to_pos
        steps += 1
    print(f'Resolved in {steps} steps')
    return code_list


def opcode_step_through_df(df, input_col='input', output_col='output', show_it=False):
    df[output_col] = df[input_col].apply(lambda x: opcode_step_through(x, show_it=show_it))
    return df


def compute_intcode(src_df, noun=12, verb=2, code_col='code', result_col='result', show_it=False):
    df = src_df.copy()
    df.iloc[1]=noun
    df.iloc[2]=verb
    df[result_col] = opcode_step_through(df[code_col], show_it=show_it)
    return df


