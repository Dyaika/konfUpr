import zipfile
import sys
def check(filelist, fulldir):
    if fulldir not in filelist:
        print('cat: ' + fulldir +': no such file or directory')
        return False
    else:
        return True
    
def do_pwd(filelist, curdir):
    if curdir == '':
        print('/root')
    else:
        print('/root/' + curdir[0:-1])
    
def do_ls(filelist, curdir):
    for path in filelist:
        if path.find(curdir) != -1:
            subpath = path[len(curdir): : ]
            sl_count = subpath.count('/')
            if (sl_count == 1 and subpath[-1] == '/') or (sl_count == 0 and subpath != ''):
                if subpath[-1] == '/':
                    subpath = subpath[0:-1]
                print(subpath, end='\t')
    print()
    
def do_cat(filelist, curdir, f_name, z_name):
    index = f_name.rfind('/')
    dir1 = curdir
    if index != -1:
        dir1 = do_cd(filelist, dir1, f_name[0:index+1])
        f_name = f_name[index+1::]
    if check(filelist, dir1+ f_name):
        file = zipfile.ZipFile(z_name).open(dir1+f_name, 'r')
        for line in file.readlines():
            cur_line = str(line.strip())[2:-1]
            print(cur_line)
        
def do_cd(filelist, curdir, arg):
    basedir = curdir;
    if (len(arg) > 0):
        if arg[-1] == '/':
            arg = arg[0:-1]
    else:
        return curdir
    comands = arg.split('/')
    for com in comands:
        if len(com) == 0:
            curdir = curdir
        elif com == '..':
            index = curdir[0:-1].rfind('/')
            if index == -1:
                curdir = ''
            else:
                curdir = curdir[0:index]
        elif com == '/root' or com == '~':
            curdir = ''
        elif curdir + com + '/' in filelist:
            curdir += com + '/'
        elif com + '/' in filelist:
            curdir = com + '/'
        else:
            print('vs: cd: ' + arg +': no such direictory')
            return basedir
    #print(curdir)
    return curdir


args = sys.argv
if len(args) != 2:
    print('No file system')
    exit()
print('Welcome to vshell')
comand = ''
#all possible paths in array
filelist = zipfile.ZipFile(args[1], 'r').namelist()
curdir = ''
while comand != 'exit':
    print('[root@localhost ', end = '')
    if curdir == '':
        print('~]', end = '# ')
    else:
        print(curdir[('/' + curdir[0: -1]).rfind('/'): -1] + ']', end = '# ')
    comand = input()
    comar = comand.split()
    if comar[0] == 'pwd':
        if len(comar) == 1:
            do_pwd(filelist, curdir)
        else:
            print('pwd should have 0 arguments')
    elif comar[0] == 'ls':
        if len(comar) == 1:
            do_ls(filelist, curdir)
        else:
            print('ls should have 0 arguments')
    elif comar[0] == 'cat':
        if len(comar) == 2:
            do_cat(filelist, curdir, comar[1], args[1])
        else:
            print('cat should have 1 argument')
    elif comar[0] == 'cd':
        if len(comar) == 2:
            curdir = do_cd(filelist, curdir, comar[1])
        else:
            print('cd should have 1 argument')
    elif comar[0] == 'exit':
        break
    else:
        print('vs: ' + comar[0] + ': command not found')
print('goodbye')
