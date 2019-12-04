from deeppavlov.skills.pattern_matching_skill import PatternMatchingSkill
from deeppavlov.core.agent import Agent, HighestConfidenceSelector

hello = PatternMatchingSkill(responses=["Hello world!"],
                             patterns=["(hi|hello|good day)"],
                             regex=True)
sorry = PatternMatchingSkill(responses=["don't be sorry", "Please don't"],
                             patterns=["(sorry|excuse)"],
                             regex=True)
perhaps = PatternMatchingSkill(responses=["Please be more specific"],
                               patterns=["(.*)perhaps(.*)"],
                               regex=True)
agent = Agent([hello, sorry, perhaps],
              skills_selector=HighestConfidenceSelector())

agent(['hi, how are you', 'I am sorry', 'perhaps, I am not sure'])
