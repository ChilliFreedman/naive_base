from classifier_server.classifier import Classifierrr
class Maneser_classifier:
    def __init__(self):
        self.model = None
        self.priors = None
        # self.dict_user = None

    def get_from_user(self,dict_user):
        return Classifierrr.classifier_data(dict_user, self.model, self.priors)