<template>
    <v-app>
        <v-dialog v-model="needRoom" max-width="600px" persistent :fullscreen="$vuetify.breakpoint.smAndDown"><WelcomeScreen /></v-dialog>
        <v-dialog v-model="needTeam" max-width="600px" persistent :fullscreen="$vuetify.breakpoint.smAndDown"><ChooseTeam :room="room" :teams="gameState['teams']" /></v-dialog>
        <v-dialog v-model="gameOver" max-width="600px" :fullscreen="$vuetify.breakpoint.smAndDown"><GameOver :teams="gameState['teams']" :score="gameState['score']" /></v-dialog>
        <TopBar :room="room" :score="gameState.score" app/>
        <v-main>
            <v-container fluid>
                <v-row>
                    <v-col cols=12 lg=7 order-lg=2><GameSheets :gamesheets="gamesheets" :team="team" :words="words" /></v-col>
                    <v-col cols=12 md=6 lg=3 order-lg=1>
                        <v-row>
                            <v-col cols=12><InputArea :gameState="gameState" :team="team" :code="code" :words="words" /></v-col>
                            <v-col cols=12><TeamChat :team="team" :gameState="gameState" :code="code"/></v-col>
                        </v-row>
                    </v-col>
                    <v-col cols=12 md=6 lg=2 order-lg=3>
                        <v-row>
                            <v-col cols=12><TeamList :pteam="team" team="White" :players="gameState.teams.White" :hasCodeMaster="gameState.hasCodeMaster.White" /></v-col>
                            <v-col cols=12><TeamList :pteam="team" team="Black" :players="gameState.teams.Black" :hasCodeMaster="gameState.hasCodeMaster.Black" /></v-col>
                        </v-row>
                    </v-col>
                    <v-col cols=12 order=4><Words :team="team" :words="words" /></v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
import WelcomeScreen from './components/Modals/WelcomeScreen.vue'
import ChooseTeam from './components/Modals/ChooseTeam.vue'
import GameSheets from './components/Gamesheets/GameSheets.vue'
import TeamList from './components/TeamList.vue'
import TeamChat from './components/TeamChat.vue'
import InputArea from './components/InputArea.vue'
import TopBar from './components/TopBar.vue'
import Words from './components/Words.vue'
import GameOver from './components/Modals/GameOver.vue'


export default {
    name: 'App',
    components: { WelcomeScreen, ChooseTeam, GameSheets, TeamList, TeamChat, InputArea, TopBar, Words, GameOver },
    data() {
        return {
            room: '',
            team: '',
            gamesheets: {
                'White': [
                    {Round: 1, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 2, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 3, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 4, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 5, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 6, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 7, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 8, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']}
                ],
                'Black': [
                    {Round: 1, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 2, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 3, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 4, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 5, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 6, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 7, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']},
                    {Round: 8, Clues: ['','',''], Black: ['','',''], White: ['','',''], Actual: ['','','']}
                ]
            },
            code: [],
            words: [],
            gameOver: false,
            gameState: {
                'hasCodeMaster': {'Black': false, 'White': false},
                'hasClues': {'Black': false, 'White': false},
                'hasGuess': {'Black': false, 'White': false},
                'codeGuessed': {'Black': false, 'White': false},
                'teams': {
                    'Black': {'Players': {}, 'CodeMaster': {}},
                    'White': {'Players': {}, 'CodeMaster': {}}},
                'score': {
                    'Black': {'Hits': 0, 'Misses': 0},
                    'White': {'Hits': 0, 'Misses': 0}
                }
            }
        }
    },
    computed: {
        needRoom: function() { return !this.room },
        needTeam: function() { return (this.room) ? !this.team : false },
    },
    sockets: {
        joinRoom(data) {
            this.gameState = data['gameState']
            this.gamesheets = data['gamesheets']
            this.room = data['room']
        },
        update(data) {
            this.gamesheets = data['gamesheets']
            this.gameState = data['gameState']
        },
        joinTeam(data) {
            this.team = data['team']
            this.words = data['words']
        },
        code(data) {
            this.code = data['code']
        },
        gameOver() {
            this.gameOver = true
        },
        words(data) {
            this.words = data['words']
        }
    },
    created() {
        let urlParams = new URLSearchParams(window.location.search)
        if (urlParams.has('room')) { this.$socket.client.emit('join', {'room':urlParams.get('room')})}
    }
}
</script>

<style>
#app {
    font-family: monospace;
    background: url("https://images.unsplash.com/photo-1532153259564-a5f24f261f51?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&h=500&q=80");
}
</style>