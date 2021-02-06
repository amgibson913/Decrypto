<template>
    <v-row no-gutters justify="center">
        <v-col cols=3 sm=2 v-for="(word, index) in words" :key="index">
            <v-card tile :color="(team=='White')? 'grey lighten-3' : 'grey darken-3'" :dark="team=='Black'" height="120px" class="d-flex justify-center align-center">
                <v-card-subtitle>{{ word }}</v-card-subtitle>
                <v-card-subtitle class=" pa-2 wordNumber">{{ index + 1 }}</v-card-subtitle>
            </v-card>
        </v-col>
    </v-row>  
</template>

<script>
export default {
    name: 'Words',
    props: ['team', 'words']
}
</script>

<style>
.wordNumber {
    position: absolute;
    bottom: 0%;
    right: 0%;
}
</style>