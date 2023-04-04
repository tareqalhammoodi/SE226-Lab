#SE226 – LAB#4
import random
words = ["a","ability","able","about","above","accept","according","account","across","act","action","activity","actually","add","address","administration","admit","adult","affect","after","again","against","age","agency",
         "agent","ago","agree","agreement","ahead","air","all","allow","almost","alone","along","already","also","although","always","American","among","amount","analysis","and","animal","another","answer","any","anyone",
         "anything","appear","apply","approach","area","argue","arm","around","arrive","art","article","artist","as","ask","assume","at","attack","attention","attorney","audience","author","authority","available","avoid",
         "away","baby","back","bad","bag","ball","bank","bar","base","be","beat","beautiful","because","become","bed","before","begin","behavior","behind","believe","benefit","best","better","between","beyond","big","bill",
         "billion","bit","black","blood","blue","board","body","book","born","both","box","boy","break","bring","brother","budget","build","building","business","but","buy","by","call","camera","campaign","can","cancer",
         "candidate","capital","car","card","care","career","carry","case","catch","cause","cell","center","central","century","certain","certainly","chair","challenge","chance","change","character","charge","check","child",
         "choice","choose","church","citizen","city","civil","claim","class","clear","clearly","close","coach","cold","collection","college","color","come","commercial","common","community","company","compare","computer",
         "concern","condition","conference","Congress","consider","consumer","contain","continue","control","cost","could","country","couple","course","court","cover","create","crime","cultural","culture","cup","current",
         "customer","cut","dark","data","daughter","day","dead","deal","death","debate","decade","decide","decision","deep","defense","degree","Democrat","democratic","describe","design","despite","detail","determine",
         "develop","development","die","difference","different","difficult","dinner","direction","director","discover","discuss","discussion","disease","do","doctor","dog","door","down","draw","dream","drive","drop",
         "drug","during","each","early","east","easy","eat","economic","economy","edge","education","effect","effort","eight","either","election","else","employee","end","energy","enjoy","enough","enter","entire",
         "environment","environmental","especially","establish","even","evening","event","ever","every","everybody","everyone","everything","evidence","exactly","example","executive","exist","expect","experience",
         "expert","explain","eye","face","fact","factor","fail","fall","family","far","fast","father","fear","federal","feel","feeling","few","field","fight","figure","fill","film","final","finally","financial","find",
         "fine","finger","finish","fire","firm","first","fish","five","floor","fly","focus","follow","food","foot","for","force","foreign","forget","form","former","forward","four","free","friend","from","front","full",
         "fund","future","game","garden","gas","general","generation","get","girl","give","glass","go","goal","good","government","great","green","ground","group","grow","growth","guess","gun","guy","hair","half","hand",
         "hang","happen","happy","hard","have","he","head","health","hear","heart","heat","heavy","help","her","here","herself","high","him","himself","his","history","hit","hold","home","hope","hospital","hot","hotel",
         "hour","house","how","however","huge","human","hundred","husband","I","idea","identify","if","image","imagine","impact","important","improve","in","include","including","increase","indeed","indicate","individual",
         "industry","information","inside","instead","institution","interest","interesting","international","interview","into","investment","involve","issue","it","item","its","itself","job","join","just","keep","key",
         "kid","kill","kind","kitchen","know","knowledge","land","language","large","last","late","later","laugh","law","lawyer","lay","lead","leader","learn","least","leave","left","leg","legal","less","let","letter",
         "level","lie","life","light","like","likely","line","list","listen","little","live","local","long","look","lose","loss","lot","love","low","machine","magazine","main","maintain","major","majority","make","man",
         "manage","management","manager","many","market","marriage","material","matter","may","maybe","me","mean","measure","media","medical","meet","meeting","member","memory","mention","message","method","middle","might",
         "military","million","mind","minute","miss","mission","model","modern","moment","money","month","more","morning","most","mother","mouth","move","movement","movie","Mr","Mrs","much","music","must","my","myself","name",
         "nation","national","natural","nature","near","nearly","necessary","need","network","never","new","news","newspaper","next","nice","night","no","none","nor","north","not","note","nothing","notice","now","n't","number",
         "occur","of","off","offer","office","officer","official","often","oh","oil","ok","old","on","once","one","only","onto","open","operation","opportunity","option","or","order","organization","other","others","our","out",
         "outside","over","own","owner","page","pain","painting","paper","parent","part","participant","particular","particularly","partner","party","pass","past","patient","pattern","pay","peace","people","per","perform",
         "performance","perhaps","period","person","personal","phone","physical","pick","picture","piece","place","plan","plant","play","player","PM","point","police","policy","political","politics","poor","popular","population",
         "position","positive","possible","power","practice","prepare","present","president","pressure","pretty","prevent","price","private","probably","problem","process","produce","product","production","professional","professor",
         "program","project","property","protect","prove","provide","public","pull","purpose","push","put","quality","question","quickly","quite","race","radio","raise","range","rate","rather","reach","read","ready","real","reality",
         "realize","really","reason","receive","recent","recently","recognize","record","red","reduce","reflect","region","relate","relationship","religious","remain","remember","remove","report","represent","Republican","require",
         "research","resource","respond","response","responsibility","rest","result","return","reveal","rich","right","rise","risk","road","rock","role","room","rule","run","safe","same","save","say","scene","school","science",
         "scientist","score","sea","season","seat","second","section","security","see","seek","seem","sell","send","senior","sense","series","serious","serve","service","set","seven","several","sex","sexual","shake","share","she",
         "shoot","short","shot","should","shoulder","show","side","sign","significant","similar","simple","simply","since","sing","single","sister","sit","site","situation","six","size","skill","skin","small","smile","so","social",
         "society","soldier","some","somebody","someone","something","sometimes","son","song","soon","sort","sound","source","south","southern","space","speak","special","specific","speech","spend","sport","spring","staff","stage",
         "stand","standard","star","start","state","statement","station","stay","step","still","stock","stop","store","story","strategy","street","strong","structure","student","study","stuff","style","subject","success","successful",
         "such","suddenly","suffer","suggest","summer","support","sure","surface","system","table","take","talk","task","tax","teach","teacher","team","technology","television","tell","ten","tend","term","test","than","thank","that",
         "the","their","them","themselves","then","theory","there","these","they","thing","think","third","this","those","though","thought","thousand","threat","three","through","throughout","throw","thus","time","to","today","together",
         "tonight","too","top","total","tough","toward","town","trade","traditional","training","travel","treat","treatment","tree","trial","trip","trouble","true","truth","try","turn","TV","two","type","under","understand","unit","until",
         "up","upon","us","use","usually","value","various","very","victim","view","violence","visit","voice","vote","wait","walk","wall","want","war","watch","water","way","we","weapon","wear","week","weight","well","west","western",
         "what","whatever","when","where","whether","which","while","white","who","whole","whom","whose","why","wide","wife","will","win","wind","window","wish","with","within","without","woman","wonder","word","work","worker","world",
         "worry","would","write","writer","wrong","yard","yeah","year","yes","yet","you","young","your","yourself"]

