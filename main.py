#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:54:32 2019

@author: awangga
"""

import kepo
import qrcode
#import getpass


saya = kepo.Kepo()
print("NPM : ")
NPM=input()
print("Proyek : ")
PROYEK=input()
print("Password SIAP : ")
PASSWORD=input()
print("Kode DOSEN : ")
Pembimbing=input()
print("Progres yang dilaporkan : ")
Bimbingan=input()
print("Nilai : ")
Nilai=input()
print("github.com/userrepo/namarepo/blob/master/namafile.pdf")
print("userrepo : ")
userrepo=input()
print("namarepo : ")
namarepo=input()
print("namafile : ")
namafile=input()
print("pertemuan ke : ")
pertemuan=input()


crot=saya.generateURL(NPM, PASSWORD, PROYEK, Nilai, Bimbingan, Pembimbing,userrepo,namarepo,namafile,pertemuan)
if crot != '':
	img = qrcode.make(crot)
	img.save("./"+NPM+".png")
	print("File QrCode Telah Dibuat")
