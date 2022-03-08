from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor
class MoveActorsAction(Action):
    """
    Moves objects (this is done with the action script)
    """
    def __init__(self):
        self.objects = []

    def execute(self, cast, script):
        """
        get list of objects and ittirate through them
        """
        self.objects = cast.get_all_actors()
        for object in self.objects:
            object.move_next()