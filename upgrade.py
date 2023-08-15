import os,time

print("""
\033[1;31;40m                                                  
                                                  
                                                  
                                                  
                 .................                
            ....:::^^^^:^^:^^^::...:^.            
         .:^?Y^.:^::::::::.:::^~. ^5G7:..         
       .:: :55?..:::~~~::......::.^?7~.~?^:       
     .:~YG!..:^^~^^..............::::.^PB?...     
    :. .?7!::::^~~~~^^:..........:::::^^.: ~::    
   :.:.  ::::::::^^^^~~^::::::::::::::::::5#J^:   
  .^7BP!^:::::::::::..:....:::.::::::::.:^~^~ .:  
  : ~77~:.::::::::::::::.::^^::::::::::..::  . :. 
 :. . .:..:.:::::::^5J^^^^!^:::...........::!G5~: 
 :~5G!^:........:.::?P5?!^~~7^.:~!?~......::^77:: 
 ::?7~::.....:::.:7!^^7Y~^!Y7.^:.:7~......:: :: : 
 :..!.::...:::::.^J:...:^ ^Y~!J...........::~GB7: 
 .^YB5:^.........^J?^...^:~!~~7~..........^ .~^~. 
  :^.^..:..::.....::.....^: .. ..........:::.  :  
   ::7G7^:^^^^^:::::^^::^::^^::::^^^^^^.::!GP!^   
    ^JJ? .^:.........................:::. ^!7~    
     :.:!: .::::......  .........  .:^. .^~..     
      .:::^^ .::::.:::^~!YBBY^:.:::....^!~:.      
        ..:^:^:....:^~7J?JBGY^:.....:^~^:.        
           .::^:^^::.. ....... ^^:^~^:.           
               ..::~^^:^^~^:~^:::..               
                      .                           
                                                  
                                                  
                                                  
                                               
""") 

print("""\33[0;32m[1] UPDATE\n[2] CANCEL\nPLEASE CHOOSE THE OPTION?""")

c = input(">>>: ")
if c == "1":
    os.system("unzip resources.zip")
    print("\033[1;93mWAIT TO OPEN RESOURCES....")
    time.sleep(2)
    os.system("rm -rf resources.zip")
    print("\33[0;32mPROCESSING NOW.....!")
    time.sleep(2)
    os.system("cd resources && mv proxies.txt /$HOME/EXECUTOR-DDOS")
    os.system("cd resources && mv socks.txt /$HOME/EXECUTOR-DDOS")
    os.system("cd resources && mv http.txt /$HOME/EXECUTOR-DDOS")
    os.system("cd resources && mv proxy.txt /$HOME/EXECUTOR-DDOS")
    os.system("cd resources && mv socks5.txt /$HOME/EXECUTOR-DDOS")
    print("\33[0;32mPROCESS TO UPDATE.....!")
    os.system("rm -rf resources")
    time.sleep(2)
    os.system("cd ZxCDDoS && rm -rf proxies.txt")
    os.system("clear")
    os.system("mv proxies.txt /$HOME/EXECUTOR-DDOS/ZxCDDoS")
    print("\33[0;32mbuild proxies C2 success...")
    os.system("cd ZxCDDoS && rm -rf socks.txt")
    time.sleep(0.8)
    os.system("cp socks.txt /$HOME/EXECUTOR-DDOS/ZxCDDoS")
    print("\33[0;32mbuild socks C2 success...")
    os.system("cd DosSkull && rm -rf socks.txt")
    time.sleep(0.8)
    os.system("mv socks.txt /$HOME/EXECUTOR-DDOS/DosSkull")
    print("\33[0;32mbuild socks DDOS SKULL success...")
    os.system("cd HTTP-SENPAI && rm -rf http.txt")
    time.sleep(0.8)
    os.system("cp http.txt /$HOME/EXECUTOR-DDOS/HTTP-SENPAI")
    print("\33[0;32mbuild http SENPAI success...")
    os.system("cd KARMA-DDoS && rm -rf proxy.txt")
    time.sleep(0.8)
    os.system("mv proxy.txt /$HOME/EXECUTOR-DDOS/KARMA-DDoS")
    print("\33[0;32mbuild proxy KARMA success...")
    os.system("cd KARMA-DDoS && cd resources && rm -rf http.txt")
    time.sleep(0.8)
    os.system("mv http.txt /$HOME/EXECUTOR-DDOS/KARMA-DDoS/resources")
    print("\33[0;32mbuild http KARMA success...")
    os.system("cd KARMA-DDoS && cd resources && rm -rf socks5.txt")
    time.sleep(0.8)
    os.system("mv socks5.txt /$HOME/EXECUTOR-DDOS/KARMA-DDoS/resources")
    print("\33[0;32mbuild socks5 KARMA success...")
    time.sleep(0.8)
    print("\033[1;93mSUCCESFULLY TO UPDATE YOUR TOOLS")
    time.sleep(2)
    os.system("rm -rf upgrade.py")

elif c == "2":
    os.system("exit")
if os.name == "nt":
    pass
else:
    os.system("clear")
