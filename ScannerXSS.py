#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, re, sys
from os import path
from concurrent.futures import ThreadPoolExecutor

class Scanner:
    def __init__(self,File,Payload):
        self.File = File
        self.Agent = {"User-Agent":"Aporlorxl23/XSScanner"}
        self.Payload = Payload
    def Parser(self,Url):
        Url = Url
        Params = re.findall("(\?|\&)([^=]+)\=([^&]+)", Url)
        Index = Url.index(Params[0][0])
        MainUrl = Url[:Index+1]
        AllParams=""
        for Param in Params:
            Param = Param[1]+"="+self.Payload+"&"
            AllParams += Param
        return MainUrl+AllParams[:len(AllParams)-1]    
    def CheckFile(self):
        if path.isfile(self.File):
            pass
        else:
            print("[-] File Not Found !")
            self.Thanks()
    def Thanks(self):
        print("[+] Thanks for use Eren Şimşek <Aporlorxl23>")
        exit(0)
    def Scan(self):
        self.CheckFile()
        File = open(self.File,"r")
        for Url in File:
            Url = Url.strip("\n")
            Url = self.Parser(Url)
            Resp = requests.get(Url,headers=self.Agent)
            if self.Payload in str(Resp.content):
                print("[+] XSS Found",Url)
        File.close()
        self.Thanks()
if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        Start = Scanner(sys.argv[1],sys.argv[2])
        with ThreadPoolExecutor(max_workers=25) as executor:
            future = executor.submit(Start.Scan)
    else:
        print("[+] Usage=> python3 Apor.py Urls.txt '\"><svg/onload=alert(1)>'")
        print("[+] Thanks for use Eren Şimşek <Aporlorxl23>")
        exit(0)
