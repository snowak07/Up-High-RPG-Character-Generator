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
        higher_ability_chosen = stringInputHandlingAndValidation(question['question'] + ': \n', question['options'])

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

    for i in range(1, 7):
        profession_choices.append(stringInputHandlingAndValidation(f'Choose a profession for your adult period ({i} of 6): ', profession_names_list))
        profession_rolls.append(intInputHandlingAndValidation('Roll a d24 (d2 + d12): ', 1, 24))
        
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
            return_value = str(input(prompt)).upper()
            if not return_value in accepted_values:
                print("\nInput must be one of the following values: ", accepted_values)
                continue
            return return_value
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Input must be one of the following values: ", accepted_values)

main()