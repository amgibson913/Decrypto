<template>
    <v-card>
        <v-card-title>Team Chat</v-card-title>
        <v-virtual-scroll
            :items="chat"
            height="170"
            :item-height="25"
            id="chatWindow"
        >
            <template v-slot:default="{ item }">
                <v-list-item>
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
            document.getElementById('chatWindow').scrollTo(0, 9999)
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