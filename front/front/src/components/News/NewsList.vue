<template>
    <div class="NewsList">
      <NewsItem v-for="(news, idx) in newsList" :key="idx" :news="news"/>
    </div>
</template>
<script>
import NewsItem from './NewsItem.vue'

export default {
    name: 'NewsList',
    components: {
        NewsItem,
    },
    props: {
      newsList: Object,
    },
    }

</script>
<style scoped>
    .news-list {
    margin-top: 47px;
    }
</style>
