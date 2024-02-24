print('''
                                        .:::::::::.
                                    .::::::::::::::::,       .::
                                  -'`;. ccccr -ccc,```'::,:::::::
                                     `,z$$$$$$c $$$F.::::::::::::
                                      'c`$'cc,?$$$$ :::::`:. ``':
                                      $$$`4$$$,$$$$ :::',   `
                                ..    F  .`$   $$"$L,`,d$c$
                               d$$$$$cc,,d$c,ccP'J$$$$,,`"$F
                               $$$$$$$$$$$$$$$$$$$$$$$$$",$F
                               $$$$$$$$$$$ ccc,,"?$$$$$$c$$F
                               `?$$$PFF",zd$P??$$$c?$$$$$$$F
                              .,cccc=,z$$$$$b$ c$$$ $$$$$$$
                           cd$$$F",c$$$$$$$$P'<$$$$ $$$$$$$
                           $$$$$$$c,"?????""  $$$$$ $$$$$$F
                       ::  $$$$L ""??"    .. d$$$$$ $$$$$P'..
                       ::: ?$$$$J$$cc,,,,,,c$$$$$$PJ$P".::::
                  .,,,. `:: $$$$$$$$$$$$$$$$$$$$$P".::::::'
        ,,ccc$$$$$$$$$P" `::`$$$$$$$$$$$$$$$$P".::::::::' c$c.
  .,cd$$PPFFF????????" .$$$$$b,
z$$$$$$$$$$$$$$$$$$$$bc.`'!>` -:.""?$$P".:::'``. `',<'` $$$$$$$$$c
$$$$$$$$$$$$$$$$$$$$$$$$$c,=$$ :::::  -`',;;!!!,,;!!>. J$$$$$$$$$$b,
?$$$$$$$$$$$$$$$$$$$$$$$$$$$cc,,,.` ."?$$$$$$$$$$$$$$$$$$.
     ""??"""   ;!!!.$$$ `?$$$$$$P'!!!!;     !!;.""?$$$$$$$$$$$$$$$r
               !!!'<$$$ :::..  .;!!!!!!;   !!!!!!!!!!!!!>  "?$$$$$$$$$$$"
              !!!!>`?$F::::::::`!!!!!!!!! ?"
                  `!!!!>`::::: :: 
               `    `!!! `:::: ,, ;!!!!!!!!!'`    ;!!!!!!!!!!!
                \;;;;!!!! :::: !!!!!!!!!!!       ;!!!!!!!!!!!!>
                `!!!!!!!!> ::: !!!!!!!!!!!      ;!!!!!!!!!!!!!!>
                 !!!!!!!!!!.` !!!!!!!!!!!!!;. ;!!!!!!!!!!!!!!!!>
                  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                  `!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                   `!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    `
                       ?$$c``!!! d $$c,c$.`!',d$$$P
                           `$$$$$c,,d$ 3$$$$$$cc$$$$$$F
                            `$$$$$$$$$b`$$$$$$$$$$$$$$
                             `$$$$$$$$$ ?$$$$$$$$$$$$$
                              `$$$$$$$$$ $$$$$$$$$$$$F
                               `$$$$$$$$,?$$$$$$$$$$$'
                                `$$$$$$$$ $$$$$$$$$$P
                                  ?$$$$$$b`$$$$$$$$$F
                                ,c$$$$$$$$c`$$"$$$$$$$cc,
                            ,z$$$$$$$$$$$$$ $L')$$$$$$$$$$b,,,,, ,
                       ,,-=P???$$$$$$$$$$PF $$$$$$$$$$$$$Lz =zr4%'
                      `?'d$ $b = $$$$$$           "???????$$$P
                         `"-"$$$$P""""                     "
                    '''     )

print("**Welcome to Treasure Island.**")
print("Your mission is to find the treasure.")


choice1 = input("'You're at a cross road. Where do you want to go? Type left or right \n").lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You won")
        elif choice3 == "blue":
            print("You enter room full of hungry lions! Game Over")
        else:
            print("Door not exist! Game over!")
    else:
        print("Bad Luck! Game over")
else:
    print('You fell into a hole, Game Over.\n')
