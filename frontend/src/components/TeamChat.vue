<template>
    <v-card>
        <v-card-title>Team Chat</v-card-title>
        <v-list>
            <v-list-item :key="line.id" v-for="line in chat">{{ line.author }}: {{ line.message }}</v-list-item>
        </v-list>
        <v-form @submit.prevent="send" ref="chat" class="px-3">
            <v-text-field
                v-model="message"
                :append-icon="'mdi-send'"
                @click:append="send"
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