#!/usr/bin/env python
# coding: utf-8

from collections import namedtuple
from faker import Faker
import datetime
from time import perf_counter
from functools import wraps
import re
import random
import string
from datetime import date
from statistics import mode
from numpy import random


# Using the Faker object to create one fake profile
fake = Faker()
fake.profile()


# Creating a named tuple with the keys in the fake profile as fields
Profile = namedtuple('Profile', fake.profile().keys())


# Defining a Decorator to obtain the execution time for namedtuples and
# dictionary
def timed(fn):
    """Decorator to determine run time of a function."""
    @wraps(fn)
    def inner(*args, **kwargs):
        """
        Inner function to calculate the time.
        """
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_elapsed = (end - start)
        return time_elapsed, result
    return inner


# Question1

def init_profiles_using_namedtuple(no_profiles: int):
    """Creating fake profiles for given number of people using namedtuples"""
    profiles = []
    Profile = namedtuple('Profile', fake.profile().keys())
    for _ in range(no_profiles):
        profiles.append(Profile(**fake.profile()))
    return profiles


@timed
def oldest_person_nt(all_profile_nt: namedtuple) -> float:
    """This function finds the oldest person from the slot, calculates the \
        duration. The minimum birthdate and time is returned."""
    """Param: all_profile_nt: Named tuple containing all profiles"""
    value = min(all_profile_nt, key=lambda v: v[-1])
    date_today = datetime.date.today()
    age = (date_today - value.birthdate).days
    return int(age/365)


@timed
def average_age_nt(all_profile_nt: namedtuple) -> tuple:
    """This function finds the average age of the person from the slot, \
        calculates the duration to perform that operation. \
            The average age and time is returned."""
    """Param: all_profile_nt: Named tuple containing all profiles"""
    today = date.today()
    value = sum(map(lambda v: today.year - v[-1].year - ((today.month, today.day) < (
        v[-1].month, v[-1].day)), all_profile_nt))/len(all_profile_nt)
    return value


@timed
def average_coords_nt(all_profile_nt: namedtuple) -> tuple:
    """This function finds the average coordinates  from the slot, calculates \
        the duration to perform that operation. The average coordinates and \
            time is returned."""
    """Param: all_profile_nt: Named tuple containing all profiles"""
    x, y = sum(map(lambda t: t[0], map(lambda v: v[4], all_profile_nt)))/len(all_profile_nt), sum(
        map(lambda t: t[1], map(lambda v: v[4], all_profile_nt)))/len(all_profile_nt)
    return x, y


@timed
def max_bloodgroup_nt(all_profile_nt: namedtuple) -> tuple:
    """This function uses the mode function defined in statisics library to find \
        the most occured blood group from the list. The list is generated \
            using the lambda function and returned to the mode function as a \
                parameters. The code is then timed and the result and time is \
                    sent back."""
    """Param:all_profile_nt: Named tuple containing all profiles"""
    blood_group = mode(list(map(lambda v: v[5], all_profile_nt)))
    return blood_group


def time_nt(fk_Profile_nt: namedtuple, N: int) -> 'float':
    ti = 0
    for _ in range(N):
        total_exec_time_nt = oldest_person_nt(fk_Profile_nt)[0] + average_age_nt(fk_Profile_nt)[
            0] + average_coords_nt(fk_Profile_nt)[0] + max_bloodgroup_nt(fk_Profile_nt)[0]
        ti += total_exec_time_nt
    return ti/N


# Question2

# Converting the Profile Data generated into Dictionary

def namedtup_dict(all_profile_nt: namedtuple) -> dict:
    return {'Profile'+str(_): t._asdict() for _, t in enumerate(all_profile_nt)}


@timed
def oldest_person_dc(all_profile_dict: dict) -> float:
    """This function finds the oldest person from the slot, calculates the \
        duration. The minimum birthdate and time is returned."""
    """Param:all_profile_dc: dictionary containing all profiles"""
    value = min(all_profile_dict.values(), key=lambda v: v['birthdate'])
    date_today = datetime.date.today()
    age = (date_today - value['birthdate']).days
    return int(age/365)


