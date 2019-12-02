# Python Imports

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