with open('inputs/2015/day23.txt') as file:
    cmds = [x.split() for x in file.read().replace(',','').split('\n')]


class Register:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def run(self, cmds):
        i = 0
        while i < len(cmds):
            cmd = cmds[i]
            if cmd[0] == 'hlf':
                old = getattr(self,cmd[1])
                setattr(self, cmd[1], old/2)
                i+=1

            elif cmd[0] == 'tpl':
                old = getattr(self,cmd[1])
                setattr(self, cmd[1], old*3)
                i+=1

            elif cmd[0] == 'inc':
                old = getattr(self,cmd[1])
                setattr(self, cmd[1], old+1)
                i+=1

            elif cmd[0] == 'jmp':
                i = i + int(cmd[1])

            elif cmd[0] == 'jie':
                old = getattr(self,cmd[1])
                if old%2 == 0:
                    i = i + int(cmd[2])
                else:
                    i+=1
            elif cmd[0] == 'jio':
                old = getattr(self,cmd[1])
                if old == 1:
                    i = i + int(cmd[2])
                else:
                    i+=1
        print(i,self.b)

reg = Register(0,0)
reg.run(cmds)

reg = Register(1,0)
reg.run(cmds)