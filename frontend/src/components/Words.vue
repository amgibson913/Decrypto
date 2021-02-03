<template>
    <v-row no-gutters justify="center">
        <v-col cols=3 lg=2 v-for="(word, index) in words" :key="index">
            <v-card tile :color="(team=='White')? 'grey lighten-3' : 'grey darken-3'" height="120px" class="text-center">
                <div>{{ word }}</div>
                <v-card-subtitle>{{ index + 1 }}</v-card-subtitle>
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
</style>