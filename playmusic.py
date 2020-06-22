#!/usr/bin/python3 
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''

import datetime
import sys
import os
import time
import pygame
from pygame import mixer
from pygame.locals import USEREVENT
 
 
STOPEVENT     = USEREVENT + 1 #音乐停止事件
timing_hour   =   9 # 时间
timing_minute = 26 # 分钟
play_long     = 60 * 10  # 播放时长
timing_list   = []
 
 
def play(start):
    paths = os.listdir('.') #当前目录下所有文件
 
    def ismp3(path):
        return path.endswith(".mp3")
    paths = list(filter(ismp3, paths)) #保留mp3文件
 
    if len(paths) > 0:
        cur = 0
        mixer.init()
        pygame.init()

        mixer.music.set_endevent(STOPEVENT) #设置音乐停止事件
        print("play first {} ".format(paths[cur]))   
        mixer.music.load(paths[cur].encode("utf-8")) #加载,支持中文文件名
        mixer.music.play() #播放

        #当超过播放时长后，停止播放
        while (datetime.datetime.now() - start).seconds < play_long:
            time.sleep(1) #1秒监听一次事件
            event = pygame.event.poll()
 
            if event.type == STOPEVENT:
                cur += 1

                if cur != len(paths):
                    print("play next {} ".format(paths[cur]))                        
                    mixer.music.load(paths[cur].encode("utf-8")) #支持中文文件名
                    mixer.music.play()
                else:
                    break;
                    
        print("pygame quit...")            
        pygame.quit()
 

def istiming(now.hour,now.minute,timing_list):
    for timing in timing_list:
        if now.hour == timing[0] and now.minute == timing[1]:
            return True

    return False


 
def detect():
    while True:
        now = datetime.datetime.now()
        if istiming(now.hour , now.minute , timing_list):
            print("begin to play:{}".format(now))
            play(now)
        else:
            print("play settings:{} ; curTime hour:{},minute:{}".format(timing_list,now.hour,now.minute))
            time.sleep(1)
 
 
if __name__ == '__main__':
  if len(sys.argv) >=2 :

    arg_loop = 1
    while arg_loop < len(sys.argv) :
        
        parse_args = sys.argv[arg_loop].split(':')
        timing_list.append((int(parse_args[0]),int(parse_args[1]))

        arg_loop += 1
    
    # begin to loop
    detect()
  else:
    print("Usage:python3 playmusic.py 10:30 ...")