<template>
    <v-data-table dense hide-default-footer class="elevation-1" :headers="headers" :items="rows">
    </v-data-table>
</template>

<script>
export default {
    name: 'RoundCard',
    props: ['round'],
    data() {
        return {
            headers: [
                {text: '# 0'+this.round.Round, value: 'Clue', width: "70%", align: 'center', sortable: false},
                {text: 'B', value: 'Black', width: "10%", align: 'end', sortable: false},
                {text: 'W', value: 'White', width: "10%", align: 'end', sortable: false},
                {text: 'A', value: 'Actual', width: "10%", align: 'end', sortable: false}
            ],
            rows: [
                {Clue: this.round.Clues[0], Black: this.round.Black[0], White: this.round.White[0], Actual: this.round.Actual[0]},
                {Clue: this.round.Clues[1], Black: this.round.Black[1], White: this.round.White[1], Actual: this.round.Actual[1]},
                {Clue: this.round.Clues[2], Black: this.round.Black[2], White: this.round.White[2], Actual: this.round.Actual[2]},
            ]

        }
    }
}
</script>

<style scoped>
th {
    background-color: lightgrey;
}
tr:nth-child(even) {
    background-color: lightgrey;
}
.test {
    width: 100%;
}
</style>