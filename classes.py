''' The module supports work with birth and destruction operators.
Separation by sign + - occurs by means of separation into elements of the matrix.
The result of multiplication is a nested list.

{}'''.format(open('plus.py').read())

import itertools
class delta:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def res(self):
        if self.x.n==self.y.n:
            return self.x.coefficient
        else:
            return 0

class state:
    def __init__(self,n):
        self.n = n
        self.coefficient = 1
    def __rmul__(self,i):
        if i.__class__.__name__ == 'state':
            return delta(self.n,i.n)
    def __mul__(self,i):
        if i.__class__.__name__ == 'state':
            return delta(self,i)
        elif i.__class__.__name__ == 'destruction_operator_mq':
            self.coefficient*=(self.n)**.5
            self.n+=1
            return self
        elif i.__class__.__name__ == 'creation_operator_mq':
            self.coefficient*=(self.n-1)**.5
            self.n-=1
            return self

class creation_operator_mq:
    def __init__(self):
        pass
    def __rmul__(self,i):
        if i.__class__.__name__ == 'state':
            i.n+=1
            return i

class destruction_operator_mq:
    def __init__(self):
        pass
    def __rmul__(self,i):
        if i.__class__.__name__ == 'state':
            i.n-=1
            return i

class delta:
    def __inin__(self,a,b):
        self.a = a
        self.b = b
    def res(self):
        return True if a.imp == b.imp else False

class state_zero:
    def __init__(self,st=[0], isym = 0):
        self.st = st
        self.internal_symmetry = isym
    def __mul__(self,i):
        if i.__class__.__name__ in ['creation_operator','creation_operator_anti']:
            return 0
        elif i.__class__.__name__ in ['destruction_operator','destruction_operator_anti']:
            return 1
        elif i.__class__.__name__ == 'state_zero':
            return 1
        elif i==0:
            return 0
        elif i==1:
            return 1
    def __rmul__(self,i):
        if i.__class__.__name__ == 'state_zero':
            return 1
        elif i==0:
            return 0
        elif i==1:
            return 1
    def __add__(self,i):
        return [self,i]
    def __radd__(self,i):
        return [i,self]
            

class strang:
    """A helper class for working with birth and destruction operators."""
    def __init__(self,*l):
        self.l = [*l]
    def __pow__(self,pows):
        res = []
        u = []
        for i in self.l: 
            for j in range(len(i)):
                u.append(i[j])
            res.append(u)
        res = [itertools.product(u,repeat = pows) for i in range(len(u))]
        res = list(res[0])
        for i in range(len(res)):
            res[i]=[j for j in res[i]]
        self.l = res
        return self
    def __mul__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            for j in range(len(self.l)):
                if type(self.l[j])==list:
                    self.l[j].append(i)
            return self
        elif i.__class__.__name__ == 'strang':
            self.l = [op1+op2 for op1 in self.l for op2 in i.l]
            return self
                     
    def __add__(self,i):
        self.l.append([i])
        return self
        

class creation_operator:
    """The birth operator. The basic structural unit. It supports multiplication, addition, exponentiation."""
    def __init__(self,imp,isym=0,spin = 0, mark = 1):
        self.imp = imp
        self.internal_symmetry = isym
        self.spin = spin
        self.mark = mark
    def __mul__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            return strang([self,i])
        elif i.__class__.__name__ == 'strang':
            for j in range(len(i.l)):
                if type(i.l[j])==list:
                    i.l[j].insert(0,self)
            return i
        elif i.__class__.__name__ == 'state_zero':
            return 1
        elif i==0:
            return 0
        elif i==1:
            return 1
    def __rmul__(self,i):
        if i==0:
            return 0
        elif i==1:
            return 1
    def __sub__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            i.mark*=-1
            return strang([self,i])
        elif i.__class__.__name__ == 'strang':
            for j in i.l:
                for j1 in j:
                    j.mark*=-1
            i.l.insert(0,[self])
            return i 
    def __add__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            return strang([self],[i])
        elif i.__class__.__name__ == 'strang':
            i.l.insert(0,[self])
            return i
    def __pow__(self,pows):
        return strang([self for i in range(pows)])
    
        
class destruction_operator(creation_operator):
    """The birth operator. The basic structural unit. It supports multiplication, addition, exponentiation."""
    def __mul__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            return strang([self,i])
        elif i.__class__.__name__ == 'strang':
            for j in range(len(i.l)):
                if type(i.l[j])==list:
                    i.l[j].insert(0,self)
            return i
        elif i.__class__.__name__ == 'state_zero':
            return 0
        elif i==0:
            return 0
        elif i==1:
            return 1
    def __rmul__(self,i):
        if i==0:
            return 0
        elif i==1:
            return 1

class creation_operator_anti(creation_operator):
    """The birth operator. The basic structural unit. It supports multiplication, addition, exponentiation."""
    def __mul__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            return strang([self,i])
        elif i.__class__.__name__ == 'strang':
            for j in range(len(i.l)):
                if type(i.l[j])==list:
                    i.l[j].insert(0,self)
            return i
        elif i.__class__.__name__ == 'state_zero':
            return 1
        elif i==0:
            return 0
        elif i==1:
            return 1
    def __rmul__(self,i):
        if i==0:
            return 0
        elif i==1:
            return 1
        
