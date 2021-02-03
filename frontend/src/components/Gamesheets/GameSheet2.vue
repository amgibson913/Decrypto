<template>
<v-card :color="(color == 'White') ? 'grey lighten-3' : 'grey darken-3'" width="371px">
    <v-card-subtitle
        :class="(color == 'White') ? 'black--text' : 'white--text'"
    >{{ color }} {{ (team == color) ? "(You)" : "(Them)" }}</v-card-subtitle>
    <v-row no-gutters align="center">
        <v-col cols="6" v-for="round in 8" :key="round"><RoundCard :round="sheet[round-1]"/></v-col>
        <v-col>
            <v-row no-gutters>
                <v-col cols="3" v-for="i in 4" :key="i">
                    <UsedClues :clues="clues(i)" :clue="i"/>
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</v-card>
</template>

<script>
import RoundCard from './RoundCard.vue'
import UsedClues from './UsedClues.vue'

export default {
    name: 'GameSheet',
    props: ['sheet', 'color', 'team', 'words'],
    components: { RoundCard, UsedClues },
    methods: {
        clues: function(clue) {
            var l = []
            for ( var i = 0; i < this.sheet.length; i++) {
                for ( var j = 0; j < 3; j++) {
                    if (this.sheet[i].Actual[j] == clue) {
                        l.push(this.sheet[i].Clues[j])
                    }
                }
            }
            return l
        }
    }
}
</script>

<style>
</style>