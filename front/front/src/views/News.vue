<template>
  <div class="main text-center">
    <Navbar/>
    <input
    type="text"
    class="search-query"
    placeholder="뉴스 검색어를 입력해 주세요."
    v-model="searchQuery"
    v-on:keyup.enter="findNews"
    />
    <div class="newslist">
      <NewsList :newsList="newsList" />
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/MainPage/Navbar.vue'
import axios from 'axios';
import NewsList from '@/components/News/NewsList.vue'

export default {
  components: {
    Navbar,
    NewsList,
  },
  data() {
    return {
      searchQuery: '',
      newsList: [],
      noResult: false,
    };
  },
  methods: {
    findNews: function() {
      axios
        .get('https://k5a405.p.ssafy.io/backend/news/' + encodeURI(this.searchQuery, 'utf-8'))
        .then((response) => {
          this.newsList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.clearInput();
    },

clearInput: function() {
      this.searchQuery = "";
    }
  }
}
</script>

<style>
.search-query {
  padding: 10px 3px 10px 6px;
  border-radius: 5px;
  border: 1px solid #dacca6;
  width: 500px;
  font-size: 14px;
  text-indent: 0.5em;
  margin-bottom: 4em;
  margin-top: 2em
}
</style>