class destruction_operator_anti(creation_operator):
    """The birth operator. The basic structural unit. It supports multiplication, addition, exponentiation."""
    def __mul__(self,i):
        if i.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
            return strang([self,i])
        elif i.__class__.__name__ == 'strang':
            for j in range(len(i.l)):
                if type(i.l[j])==list:
                    i.l[j].insert(0,self)
            return i
        elif i.__class__.__name__ == 'state_zero':
            return 0
        elif i==0:
            return 0
        elif i==1:
            return 1
    def __rmul__(self,i):
        if i==0:
            return 0
        elif i==1:
            return 1
    
def commutation(dict_state):
    '''The function is build a list of the commutations of creation operators and destruction operators. It return nothing.'''
    import copy
    for i in range(len(dict_state.l)):
        for j in range(len(dict_state.l[i])-1):
            if dict_state.l[i][j].__class__.__name__ in ['creation_operator','creation_operator_anti']:
                pass
            elif dict_state.l[i][j].__class__.__name__=='destruction_operator' and dict_state.l[i][j+1].__class__.__name__ in ['destruction_operator','destruction_operator_anti','creation_operator_anti']:
                j_p = copy.deepcopy(dict_state.l[i][j+1])
                j_ = copy.deepcopy(dict_state.l[i][j])
                dict_state.l[i][j] = j_p
                dict_state.l[i][j+1] = j_
                if dict_state.l[i][j].spin%2==1:
                    dict_state.l[i][j].mark*=-1
            elif dict_state.l[i][j].__class__.__name__=='destruction_operator_anti' and dict_state.l[i][j+1].__class__.__name__ in ['destruction_operator','destruction_operator_anti','creation_operator']:
                j_p = copy.deepcopy(dict_state.l[i][j+1])
                j_ = copy.deepcopy(dict_state.l[i][j])
                dict_state.l[i][j] = j_p
                dict_state.l[i][j+1] = j_
                if dict_state.l[i][j].spin%2==1:
                    dict_state.l[i][j].mark*=-1
            elif dict_state.l[i][j].__class__.__name__=='destruction_operator' and dict_state.l[i][j+1].__class__.__name__=='creation_operator' and dict_state.l[i][j].internal_symmetry==dict_state.l[i][j+1].internal_symmetry:
                dict_state.l.append(dict_state.l[i][:j]+['delta({},{})'.format(dict_state.l[i][j].imp,dict_state.l[i][j+1].imp)]+dict_state.l[i][j+2:])
                j_p = copy.deepcopy(dict_state.l[i][j+1])
                j_ = copy.deepcopy(dict_state.l[i][j])
                dict_state.l[i][j] = j_p
                dict_state.l[i][j+1] = j_
                if dict_state.l[i][j].spin%2==1:
                    dict_state.l[i][j].mark*=-1
            elif dict_state.l[i][j].__class__.__name__=='destruction_operator_anti' and dict_state.l[i][j+1].__class__.__name__=='creation_operator_anti' and dict_state.l[i][j].internal_symmetry==dict_state.l[i][j+1].internal_symmetry:
                dict_state.l.append(dict_state.l[i][:j]+['delta({},{})'.format(dict_state.l[i][j].imp,dict_state.l[i][j+1].imp)]+dict_state.l[i][j+2:])
                j_p = copy.deepcopy(dict_state.l[i][j+1])
                j_ = copy.deepcopy(dict_state.l[i][j])
                dict_state.l[i][j] = j_p
                dict_state.l[i][j+1] = j_
                if dict_state.l[i][j].spin%2==1:
                    dict_state.l[i][j].mark*=-1
            elif dict_state.l[i][j].__class__.__name__=='destruction_operator_anti' and dict_state.l[i][j+1].__class__.__name__=='str':
                j_p = copy.deepcopy(dict_state.l[i][j+1])
                j_ = copy.deepcopy(dict_state.l[i][j])
                dict_state.l[i][j] = j_p
                dict_state.l[i][j+1] = j_
            elif dict_state.l[i][j].__class__.__name__=='destruction_operator' and dict_state.l[i][j+1].__class__.__name__=='str':
                j_p = copy.deepcopy(dict_state.l[i][j+1])
                j_ = copy.deepcopy(dict_state.l[i][j])
                dict_state.l[i][j] = j_p
                dict_state.l[i][j+1] = j_


def multiplication(dict_state):
    '''The function multiplies mutated operators'''
    for i in range(len(dict_state.l)):
        stt_z = state_zero()
        for j in dict_state.l[i]:
            if not j.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
                stt_z = stt_z
            else:
                stt_z = stt_z*j
        stt_z=state_zero()*stt_z
        if stt_z==0:
            dict_state.l[i]=0
    res = []
    for i in dict_state.l:
        if i!=0:
            res.append(i)
    dict_state.l = res
    for i in range(len(dict_state.l)):
        stt_z = state_zero()
        for j in dict_state.l[i][::-1]:
            if not j.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
                stt_z = stt_z
            else:
                stt_z = j*stt_z
        stt_z*=state_zero()
        if stt_z==0:
            dict_state.l[i]=0
    res = []
    for i in dict_state.l:
        if i!=0:
            res.append(i)
    dict_state.l = res

def run(dict_state):
    '''Starts the main process. The input is a product of operators or one operator. The function returns a list of delta functions.'''
    if dict_state.__class__.__name__ != 'strang':
        return [[0]]
    while True:
        commutation(dict_state)
        multiplication(dict_state)
        br = 0
        for i in dict_state.l:
            for j in i:
                if j.__class__.__name__ in ['destruction_operator','creation_operator','creation_operator_anti','destruction_operator_anti']:
                    br = 1
        if br==0:
            break
    return dict_state.l
     
if __name__=='__main__':
    pass
    
