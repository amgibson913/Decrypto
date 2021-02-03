import string
import random

'''
Reminder:
All dictionaries containing players will have the form
{sid: username}
'''


class Game():
    def __init__(self, wordlist='default'):
        self.words = self.selectWords(wordlist)
        self.room = ''.join(random.choices(string.ascii_uppercase, k=4))
        self.gamesheets = {
            'Black': [{
                'Round': i,
                'Clues': ['','',''],
                'Black': ['','',''],
                'White': ['','',''],
                'Actual': ['','','']} for i in range(1, 9)],
            'White': [{
                'Round': i,
                'Clues': ['','',''],
                'Black': ['','',''],
                'White': ['','',''],
                'Actual': ['','','']} for i in range(1, 9)]}
        self.gameState = {
            'hasCodeMaster': {'Black': False, 'White': False},
            'hasClues': {'Black': False, 'White': False},
            'hasGuess': {'Black': False, 'White': False},
            'codeGuessed': {'Black': False, 'White': False},
            'teams': {
                'Black': {'Players': {}, 'CodeMaster': {}},
                'White': {'Players': {}, 'CodeMaster': {}}},
            'score': {
                'Black': {'Hits': 0, 'Misses': 0},
                'White': {'Hits': 0, 'Misses': 0}
            }
        }
        self.currentCode = {'Black': [], 'White': []}
        self.currentRound = {}
        self.newRound(1)

    def newRound(self, _round):
        self.currentRound = {
            'Black': {
                'Round': _round,
                'Clues': ['', '', ''],
                'Black': ['', '', ''],
                'White': ['', '', ''],
                'Actual': ['', '', '']},
            'White': {
                'Round': _round,
                'Clues': ['', '', ''],
                'Black': ['', '', ''],
                'White': ['', '', ''],
                'Actual': ['', '', '']}
        }

    def selectWords(self, wordlist):
        with open('./wordbanks/'+wordlist) as file:
            wordbank = file.read().splitlines()
            words = random.sample(wordbank, k=8)
            return {'Black': words[0:4], 'White': words[4:8]}

    def returnData(self):
        return {
            'gamesheets': self.gamesheets,
            'gameState': self.gameState,
            'room': self.room
        }

    def otherTeam(self, team):
        if team == 'White':
            return 'Black'
        else:
            return 'White'

    def regenerateRoomName(self):
        self.room = ''.join(random.choices(string.ascii_uppercase, k=4))
        return self.room

    def addPlayer(self, sid, team, username):
        self.gameState['teams'][team]['Players'].update({sid: username})
        return

    def removePlayer(self, sid):
        isEmpty = True
        for team in ['Black', 'White']:
            self.gameState['teams'][team]['Players'].pop(sid, None)
            lostCodeMaster = self.gameState['teams'][team]['CodeMaster'].pop(sid, False)
            if lostCodeMaster and not self.gameState['hasClues'][team]:
                self.gameState['hasCodeMaster'][team] = False
            if (
                len(self.gameState['teams'][team]['Players']) > 0
                or len(self.gameState['teams'][team]['CodeMaster']) > 0
            ):
                isEmpty = False

        return isEmpty

    def addCodeMaster(self, sid, team):
        if self.gameState['teams'][team]['CodeMaster'] == {}:
            username = self.gameState['teams'][team]['Players'][sid]
            self.gameState['teams'][team]['CodeMaster'] = {sid: username}
            self.gameState['hasCodeMaster'][team] = True
            code = random.sample([1, 2, 3, 4], k=3)
            self.currentCode[team] = code
            return code
        return None

    def submitClues(self, clues, team):
        if not self.gameState['hasClues'][team]:
            self.gameState['hasClues'][team] = True
            self.currentRound[team]['Clues'] = clues
        if False not in self.gameState['hasClues'].values():
            _round = self.currentRound['White']['Round']
            self.gamesheets['White'][_round - 1] = self.currentRound['White'].copy()
        return

    def submitGuess(self, guess, team):
        if not self.gameState['hasGuess'][team]:
            self.gameState['hasGuess'][team] = True
            if not self.gameState['codeGuessed']['White']:
                self.currentRound['White'][team] = guess
                if False not in self.gameState['hasGuess'].values():
                    self.gameState['hasGuess']['White'] = False
                    self.gameState['hasGuess']['Black'] = False
                    self.gameState['codeGuessed']['White'] = True
                    _round = self.currentRound['White']['Round']
                    self.scoreGuess('White')
                    self.gamesheets['White'][_round - 1] = self.currentRound['White'].copy()
                    self.gamesheets['Black'][_round - 1] = self.currentRound['Black'].copy()
                    return False, False
            else:
                self.currentRound['Black'][team] = guess
                if False not in self.gameState['hasGuess'].values():
                    self.gameState['hasGuess']['White'] = False
                    self.gameState['hasGuess']['Black'] = False
                    self.gameState['codeGuessed']['Black'] = True
                    _round = self.currentRound['Black']['Round']
                    self.scoreGuess('Black')
                    self.gamesheets['Black'][_round - 1] = self.currentRound['Black'].copy()
                    if (
                        2 in self.gameState['score']['Black'].values()
                        or 2 in self.gameState['score']['White'].values()
                    ):
                        return True, True
                    else:
                        self.nextRound()
                        return True, False

        return False, False

    def scoreGuess(self, team):
        guessRound = self.currentRound[team]
        otherTeam = self.otherTeam(team)
        guessRound['Actual'] = self.currentCode[team].copy()
        if guessRound[team] != guessRound['Actual']:
            self.gameState['score'][team]['Misses'] += 1
        if guessRound[otherTeam] == guessRound['Actual']:
            self.gameState['score'][otherTeam]['Hits'] += 1

    def nextRound(self):
        for team in ['White', 'Black']:
            self.gameState['hasCodeMaster'][team] = False
            self.gameState['hasClues'][team] = False
            self.gameState['hasGuess'][team] = False
            self.gameState['codeGuessed'][team] = False
            self.currentCode[team] = []
            self.gameState['teams'][team]['CodeMaster'] = {}

        _round = self.currentRound['White']['Round']
        self.newRound(_round + 1)

    def reset(self, sameTeam=False):
        _room = self.room
        _teams = self.gameState['teams'].copy()
        self.__init__()
        self.room = _room
        if sameTeam:
            self.gameState['teams'] = _teams.copy()
