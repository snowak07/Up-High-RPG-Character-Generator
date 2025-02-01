import constants
import math
import sys

gpt_provider_enabled = True
try:
    import gpt_provider
except ImportError:
    gpt_provider_enabled = False

def handleArguments():
    print_to_file_enabled = False
    summary_enabled = False
    load_backstory = False
    backstory_file_path = ''

    if (len(sys.argv) > 3):
        print('Invalid number of arguments. Please provide at most 2 arguments.')
        sys.exit()
    elif (len(sys.argv) > 1):
        for arg in sys.argv:
            if (arg.lower() == 'print=true'):
                print_to_file_enabled = True
            elif (arg.lower() == 'summary=true'):
                summary_enabled = True
            elif (arg.lower() == 'load_backstory=true'):
                load_backstory = True
            elif (arg != 'char-gen.py'):
                backstory_file_path = arg

    if (summary_enabled or load_backstory) and not gpt_provider_enabled:
        print('ERROR: openai package was not able to be loaded. Please remove the summary argument or check your openai installation.')
        sys.exit()

    if load_backstory and not backstory_file_path:
        print('Please provide a file path to load the backstory from.')
        sys.exit()

    return (print_to_file_enabled, summary_enabled, load_backstory, backstory_file_path)

def printWelcomeMessage():
    print('''
-----------------------------------------------
| Welcome to the Up High Character Generator! |

This program will ask for your rolls for each stage of your life with some requiring successive die rolls.

Order of ability checks will be as follows:
STR, DEX, CON, INT, WIS, CHA
-----------------------------------------------''')

def getCharacterName():
    return input('\nWhat is your character\'s name?: ')

def initializeAbilities():
    return {
        'STR': 0,
        'DEX': 0,
        'CON': 0,
        'INT': 0,
        'WIS': 0,
        'CHA': 0
    }

def main():
    (print_to_file_enabled, summary_enabled, load_backstory, backstory_file_path) = handleArguments()

    if (load_backstory):
        handleBackstoryLoad(backstory_file_path)
        sys.exit()

    printWelcomeMessage()
    character_name = getCharacterName()

    ability_totals = initializeAbilities()
    adv_disadv = initializeAbilities()
    learned_skills = []

    childhood_backstory = handleChildhood(ability_totals)
    adolescence_backstory = handleAdolescence(ability_totals)
    adult_backstory = handleAdulthood(ability_totals, adv_disadv, learned_skills)

    character_sheet = constructCharacterSheet(ability_totals, learned_skills, childhood_backstory, adolescence_backstory, adult_backstory)

    if (summary_enabled):
        summary = gpt_provider.getGPTSummary(character_sheet)
        character_sheet += summary

    if (print_to_file_enabled):
        with open(character_name + ".txt", "w") as file:
            print(character_sheet, file=file)
    else:
        print(character_sheet)

def handleBackstoryLoad(backstory_file_path):
    backstory_file_read = open(backstory_file_path, "r")
    backstory = backstory_file_read.read()
    backstory_summary = gpt_provider.getGPTSummary(backstory)

    # Append summary to the same file
    with open(backstory_file_path, "a") as file:
        print(backstory_summary, file=file)

def handleChildhood(ability_totals):
    childhood_backstory = []
    for ability in ability_totals:
        results = handleChildhoodStatRoll(ability)
        ability_additive = results[1]
        backstory_snippet = results[0]

        childhood_backstory.append({
            "ability": ability,
            "backstory_snippet": backstory_snippet
        })

        ability_totals[ability] += ability_additive

    return childhood_backstory

def handleAdolescence(ability_totals):
    print("\nNow moving on to adolescence...")
    adolescence_backstory = []
    adolescence_question_group_roll_result = intInputHandlingAndValidation('Roll a d10: ', 1, 10)
    adolescence_question_group_roll_index = math.ceil(adolescence_question_group_roll_result / 2) - 1
    adolescence_question_group_dict = constants.ADOLESCENT_QUESTION_GROUP_DECISION_ROLL_MAP[adolescence_question_group_roll_index]

    for question in adolescence_question_group_dict:
        results = handleAdolescenceStatRoll(question['question'], question['options'])
        adolescence_backstory.append({
            "question": question['question'],
            "option_chosen": results[0]
        })
        ability_additives = results[1]
        for ability, additive in ability_additives.items():
            ability_totals[ability] += additive
    
    return adolescence_backstory

