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

ADOLESCENT_DECISION_ROLL_MAP = [
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
                "scenario": "Your training was more difficult than most. Test Str to influence Dex.",
                "tested_skill": "Str",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Assigned to carry the heaviest load. Test Str to influence Con.",
                "tested_skill": "Str",
                "influenced_skill": "Con"
            },
            {
                "scenario": "The commander asked to see a test of your marksmanship. Test Dex to influence Str.",
                "tested_skill": "Dex",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Fled a losing battle. Test Dex to influence Con.",
                "tested_skill": "Dex",
                "influenced_skill": "Con"
            },
            {
                "scenario": "Sustained a major injury. Test Con to influence Str.",
                "tested_skill": "Con",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Captured. Test Con to influence Dex.",
                "tested_skill": "Con",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Considered for officer training. Test Str to influence Int.",
                "tested_skill": "Str",
                "influenced_skill": "Int"
            },
            {
                "scenario": "Fellow scouting party depended on you. Test Dex to influence Cha.",
                "tested_skill": "Dex",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Starving and forced to forage for your own food. Test Con to influence Wis.",
                "tested_skill": "Con",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Tried a risky tactic involving stealth. Test Int to influence Dex.",
                "tested_skill": "Int",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Walked into an ambush. Test Wis to influence Str.",
                "tested_skill": "Wis",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Attempted to befriend the cook. Test Cha to influence Con.",
                "tested_skill": "Cha",
                "influenced_skill": "Con"
            },
            {
                "scenario": "Hung out in the officer's club. Learn Military.",
                "learned_skill": "Military"
            },
            {
                "scenario": "Worked with the supply train and logistics. Learn Roads.",
                "learned_skill": "Roads"
            },
            {
                "scenario": "Worked with weapon salvage and repair. Learn Blacksmithing.",
                "learned_skill": "Blacksmithing"
            },
            {
                "scenario": "Always kept your weapons in immaculate condition. Learn Weapons.",
                "learned_skill": "Weapons"
            },
            {
                "scenario": "Learned the symbols and flags for all sorts of armies. Learn Heraldry.",
                "learned_skill": "Heraldry"
            },
            {
                "scenario": "Prepared food for your companions. Learn Cooking.",
                "learned_skill": "Cooking"
            },
            {
                "scenario": "Assigned as a bodyguard. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Spy in an enemy country. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Spent time guarding your home, away from the front lines. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Had a little business on the side. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Learned something from a prisoner. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Fought something unusual, or in an unusual circumstance. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Clergy",
        "hint": "(Useful: Int, Wis, and Cha)",
        "scenarios": [
            {
                "scenario": "Recited scripture from memory to an audience. Test Int to influence Wis.",
                "tested_skill": "Int",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Taught the doctrine to the neophytes. Test Int to influence Cha.",
                "tested_skill": "Int",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Debated your faith with the infidels. Test Wis to influence Int.",
                "tested_skill": "Wis",
                "influenced_skill": "Int"
            },
            {
                "scenario": "A tragedy shook your faith. Test Wis to influence Cha.",
                "tested_skill": "Wis",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Had a great/horrible relationship with your mentor. Test Cha to influence Int.",
                "tested_skill": "Cha",
                "influenced_skill": "Int"
            },
            {
                "scenario": "Received a visitation from your god. Test Cha to influence Wis.",
                "tested_skill": "Cha",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Responsible for calling the faithful to their daily prayer. Test Int to influence Dex.",
                "tested_skill": "Int",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Attempted a great labor for your god. You worked until collapse. Test Wis to influence Con.",
                "tested_skill": "Wis",
                "influenced_skill": "Con"
            },
            {
                "scenario": "You often carried and prepared the bodies before the funeral. Test Cha to influence Str.",
                "tested_skill": "Cha",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Traveled to study with a distant branch of your faith. Test Con to influence Int.",
                "tested_skill": "Con",
                "influenced_skill": "Int"
            },
            {
                "scenario": "You helped build/repair a church/holy site. Test Str to influence Wis.",
                "tested_skill": "Str",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Tried to avert disaster during a wedding/baptism. Test Dex to influence Cha.",
                "tested_skill": "Dex",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Trained to overcome the evil that lurks in the world. Learn Demons.",
                "learned_skill": "Demons"
            },
            {
                "scenario": "Your church/temple is historically significant. Learn History.",
                "learned_skill": "History"
            },
            {
                "scenario": "Once a servant of the Forest God. Learn Religion (Forest God).",
                "learned_skill": "Religion (Forest God)"
            },
            {
                "scenario": "Once a servant of the Moon God. Learn Religion (Moon God).",
                "learned_skill": "Religion (Moon God)"
            },
            {
                "scenario": "Once a servant of the Ocean God. Learn Religion (Ocean God).",
                "learned_skill": "Religion (Ocean God)"
            },
            {
                "scenario": "Once a servant of the Sun God. Learn Religion (Sun God).",
                "learned_skill": "Religion (Sun God)"
            },
            {
                "scenario": "Your life was different before you committed yourself to your god. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Your church/temple is famous for something. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "A vision of your god imbued you with knowledge. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You were required to learn a certain skill before you began your education. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You've traveled far preaching the doctrine of your god. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "While living with heathens, you learned some of their ways. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Criminal",
        "hint": "(Useful: Str, Dex, and Cha)",
        "scenarios": [
            {
                "scenario": "The boss asked you to crack a lot of skulls. Test Str to influence Dex.",
                "tested_skill": "Str",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "You survived your initiation in a dramatic fashion. Test Str to influence Cha.",
                "tested_skill": "Str",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "You'll never forget the first time you killed someone. Test Dex to influence Str.",
                "tested_skill": "Dex",
                "influenced_skill": "Str"
            },
            {
                "scenario": "The boss personally asked you to steal something important. Test Dex to influence Cha.",
                "tested_skill": "Dex",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "You were tasked with killing a friend to prove your loyalty. Test Cha to influence Str.",
                "tested_skill": "Cha",
                "influenced_skill": "Str"
            },
            {
                "scenario": "You had a complicated relationship with the people you extorted. Test Cha to influence Dex.",
                "tested_skill": "Cha",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Entered a lethal-force duel. Test Str to influence Wis.",
                "tested_skill": "Str",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Stole from a wizard. Test Dex to influence Int.",
                "tested_skill": "Dex",
                "influenced_skill": "Int"
            },
            {
                "scenario": "Your “friendly” rival is a fan of poison. Test Cha to influence Con.",
                "tested_skill": "Cha",
                "influenced_skill": "Con"
            },
            {
                "scenario": "Spent some time in prison. Test Con to influence Str.",
                "tested_skill": "Con",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Had a mentor. Test Int to influence Dex.",
                "tested_skill": "Int",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Made a lot of friends/enemies on that street. Test Wis to influence Cha.",
                "tested_skill": "Wis",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Been to some intense parties. Learn Carouse.",
                "learned_skill": "Carouse"
            },
            {
                "scenario": "Born into your family profession. Learn Criminals.",
                "learned_skill": "Criminals"
            },
            {
                "scenario": "Burgled quite a few houses. Learn Locks.",
                "learned_skill": "Locks"
            },
            {
                "scenario": "You know what money is for. Learn Gambling.",
                "learned_skill": "Gambling"
            },
            {
                "scenario": "Strangers paid for most of your meals. Learn Pick Pocket.",
                "learned_skill": "Pick Pocket"
            },
            {
                "scenario": "You'll never forget that brothel. Learn Sex.",
                "learned_skill": "Sex"
            },
            {
                "scenario": "Crime is your business, but you have another passion. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "The boss had an interesting collection. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You can never return to your old life. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Had a little business on the side. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Learned something in prison. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You stole something very unusual once. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Forest",
        "hint": "(Useful: Str, Dex, and Wis)",
        "scenarios": [
            {
                "scenario": "Fought off a beast with only a knife. Test Str to influence Dex.",
                "tested_skill": "Str",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Unable to find your way home, you made a new home. Test Str to influence Wis.",
                "tested_skill": "Str",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Trapped for days. You thought you were going to die. Test Dex to influence Str.",
                "tested_skill": "Dex",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Encountered the elves. Test Dex to influence Wis.",
                "tested_skill": "Dex",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Hunger made you weak. Test Wis to influence Str.",
                "tested_skill": "Wis",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Heard voices on the wind. Test Wis to influence Dex.",
                "tested_skill": "Wis",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Trusted a stranger enough to share food with them. Test Str to influence Cha.",
                "tested_skill": "Str",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "You have been hunted. Test Dex to influence Con.",
                "tested_skill": "Dex",
                "influenced_skill": "Con"
            },
            {
                "scenario": "Followed tracks that you didn't recognize. Test Wis to influence Int.",
                "tested_skill": "Wis",
                "influenced_skill": "Int"
            },
            {
                "scenario": "Tracked down a human, and fought them. Test Int to influence Str.",
                "tested_skill": "Int",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Encountered the fey. Test Cha to influence Wis.",
                "tested_skill": "Cha",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Dysentery was awful. Test Con to influence Dex.",
                "tested_skill": "Con",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Eyes are always turned skyward. Learn Weather.",
                "learned_skill": "Weather"
            },
            {
                "scenario": "Flesh is food and food is strength. Learn Butcher.",
                "learned_skill": "Butcher"
            },
            {
                "scenario": "You are most comfortable here. Learn Forests.",
                "learned_skill": "Forests"
            },
            {
                "scenario": "Easier than hunting. Learn Fishing.",
                "learned_skill": "Fishing"
            },
            {
                "scenario": "You wander far. Learn Navigation.",
                "learned_skill": "Navigation"
            },
            {
                "scenario": "Eyes are always turned to the ground. Learn Track.",
                "learned_skill": "Track"
            },
            {
                "scenario": "Strange things are shared around a campfire. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Born in the city. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "The real reason you go back to town. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "The real reason why you travel. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You learned it from a wizard. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You learned it from the birds. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Noble",
        "hint": "(Useful: Dex, Int, and Cha)",
        "scenarios": [
            {
                "scenario": "Attempted to read all of the books that you own. Test Dex to influence Int.",
                "tested_skill": "Dex",
                "influenced_skill": "Int"
            },
            {
                "scenario": "Seduced someone of a higher/lower social class. Test Dex to influence Cha.",
                "tested_skill": "Dex",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Involved in blackmail. Test Int to influence Dex.",
                "tested_skill": "Int",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Aspirations to wear the crown. Test Int to influence Cha.",
                "tested_skill": "Int",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Involved in a scandalous relationship. Test Cha to influence Dex.",
                "tested_skill": "Cha",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Lied to your tutor (that old fool). Test Cha to influence Int.",
                "tested_skill": "Cha",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "You love/hate practicing with your swordmaster. Test Dex to influence Con.",
                "tested_skill": "Dex",
                "influenced_skill": "Con"
            },
            {
                "scenario": "Once saw a demon summoned at a party. Test Int to influence Wis.",
                "tested_skill": "Int",
                "influenced_skill": "Wis"
            },
            {
                "scenario": "Tried to avoid actual combat in the war. Test Cha to influence Str.",
                "tested_skill": "Cha",
                "influenced_skill": "Str"
            },
            {
                "scenario": "Member of an archery/polo/yacht club. Test Con to influence Dex.",
                "tested_skill": "Con",
                "influenced_skill": "Dex"
            },
            {
                "scenario": "Member of (mostly social, somewhat strange) secret society. Test Str to influence Int.",
                "tested_skill": "Str",
                "influenced_skill": "Int"
            },
            {
                "scenario": "Manipulated with your own betrothal. Test Wis to influence Cha.",
                "tested_skill": "Wis",
                "influenced_skill": "Cha"
            },
            {
                "scenario": "Politeness opens many doors (but not as many as money). Learn Etiquette.",
                "learned_skill": "Etiquette"
            },
            {
                "scenario": "You are a fish among fish in a very expensive ocean. Learn Nobles.",
                "learned_skill": "Nobles"
            },
            {
                "scenario": "Form before function. Learn Fashion.",
                "learned_skill": "Fashion"
            },
            {
                "scenario": "You do your own wealth, and want more. Learn Money.",
                "learned_skill": "Money"
            },
            {
                "scenario": "Everything else is boring. Learn Drugs.",
                "learned_skill": "Drugs"
            },
            {
                "scenario": "Your notebook is always close at hand, should inspiration strike. Learn Poetry.",
                "learned_skill": "Poetry"
            },
            {
                "scenario": "You've been to some strange parties. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "No one suspects what really goes on inside your private social club. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You've cultivated a hobby to make yourself seem interesting. You loathe it. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "You've traveled to some distant shores. They were boring, too. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "An exotic visitor lived in your house for a good length of time. Learn Random.",
                "learned_skill": "Random"
            },
            {
                "scenario": "Only one thing keeps you sane. Learn Random.",
                "learned_skill": "Random"
            }
        ]
    },
    {
        "profession": "Rural",
        "hint": "(Useful: Str, Con, and Wis)",
    },
    {
        "profession": "Town",
        "hint": "(Useful: Con, Int, and Cha)",
    },
    {
        "profession": "Wizard's Apprentice",
        "hint": "(Useful: Dex, Int, and Wis)",
    }
]