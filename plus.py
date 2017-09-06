#example
from classes import *
u = destruction_operator('q1')*destruction_operator('q2')*(destruction_operator('p')+creation_operator('p'))**2*creation_operator('q3')*creation_operator('q4')
res = run(u)
print(res)
res = '''[['delta(q1,p)', 'delta(q2,q3)', 'delta(p,q4)'], ['delta(q1,p)', 'delta(p,q3)', 'delta(q2,q4)'], ['delta(q2,p)', 'delta(q1,q3)', 'delta(p,q4)'], ['delta(p,p)', 'delta(q1,q3)', 'delta(q2,q4)'], ['delta(q2,p)', 'delta(p,q3)', 'delta(q1,q4)'], ['delta(p,p)', 'delta(q2,q3)', 'delta(q1,q4)'], ['delta(q1,p)', 'delta(q2,q3)', 'delta(p,q4)'], ['delta(q1,p)', 'delta(p,q3)', 'delta(q2,q4)'], ['delta(q2,p)', 'delta(q1,q3)', 'delta(p,q4)'], ['delta(q2,p)', 'delta(p,q3)', 'delta(q1,q4)']]'''
res = run(destruction_operator('q1'))
print(res)
res = '''[[0]]'''
