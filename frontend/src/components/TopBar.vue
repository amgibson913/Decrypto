<template>
    <v-app-bar app color="grey lighten-2">
        <v-tooltip v-model="copied" bottom>
            <template v-slot:activator="on">
                <v-btn @click="copy('localhost:8080?room='+room)" v-on="on">
                    <v-toolbar-title>Room: {{ room }}</v-toolbar-title>
                </v-btn>
            </template>
            <span>Link Copied!</span>
        </v-tooltip>
        <v-spacer></v-spacer>
        <v-toolbar-title>
            Black:
            <v-icon v-for="n in score.Black.Hits" :key="n">mdi-checkbox-marked-circle</v-icon>
            <v-icon v-for="n in score.Black.Misses" :key="n">mdi-skull-crossbones</v-icon>
            <v-spacer></v-spacer>
            White:
            <v-icon v-for="n in score.White.Hits" :key="n">mdi-checkbox-marked-circle</v-icon>
            <v-icon v-for="n in score.White.Misses" :key="n">mdi-skull-crossbones</v-icon>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn><v-icon>mdi-home</v-icon></v-btn>
    </v-app-bar>
</template>

<script>
export default {
    name: 'TopBar',
    props: ['room', 'score'],
    data () {
        return {
            copied: false
        }
    },
    methods: {
        async copy(s) {
            await navigator.clipboard.writeText(s)
            this.copied = true
            await new Promise(r => setTimeout(r, 2000))
            this.copied = false
        }
    }
}
</script>

<style>

</style>