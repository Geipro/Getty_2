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
  // watch: {
  //   search: function (val) {
  //     axios
  //       .get('http://127.0.0.1/news/' + encodeURI(val, 'utf-8'))
  //       .then((response) => {
  //         this.Newslist = response.data;
  //         console.log(this.NewsList);
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  // },
  data() {
    return {
      searchQuery: '',
      newsList: [],
      noResult: false,
    };
  },
  methods: {
    findNews: function() {
      console.log(this.searchQuery);
      console.log('http://127.0.0.1:8000/news/' + encodeURI(this.searchQuery, 'utf-8'));
      // axios
      //   .get('http://127.0.0.1:8000/news/' + encodeURI(this.searchQuery, 'utf-8'))
      //   .then((response) => {
      //     this.newslist = response.data;
      //     console.log(this.newslist);
      //   })
      //   .catch((error) => {
      //     console.log(error);
      //   });
      axios
        .get('/news/' + encodeURI(this.searchQuery, 'utf-8'))
        .then((response) => {
          this.newsList = response.data;
          console.log(this.newsList);
        })
        .catch((error) => {
          console.log(error);
        });
// 클릭 후 저장
      // localStorage.setItem('key', 'value')
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
