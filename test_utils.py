import pytest


def find_plan(input_string, plans):
  lst_of_relevant_plans = []

  for item in plans:
    if input_string.lower() in item.lower():
       lst_of_relevant_plans.append(item)

  return lst_of_relevant_plans

def test_find_plan():
  assert find_plan('AGG', ['aggokoko', 'ssd323aggoo', 'asdsd22AGg', 'sdff']) == ['aggokoko', 'ssd323aggoo', 'asdsd22AGg']

  assert find_plan('AGG', ['okoko', 'ssd323oo', 'asdsd22', 'sdff']) == []




