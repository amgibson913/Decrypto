<template>
    <v-card>
        <v-card-title class="justify-center">Welcome to room {{ room }}</v-card-title>
        <v-card-text class="text-center">
            <v-form class="px-3" @submit.prevent="" ref="form">
                <v-card-subtitle>Enter a username below</v-card-subtitle>
                <v-text-field ref="input" v-model="username" label="Username" :rules="inputRules"></v-text-field>
                <v-card-subtitle>And choose a team</v-card-subtitle>
                <v-card-actions>
                    <v-card>
                        <v-btn @click.prevent="join('White')">Team White</v-btn>
                        <v-card-subtitle :key="player.user" v-for="player in teams['White']['Players']">{{ player }}</v-card-subtitle>
                    </v-card>
                    <v-spacer></v-spacer>
                    <v-card>
                        <v-btn @click.prevent="join('Black')">Team Black</v-btn>
                        <v-card-subtitle :key="player.user" v-for="player in teams['Black']['Players']">{{ player }}</v-card-subtitle>
                    </v-card>
                </v-card-actions>
            </v-form>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: 'ChooseTeam',
    props: ['room', 'teams'],
    data() {
        return {
            username: '',
            inputRules: [
                v => v.length > 0 || 'Username required'
            ]
        }
    },
    methods: {
        join: function(team) {
            if (this.$refs.form.validate()) { 
                this.$socket.client.emit('joinTeam', {'team': team, 'username': this.username})
            }
        }
    }
}
</script>

<style>

</style>