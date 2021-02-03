import eventlet
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms, close_room
from game import Game


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SESSION_TYPE'] = 'filesystem'

socketio = SocketIO(app)
games = {}  # Holds all game objects
players = {}  # Holds players and their corresponding room, for disconnects


@app.route('/')
def index():
    return "<p>Something isn't quite right here</p>"


@socketio.on('connect')
def connect():
    print(request.sid+' has connected')


@socketio.on('disconnect')
def disconnect():
    room = players.get(request.sid, None)
    print(request.sid+' has disconnected')
    if room and room in list(games):
        game = games[room]
        isEmpty = game.removePlayer(request.sid)
        if isEmpty:
            games.pop(room)
        else:
            emit('update', game.returnData(), room=room)

    players.pop(request.sid, None)


@socketio.on('create')
def create():
    game = Game()
    while game.room in list(games):
        game.regenerateRoomName()
    games.update({game.room: game})

    join_room(game.room)
    emit('joinRoom', {'room': game.room})
    emit('update', game.returnData())
    players.update({request.sid: game.room})
    print(game.room + ' created')


@socketio.on('join')
def joinRoom(data):
    room = data['room'].upper()
    if room in list(games):
        game = games[room]
        join_room(room)
        emit('joinRoom', game.returnData())
        players.update({request.sid: room})
    else:
        emit('joinError')


@socketio.on('joinTeam')
def chooseTeam(data):
    room = players[request.sid]
    team = data['team']
    username = data['username']
    if room in list(games):
        game = games[room]
        join_room(room+team)
        game.addPlayer(request.sid, team, username)
        emit('joinTeam', {'team': team, 'words': game.words[team]})
        emit('update', game.returnData(), room=room)


@socketio.on('codeMaster')
def codeMaster(data):
    team = data['team']
    room = players[request.sid]
    game = games.get(room, None)
    if game is not None:
        code = game.addCodeMaster(request.sid, team)
        if code is not None:
            emit('code', {'code': code})
    emit('update', game.returnData(), room=room)


@socketio.on('clues')
def clues(data):
    game = games.get(players[request.sid], None)
    team = data['team']
    clues = data['clues']
    if game is not None:
        game.submitClues(clues, team)
        emit('update', game.returnData(), room=game.room)


@socketio.on('guess')
def guess(data):
    game = games.get(players[request.sid], None)
    team = data['team']
    guess = data['guess']
    if game is not None:
        isRoundOver, isGameOver = game.submitGuess(guess, team)
        emit('update', game.returnData(), room=game.room)
        if isRoundOver:
            emit('code', {'code': []}, room=game.room)
        if isGameOver:
            emit('gameOver', room=game.room)


@socketio.on('chat')
def chat(data):
    team = data['team']
    room = players[request.sid]
    if room in list(games):
        game = games[room]
    username = game.gameState['teams'][team]['Players'][request.sid]
    emit('chat', {'username': username, 'msg': data['message']}, room=room+team)


@socketio.on('reset')
def reset(data):
    game = games.get(players[request.sid], None)
    if game is not None:
        if data['opt'] == 'same':
            game.reset(sameTeam=True)
            emit('words', {'words': ['','','','']}, room=game.room)
        else:
            game.reset()
            close_room(game.room+'White')
            close_room(game.room+'Black')
            emit('joinTeam', {'team': '', 'words': ['','','','']}, room=game.room)
            emit('update', game.returnData(), room=game.room)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', use_reloader=True)
