<template>
    <v-card v-if="wait" height="200px">
        <v-card-title class="justify-center">{{ message }}</v-card-title>
    </v-card>
    <v-card v-else-if="gameRound == 'needCodeMaster'" class="pa-2 d-flex flex-column justify-center align-center">
        <v-card-title>Your team has no codemaster yet</v-card-title>
        <v-btn large @click="claimCodeMaster">Become Codemaster</v-btn>
    </v-card>
    <v-card v-else-if="gameRound == 'needClues'" class="pa-2">
        <v-card-title>Your code is {{ code }}</v-card-title>
        <v-card-subtitle>Enter clues below</v-card-subtitle>
        <v-form ref="clueInput">
            <v-text-field v-model="clues[0]" :rules="clueRules" :label="words[code[0] - 1]" validate-on-blur></v-text-field>
            <v-text-field v-model="clues[1]" :rules="clueRules" :label="words[code[1] - 1]" validate-on-blur></v-text-field>
            <v-text-field v-model="clues[2]" :rules="clueRules" :label="words[code[2] - 1]" validate-on-blur></v-text-field>
            <v-btn block @click="submitClues" :disabled="cluesValid">{{ !cluesValid ? 'Submit' : 'Enter Clues' }}</v-btn>
        </v-form>
    </v-card>
    <v-card v-else-if="gameRound == 'needGuess'">
        <v-card-title class="justify-center pa-1">Guess the code!</v-card-title>
        <v-form ref="guessInput">
            <v-row>
                <v-col cols=4 v-for="i in [0,1,2]" :key="i">
                    <v-text-field
                        v-model="guess[i]"
                        class="px-5 centered-input"
                        readonly
                        prepend-inner-icon="mdi-minus"
                        append-icon="mdi-plus"
                        @click:append="increase(i)"
                        @click:prepend-inner="decrease(i)"
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-btn block @click="submitGuess" :disabled="codeValid">{{ !codeValid ? 'Submit' : 'Must be 3 unique numbers' }}</v-btn>
        </v-form>
    </v-card>
</template>

<script>
export default {
    name: "InputArea",
    props: ['gameState', 'team', 'code', 'words'],
    data() {
        return {
            guess: [1,1,1],
            clues: ['','',''],
            message: '',
            gameRound: '',
            clueRules: []
        }
    },
    methods: {
        changeRound(data) { this.gameRound = data },
        changeMessage(msg) { this.message = msg },
        claimCodeMaster() { this.$socket.client.emit('codeMaster', { 'team': this.team })},
        submitClues() {
            if (this.$refs.clueInput.validate()) {
            this.$socket.client.emit('clues', { 'team': this.team, 'clues': this.clues})
            this.clues = ['','','']
            }
        },
        submitGuess() {
            if (this.$refs.guessInput.validate()) {
                this.$socket.client.emit('guess', { 'team': this.team, 'guess': this.guess})
                this.guess = [1,1,1]
            }
        },
        increase(i) {
            if (this.guess[i] == 4) { this.$set(this.guess, i, 1) }
            else {this.$set(this.guess, i, this.guess[i]+1)}
        },
        decrease(i) {
            if (this.guess[i] == 1) {this.$set(this.guess, i,4)}
            else {this.$set(this.guess, i, this.guess[i]-1)}
        }
    },
    computed: {
        codeValid: function() {return (this.guess[0] == this.guess[1] || this.guess[0] == this.guess[2] || this.guess[1] == this.guess[2])},
        cluesValid: function() {return (this.clues[0] == '' || this.clues[1] == '' || this.clues[2] == '')},
        otherTeam: function() { return (this.team == 'White') ? 'Black' : 'White' },
        codeMaster: function() { return (this.code.length != 0) ? true : false },
        wait: function() {
            var msg

            //If either team is looking for a codemaster
            if (!this.gameState.hasCodeMaster[this.team]) {
                this.changeRound('needCodeMaster')
                return false
            }
            else if (!this.gameState.hasCodeMaster[this.otherTeam]) {
                this.changeMessage('Wait for the other team to pick a codemaster')
                return true
            }
            
            //If either team is waiting on clues
            if (!this.gameState.hasClues[this.team]) {
                if (this.codeMaster) {
                    this.changeRound('needClues')
                    return false
                }
                else {
                    msg = (this.gameState.hasClues[this.otherTeam]) ? 'Wait for your codemaster to submit clues'
                    : 'Wait for both codemasters to submit clues'
                    this.changeMessage(msg)
                    return true
                }
            }
            else if (!this.gameState.hasClues[this.otherTeam]) {
                this.changeMessage('Wait for the other codemaster to create clues')
                return true
            }

            //Time for guessing (or wait if you're the codemaster)
            if (!this.gameState.hasGuess[this.team]) {
                //If you're the codemaster and teams are guessing your clue
                if ((this.codeMaster && this.team == 'White' && !this.gameState.codeGuessed.White)
                    || (this.codeMaster && this.team == 'Black' && this.gameState.codeGuessed.White)) {
                    msg = (this.gameState.hasGuess[this.otherTeam]) ? 'Wait for your team to guess your code'
                        : 'Wait for both teams to guess your code'
                    this.changeMessage(msg)
                    return true
                }
                else {
                    this.changeRound('needGuess')
                    return false
                }
            }
            else if (!this.gameState.hasGuess[this.otherTeam]) {
                this.changeMessage('Wait for the other team to guess the code')
                return true
            }

            //Should not make it this far unless error occurs
            this.changeMessage('I think something went wrong')
            return true
        }
    }
}
</script>

<style scoped>
/deep/ .centered-input input {
  text-align: center
}
.v-card__text, .v-card__title {
    word-break: normal;
}
</style>