#Task1
while True:
    # get input from user
    input1 = int(input("Please enter a number (between 1-999 and the first one must be greater than the second one) : "))
    input2 = int(input("Please enter another number (between 1-999) : "))
    # check if the first number is greater than the second number
    if input1 and input2 > 1 or input1 and input2 < 999:
        if input1 > input2:
            print(words[input2 - 1:input1])
            break
        else:
            print("Error: The first number should be greater than the second number.")
    else:
        print("Invalid number, the number should be between 1-999.")

print("-----------------------------------------------------------------------------------------")

#Task2
password = ""
initialPassword = ""
while True:
    user_number = int(input("Please enter a number (between 3 and 7) : "))
    if user_number < 3 or user_number > 7:
        print("Invalid number, the number should be between 3-7.")
    else:
        print("List of random words : ")        # for testing purposes we can delete it         ------------
        for i in range(user_number):
            randomwords = random.choice(words)  # randomly choose words from the words list
            print(randomwords)                  # for testing purposes we can delete it         ------------
            initialPassword += randomwords      # merge these words into one string
        break
password = initialPassword[::-1]                # reverse
print()
print("\033[1mPassword generated by our program from the list :\033[0m")
print(password)                                 # print the final password

print("-----------------------------------------------------------------------------------------")

#Task3
Password = ""
shorter = set()                                     # create short set
longer = set()                                      # create long set
for j in range(8):
    while True:
        print("================ Password number " + str(j+1) + " ===============")
        User_number = int(input("Please enter a number (between 3 and 7) : "))
        if User_number < 3 or User_number > 7:
            print("Invalid number, the number should be between 3-7.")
        else:
            for i in range(User_number):
                Randomwords = random.choice(words)  # randomly choose words from the words list
                Password += Randomwords             # merge these words into one string
            Password = Password[::-1]
            break
    if User_number < 5:
        shorter.add(Password)
    else:
        longer.add(Password)
    Password = ""                                   # to avoid repetition
setsUnion = shorter.union(longer)
print("\033[1mThe union set of all generated passwords : \033[0m", setsUnion)

print("-----------------------------------------------------------------------------------------")

#Task4
#part A
dictionary = {}
for i in range(1, 31):
    value = i * (i-1)                               # calculate the multiplication of the key and its predecessor
    dictionary[i] = value                           # add the key-value pair to the dictionary
print("\033[1mPrint dictionary horizontally : \033[0m")
print(dictionary)

print("-----------------------------------------------------------------------------------------")

#part B
print("\033[1mPrint dictionary vertically : \033[0m")
for key, value in dictionary.items():
    print(f"{key}: {value}")

print("-----------------------------------------------------------------------------------------")

#part C
sumValues = 0
for value in dictionary.values():
    sumValues += value
print("\033[1mThe summation of values : \033[0m", sumValues)

print("-----------------------------------------------------------------------------------------")

#part D
while True:
    Input = int(input("Enter a number to remove from the dictionary: "))
    if Input in dictionary:
        del dictionary[Input]
        print(str(Input) + " removed from the dictionary.")
        print("\033[1mPrint the dictionary after deletion : \033[0m")
        print(dictionary)
        break
    else:
        print("Error : The input is not a key in the dictionary, try another value.")

print("-----------------------------------------------------------------------------------------")

#Task5
#part A
divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}
united_we_stand = {**divided, **we_fall}
def printFunction(dictionaryName):
    print("Printing the dictionary elements :")
    print("Name     Age")
    for key, value in dictionaryName.items():
        print(f"{key:6}   {value}")
printFunction(united_we_stand)

print("-----------------------------------------------------------------------------------------")

#part B
del united_we_stand['Nat']
printFunction(united_we_stand)                      # after deletion

print("-----------------------------------------------------------------------------------------")

#part C
sorted_united_we_stand = dict(sorted(united_we_stand.items()))
printFunction(sorted_united_we_stand)

print("-----------------------------------------------------------------------------------------")

#part D
maxValue = max(united_we_stand.values())
minValue = min(united_we_stand.values())
print("Maximum value : " + str(maxValue))
print("Minimum value : " + str(minValue))