def handleAdulthood(ability_totals, adv_disadv, learned_skills):
    print("\nNow finishing up with adulthood...")
    profession_names_list = [profession['profession'].lower() for profession in constants.PROFESSIONS]
    print("profession_names_list", profession_names_list)
    adult_backstory = []

    for i in range(1, 7):
        current_profession_choice = getProfessionChoice(profession_names_list, i)
        profession_index = profession_names_list.index(current_profession_choice)
        current_scenario = getScenario(profession_index)

        backstory_element = {
            "profession": current_profession_choice,
            "scenario": current_scenario
        }
        
        if "tested_ability" in current_scenario:
            passed_test = processTestedAbilityScenario(current_scenario, ability_totals, adv_disadv)
            backstory_element["scenario"]["passed_test"] = passed_test

        elif "learned_skill" in current_scenario:
            learned_skill = resolveSkill(current_scenario)
            print('\nYour skill is: ' + learned_skill + '!')
            learned_skills.append(learned_skill)
            backstory_element["scenario"]["learned_skill"] = learned_skill
        
        adult_backstory.append(backstory_element)

    handleFinalRolls(ability_totals, adv_disadv)

    return adult_backstory

def handleFinalRolls(ability_totals, adv_disadv):
    print('\nNow for the final rolls...\n')

    for ability in ability_totals:
        ability_totals[ability] += handleAdulthoodAdvDisadvStatRoll(ability, adv_disadv[ability])

def constructFinalResults(ability_totals, learned_skills):
    return f'''
-----------------------------------------------
Final Results:
|STR ({ability_totals['STR']})|DEX ({ability_totals['DEX']})|CON ({ability_totals['CON']})|INT ({ability_totals['INT']})|WIS ({ability_totals['WIS']})|CHA ({ability_totals['CHA']})|

Skills: {learned_skills}
-----------------------------------------------
'''

def handleChildhoodStatRoll(ability):
    childhood_ability_roll_result = intInputHandlingAndValidation('Roll a d12 for ' + ability + ': ', 1, 12)
    ability_additive = math.ceil(childhood_ability_roll_result / 2)

    lore_roll_map = {}
    match ability:
        case 'STR':
            lore_roll_map = constants.CHILDHOOD_STR_ROLL_MAP
        case 'DEX':
            lore_roll_map = constants.CHILDHOOD_DEX_ROLL_MAP
        case 'CON':
            lore_roll_map = constants.CHILDHOOD_CON_ROLL_MAP
        case 'INT':
            lore_roll_map = constants.CHILDHOOD_INT_ROLL_MAP
        case 'WIS':
            lore_roll_map = constants.CHILDHOOD_WIS_ROLL_MAP
        case 'CHA':
            lore_roll_map = constants.CHILDHOOD_CHA_ROLL_MAP
        case _:
            raise ValueError('Invalid ability')
    
    childhood_ability_map_index = childhood_ability_roll_result - 1
    childhood_ability_lore_snippet = lore_roll_map[childhood_ability_map_index]
    print(childhood_ability_lore_snippet)

    return (childhood_ability_lore_snippet, ability_additive)

def handleAdolescenceStatRoll(question, options):
    higher_ability_chosen = stringInputHandlingAndValidation('\n' + question + ': ', options).upper()

    # Roll 2d6 and apply higher to chosen ability and lower to the other option
    print("\nNow Roll 2d6")
    higher_ability_roll = intInputHandlingAndValidation('What is the higher roll?: ', 1, 6)
    lower_ability_roll = intInputHandlingAndValidation('What is the lower roll?: ', 1, 6)

    # Add to dict that will be added to ability totals
    sortAbilityRoll = lambda ability: higher_ability_roll if ability == higher_ability_chosen else lower_ability_roll
    ability_additives = dict(map(lambda ability: (ability, sortAbilityRoll(ability)), options))
    return (higher_ability_chosen, ability_additives)

def getProfessionChoice(profession_names_list, period):
    return stringInputHandlingAndValidation(f'\nAvailable Professions: \n\n\t|Army|Clergy|Criminal|Forest|Noble|Rural|Town|Wizard\'s Apprentice|\n\nChoose a profession for your adult period ({period} of 6): ', profession_names_list).lower()

def getScenario(profession_index):
    # Roll for scenario within profession
    current_scenario_roll = intInputHandlingAndValidation('Roll a d24 (d2 + d12): ', 1, 24)
    current_scenario_index = current_scenario_roll - 1

    # Get scenario data for chosen profession and roll
    current_profession = constants.PROFESSIONS[profession_index]
    current_scenario = current_profession['scenarios'][current_scenario_index]
    return current_scenario

