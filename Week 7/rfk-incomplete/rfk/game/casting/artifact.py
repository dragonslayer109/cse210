from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifacts(Actor):
    """
    Create message about the artifact
    """
    def __init__(self):
        super().__init__()
        self._message = ""

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message 
        return self._message