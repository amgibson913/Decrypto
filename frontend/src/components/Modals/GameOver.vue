<template>
    <v-card>
        <v-card-title class="justify-center">Game Over!</v-card-title>
        <v-card-subtitle class="text-center">{{ result }}</v-card-subtitle>
        <v-card-text>
            <v-row class="justify-space-around text-center">
                <v-col cols=6>
                    <v-card-subtitle>Black score: {{ score.Black.Hits - score.Black.Misses }}</v-card-subtitle>
                    <v-icon v-for="n in score.Black.Hits" :key="n">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-for="n in score.Black.Misses" :key="n">mdi-skull-crossbones</v-icon>
                </v-col>
                <v-col cols=6>
                    <v-card-subtitle>White score: {{ score.White.Hits - score.White.Misses }}</v-card-subtitle>
                    <v-icon v-for="n in score.White.Hits" :key="n">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-for="n in score.White.Misses" :key="n">mdi-skull-crossbones</v-icon>
                </v-col>
            </v-row>
            <v-card-subtitle class="text-center">Play again?</v-card-subtitle>
        </v-card-text>
        <v-card-actions>
            <v-btn @click="reset('same')">Same Teams</v-btn>
            <v-spacer></v-spacer>
            <v-btn @click="reset('new')">New Teams</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    name: 'GameOver',
    props: ['teams', 'score'],
    methods: {
        reset(opt) { this.$socket.client.emit('reset', {'opt': opt})}
    },
    computed: {
        result: function() {
            if (this.score.Black.Misses == 2 && this.score.White.Misses < 2) {
                if (this.score.Black.Hits == 2) {return this.tiebreaker}
                else {return "White Team Wins!"}
            }
            else if (this.score.White.Misses == 2 && this.score.Black.Misses < 2) {
                if (this.score.White.Hits == 2) {return this.tiebreaker}
                else {return "Black Team Wins!"}
            }
            else if (this.score.Black.Hits == 2 && this.score.White.Hits < 2) {return "Black Team Wins!"}
            else if (this.score.White.Hits == 2) {return "White Team Wins!"}
            else {return "Something Went Wrong"}
        },
        tiebreaker: function() {
            var blackScore = this.score.Black.hits - this.score.Black.misses
            var whiteScore = this.score.White.hits - this.score.White.misses
            if (blackScore == whiteScore) {return "It's A Draw!"}
            else if (blackScore > whiteScore) {return 'Black Team Wins!'}
            else {return 'White Team Wins!'}
        }
    }


}
</script>

<style>

</style>