def processTestedAbilityScenario(scenario, ability_totals, adv_disadv):
    ability_to_test = scenario['tested_ability'].upper()
    ability_score = ability_totals[ability_to_test]
    passed_scenario = scenarioTest(scenario['explanation'], ability_to_test, ability_score)

    influenced_ability = scenario['influenced_ability'].upper()
    adv_disadv[influenced_ability] += 1 if passed_scenario else -1
    print("\nSuccess!") if passed_scenario else print("\nFailure!")
    return passed_scenario

def resolveSkill(scenario):
    learned_skill = ""
    if scenario['learned_skill'] == "Random":
        # Roll d100
        roll_result = intInputHandlingAndValidation(scenario['explanation'] + ' (Roll a d100 to determine skill): ', 1, 100)
        roll_result_index = roll_result - 1
        learned_skill = constants.RANDOM_SKILLS[roll_result_index]
    else:
        learned_skill = scenario['learned_skill']
    
    return learned_skill

def scenarioTest(scenario_explanantion, tested_ability, ability_score):
    roll_result = intInputHandlingAndValidation(scenario_explanantion + ' [' + tested_ability + ' (' + str(ability_score) + ')] ' +  '(Roll a d12): ', 1, 12)
    return roll_result <= ability_score

def handleAdulthoodAdvDisadvStatRoll(ability, adv_disadv_amt):
    ability_addendum = ' take the highest ' if adv_disadv_amt > 0 else ' '
    ability_addendum = ' take the lowest ' if adv_disadv_amt < 0 else ability_addendum
    adult_ability_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv_amt) + 1) + 'd6' + ability_addendum + 'for ' + ability + ': ', 1, 6)
    return adult_ability_result

def constructBackstory(childhood_backstory, adolescence_backstory, adult_backstory):
    childhood_backstory_write_up = constructChildhoodBackstory(childhood_backstory)
    adolescence_backstory_write_up = constructAdolescenceBackstory(adolescence_backstory)
    adult_backstory_write_up = constructAdultBackstory(adult_backstory)
    return '\n' + childhood_backstory_write_up + '\n' + adolescence_backstory_write_up + '\n' + adult_backstory_write_up

def constructChildhoodBackstory(childhood_backstory):
    childhood_backstory_write_up = 'Childhood:\n'
    for entry in childhood_backstory:
        childhood_backstory_write_up += entry['backstory_snippet'] + '\n'
    return childhood_backstory_write_up

def constructAdolescenceBackstory(adolescence_backstory):
    adolescence_backstory_write_up = 'Adolescence:'
    for entry in adolescence_backstory:
        adolescence_backstory_write_up += '\n' + entry['question'] + '. \nYou chose the ' + entry['option_chosen'] + ' option. \n'
    return adolescence_backstory_write_up

def constructAdultBackstory(adult_backstory):
    adult_backstory_write_up = 'Adulthood:'
    adult_period = 1
    for entry in adult_backstory:
        adult_backstory_write_up += f"\nFor period {adult_period} of 6 your background was {entry['profession']}. You faced the following scenario: \n{entry['scenario']['explanation']}.\n"
        if 'passed_test' in entry['scenario']:
            adult_backstory_write_up += f"You {'succeeded' if entry['scenario']['passed_test'] else 'failed'} on the test.\n"
        elif 'learned_skill' in entry['scenario']:
            adult_backstory_write_up += f"You learned the skill: {entry['scenario']['learned_skill']}.\n"
        adult_period += 1
    return adult_backstory_write_up

def constructCharacterSheet(ability_totals, learned_skills, childhood_backstory, adolescence_backstory, adult_backstory):
    return f'''\n-----------------------------------------------
Here is your full backstory:
    {constructBackstory(childhood_backstory, adolescence_backstory, adult_backstory)}
    {constructFinalResults(ability_totals, learned_skills)}
    '''

def intInputHandlingAndValidation(prompt, min_value, max_value):
    while True:
        try:
            return_value = int(input(prompt))
            if return_value < min_value or return_value > max_value:
                print(f"\nInput must be between {min_value} and {max_value}")
                continue
            return return_value
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(f"Input must be between {min_value} and {max_value}")

def stringInputHandlingAndValidation(prompt, accepted_values):
    accepted_values = list(map(lambda value: value.upper(), accepted_values))
    while True:
        try:
            return_value = str(input(prompt))
            if not return_value.upper() in accepted_values:
                print(f'\nERROR: Input must be one of the following values: {accepted_values}')
                continue
            return return_value
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Input must be one of the following values: ", accepted_values)

try:
    main()
except KeyboardInterrupt:
    # Cleanly handle keyboard interrupt exit
    sys.exit(0)