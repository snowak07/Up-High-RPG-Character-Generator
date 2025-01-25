import constants
import math
import sys

def main():
    print('''

    --------------------------------
    | Welcome to the Up High Character Generator! |

    This program will ask for your rolls for each stage of your life with some requiring successive die rolls.

    Order of ability checks will be as follows:
    STR, DEX, CON, INT, WIS, CHA
    --------------------------------

    ''')

    ability_totals = {
        'STR': 0,
        'DEX': 0,
        'CON': 0,
        'INT': 0,
        'WIS': 0,
        'CHA': 0
    }

    #################### CHILDHOOD ####################
    print ('Starting with childhood...')
    childhood_str_roll_result = intInputHandlingAndValidation('Roll a d12 for STR: ', 1, 12)
    ability_totals['STR'] += math.ceil(childhood_str_roll_result / 2)
    childhood_str_map_index = childhood_str_roll_result - 1
    childhood_str_lore_snippet = constants.CHILDHOOD_STR_ROLL_MAP[childhood_str_map_index]
    print(childhood_str_lore_snippet)

    childhood_dex_roll_result = intInputHandlingAndValidation('Roll a d12 for DEX: ', 1, 12)
    ability_totals['DEX'] += math.ceil(childhood_dex_roll_result / 2)
    childhood_dex_map_index = childhood_dex_roll_result - 1
    childhood_dex_lore_snippet = constants.CHILDHOOD_DEX_ROLL_MAP[childhood_dex_map_index]
    print(childhood_dex_lore_snippet)

    childhood_con_roll_result = intInputHandlingAndValidation('Roll a d12 for CON: ', 1, 12)
    ability_totals['CON'] += math.ceil(childhood_con_roll_result / 2)
    childhood_con_map_index = childhood_con_roll_result - 1
    childhood_con_lore_snippet = constants.CHILDHOOD_CON_ROLL_MAP[childhood_con_map_index]
    print(childhood_con_lore_snippet)

    childhood_int_roll_result = intInputHandlingAndValidation('Roll a d12 for INT: ', 1, 12)
    ability_totals['INT'] += math.ceil(childhood_int_roll_result / 2)
    childhood_int_map_index = childhood_int_roll_result - 1
    childhood_int_lore_snippet = constants.CHILDHOOD_INT_ROLL_MAP[childhood_int_map_index]
    print(childhood_int_lore_snippet)

    childhood_wis_roll_result = intInputHandlingAndValidation('Roll a d12 for WIS: ', 1, 12)
    ability_totals['WIS'] += math.ceil(childhood_wis_roll_result / 2)
    childhood_wis_map_index = childhood_wis_roll_result - 1
    childhood_wis_lore_snippet = constants.CHILDHOOD_WIS_ROLL_MAP[childhood_wis_map_index]
    print(childhood_wis_lore_snippet)

    childhood_cha_roll_result = intInputHandlingAndValidation('Roll a d12 for CHA: ', 1, 12)
    ability_totals['CHA'] += math.ceil(childhood_cha_roll_result / 2)
    childhood_cha_map_index = childhood_cha_roll_result - 1
    childhood_cha_lore_snippet = constants.CHILDHOOD_CHA_ROLL_MAP[childhood_cha_map_index]
    print(childhood_cha_lore_snippet)

    #################### ADOLESCENCE ####################
    print("\nNow moving on to adolescence...")
    adolescence_initial_roll_result = intInputHandlingAndValidation('Roll a d10: \n', 1, 10)
    adolescence_initial_roll_index = math.ceil(adolescence_initial_roll_result / 2) - 1
    
    adolescence_question_dict = constants.ADOLESCENT_DECISION_ROLL_MAP[adolescence_initial_roll_index]
    for question in adolescence_question_dict:
        higher_ability_chosen = stringInputHandlingAndValidation(question['question'] + ': \n', question['options']).upper()

        # Roll 2d6 and apply higher to chosen and lower to other option
        print("\nNow Roll 2d6")
        higher_ability_roll = intInputHandlingAndValidation('what is the higher roll?: ', 1, 6)
        lower_ability_roll = intInputHandlingAndValidation('what is the lower roll?: ', 1, 6)

        # Add to ability totals
        ability_totals[higher_ability_chosen] += higher_ability_roll
        for option in question['options']:
            if option != higher_ability_chosen:
                ability_totals[option] += lower_ability_roll

    #################### ADULTHOOD ####################
    print("\nNow finishing up with adulthood...")
    profession_names_list = list(map(lambda profession: profession['profession'], constants.PROFESSIONS))

    profession_choices = []
    profession_rolls = []
    profession_test_results = []
    learned_skills = []
    adv_disadv = {
        'STR': 0,
        'DEX': 0,
        'CON': 0,
        'INT': 0,
        'WIS': 0,
        'CHA': 0
    }

    for i in range(1, 7):
        current_profession_choice = stringInputHandlingAndValidation(f'Available Professions: \n\n\t|Army|Clergy|Criminal|Forest|Noble|Rural|Town|Wizard\'s Apprentice|\n\nChoose a profession for your adult period ({i} of 6): ', profession_names_list).capitalize()
        profession_choices.append(current_profession_choice)
        
        current_profession_roll = intInputHandlingAndValidation('Roll a d24 (d2 + d12): \n', 1, 24)
        current_profession_index = current_profession_roll - 1
        profession_rolls.append(current_profession_roll)

        profession_index = profession_names_list.index(current_profession_choice)
        current_profession = constants.PROFESSIONS[profession_index]
        current_scenario = current_profession['scenarios'][current_profession_index]
        
        if "tested_ability" in current_scenario:
            # Roll d12 compare against tested ability
            roll_result = intInputHandlingAndValidation(current_scenario['scenario'] + ' (Roll a d12): ', 1, 12)
            current_tested_ability = current_scenario['tested_ability'].upper()
            tested_ability_score = ability_totals[current_tested_ability]
            if roll_result <= tested_ability_score:
                adv_disadv[current_tested_ability] += 1
            else:
                adv_disadv[current_tested_ability] -= 1
            
            profession_test_results.append(roll_result)

        elif "learned_skill" in current_scenario:
            learned_skill = "ERROR"
            if current_scenario['learned_skill'] == "Random":
                # Roll d100
                roll_result = intInputHandlingAndValidation(current_scenario['scenario'] + ' (Roll a d100 to determine skill): ', 1, 100)
                roll_result_index = roll_result - 1
                learned_skill = constants.RANDOM_SKILLS[roll_result_index]
            else:
                learned_skill = current_scenario['learned_skill']
            print('\nYour skill is: ' + learned_skill + '!')
            learned_skills.append(learned_skill)

    print('\nNow for the final rolls...\n\n')

    # Roll with adv/disadv for each of the stats.
    str_addendum = 'take highest' if adv_disadv['STR'] > 0 else ''
    str_addendum = 'take lowest' if adv_disadv['STR'] < 0 else str_addendum
    adult_str_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv['STR']) + 1) + 'd6 ' + str_addendum + ': ', 1, 6)
    ability_totals['STR'] += adult_str_result

    dex_addendum = 'take highest' if adv_disadv['DEX'] > 0 else ''
    dex_addendum = 'take lowest' if adv_disadv['DEX'] < 0 else dex_addendum
    adult_dex_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv['DEX']) + 1) + 'd6 ' + dex_addendum + ': ', 1, 6)
    ability_totals['DEX'] += adult_dex_result

    con_addendum = 'take highest' if adv_disadv['CON'] > 0 else ''
    con_addendum = 'take lowest' if adv_disadv['CON'] < 0 else con_addendum
    adult_con_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv['CON']) + 1) + 'd6 ' + con_addendum + ': ', 1, 6)
    ability_totals['CON'] += adult_con_result

    int_addendum = 'take highest' if adv_disadv['INT'] > 0 else ''
    int_addendum = 'take lowest' if adv_disadv['INT'] < 0 else int_addendum
    adult_int_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv['INT']) + 1) + 'd6 ' + int_addendum + ': ', 1, 6)
    ability_totals['INT'] += adult_int_result

    wis_addendum = 'take highest' if adv_disadv['WIS'] > 0 else ''
    wis_addendum = 'take lowest' if adv_disadv['WIS'] < 0 else wis_addendum
    adult_wis_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv['WIS']) + 1) + 'd6 ' + wis_addendum + ': ', 1, 6)
    ability_totals['WIS'] += adult_wis_result

    cha_addendum = 'take highest' if adv_disadv['CHA'] > 0 else ''
    cha_addendum = 'take lowest' if adv_disadv['CHA'] < 0 else cha_addendum
    adult_cha_result = intInputHandlingAndValidation('Roll ' + str(abs(adv_disadv['CHA']) + 1) + 'd6 ' + cha_addendum + ': ', 1, 6)
    ability_totals['CHA'] += adult_cha_result

    print(f'''
    --------------------------------
    Final Results:
    |STR ({ability_totals['STR']})|DEX ({ability_totals['DEX']})|CON ({ability_totals['CON']})|INT ({ability_totals['INT']})|WIS ({ability_totals['WIS']})|CHA ({ability_totals['CHA']})|

    Skills: {learned_skills}
    --------------------------------
    ''')

        # TODO: Ask each of the scenario questions and keep track of successes and failures. Ask for appropriate
        # advantage/disadvantage roll for each stat.

        # TODO: Print ability score totals and full lore readout (summarized together by chatGPT?)

        # TODO: Give additional full backstory writeup incorporating all generated elements.

        # TODO: Print backstory and stats to a text file.

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
                print("\nInput must be one of the following values: ", accepted_values)
                continue
            return return_value
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Input must be one of the following values: ", accepted_values)

main()