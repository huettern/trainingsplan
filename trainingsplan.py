# -*- coding: utf-8 -*-
# @Author: noah
# @Date:   2020-10-18 09:31:13
# @Last Modified by:   Noah Huetter
# @Last Modified time: 2020-10-19 10:06:57
import numpy as np
import itertools, copy, sys, datetime
import matplotlib
import matplotlib.pyplot as plt

# offset data to start plan
start_date = '19.10.2020'

# training days in day numbers, Monday = 0.
# currently only supporting 2 trainings per week
training_days = [0, 4]
trainings_per_week = len(training_days)

# number of events per day
events_per_day = 3

# training group names
groups = ['K1', 'K2', 'K3', 'K5+']

# events in their correct order
events = ['Re', 'Tr', 'Bo', 'Sr', 'Sp', 'Ba']

# if set to 0, every week the same assignment is generated
# any value greater than 0 sets the increment of the first 
# event in a week so that each week the trianing is newly
# distributed to the two days
weekly_increment = 2

# halls and the events they contain
halls = [ ['Re', 'Tr', 'Bo', 'Sr'],
          ['Ba', 'Sp'] ]

# special occasions and their period in weeks
specials = [ { 'Airtrack': 4 } ]

# mapping for pre-competition week
competition_training = [('K1', 'RE'), ('K2', 'SP'), ('K3',' SR'), ('K5+', 'BO')]


def event_to_hall(idx):
  """Given an event index, return the hall index
  
  
  
  Arguments:
    idx {int} -- event index in the events list
  """
  event = events[idx]
  hall_idx = 0
  for hall in halls:
    if event in hall:
      return hall_idx
    hall_idx += 1
  print('Could not find mapping from event index %d to hall' % (idx))
  return -1

def exponential_cost(x, b):
  """maps a linear normalized cost to an exponential
  Arguments:
    x {float} -- linear cost in [0,1]
    b {float} -- how much exponential. 0->linear, pos -> higher cost have higher influence
  """
  return 1/(np.exp(b)-1)*np.exp(x*b)-1/(np.exp(b)-1)

def cost_funtion(mapping):
  """Cost function of a given mapping from groups to events
  
  Returns a relative metric. Lower is better. A mapping that violates 
  hard rules returns infinity
  
  Arguments:
    mapping {list of tuples of int} -- every tuple represents a group ([0]) mapped 
      to an event ([1]). The list length must be len(groups)
  """
  inf = float('inf')

  # Assertions
  if len(mapping) != len(groups):
    return inf

  ####################
  # Hard metrics
  ####################

  # Never two groups on same event -> check for duplicates in tuple[1]
  if len([t[1] for t in mapping]) != len(set([t[1] for t in mapping])):
    print('Found duplicate events in mapping')
    return inf

  ####################
  # Soft metrics
  ####################
  # Different metrics can be weighed. All are normalized to [0,1]
  distribution_weight = 1.0
  cost = 0

  # We want the groups distributed accross the two halls
  occupancy =  [0]*len(halls)
  for t in mapping:
    occupancy[event_to_hall(t[1])] += 1
  # Use the spread as a measure of cost. it is zero for perfect distribution
  spread = np.max(occupancy) - np.min(occupancy)
  worst_spread = len(groups)
  # give higher spread an exponential cost so that in longer training
  # sequences, bad distribution among halls gets penalized more heavily
  cost += distribution_weight*exponential_cost(spread/worst_spread, 3)

  return cost

def gen_initials():
  """Generate all possible initial mappings from groups to events.
  
  Initial by only a single mapping that can then be used to start iteration 
  by means of trainings per week and weekly increment
  """

  # distribute groups to events. create a list containing all groups and extend
  # it with [-1] to the length of events
  perms = list(range(len(groups))) + [-1]*(len(events)-len(groups))
  # all possible mappings are now generated by permuting this list, -1 representing
  # the unused events
  perms = list(itertools.permutations(perms))
  # remove identic entries caused by multiple [-1]
  perms = list((set(perms)))
  # generate mappings in the form of list of tuples (group, event)
  initials = []
  for m in perms:
    mapping = []
    event_idx = 0
    for e in m:
      if e != -1:
        mapping.append((e, event_idx))
      event_idx += 1
    # sort by group
    mapping.sort(key=lambda tup: tup[0])
    # append to all initials
    initials.append(mapping)
  # assert length of initial condition, should be permutation of n=events, r=groups
  assert len(initials) == (np.math.factorial(len(events))/np.math.factorial(len(events)-len(groups))), "Error in generating initials"

  return initials

def get_training_initial(initial, offset, weekly_incr):
  """Given an initial mapping and offset in days, return the mapping for this trianing
  
  The offset is in trainings. 0 -> initial training, 2 -> with 2 traninngs per week, the
  training the week after the initial
  
  Arguments:
    initial {list of tuples} -- initial mapping
    offset {int} -- n-th training
    weekly_incr {int} -- number of events to skeep over a weekend
  """
  n_weeks = offset // trainings_per_week
  remainder = offset % trainings_per_week

  increment = n_weeks*(weekly_incr + trainings_per_week*events_per_day) + remainder*events_per_day

  print("event increment for training offset %d = %d events (%d weeks, %d days)" % (offset, increment, n_weeks, remainder) )

  # actual increment
  ret = []
  for m in initial:
    ret.append((m[0], (m[1] + increment) % len(events)))

  return ret

