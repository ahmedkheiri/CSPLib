# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:25:42 2023

@authors: Yaroslav Pylyavskyy (pylyavskyy@hotmail.com) & Ahmed Kheiri (a.o.kheiri@gmail.com)

"""



class Room:
    def __init__(self, name):
        self.__name = name
    def getRoomName(self):
        return str(self.__name)
    def setRoomName(self, name):
        self.__name = name
    def __str__(self):
        return self.__name
    
if __name__ == '__main__':
    r = Room("Room 1")
    print(r.getRoomName())
    r.setRoomName("Room 2")
    print(r)
    