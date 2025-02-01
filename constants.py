CHILDHOOD_STR_ROLL_MAP = [
    "You were picked on. (+1 to STR)",
    "You killed your mother in childbirth. (+1 to STR)",
    "Your siblings ate your food. (+2 to STR)",
    "You never got enough to eat. (+2 to STR)",
    "You followed your mother around. (+3 to STR)",
    "You loved to climb. (+3 to STR)",
    "You got in a lot of fights and lost most. (+4 to STR)",
    "You wrestled your father. (+4 to STR)",
    "You fought a huge dog. (+5 to STR)",
    "You were a fat kid. (+5 to STR)",
    "You got into a lot of of fights and won most. +6",
    "You were a bully. +6"
]

CHILDHOOD_DEX_ROLL_MAP = [
    "You always overslept. (+1 to DEX)",
    "You took a nasty fall. (+1 to DEX)",
    "You broke something precious. (+2 to DEX)",
    "You carried a blanket everywhere. (+2 to DEX)",
    "You were an illegitimate child. (+3 to DEX)",
    "You got caught stealing. (+3 to DEX)",
    "Your father took you with him. (+4 to DEX)",
    "You saw a man commit suicide. (+4 to DEX)",
    "You were once trapped somewhere. (+5 to DEX)",
    "You stole candy. (+5 to DEX)",
    "You ran for your life. (+6 to DEX)",
    "You killed an animal. (+6 to DEX)"
]

CHILDHOOD_CON_ROLL_MAP = [
    "You almost died from a fever. (+1 to CON)",
    "You preferred to stay indoors. (+1 to CON)",
    "You broke an arm. (+2 to CON)",
    "Your family is a small one. (+2 to CON)",
    "You had an awkward puberty. (+3 to CON)",
    "You learned to cook from your mom. (+3 to CON)",
    "You remember when you became an orphan. (+4 to CON)",
    "You know your family's secret. (+4 to CON)",
    "Your siblings looked up to you. (+5 to CON)",
    "You had the best holiday meals. (+5 to CON)",
    "You have too many cousins. (+6 to CON)",
    "You walked a very long distance. (+6 to CON)"
]

CHILDHOOD_INT_ROLL_MAP = [
    "You've never read a book. (+1 to INT)",
    "You were dropped on your head. (+1 to INT)",
    "You learned from doing, not being taught. (+2 to INT)",
    "You hated school. (+2 to INT)",
    "You had a secret place. (+3 to INT)",
    "You invented a code. (+3 to INT)",
    "You caught a parent doing something bad. (+4 to INT)",
    "You met a wizard! (+4 to INT)",
    "You kept a diary. (+5 to INT)",
    "Curiosity earned you more than a few scars. (+5 to INT)",
    "Your mother taught you all the legends. (+6 to INT)",
    "You drew a map. (+6 to INT)"
]

CHILDHOOD_WIS_ROLL_MAP = [
    "You embarrassed yourself publicly. (+1 to WIS)",
    "You got lost. Very lost. (+1 to WIS)",
    "It was terrifying. (+2 to WIS)",
    "You believed whatever your siblings said. (+2 to WIS)",
    "You loved to explore. You never got lost. (+3 to WIS)",
    "You planned a trip you never took. (+3 to WIS)",
    "You remember when the strangers arrived. (+4 to WIS)",
    "You have very early memories. (+4 to WIS)",
    "You solved a mystery. (+5 to WIS)",
    "You saw a ghost! (+5 to WIS)",
    "You had a beloved pet. (+6 to WIS)",
    "You had many imaginary friends. (+6 to WIS)"
]

CHILDHOOD_CHA_ROLL_MAP = [
    "No one loved you. (+1 to CHA)",
    "You ran away from home. (+1 to CHA)",
    "Your friends mocked you behind your back. (+2 to CHA)",
    "You didn't talk until very late. (+2 to CHA)",
    "You grew up among strangers. (+3 to CHA)",
    "A trusted person hurt you dearly. (+3 to CHA)",
    "You received a precious gift. (+4 to CHA)",
    "People traveled to see you. (+4 to CHA)",
    "You'd do anything on a dare. (+5 to CHA)",
    "You had an army of friends. (+5 to CHA)",
    "You were the favorite. (+6 to CHA)",
    "An enemy became a lifelong friend. (+6 to CHA)"
]

