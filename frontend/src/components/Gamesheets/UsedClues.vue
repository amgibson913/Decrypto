<template>
    <v-card
        tile
        outlined
        height="120px"
        :color="(clue % 2 == 0) ? 'grey' : 'grey lighten-2'"
        class="caption"
    >
        <div><v-icon small>mdi-key</v-icon>{{ clue }}</div>
        <div v-for="word in clues" :key="word">{{ word }}</div>
    </v-card>
</template>

<script>
export default {
    name: 'UsedClues',
    props: ['clues', 'clue']
}
</script>

<style scoped>
.v-card {
    clip-path: polygon(
        0% 0%,
        50% 0%,
        60% 10%,
        100% 10%,
        100% 100%,
        0% 100%
    );
}
</style>