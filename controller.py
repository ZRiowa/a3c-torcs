
#-*- coding:utf-8 -*-
#导入上面的文件
import random,os,time
import subprocess

 
# # test_list=[]  #本教程的目的就是要在多进程下，取代类似这样子的对象
# conn=redis_middle_class.Conn_db()   #创建redis连接对象
 


# def update_redis(buff):
#     global conn
#     buff_x=buff.copy()
#     conn.set('cmd_buff',buff_x)
#     print("update redis with data {} /n ,{}".format(type(buff_x),buff_x))


# def clear_redis():
#     update_redis({})


# def controller():
#     cmd_buff=conn.get("cmd_buff")
#     buff=cmd_buff.copy()
#     for w in buff.keys():
#         port=buff[w]['port']
#         pid=buff[w]['pid']
#         cmd=buff[w]['cmd']

#         if cmd=="start":
#             pid=start_game(port,pid)
#             buff[w]["cmd"]="run"
#             buff[w]['pid']=pid

    


class controller():
    def __init__(self):
        self.cmd_buff={}
        """
        {worker1:[port,pid,cmd],
        worker2:[port,pid,cmd],
        
        }
        
        
        """

    def create(self,worker,port):
        if worker not in  self.cmd_buff:
            self.cmd_buff.update({worker:[port,0,"start"]})
        else:
            self.cmd_buff[worker][2]="start"
            

        self.start_cmd()
        return 
    def start_cmd(self):
        buff=self.cmd_buff
        for w in buff.keys():
            port=buff[w][0]
            pid=buff[w][1]
            cmd=buff[w][2]

            if cmd=="start":
                buff[w][2]="starting"
                self.cmd_buff.update(buff)


                pid=start_game(port,pid)
                buff[w][2]="run"
                buff[w][1]=pid
        self.cmd_buff.update(buff)


def kill(pid):
    ck=os.system("ps -l|grep {}".format(pid))
    while ck==0:
        os.system('sudo kill -9 {}'.format(pid ))
        ck=os.system("ps -l|grep {}".format(pid))


def start_game(port,pid):
    if pid !=0:
        kill(pid)
        print("================"*10)
        print("kill torcs",pid)
    pid=subprocess.Popen(['/usr/local/bin/torcs',  ' -nofuel -nolaptime -p {} &'.format(port) ])
    print("***************************"*10)
    print("start torcs {} port {} ".format(pid ,port))
    time.sleep(2)
    os.system('sh autostart.sh')
    print("***************************sleep start")
    time.sleep(4)
    print("***************************sleep end")
    print(" ")
    print(" ")
    print(" ")
    return pid




if __name__ =="__main__":
    # while True:


    c=controller()
    c.create(2,4)
    time.sleep(1)