ADOLESCENT_QUESTION_GROUP_DECISION_ROLL_MAP = [
    [
        {
            "question": "Things had taken a turn for the worse. You needed to succeed here, but the risks were great. \n\t - Did you grit your teeth and wade in (STR) \n\t - or back off and retry it when you were better prepared (DEX)?",
            "options": ["STR", "DEX"]
        },
        {
            "question": "You were about to deliver bad news. It would break their heart. \n\t - Were you quick and blunt (INT) \n\t - or did you soften the blow with reassurances and sympathies (CON)?",
            "options": ["INT", "CON"]
        },
        {
            "question": "Did you let him hug you? \n\t - Yes (CHA) \n\t - or No (WIS).",
            "options": ["CHA", "WIS"]
        }
    ],
    [
        {
            "question": "Well, you messed up this time. They're gone. And with it, all the opportunities you once looked forward to. \n\t - Did you chase after them (STR) \n\t - or accept the loss and move on (CON)?",
            "options": ["STR", "CON"]
        },
        {
            "question": "Your friend was in an argument, and making some bold assertions. However, you knew she was wrong. Did you stand up for her? \n\t - Yes (CHA) \n\t - or no (DEX)?",
            "options": ["CHA", "DEX"]
        },
        {
            "question": "\t - Did you divide the food equally (INT) \n\t - or give the hungrier ones a little bit more (WIS)?",
            "options": ["INT", "WIS"]
        }
    ],
    [
        {
            "question": "When you were insulted, \n\t - did your honor demand satisfaction (STR) \n\t - or did you just quietly promise eventual vengeance (INT)?",
            "options": ["STR", "INT"]
        },
        {
            "question": "It was none of your business, really. But it looked like things were escalating, and somebody might get hurt. \n\t - Did you meddle in the affairs of others (WIS) \n\t - or stay out of it (DEX)?",
            "options": ["WIS", "DEX"]
        },
        {
            "question": "You lost. They were all laughing at you. \n\t - Did you offer your congratulations and walk away (CON) \n\t - or challenge them to a rematch (CHA)?",
            "options": ["CON", "CHA"]
        }
    ],
    [
        {
            "question": "It was supposed to be here by now, but it wasn't. People were getting worried. \n\t - Did you go out yourself to fetch it (STR) \n\t - or trust that it would arrive, and urge others to do the same (WIS)?",
            "options": ["STR", "WIS"]
        },
        {
            "question": "You badly needed something that you couldn't afford. \n\t - Did you steal it (DEX) \n\t - or resolve to save up the money, no matter how long it took (CON)?",
            "options": ["DEX", "CON"]
        },
        {
            "question": "Since it was so important, \n\t - did you talk to them in person (CHA) \n\t - or write a carefully-written letter, being sure to include all the details (INT)?",
            "options": ["CHA", "INT"]
        }
    ],
    [
        {
            "question": "\t - Did you choose love (CHA) \n\t - or career (STR)?",
            "options": ["CHA", "STR"]
        },
        {
            "question": "This was taking longer than you thought. \n\t - Did you ask for help (DEX) \n\t - or try to find a more efficient way of doing it (INT)?",
            "options": ["DEX", "INT"]
        },
        {
            "question": "The bastard had it coming. The only thing is, he didn't do the thing he's accused of. You did. \n\t - Did you step up and take your punishment (WIS) \n\t - or remain silent and watch karma descend (CON).",
            "options": ["WIS", "CON"]
        }
    ]
]

