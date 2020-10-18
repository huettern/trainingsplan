# -*- coding: utf-8 -*-
# @Author: noah
# @Date:   2020-10-18 13:23:02
# @Last Modified by:   noah
# @Last Modified time: 2020-10-18 14:49:55

import trainingsplan as tp
import datetime

# Initial state that was found with the trainingsplan main
initial = [(0, 5), (1, 4), (2, 1), (3, 3)]

def gen_html_week(mapping, offset):
  """Generate a single week html table


  """
  class Default(dict):
    def __missing__(self, key):
      return key

  mon = 'Montag, ' + tp.get_date_from_offset(offset).strftime('%d.%m.%Y')
  fri = 'Freitag, ' + tp.get_date_from_offset(offset+1).strftime('%d.%m.%Y')

  with open('template/week.html', 'r') as f_tplt:
    tplt = f_tplt.read()

    tplt = tplt.format_map(Default(
        monday = mon,
        friday = fri,
        group0 = tp.groups[0],
        group1 = tp.groups[1],
        group2 = tp.groups[2],
        group3 = tp.groups[3],
        g0e0 = tp.get_event_by_group(mapping, 0, 0),
        g0e1 = tp.get_event_by_group(mapping, 1, 0),
        g0e2 = tp.get_event_by_group(mapping, 2, 0),
        g0e3 = tp.get_event_by_group(mapping, 3, 0),
        g0e4 = tp.get_event_by_group(mapping, 4, 0),
        g0e5 = tp.get_event_by_group(mapping, 5, 0),
        g1e0 = tp.get_event_by_group(mapping, 0, 1),
        g1e1 = tp.get_event_by_group(mapping, 1, 1),
        g1e2 = tp.get_event_by_group(mapping, 2, 1),
        g1e3 = tp.get_event_by_group(mapping, 3, 1),
        g1e4 = tp.get_event_by_group(mapping, 4, 1),
        g1e5 = tp.get_event_by_group(mapping, 5, 1),
        g2e0 = tp.get_event_by_group(mapping, 0, 2),
        g2e1 = tp.get_event_by_group(mapping, 1, 2),
        g2e2 = tp.get_event_by_group(mapping, 2, 2),
        g2e3 = tp.get_event_by_group(mapping, 3, 2),
        g2e4 = tp.get_event_by_group(mapping, 4, 2),
        g2e5 = tp.get_event_by_group(mapping, 5, 2),
        g3e0 = tp.get_event_by_group(mapping, 0, 3),
        g3e1 = tp.get_event_by_group(mapping, 1, 3),
        g3e2 = tp.get_event_by_group(mapping, 2, 3),
        g3e3 = tp.get_event_by_group(mapping, 3, 3),
        g3e4 = tp.get_event_by_group(mapping, 4, 3),
        g3e5 = tp.get_event_by_group(mapping, 5, 3),
      ))

    with open('out/week.html', 'w') as f_tplt_o:
      f_tplt_o.write(tplt)


