def find_plan(input_string, plans):
  lst_of_relevant_plans = []

  for item in plans:
    if input_string.lower() in item.lower():
       lst_of_relevant_plans.append(item)

  return lst_of_relevant_plans