PROFESSIONS = [
    {
        "profession": "Army",
        "hint": "(Useful: Str, Dex, and Con)",
        "scenarios": [
            {
                "explanation": "Your training was more difficult than most. Test Str to influence Dex.",
                "tested_ability": "Str",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Assigned to carry the heaviest load. Test Str to influence Con.",
                "tested_ability": "Str",
                "influenced_ability": "Con"
            },
            {
                "explanation": "The commander asked to see a test of your marksmanship. Test Dex to influence Str.",
                "tested_ability": "Dex",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Fled a losing battle. Test Dex to influence Con.",
                "tested_ability": "Dex",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Sustained a major injury. Test Con to influence Str.",
                "tested_ability": "Con",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Captured. Test Con to influence Dex.",
                "tested_ability": "Con",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Considered for officer training. Test Str to influence Int.",
                "tested_ability": "Str",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Fellow scouting party depended on you. Test Dex to influence Cha.",
                "tested_ability": "Dex",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Starving and forced to forage for your own food. Test Con to influence Wis.",
                "tested_ability": "Con",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Tried a risky tactic involving stealth. Test Int to influence Dex.",
                "tested_ability": "Int",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Walked into an ambush. Test Wis to influence Str.",
                "tested_ability": "Wis",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Attempted to befriend the cook. Test Cha to influence Con.",
                "tested_ability": "Cha",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Hung out in the officer's club. Learn Military.",
                "learned_skill": "Military"
            },
            {
                "explanation": "Worked with the supply train and logistics. Learn Roads.",
                "learned_skill": "Roads"
            },
            {
                "explanation": "Worked with weapon salvage and repair. Learn Blacksmithing.",
                "learned_skill": "Blacksmithing"
            },
            {
                "explanation": "Always kept your weapons in immaculate condition. Learn Weapons.",
                "learned_skill": "Weapons"
            },
            {
                "explanation": "Learned the symbols and flags for all sorts of armies. Learn Heraldry.",
                "learned_skill": "Heraldry"
            },
            {
                "explanation": "Prepared food for your companions. Learn Cooking.",
                "learned_skill": "Cooking"
            },
            {
                "explanation": "Assigned as a bodyguard. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Spy in an enemy country. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Spent time guarding your home, away from the front lines. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Had a little business on the side. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Learned something from a prisoner. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Fought something unusual, or in an unusual circumstance. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Clergy",
        "hint": "(Useful: Int, Wis, and Cha)",
        "scenarios": [
            {
                "explanation": "Recited scripture from memory to an audience. Test Int to influence Wis.",
                "tested_ability": "Int",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Taught the doctrine to the neophytes. Test Int to influence Cha.",
                "tested_ability": "Int",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Debated your faith with the infidels. Test Wis to influence Int.",
                "tested_ability": "Wis",
                "influenced_ability": "Int"
            },
            {
                "explanation": "A tragedy shook your faith. Test Wis to influence Cha.",
                "tested_ability": "Wis",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Had a great/horrible relationship with your mentor. Test Cha to influence Int.",
                "tested_ability": "Cha",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Received a visitation from your god. Test Cha to influence Wis.",
                "tested_ability": "Cha",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Responsible for calling the faithful to their daily prayer. Test Int to influence Dex.",
                "tested_ability": "Int",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Attempted a great labor for your god. You worked until collapse. Test Wis to influence Con.",
                "tested_ability": "Wis",
                "influenced_ability": "Con"
            },
            {
                "explanation": "You often carried and prepared the bodies before the funeral. Test Cha to influence Str.",
                "tested_ability": "Cha",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Traveled to study with a distant branch of your faith. Test Con to influence Int.",
                "tested_ability": "Con",
                "influenced_ability": "Int"
            },
            {
                "explanation": "You helped build/repair a church/holy site. Test Str to influence Wis.",
                "tested_ability": "Str",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Tried to avert disaster during a wedding/baptism. Test Dex to influence Cha.",
                "tested_ability": "Dex",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Trained to overcome the evil that lurks in the world. Learn Demons.",
                "learned_skill": "Demons"
            },
            {
                "explanation": "Your church/temple is historically significant. Learn History.",
                "learned_skill": "History"
            },
            {
                "explanation": "Once a servant of the Forest God. Learn Religion (Forest God).",
                "learned_skill": "Religion (Forest God)"
            },
            {
                "explanation": "Once a servant of the Moon God. Learn Religion (Moon God).",
                "learned_skill": "Religion (Moon God)"
            },
            {
                "explanation": "Once a servant of the Ocean God. Learn Religion (Ocean God).",
                "learned_skill": "Religion (Ocean God)"
            },
            {
                "explanation": "Once a servant of the Sun God. Learn Religion (Sun God).",
                "learned_skill": "Religion (Sun God)"
            },
            {
                "explanation": "Your life was different before you committed yourself to your god. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Your church/temple is famous for something. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "A vision of your god imbued you with knowledge. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You were required to learn a certain skill before you began your education. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You've traveled far preaching the doctrine of your god. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "While living with heathens, you learned some of their ways. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Criminal",
        "hint": "(Useful: Str, Dex, and Cha)",
        "scenarios": [
            {
                "explanation": "The boss asked you to crack a lot of skulls. Test Str to influence Dex.",
                "tested_ability": "Str",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "You survived your initiation in a dramatic fashion. Test Str to influence Cha.",
                "tested_ability": "Str",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "You'll never forget the first time you killed someone. Test Dex to influence Str.",
                "tested_ability": "Dex",
                "influenced_ability": "Str"
            },
            {
                "explanation": "The boss personally asked you to steal something important. Test Dex to influence Cha.",
                "tested_ability": "Dex",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "You were tasked with killing a friend to prove your loyalty. Test Cha to influence Str.",
                "tested_ability": "Cha",
                "influenced_ability": "Str"
            },
            {
                "explanation": "You had a complicated relationship with the people you extorted. Test Cha to influence Dex.",
                "tested_ability": "Cha",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Entered a lethal-force duel. Test Str to influence Wis.",
                "tested_ability": "Str",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Stole from a wizard. Test Dex to influence Int.",
                "tested_ability": "Dex",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Your “friendly” rival is a fan of poison. Test Cha to influence Con.",
                "tested_ability": "Cha",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Spent some time in prison. Test Con to influence Str.",
                "tested_ability": "Con",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Had a mentor. Test Int to influence Dex.",
                "tested_ability": "Int",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Made a lot of friends/enemies on that street. Test Wis to influence Cha.",
                "tested_ability": "Wis",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Been to some intense parties. Learn Carouse.",
                "learned_skill": "Carouse"
            },
            {
                "explanation": "Born into your family profession. Learn Criminals.",
                "learned_skill": "Criminals"
            },
            {
                "explanation": "Burgled quite a few houses. Learn Locks.",
                "learned_skill": "Locks"
            },
            {
                "explanation": "You know what money is for. Learn Gambling.",
                "learned_skill": "Gambling"
            },
            {
                "explanation": "Strangers paid for most of your meals. Learn Pick Pocket.",
                "learned_skill": "Pick Pocket"
            },
            {
                "explanation": "You'll never forget that brothel. Learn Sex.",
                "learned_skill": "Sex"
            },
            {
                "explanation": "Crime is your business, but you have another passion. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "The boss had an interesting collection. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You can never return to your old life. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Had a little business on the side. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Learned something in prison. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You stole something very unusual once. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Forest",
        "hint": "(Useful: Str, Dex, and Wis)",
        "scenarios": [
            {
                "explanation": "Fought off a beast with only a knife. Test Str to influence Dex.",
                "tested_ability": "Str",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Unable to find your way home, you made a new home. Test Str to influence Wis.",
                "tested_ability": "Str",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Trapped for days. You thought you were going to die. Test Dex to influence Str.",
                "tested_ability": "Dex",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Encountered the elves. Test Dex to influence Wis.",
                "tested_ability": "Dex",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Hunger made you weak. Test Wis to influence Str.",
                "tested_ability": "Wis",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Heard voices on the wind. Test Wis to influence Dex.",
                "tested_ability": "Wis",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Trusted a stranger enough to share food with them. Test Str to influence Cha.",
                "tested_ability": "Str",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "You have been hunted. Test Dex to influence Con.",
                "tested_ability": "Dex",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Followed tracks that you didn't recognize. Test Wis to influence Int.",
                "tested_ability": "Wis",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Tracked down a human, and fought them. Test Int to influence Str.",
                "tested_ability": "Int",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Encountered the fey. Test Cha to influence Wis.",
                "tested_ability": "Cha",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Dysentery was awful. Test Con to influence Dex.",
                "tested_ability": "Con",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Eyes are always turned skyward. Learn Weather.",
                "learned_skill": "Weather"
            },
            {
                "explanation": "Flesh is food and food is strength. Learn Butcher.",
                "learned_skill": "Butcher"
            },
            {
                "explanation": "You are most comfortable here. Learn Forests.",
                "learned_skill": "Forests"
            },
            {
                "explanation": "Easier than hunting. Learn Fishing.",
                "learned_skill": "Fishing"
            },
            {
                "explanation": "You wander far. Learn Navigation.",
                "learned_skill": "Navigation"
            },
            {
                "explanation": "Eyes are always turned to the ground. Learn Track.",
                "learned_skill": "Track"
            },
            {
                "explanation": "Strange things are shared around a campfire. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Born in the city. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "The real reason you go back to town. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "The real reason why you travel. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You learned it from a wizard. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You learned it from the birds. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Noble",
        "hint": "(Useful: Dex, Int, and Cha)",
        "scenarios": [
            {
                "explanation": "Attempted to read all of the books that you own. Test Dex to influence Int.",
                "tested_ability": "Dex",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Seduced someone of a higher/lower social class. Test Dex to influence Cha.",
                "tested_ability": "Dex",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Involved in blackmail. Test Int to influence Dex.",
                "tested_ability": "Int",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Aspirations to wear the crown. Test Int to influence Cha.",
                "tested_ability": "Int",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Involved in a scandalous relationship. Test Cha to influence Dex.",
                "tested_ability": "Cha",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Lied to your tutor (that old fool). Test Cha to influence Int.",
                "tested_ability": "Cha",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "You love/hate practicing with your swordmaster. Test Dex to influence Con.",
                "tested_ability": "Dex",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Once saw a demon summoned at a party. Test Int to influence Wis.",
                "tested_ability": "Int",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Tried to avoid actual combat in the war. Test Cha to influence Str.",
                "tested_ability": "Cha",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Member of an archery/polo/yacht club. Test Con to influence Dex.",
                "tested_ability": "Con",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Member of (mostly social, somewhat strange) secret society. Test Str to influence Int.",
                "tested_ability": "Str",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Manipulated with your own betrothal. Test Wis to influence Cha.",
                "tested_ability": "Wis",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Politeness opens many doors (but not as many as money). Learn Etiquette.",
                "learned_skill": "Etiquette"
            },
            {
                "explanation": "You are a fish among fish in a very expensive ocean. Learn Nobles.",
                "learned_skill": "Nobles"
            },
            {
                "explanation": "Form before function. Learn Fashion.",
                "learned_skill": "Fashion"
            },
            {
                "explanation": "You do your own wealth, and want more. Learn Money.",
                "learned_skill": "Money"
            },
            {
                "explanation": "Everything else is boring. Learn Drugs.",
                "learned_skill": "Drugs"
            },
            {
                "explanation": "Your notebook is always close at hand, should inspiration strike. Learn Poetry.",
                "learned_skill": "Poetry"
            },
            {
                "explanation": "You've been to some strange parties. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "No one suspects what really goes on inside your private social club. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You've cultivated a hobby to make yourself seem interesting. You loathe it. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You've traveled to some distant shores. They were boring, too. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "An exotic visitor lived in your house for a good length of time. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Only one thing keeps you sane. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Rural",
        "hint": "(Useful: Str, Con, and Wis)",
        "scenarios": [
            {
                "explanation": "Abundant crops means exhausting harvests. Test Str to influence Con.",
                "tested_ability": "Str",
                "influenced_ability": "Con"
            },
            {
                "explanation": "After that day, you were the only one left to take care of the farm. Test Str to influence Wis.",
                "tested_ability": "Str",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Famine. Test Con to influence Str.",
                "tested_ability": "Con",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Drank too much mead at a festival. Test Con to influence Wis.",
                "tested_ability": "Con",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Entered your crops/animals in a county fair. Test Wis to influence Str.",
                "tested_ability": "Wis",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Oversaw a birth in the absence of anyone more qualified. Test Wis to influence Con.",
                "tested_ability": "Wis",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Once carried an animal/person a great distance in an emergency. Test Str to influence Cha.",
                "tested_ability": "Str",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Caught the plague. Test Con to influence Dex.",
                "tested_ability": "Con",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Buried your own parents behind the farm. Test Wis to influence Int.",
                "tested_ability": "Wis",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Forced to improvise when a disease ravaged your crops. Test Int to influence Con.",
                "tested_ability": "Int",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Got married. Test Cha to influence Wis.",
                "tested_ability": "Cha",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Ran for your life. Test Dex to influence Str.",
                "tested_ability": "Dex",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Your pig trusts you. Learn Animal Handling.",
                "learned_skill": "Animal Handling"
            },
            {
                "explanation": "And your ancestors are farmers, too. As far back as anyone remembers. Learn Farming.",
                "learned_skill": "Farming"
            },
            {
                "explanation": "You have a passion for equines. Learn Horses.",
                "learned_skill": "Horses"
            },
            {
                "explanation": "About 10% of your waking hours are spent talking about the weather. Learn Weather.",
                "learned_skill": "Weather"
            },
            {
                "explanation": "You might be an alcoholic. Learn Booze.",
                "learned_skill": "Booze"
            },
            {
                "explanation": "The well-to-do men who buy your crops are not strangers. Learn Merchants.",
                "learned_skill": "Merchants"
            },
            {
                "explanation": "You read a book once. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You and your friends have a tradition you all do on festival days. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You're pretty sure that this is what you learned in church. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "One of your siblings gave up farming. They visit sometimes. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Aspirations of a better life. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You've been talking to caravan guards too much. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Town",
        "hint": "(Useful: Con, Int, and Cha)",
        "scenarios": [
            {
                "explanation": "Apprenticeship was not what you expected. Test Con to influence Int.",
                "tested_ability": "Con",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Survived the slow pox. Not everyone did. Test Con to influence Cha.",
                "tested_ability": "Con",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Noticed a discrepancy in your finances. Test Int to influence Con.",
                "tested_ability": "Int",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Helped look for a missing child. Test Int to influence Cha.",
                "tested_ability": "Int",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "Called for help while being mugged. Test Cha to influence Con.",
                "tested_ability": "Cha",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Ran for a position in your guild. Test Cha to influence Int.",
                "tested_ability": "Cha",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Something strange happened while you were working late one night. Test Con to influence Dex.",
                "tested_ability": "Con",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Helped hunt for a witch. Test Int to influence Wis.",
                "tested_ability": "Int",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Epic bar brawl. You still owe money for damages. Test Cha to influence Str.",
                "tested_ability": "Cha",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Trampled by a mob. Test Dex to influence Con.",
                "tested_ability": "Dex",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Abused by a noble's thugs. Test Str to influence Int.",
                "tested_ability": "Str",
                "influenced_ability": "Int"
            },
            {
                "explanation": "They tried to cheat you. Test Wis to influence Cha.",
                "tested_ability": "Wis",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "You forged your own weapon. Learn Blacksmithing.",
                "learned_skill": "Blacksmithing"
            },
            {
                "explanation": "Built all the furniture in your house. Learn Carpentry.",
                "learned_skill": "Carpentry"
            },
            {
                "explanation": "You have fed hungry mouths. Learn Cooking.",
                "learned_skill": "Cooking"
            },
            {
                "explanation": "A regular at the tavern. Learn Gossip.",
                "learned_skill": "Gossip"
            },
            {
                "explanation": "A fountain of good humor among your friends. Learn Comedy.",
                "learned_skill": "Comedy"
            },
            {
                "explanation": "Like most, you've struggled with taxes, permits, and passes. Learn Bureaucracy.",
                "learned_skill": "Bureaucracy"
            },
            {
                "explanation": "No one knows about your secret. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "A little business on the side. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "A remnant of your meager education. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "A reminder of that one time you traveled somewhere. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Your family is known for it. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You weren't born here. You can still remember your former life vividly. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Wizard's Apprentice",
        "hint": "(Useful: Dex, Int, and Wis)",
        "scenarios": [
            {
                "explanation": "Endless hours of scribing text. Test Dex to influence Int.",
                "tested_ability": "Dex",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Had to improvise when something didn't go as planned. Test Dex to influence Wis.",
                "tested_ability": "Dex",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Tried to cast a spell in an emergency. Test Int to influence Dex.",
                "tested_ability": "Int",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Tried to cast a spell that you had not been taught. Test Int to influence Wis.",
                "tested_ability": "Int",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Body was temporarily possessed by otherworldly powers. Test Wis to influence Dex.",
                "tested_ability": "Wis",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "Tried to save your master's life. Test Wis to influence Int.",
                "tested_ability": "Wis",
                "influenced_ability": "Int"
            },
            {
                "explanation": "In charge of wrangling your master's magical beasts. Test Dex to influence Str.",
                "tested_ability": "Dex",
                "influenced_ability": "Str"
            },
            {
                "explanation": "Neglected your studies in order to socialize. Test Int to influence Cha.",
                "tested_ability": "Int",
                "influenced_ability": "Cha"
            },
            {
                "explanation": "You tried the weird drugs. Test Wis to influence Con.",
                "tested_ability": "Wis",
                "influenced_ability": "Con"
            },
            {
                "explanation": "Endless hours of meditation. Test Con to influence Int.",
                "tested_ability": "Con",
                "influenced_ability": "Int"
            },
            {
                "explanation": "Communicated with a vast and inhuman intelligence. Test Cha to influence Wis.",
                "tested_ability": "Cha",
                "influenced_ability": "Wis"
            },
            {
                "explanation": "Mopped up after messy experiments. Test Str to influence Dex.",
                "tested_ability": "Str",
                "influenced_ability": "Dex"
            },
            {
                "explanation": "You master had access to an incredible observatory. Learn Astronomy.",
                "learned_skill": "Astronomy"
            },
            {
                "explanation": "Studied briefly among elves. Learn Elves.",
                "learned_skill": "Elves"
            },
            {
                "explanation": "Studied from ancient books written in unusual languages. Learn Linguistics.",
                "learned_skill": "Linguistics"
            },
            {
                "explanation": "Your master had access to an incredible library. Learn Literature.",
                "learned_skill": "Literature"
            },
            {
                "explanation": "Your master had access to an magnificent alchemy lab. Learn Alchemy.",
                "learned_skill": "Alchemy"
            },
            {
                "explanation": "Socialized with a certain group of wizards. Learn Wizards.",
                "learned_skill": "Wizards"
            },
            {
                "explanation": "Traveled to a distant place with your master. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Forced to learn strange skills before being allowed to learn magic. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "You learned magic through a very unorthodox method.. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Your master had eclectic interests. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Learned something from another apprentice. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "explanation": "Still remember what you learned before becoming an apprentice. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    }
]

RANDOM_SKILLS = [
    "Alchemy", "Animal Handling", "Architecture", "Astronomy", "Bureaucracy", "Beg", "Blacksmithing", "Booze", "Butcher", "Carpentry",
    "Carouse", "Caves", "Comedy", "Cooking", "Criminals", "Cults", "Dance", "Demons", "Deserts", "Disguise",
    "Drugs", "Drums", "Dwarves", "Elves", "Engineering", "Etiquette", "Fashion", "Farms", "Fishing", "Flutes",
    "Folklore", "Forests", "Forgery", "Fortune Telling", "Gambling", "Geography", "Geology", "Gossip", "Guitars", "Halflings",
    "Harps", "Heraldry", "History", "Horses", "Jewelry", "Jungle", "Lakes", "Lang. (Northspeak)", "Lang. (Oldspeak)", "Lang. (Southspeak)",
    "Law", "Linguistics", "Literature", "Locale (E. Country)", "Locale (N. Country)", "Locale (S. Country)", "Locale (W. Country)", "Locale (Far Country)", "Locks", "Lutes",
    "Maps", "Medicine", "Merchants", "Military", "Money", "Mountains", "Navigation", "Necromancers", "Nobles", "Oceans",
    "Orcs", "Pick Pockets", "Philosophy", "Plains", "Poetry", "Religion (Forest God)", "Religion (Moon God)", "Religion (Ocean God)", "Religion (Sun God)", "Research",
    "Rivers", "Roads", "Royalty", "Scavenge", "Sailing", "Sex", "Sing", "Smuggling", "Swamps", "Tailoring",
    "Teach", "Track", "Trumpets", "Tundras", "Paint", "Warfare", "Weapons", "Weather", "Wizards", "Writing"
]