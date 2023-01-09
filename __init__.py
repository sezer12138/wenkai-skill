from mycroft import MycroftSkill, intent_file_handler


class Wenkai(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wenkai.intent')
    def handle_wenkai(self, message):
        self.speak_dialog('wenkai')


def create_skill():
    return Wenkai()

