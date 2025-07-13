def get_logo():
    import platform

    arch_logo = r"""                     
                  -`                     
                 .o+`                    
                `ooo/                    
               `+oooo:                   
              `+oooooo:                  
              -+oooooo+:                 
            `/:-:++oooo+:                
           `/++++/+++++++:               
          `/++++++++++++++:              
         `/+++ooooooooooooo/`            
        ./ooosssso++osssssso+`           
       .oossssso-````/ossssss+`          
      -osssssso.      :ssssssso.         
     :osssssss/        osssso+++.        
    /ossssssss/        +ssssooo/-        
  `/ossssso+/:-        -:/+osssso+-      
 `+sso+:-`                 `.-/+oso:     
`++:.                           `-/+/    
.`                                 `/    """

    debian_logo = r"""
       _,met$$$$$gg.
    ,g$$$$$$$$$$$$$$$P.
  ,g$$P\"     \"\"\"Y$$.".
 ,$$P'              `$$$.
',$$P       ,ggs.     `$$b:
`d$$'     ,$P\"'   .    $$$
 $$P      d$'     ,    $$P
 $$:      $$.   -    ,d$$'
 $$;      Y$b._   _,d$P'
 Y$$.    `.`\"Y$$$$P\"'
 `$$b      \"-.__
  `Y$$
   `Y$$.
     `$$b.
       `Y$$b.
          `\"Y$b._
              `\"\"\"\" """

    ubuntu_logo = r"""
            .-/+oossssoo+/-.
        `:+ssssssssssssssssss+:`
      -+ssssssssssssssssssyyssss+-
    .ossssssssssssssssss/    /ssssso.
   /sssssssssssssssss/      /ssssssss/
  +sssssssssssssss/        /ssssssssss+
 /ssssssssssssss/         /sssssssssssss
.ssssssssssssss+         +sssssssssssssss.
+ssssssssssssss/        /ssssssssssssssss+
ssssssssssssssss+/:  -/sssssssssssssssssss
ssssssssssssssssssssssssssssssssssssssssss
+ssssssssssssssssssssssssssssssssssssssss+
.ssssssssssssssssssssssssssssssssssssssss.
 /ssssssssssssssssssssssssssssssssssssss/
  +sssssssssssssssssssssssssssssssssss+
   /sssssssssssssssssssssssssssssssss/
    .ossssssssssssssssssssssssssssso.
      -+sssssssssssssssssssssssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-."""

    mint_logo = r"""
 MMMMMMMMMMMMMMMMMMMMMMMMMmds+.
 MMm----::-://////////////oymNMd+`
 MMd      /++                -sNMd:
 MMNso/`  dMM    `.::-. .-::.`/NMd
 ddddMMh  dMM   :hNMNMNhNMNMNh: `NMm
     NMm  dMM  .NMN/-+MMM+-/NMN` dMM
     NMm  dMM  -MMm  `MMM   dMM. dMM
     NMm  dMM  -MMm  `MMM   dMM. dMM
     NMm  dMM  .mmd  `mmm   yMM. dMM
     NMm  dMM`  ..`   ...   ydm. dMM
     hMM- +MMd/-------...-:sdds  dMM
     -NMm- :hNMNNNmdddddddddy/`  dMM
      -dMNs-``-::::-------.``    dMM
       `/dMNmy+/:-------------:/yMMM
          ./ydNMMMMMMMMMMMMMMMMMMMMM
             .MMMMMMMMMMMMMMMMMMM"""

    mac_logo = r"""
                    'c.
                 ,xNMM.
               .OMMMMo
               OMMM0,
     .;loddo:' loolloddol;.
   cKMMMMMMMMMMNWMMMMMMMMMM0:
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.
 XMMMMMMMMMMMMMMMMMMMMMMMX.
;MMMMMMMMMMMMMMMMMMMMMMMM:
:MMMMMMMMMMMMMMMMMMMMMMMM:
.MMMMMMMMMMMMMMMMMMMMMMMMX.
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.
    kMMMMMMMMMMMMMMMMMMMMMMd
     ;KMMMMMMMWXXWMMMMMMMk.
       .cooc,.    .,coo:."""

    windows_logo = r"""                                   
                                ..,
                    ....,,:;+ccllll
      ...,,+:;  cllllllllllllllllll
,cclllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
                                    
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
`'ccllllllllll  lllllllllllllllllll
       `' \*::  :ccllllllllllllllll
                       ````''*::cll"""

    fedora_logo = r"""
          /:-------------:\          
       :-------------------::       
     :-----------/shhOHbmp---:\     
   /-----------omMMMNNNMMD  ---:   
  :-----------sMMMMNMNMP.    ---:  
 :-----------:MMMdP-------    ---\
,------------:MMMd--------    ---:
:------------:MMMd-------    .---:
:----    oNMMMMMMMMMNho     .----:
:--     .+shhhMMMmhhy++   .------/
:-    -------:MMMd--------------:
:-   --------/MMMd-------------;
:-    ------/hMMMy------------:
:-- :dMNdhhdNMMNo------------;
:---:sdNMMMMNds:------------:
:------:://:-------------::
:---------------------://"""

    redhat_logo = r"""                                   .
           .MMM..:MMMMMMM                   
          MMMMMMMMMMMMMMMM                  
          MMMMMMMMMMMMMMMMMM.              
         MMMMMMMMMMMMMMMMMMMM              
        ,MMMMMMMMMMMMMMMMMMMM:             
        MMMMMMMMMMMMMMMMMMMMMM             
  .MMMM'  MMMMMMMMMMMMMMMMMMMM            
 MMMMMM    `MMMMMMMMMMMMMMMMMM.             
MMMMMMMM      MMMMMMMMMMMMMMMM .          
MMMMMMMMM.       `MMMMMMMMMMM' MM.        
MMMMMMMMMMM.                     MM        
`MMMMMMMMMMMMM.                 MM'           
 `MMMMMMMMMMMMMMMMM.           MM'         
    MMMMMMMMMMMMMMMMMMMMMMMMMM'           
      MMMMMMMMMMMMMMMMMMMMM'              
         MMMMMMMMMMMMMMMM'                     
            `MMMMMMMM'                 
                                        """

    manjaro_logo = r"""
██████████████████  ████████
██████████████████  ████████
██████████████████  ████████
██████████████████  ████████
████████            ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████"""

    os_name = platform.system().lower()
    if os_name == "linux":
        try:
            with open("/etc/os-release") as f:
                os_release = f.read().lower()
                if "arch" in os_release:
                    return arch_logo
                elif "debian" in os_release:
                    return debian_logo
                elif "ubuntu" in os_release:
                    return ubuntu_logo
                elif "mint" in os_release:
                    return mint_logo
                elif "fedora" in os_release:
                    return fedora_logo
                elif "red hat" in os_release:
                    return redhat_logo
                elif "manjaro" in os_release:
                    return manjaro_logo
                else:
                    return arch_logo  # Default to Arch logo
        except:
            return arch_logo
    elif os_name == "darwin":
        return mac_logo
    elif os_name == "windows":
        return windows_logo
