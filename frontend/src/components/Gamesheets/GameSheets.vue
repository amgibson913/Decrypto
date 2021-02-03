<template>
    <v-row v-if="$vuetify.breakpoint.mdAndUp">
        <v-col cols=6><GameSheet :sheet="gamesheets.White" color="White" :team="team" :words="(team=='White')?words:''" /></v-col>
        <v-col cols=6><GameSheet :sheet="gamesheets.Black" color="Black" :team="team" :words="(team=='Black')?words:''" /></v-col>
    </v-row>
    <v-card v-else class="mx-auto">
        <v-tabs grow>
            <v-tab>White {{ (team == 'White') ? "(You)" : "(Them)" }}</v-tab>
            <v-tab>Black {{ (team == 'Black') ? "(You)" : "(Them)" }}</v-tab>
            <v-tab-item v-for="color in ['White', 'Black']" :key="color">
                <GameSheet :sheet="gamesheets[color]" :color="color" :words="(team==color)?words:''"/>
            </v-tab-item>
        </v-tabs>
    </v-card>
</template>

<script>
import GameSheet from './GameSheet2.vue'

export default {
    name: 'GameSheets',
    components: { GameSheet },
    props: ['gamesheets', 'team', 'words']
}
</script>

<style>
</style>