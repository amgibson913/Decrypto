<template>
<v-card>
    <v-card-title>{{ team }} Team</v-card-title>
    <v-row>
        <v-col>
            <v-chip-group column>
                <v-chip v-for="(player,index) in Object.values(players.Players)" :key=index outlined>
                    {{ player }}
                </v-chip>
            </v-chip-group>
            <v-btn v-if="pteam == team"
                :disabled="hasCodeMaster"
                @click="claimCodeMaster"
                outlined
                block
                small
                width="100%"
            ><v-avatar left size=32><v-icon>mdi-account-search</v-icon></v-avatar>{{ codeMaster }}</v-btn>
        </v-col>
    </v-row>
</v-card>
</template>

<script>
export default {
    name: 'TeamList',
    props: ['players', 'hasCodeMaster', 'team', 'pteam'],
    data() {
        return {
        }
    },
    methods: {
        claimCodeMaster: function() { this.$socket.client.emit('codeMaster', { 'team': this.pteam }) }
    },
    computed: {
        codeMaster: function() {
            return !this.hasCodeMaster ? 'Claim Codemaster' : Object.values(this.players.CodeMaster)[0] + ' is codemaster'
        }
    }
}
</script>

<style>

</style>