def zřícenina():
    print("\nStojíš před zříceninou dávno zapomenuté pevnosti. Cítíš se sledovaný")
    volba = input("Povšiml jsi si škvíry vedoucí mezi spadenými pilíři. Pokusíš se dostat skrz? (1 = Pokusit se proniknout, 2 = Obhlédnout okolí říceniny): ")
    if volba == "1":
        if random.randint(1, 2) == 1:
            print("Opatrně jsi se prosápal skrze pilíře. Cesta pokračuje níže do podzemí.")
            return 2
        else:
            print("Nemotorně jsi se prodásal skrze pilíře a ostrý kámen tě říznul..au - 1 bod. Cesta pokračuje níže do podzemí.")
        else:
            print("Tvá cesta tě zavedla ke kamennému zdivu, nejspíše součástí starého pevnostního sklepení.  ")
        volba = input("Tvé oči se zaměřili na nález zchátralých kovových dveří. Zkusil jsi je otevřít ale samozřejmě tak jednoduché to být nemůže..je potřeba na to jít chytreji. (1 = Zkusit alternativy 2 = Nejít na to chytreji): ")
        if volba == "1": 
            if random.randint(1, 2) == 1:
                print("Po bližším prohlédnutí si povšimneš díry ve vrchní části zdiva a konvenčně vystoupaných cihel vedoucí k ní. Bezproblému jsi  ")
                return 2
            else:
                print("Po bližším prohlédnutí dveří si povšimneš že vlastně stačí táhnout od sebe a ne k sobě..nakonec to tak jednoduché bylo.")
            else:
                print("")
            
        if volba == "2":
            if random.randint(1, 2) == 1:
                print("Nějáký kus zrezlýho šrotu tě přece nezastaví, od dveří odstoupíš a začneš do nich sypat kombinaci kopů, bušení a nadávek. \nPři tvém nejvíce odhodlanému útoku se kamenný rám dveří poddal tvé agresi a dveře se vyrvali i se zdivem okolo. Získáváš +1 bod za tvrdohlavost ")
                return 2
            else:
                print("Nějáký kus zrezlýho šrotu tě přece nezastaví, od dveří odstoupíš a začneš do nich sypat kombinaci kopů, bušení a nadávek. \nPo nějáké době vynaložení nadměrné frustrace dveře stále stojí, uznáváš svou prohru a od dveří opouštíš ale mezitím co přemýšlíš jak se dostat zpátky na povrch mírný průvan nedobytné dveře pomalu otevře směrem k tobě...tahal jsi na špoutnou stranu. Snad to nikdo neviděl...")
        
    if volba == "2":
        volba = input("Po okroužení místa jsi si povšimnul ohniště, dle stále doutnajícího dříví dedukuješ že někdo v nedávné době v okolí. \nV černočerných ostatcích spáleného dříví vidíš nerozpoznatelný objekt. Chceš se pokusit sebrat záhadný předmět? (1 = Vzít možnou kořist 2 = Zavrhnout své temptace): ")
            if random.randint(1, 2) == 1:
                print("S vidinou možné hodnoty a pomocí ohořelého dřeva opatrně vytáhneš popelem osypený objekt, ")
            else: 
                print("")
                

            
    else: 
        return -1