def get_training_map(initial, rotation):
  """For a initial map, generate the map of the rotation-th rotation on the same triaining
  
  simply increments each event by 1 and wraps at number of events
  
  Arguments:
    initial {list of tuples} -- initial mapping
    rotation {int} -- 0 -> returns initial. else, increments by rotation and wraps at len(events)
  """
  ret = []
  for m in initial:
    ret.append((m[0], (m[1] + rotation) % len(events)))
  return ret

def cost_of_sequence(initial, n_trainings, weekly_incr):
  """Given an initial mapping, the number of trainings per week and iteration,
  calcualte the cost of this mapping. n_trainings defines how many trainings 
  are tested. The cost is added and normalized

  
  Arguments:
    initial {list of tuples} -- mapping of groups to events for initial training
    n_trainings {int} -- number of subsequent trainings to simulate
  """
  cost = 0

  for off in range(n_trainings):
    training_initial = get_training_initial(initial, off, weekly_incr)
    for rot in range(events_per_day):
      m = get_training_map(training_initial, rot)
      c = cost_funtion(m)
      # print("Map ", m, "cost ", c)
      cost += c

  return cost / (n_trainings*events_per_day)

def get_event_by_group(initial, rotaion, group):
  """return event string by weekly initial, event rotation and group
  
  Arguments:
    initial {list} -- initial list of mapping
    rotaion {int} -- which event
    group {int} -- group index
  """
  mping = get_training_map(initial, rotaion)
  for m in mping:
    if m[0] == group:
      return events[m[1]]

def start_date_to_offset(date):
  """Calculate offset from start date string. Offset can then be used to 
  get training data
  
  
  Arguments:
    date {str} -- start date in form DD.MM.YYYY
  """
  now = datetime.datetime.strptime(date, '%d.%m.%Y')
  off = datetime.datetime.strptime(start_date, '%d.%m.%Y')
  delta = now-off
  return (delta.days//7) * trainings_per_week

def get_date_from_offset(offset):
  """Return date object from offset of initial date
  
  Arguments:
    off {int} -- offset in number of trainings
  """
  off = datetime.datetime.strptime(start_date, '%d.%m.%Y')
  return off + datetime.timedelta(days = 7*(offset//trainings_per_week)+training_days[(offset%trainings_per_week)])

def main():
  """Main program entry
  """

  # do some assertions
  assert len(training_days) == 2, "currently supporting only 2 training days"
  assert len(events) == 6, "Only tested with 6 events"
  assert len(groups) == 4, "Only tested with 4 groups"

  # generate initial state
  initials = gen_initials()
  print("Got %d initials" % (len(initials)))

  # test cost function
  # for mapping in initials:
  #   print("Mapping: ")
  #   print(mapping)
  #   print("Cost: %f" % (cost_funtion(mapping)))

  # initial = initials[2]
  # print("initial ", initial)
  # print( get_training_map(initial, 1) )
  # print( get_training_map(initial, 2) )

  # print("total cost ", cost_of_sequence(initial, 5, 2))

  # loop over different weekly increments
  wi = weekly_increment

  # tracking
  costs = np.zeros(len(initials))

  print("Running for weekly increment %d" % wi)
  min_cost = sys.float_info.max
  best_candidates = []
  # find period where pattern repeats
  n_trainings = -1
  for sim_time in range(trainings_per_week,1000,trainings_per_week):
    tmp_init = get_training_initial(initials[0], sim_time, wi)
    if tmp_init == initials[0]:
      print("Found period of %d trainings" % sim_time)
      n_trainings = sim_time
      break
  assert n_trainings > 0, 'Could not find a period for these parameters'

  # now, calculate training cost for this period for all possible initials
  itr = 0
  for init in initials:
    c = cost_of_sequence(init, n_trainings, wi)

    # keep the best
    if c < min_cost:
      best_candidates = []
      best_candidates.append(init)
      min_cost = c
    elif c == min_cost:
      best_candidates.append(init)

    # tracking
    costs[itr] = c
    itr = itr + 1

  # report
  print("Found %d best initials (%.0f%%) with cost %f" % (len(best_candidates), 100.0/len(initials)*len(best_candidates), c))
  print(best_candidates[0])

  # plot
  print(costs.shape)
  fig, ax = plt.subplots(2, 1)
  ax[0].plot(costs)
  ax[0].set(xlabel='iteration', ylabel='cost',
         title='Costs for given initial condition')
  ax[0].grid()

  n, bins, patches = ax[1].hist(costs, bins=50, density=True, facecolor='b', alpha=0.75)
  ax[1].set(xlabel='cost bin', ylabel='count',
         title='Cost histogram')
  ax[1].grid()

  plt.show()


if __name__ == '__main__':
  main()