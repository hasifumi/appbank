# -*- coding: utf-8 -*-

from bottle import route, run, debug, template
import sqlite3
from os import path

dirname = path.dirname(path.abspath(__file__))
dirname = dirname.replace('bottle', '')
#print dirname
db_dir = dirname + 'sqlite\\'

@route('/pd/')
@route('/pd/mon/list/')
def pd_mon_list():
    conn = sqlite3.connect(db_dir + 'pdAppbank.db')
    c = conn.cursor()
    #c.execute('select mon_no, name from monster where monster.mon_no = 100')
    #c.execute("""
    sql_exe =  """
      select monster.mon_no,
             monster.name,
             skill.name,
             skill.function
      from monster, skill
      where monster.mon_no <= {upper}
        and monster.skill_no = skill.skill_no
      order by monster.mon_no
    """

      #where monster.mon_no <= 80
    c.execute(sql_exe.format(upper = 50))
    #c.execute(sql_exe)
    #c.execute('select mon_no, name from monster')
    result = c.fetchall()
    #return str(result)
    c.close()
    output = template('make_table', rows= result)
    return output

run(host='0.0.0.0', port=8080, debug=True, reloader=True)

# cur.execute("""
#   create table monster(
#         mon_no integer,
#         name text,
#         skill_no integer,
#         leader_skill_no integer,
#         hp_init integer,
#         hp_max integer,
#         hp_plus integer,
#         attack_init integer,
#         attack_max integer,
#         attack_plus integer,
#         recovery_init integer,
#         recovery_max integer,
#         recovery_plus integer,
#         PRIMARY KEY(mon_no)
#         );
# """)
