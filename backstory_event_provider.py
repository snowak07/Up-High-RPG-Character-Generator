from adulthood_backstory import AdulthoodBackstoryEvent
from adolescence_backstory import AdolescenceBackstoryEvent, AdolescenceBackstory
from childhood_backstory import ChildhoodBackstoryEvent
from constants import ADOLESCENT_QUESTION_GROUP_DECISION_ROLL_MAP, PROFESSIONS

class BackstoryEventProvider:
    instance = None

    @staticmethod
    def getAdolescenceEventGroups() -> list[AdolescenceBackstory]:
        '''Construct list of potential backstory event lists'''
        backstory_event_group_options = []
        for question_group in ADOLESCENT_QUESTION_GROUP_DECISION_ROLL_MAP:
            backstory = AdolescenceBackstory()
            for adolescence_event_data in question_group:
                backstory.addEvent(AdolescenceBackstoryEvent(adolescence_event_data['question'], adolescence_event_data['question_options'], adolescence_event_data['answer_options']))
            backstory_event_group_options.append(backstory)

        return backstory_event_group_options

    @staticmethod
    def getAdulthoodProfessionEventList(profession) -> list[AdulthoodBackstoryEvent]:
        '''Construct list of potential backstory events for chosen profession'''
        potential_events: list[AdulthoodBackstoryEvent] = []
        for potential_event_data in PROFESSIONS[profession]['scenarios']:
            potential_events.append(AdulthoodBackstoryEvent(
                profession,
                potential_event_data['scenario'],
                potential_event_data['tested_ability'] if potential_event_data.get('tested_ability') != None else '',
                potential_event_data['influenced_ability'] if potential_event_data.get('influenced_ability') != None else '',
                potential_event_data['learned_skill'] if potential_event_data.get('learned_skill') != None else ''
            ))

        return potential_events

    @staticmethod
    def getChildhoodBackstoryEventList(ability):
        return [ChildhoodBackstoryEvent(ability, backstory_event['bonus'], backstory_event['lore']) for backstory_event in constants.CHILDHOOD_ROLL_MAPS[ability]]