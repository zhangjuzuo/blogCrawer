# -*- coding: UTF-8 -*-
import crawer
import re
import global_var
import time
import os
import sys
from threading import Thread

poolnum = 10

def start_craw(start):
    nogi = crawer.Nogizaka()
    pool = []
    dirList = nogi.setDir()
    #嫂子是从201210开始
    idol_url = global_var.url28
    idolname = "matsumura_sayuri"
    for d in range(start,len(dirList)):
        os.makedirs("./{}/{}".format(idolname,  dirList[d]))
        blogdir = idolname+'/'+ dirList[d]
        task = Thread(target=nogi.craw_whole_pages, args=(blogdir, idol_url, dirList[d],))
        task.start()
        pool.append(task)
        if len(pool) == poolnum: 
            crawer.wait_tasks_done(pool)
        print(dirList[d]+' DONE!!!')
        time.sleep(1)

start_craw(int(sys.argv[1]))

