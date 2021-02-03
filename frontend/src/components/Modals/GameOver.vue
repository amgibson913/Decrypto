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
            var blackScore = this.score.Black.hits - this.score.Black.misses
            var whiteScore = this.score.White.hits - this.score.White.misses
            if (blackScore == whiteScore) {return "It's a draw!"}
            else if (blackScore > whiteScore) {return 'Black team wins!'}
            else {return 'White team wins!'}
        }
    }


}
</script>

<style>

</style>