import argparse

class CmdLine():
    def __init__(self):
        parser = argparse.ArgumentParser(
                           description='PyPh')
        parser.add_argument("--game", dest='game', type=str, required=False,
                           help='aa || l2', default='aa')
        parser.add_argument("--l2_chronicle", dest='l2_chronicle', type=str, required=False,
                           help='so many options', default='gracia_final')
        self.args = parser.parse_args()

    @property
    def game(self):
        return self.args.game

    @property
    def l2_chronicle(self):
        return self.args.l2_chronicle


assert(type(CmdLine().game) == str)
assert(type(CmdLine().l2_chronicle) == str)
