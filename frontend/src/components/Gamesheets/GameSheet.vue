<template>
    <div class="d-flex flex-column align-center justify-space-around flex-wrap">
        <RoundCard v-for="round in sheet" :key="round.Round" :round="round"/>
    </div>
</template>

<script>
import RoundCard from './RoundCard.vue'

export default {
    name: 'GameSheet',
    props: ['sheet', 'color'],
    components: { RoundCard }
}
</script>

<style scoped>
div {
    height: 340px;
}
</style>