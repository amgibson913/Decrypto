<template>
    <v-card>
        <v-card-title>Team Chat</v-card-title>
        <v-virtual-scroll
            :items="chat"
            height="150"
            item-height="25"
            id="chatWindow"
        >
            <template v-slot:default="{ item }">
                <v-list-item :key="item.id" class="word-wrap">
                    <v-chip small>{{ item.author }}</v-chip>
                    : {{ item.message }}
                </v-list-item>
            </template>
        </v-virtual-scroll>
        <v-form @submit.prevent="send" ref="chat" class="px-3 py-0">
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
            document.getElementById('chatWindow').scrollBy(0, 9999)
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