def gen_html_large(mapping, offset):
  """Generates the large html


  """
  class Default(dict):
    def __missing__(self, key):
      return key

  out = ''

  for row in range(4):

    off = offset + row*12
    init = tp.get_training_initial(initial, row*12, tp.weekly_increment)

    mon0 = 'Montag, ' + tp.get_date_from_offset(off).strftime('%d.%m.%Y')
    fri0 = 'Freitag, ' + tp.get_date_from_offset(off+1).strftime('%d.%m.%Y')
    mon1 = 'Montag, ' + tp.get_date_from_offset(off+2).strftime('%d.%m.%Y')
    fri1 = 'Freitag, ' + tp.get_date_from_offset(off+3).strftime('%d.%m.%Y')
    mon2 = 'Montag, ' + tp.get_date_from_offset(off+4).strftime('%d.%m.%Y')
    fri2 = 'Freitag, ' + tp.get_date_from_offset(off+5).strftime('%d.%m.%Y')
    mon3 = 'Montag, ' + tp.get_date_from_offset(off+6).strftime('%d.%m.%Y')
    fri3 = 'Freitag, ' + tp.get_date_from_offset(off+7).strftime('%d.%m.%Y')
    mon4 = 'Montag, ' + tp.get_date_from_offset(off+8).strftime('%d.%m.%Y')
    fri4 = 'Freitag, ' + tp.get_date_from_offset(off+9).strftime('%d.%m.%Y')
    mon5 = 'Montag, ' + tp.get_date_from_offset(off+10).strftime('%d.%m.%Y')
    fri5 = 'Freitag, ' + tp.get_date_from_offset(off+11).strftime('%d.%m.%Y')

    with open('template/large.html', 'r') as f_tplt:
      tplt = f_tplt.read()

      tplt = tplt.format_map(Default(
          monday0 = mon0,
          friday0 = fri0,
          monday1 = mon1,
          friday1 = fri1,
          monday2 = mon2,
          friday2 = fri2,
          monday3 = mon3,
          friday3 = fri3,
          monday4 = mon4,
          friday4 = fri4,
          monday5 = mon5,
          friday5 = fri5,
          group0 = tp.groups[0],
          group1 = tp.groups[1],
          group2 = tp.groups[2],
          group3 = tp.groups[3],
          # group literals
          g0name = 'Kim/Dani',
          g1name = 'Bea/Noah',
          g2name = 'Larissa/Lukas',
          g3name = 'Adi',
          # einturnen
          e0='',
          e1='',
          e2='',
          e3='',
          e4='',
          e5='',
          e6='',
          e7='',
          e8='',
          e9='',
          e10='',
          e11='',
          # events
          g0e00 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 0, 0),
          g0e01 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 1, 0),
          g0e02 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 2, 0),
          g0e03 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 3, 0),
          g0e04 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 4, 0),
          g0e05 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 5, 0),
          g0e10 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 0, 0),
          g0e11 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 1, 0),
          g0e12 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 2, 0),
          g0e13 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 3, 0),
          g0e14 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 4, 0),
          g0e15 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 5, 0),
          g0e20 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 0, 0),
          g0e21 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 1, 0),
          g0e22 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 2, 0),
          g0e23 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 3, 0),
          g0e24 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 4, 0),
          g0e25 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 5, 0),
          g0e30 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 0, 0),
          g0e31 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 1, 0),
          g0e32 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 2, 0),
          g0e33 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 3, 0),
          g0e34 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 4, 0),
          g0e35 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 5, 0),
          g0e40 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 0, 0),
          g0e41 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 1, 0),
          g0e42 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 2, 0),
          g0e43 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 3, 0),
          g0e44 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 4, 0),
          g0e45 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 5, 0),
          g0e50 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 0, 0),
          g0e51 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 1, 0),
          g0e52 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 2, 0),
          g0e53 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 3, 0),
          g0e54 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 4, 0),
          g0e55 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 5, 0),
          # group 1
          g1e00 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 0, 1),
          g1e01 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 1, 1),
          g1e02 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 2, 1),
          g1e03 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 3, 1),
          g1e04 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 4, 1),
          g1e05 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 5, 1),
          g1e10 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 0, 1),
          g1e11 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 1, 1),
          g1e12 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 2, 1),
          g1e13 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 3, 1),
          g1e14 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 4, 1),
          g1e15 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 5, 1),
          g1e20 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 0, 1),
          g1e21 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 1, 1),
          g1e22 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 2, 1),
          g1e23 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 3, 1),
          g1e24 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 4, 1),
          g1e25 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 5, 1),
          g1e30 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 0, 1),
          g1e31 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 1, 1),
          g1e32 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 2, 1),
          g1e33 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 3, 1),
          g1e34 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 4, 1),
          g1e35 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 5, 1),
          g1e40 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 0, 1),
          g1e41 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 1, 1),
          g1e42 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 2, 1),
          g1e43 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 3, 1),
          g1e44 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 4, 1),
          g1e45 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 5, 1),
          g1e50 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 0, 1),
          g1e51 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 1, 1),
          g1e52 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 2, 1),
          g1e53 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 3, 1),
          g1e54 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 4, 1),
          g1e55 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 5, 1),
          #group 2
          g2e00 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 0, 2),
          g2e01 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 1, 2),
          g2e02 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 2, 2),
          g2e03 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 3, 2),
          g2e04 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 4, 2),
          g2e05 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 5, 2),
          g2e10 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 0, 2),
          g2e11 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 1, 2),
          g2e12 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 2, 2),
          g2e13 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 3, 2),
          g2e14 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 4, 2),
          g2e15 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 5, 2),
          g2e20 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 0, 2),
          g2e21 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 1, 2),
          g2e22 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 2, 2),
          g2e23 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 3, 2),
          g2e24 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 4, 2),
          g2e25 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 5, 2),
          g2e30 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 0, 2),
          g2e31 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 1, 2),
          g2e32 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 2, 2),
          g2e33 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 3, 2),
          g2e34 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 4, 2),
          g2e35 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 5, 2),
          g2e40 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 0, 2),
          g2e41 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 1, 2),
          g2e42 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 2, 2),
          g2e43 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 3, 2),
          g2e44 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 4, 2),
          g2e45 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 5, 2),
          g2e50 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 0, 2),
          g2e51 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 1, 2),
          g2e52 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 2, 2),
          g2e53 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 3, 2),
          g2e54 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 4, 2),
          g2e55 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 5, 2),
          # group 3
          g3e00 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 0, 3),
          g3e01 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 1, 3),
          g3e02 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 2, 3),
          g3e03 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 3, 3),
          g3e04 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 4, 3),
          g3e05 = tp.get_event_by_group(tp.get_training_initial(init, 2*0, tp.weekly_increment), 5, 3),
          g3e10 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 0, 3),
          g3e11 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 1, 3),
          g3e12 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 2, 3),
          g3e13 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 3, 3),
          g3e14 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 4, 3),
          g3e15 = tp.get_event_by_group(tp.get_training_initial(init, 2*1, tp.weekly_increment), 5, 3),
          g3e20 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 0, 3),
          g3e21 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 1, 3),
          g3e22 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 2, 3),
          g3e23 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 3, 3),
          g3e24 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 4, 3),
          g3e25 = tp.get_event_by_group(tp.get_training_initial(init, 2*2, tp.weekly_increment), 5, 3),
          g3e30 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 0, 3),
          g3e31 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 1, 3),
          g3e32 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 2, 3),
          g3e33 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 3, 3),
          g3e34 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 4, 3),
          g3e35 = tp.get_event_by_group(tp.get_training_initial(init, 2*3, tp.weekly_increment), 5, 3),
          g3e40 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 0, 3),
          g3e41 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 1, 3),
          g3e42 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 2, 3),
          g3e43 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 3, 3),
          g3e44 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 4, 3),
          g3e45 = tp.get_event_by_group(tp.get_training_initial(init, 2*4, tp.weekly_increment), 5, 3),
          g3e50 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 0, 3),
          g3e51 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 1, 3),
          g3e52 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 2, 3),
          g3e53 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 3, 3),
          g3e54 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 4, 3),
          g3e55 = tp.get_event_by_group(tp.get_training_initial(init, 2*5, tp.weekly_increment), 5, 3),
        ))
      out += tplt

  with open('out/large.html', 'w') as f_tplt_o:
    f_tplt_o.write(out)

def main():

  #
  # Generate a single week html starting at the given date
  #
  start_date = '19.10.2020'

  offset = tp.start_date_to_offset(start_date)
  ini = tp.get_training_initial(initial, offset, tp.weekly_increment)
  gen_html_week(ini, offset)
  gen_html_large(ini, offset)


if __name__ == '__main__':
  main()