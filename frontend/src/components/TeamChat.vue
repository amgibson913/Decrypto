<template>
    <v-card class="d-flex flex-column fill-height" max-height="340px">
        <v-card-title>Team Chat</v-card-title>
        <v-card-text class="flex-grow-1 overflow-y-auto" id="chatWindow">
            <div v-for="(msg, i) in chat" :key="i">{{ msg.author }}: {{ msg.message }}</div>
        </v-card-text>
        <v-form @submit.prevent="send" ref="chat" class="px-3 py-0">
            <v-text-field
                v-model="message"
                :append-icon="'mdi-send'"
                @click:append="send"
                dense
            ></v-text-field>
        </v-form>
    </v-card>
</template>

<script>
export default {
    name: 'TeamChat',
    props: ['gameState', 'team', 'code'],
    data() {
        return {
            chat: [],
            message: ''
        }
    },
    sockets: {
        chat: function(data) {
            this.chat.push({
                'id': this.chat.length + 1,
                'author': data['username'],
                'message': data['msg']})
            document.getElementById("chatWindow").scrollTo(0, 9999)
        }
    },
    methods: {
        send() {
            if (this.message !== '') {
                this.$socket.client.emit('chat', {'message': this.message, 'team': this.$props.team})
                this.message = ''
            }
        }
    }
}
</script>

<style>
</style>