@timed
def average_age_dc(all_profile_dict: dict) -> float:
    """This function finds the average age of the person from the slot, \
        calculates the duration to perform that operation. The average age \
            and time is returned."""
    """Param:all_profile_dc: Dictionary containing all profiles"""
    today = date.today()
    value = sum(map(lambda v: today.year - v['birthdate'].year - ((today.month, today.day) < (
        v['birthdate'].month, v['birthdate'].day)), all_profile_dict.values())) / len(all_profile_dict)
    return value


@timed
def average_coords_dc(all_profile_dict: dict) -> tuple:
    """This function finds the average coordinates  from the slot, calculates \
        the duration to perform that operation. The average coordinates and \
            time is returned."""
    """Param:all_profile_dc: dictionary containing all profiles"""
    x, y = sum(map(lambda t: t[0], map(lambda v: v['current_location'], all_profile_dict.values()))) / len(all_profile_dict.values(
    )), sum(map(lambda t: t[1], map(lambda v: v['current_location'], all_profile_dict.values()))) / len(all_profile_dict.values())
    return x, y


@timed
def max_bloodgroup_dc(all_profile_dict: dict) -> tuple:
    """This function uses the mode function defined in statisics library to \
        find the most occured blood group from the list. The list is \
            generated using the lambda function and returned to the mode \
                function as a parameters. The code is then timed and the \
                    result and time is sent back."""
    """Param:all_profile_dc: dictionary containing all profiles"""
    value = mode(
        list(map(lambda v: v['blood_group'], all_profile_dict.values())))
    return value


def time_dc(fk_Profile_dict: dict, N: int) -> 'float':
    ti = 0
    for _ in range(N):
        total_exec_time_dc = oldest_person_dc(fk_Profile_dict)[0] + average_age_dc(fk_Profile_dict)[
            0] + average_coords_dc(fk_Profile_dict)[0] + max_bloodgroup_dc(fk_Profile_dict)[0]
        ti += total_exec_time_dc
    return ti/N


# Question3

# Returns a Symbol for the Company
def symbol(string: str) -> str:
    """Returns joined string if characters are upper case"""
    L = len(string)
    P1 = random.randint(1, L-1, 2)
    chars = []
    for char in string:
        chars.append(char)
    chars[P1[0]] = chars[P1[0]].upper()
    chars[P1[1]] = chars[P1[1]].upper()
    return ''.join(x for x in chars if x.isupper())+str(random.randint(9))


def stock_market(no_profiles: int) -> tuple:
    """To create a fake stock data set for imaginary stock exchange for \
        top 100 companies (name, symbol, open, high, close). \
            Tasks_ToDo: Assign a random weight to all the companies. \
                Calculate and show what value stock market started at, what \
                    was the highest value during the day and where did \
                        it end."""
    all_companies = []
    Stocks = namedtuple("Stocks", 'name symbol open high close company_weight')
    MkValue_ = random.uniform(1000, 50000, 100)
    wts_ = random.uniform(0, 1, 100)
    wts_ = wts_/sum(wts_)

    for _ in range(100):
        name = fake.company()
        open_ = round(MkValue_[_]*wts_[_],2)
        close = round(open_ * random.uniform(0.7, 1.15), 2)
        high = round(open_ * random.uniform(0.85, 1.15), 2)
        if high < open_:
            high = open_
        if high < close:
            high = close

        all_companies.append(
            Stocks(name=name, symbol=symbol(name), open=open_, high=round(high, 2), close=round(close, 2), company_weight=round(wts_[_], 4)))

    stock_index = round(
        sum(x.open * x.company_weight for x in all_companies), 4)
    highest_for_day = round(
        sum(x.high * x.company_weight for x in all_companies), 2)
    lowest_close_for_day = round(
        sum(x.close * x.company_weight for x in all_companies), 2)

    # print(f"\n------------------------------------Top 100 listed companies on Fake Stock Exchange------------------------------------")
    # [print(x) for x in sorted(all_companies, key=lambda x:x.symbol)]
    # print(f"\n--------------Main details on {date.today()}--------------")
    # print(f"\nStart of the day: {stock_index}")
    # print(f"Highest for the day: {highest_for_day}")
    # print(f"Lowest close for the day: {lowest_close_for_day}")
    return sorted(all_companies, key=lambda x: x.symbol), stock_index, highest_for_day, lowest_close_for_day
