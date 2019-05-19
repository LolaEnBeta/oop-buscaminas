
class Box(object):
    def __init__(self):
        self.visible = False
        self.value = 0

    def has_bomb(self):
        if self.value == -1:
            return True
        else:
            return False