<template>
    <v-card color="grey lighten-2" height="80px" width="180px" class="caption my-1 mx-auto rounded-tr-lg rounded-bl-lg card">
        <v-row no-gutters class="header">
            <v-spacer></v-spacer>
            <v-col cols=8># 0{{ round.Round }}</v-col>
            <v-col>B</v-col>
            <v-col>W</v-col>
            <v-col>A</v-col>
        </v-row>
        <v-row v-for="i in 3" :key="i" no-gutters>
            <v-spacer></v-spacer>
            <v-col cols=8>{{ round.Clues[i-1] }}</v-col>
            <v-col>{{ round.Black[i-1] }}</v-col>
            <v-col>{{ round.White[i-1] }}</v-col>
            <v-col>{{ round.Actual[i-1] }}</v-col>
        </v-row>
    </v-card>
</template>

<script>
export default {
    name: 'RoundCard',
    props: ['round']
}
</script>

<style scoped>
.card {
    clip-path: polygon(
        0% 15%,
        5% 0%,
        45% 0%,
        50% 10%,
        60% 10%,
        65% 0%,
        100% 0%,
        100% 100%,
        0% 100%
    );
}
.row:nth-child(odd) {
    background-color: grey;
}
</style>