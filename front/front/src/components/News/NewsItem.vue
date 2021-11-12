<template>
  <div class="card" >
    <img :src="news.thumbnail" class="news-img" >
    <div class="container">
      <a class="news-title" :title="news.title" :href="news.url"> {{news.title}}</a>
    </div>
  </div>
</template>

<script>

export default {
  name: 'NewsItem',
  props: {
    news: Object,
  },
}
</script>

<style scoped>
.card {
  display:inline-block;
  box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
  border-radius: 20px;
  min-width: 0px;
  margin-left: 2em;
  margin-right: 2em;
  margin-top: 0em;
  margin-bottom: 4em;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.news-img {
  width: 100%;
  border-radius: 20px;
}

.container {
  padding: 18px 18px 18px 18px;
  overflow: hidden;
}

.news-title {
  font-size: 20px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: blue;
  margin-bottom: 2em;
  cursor: pointer;

}



.news-list{
  display: flex;
  flex-flow: row wrap;
  overflow: hidden;
  height: 38px;
}

</style>
