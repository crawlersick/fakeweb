from subprocess import Popen, PIPE
def enc(tempstr):
    p1 = Popen("./callenc.sh " + "'" + tempstr + "'",shell=True, stdout=PIPE).stdout.read()
    rs=str(p1,'utf-8')
    return rs.strip()
def dec(tempstr):
    p1 = Popen("./calldec.sh " + "'" + tempstr + "'",shell=True, stdout=PIPE).stdout.read()
    rs=str(p1,'utf-8')
    return rs.strip()


if __name__ == "__main__":
    t1=enc('http://asdlkfj.asdfkj.com')
    t2=dec(t1)
    print(t1)
    print(t2)
