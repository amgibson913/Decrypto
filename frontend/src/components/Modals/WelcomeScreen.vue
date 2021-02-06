<template>
    <v-card>
        <v-alert type="error" :value="error">Room does not exist!</v-alert>
        <v-card-title class="justify-center">Welcome to Decrypyto</v-card-title>
        <v-card-text class="text-center">
            <v-card-subtitle>You can click below to</v-card-subtitle>
            <v-btn @click.prevent="create">Create a room</v-btn>
            <v-card-subtitle>Or enter a room code below</v-card-subtitle>
            <v-form class="px-3" @submit.prevent="join" ref="roomInput">
                <v-text-field ref="input" v-model="roomCode" label="Join a room" :rules="inputRules" validate-on-blur></v-text-field>
                <v-btn @click.prevent="join">Join room</v-btn>
            </v-form>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: 'WelcomeScreen',
    data: function() {
        return {
            error: false,
            roomCode: '',
            inputRules: [
                v => v.length == 4 || this.roomError || 'Room codes are 4 characters'
            ]
        }
    },
    sockets: {
        joinError: function () {
            this.error = true
        }
    },
    methods: {
        join() {if (this.$refs.roomInput.validate()) { this.$socket.client.emit('join', {'room': this.roomCode}) }},
        create() { this.$socket.client.emit('create') }
    }
}
</script>

<style>

</style>