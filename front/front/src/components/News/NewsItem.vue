<template>
  <div class="card" >
    <div class="card-inner">
      <div class="card-front">
        <img v-if="news.thumbnail.length ===0" src="@/assets/logo.png" class="logo-img">
        <img v-else :src="news.thumbnail" class="news-img">

        <div class="front-container">
          <p class="news-title" :title="news.title"> {{news.title}}</p>
        </div>
      </div>
      <div class="card-back">
        <div class="news-summary">
          <p>{{news.desc}}</p>
        </div>
        <div class="redirectbutton">
          <span>
            <a class="news-redirect" :title="news.title" :href="news.url"> 기사 페이지로 </a>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'NewsItem',
  props: {
    news: Object,
  },
  methods: {
    toggleCard: function(card) {
      card.flipped = !card.flipped;
    },

  }

}
</script>

<style scoped>
.card {
  display:inline-block;
  /* box-shadow: 0 3px 8px 3px rgba(255,255,255,0.1); */
  transition: 0.5s;
  width: 250px;
  height: 300px;
  border-radius: 10px;
  min-width: 0px;
  margin-left: 2em;
  margin-right: 2em;
  margin-top: 0em;
  margin-bottom: 4em;
  background-color: transparent;
  /* perspective: 1000px; */
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  /* text-align: center; */
  transition: transform 0.8s;
  transform-style: preserve-3d;
  border-radius: 10px;
  background-color: #0a192f;

}

.card:hover .card-inner {
  /* box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); */
  transform: rotateY(180deg);
}

/* Position the front and back side */
.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

.news-img {
  border-radius: 10px 10px 0px 0px;
  width:100%;
  height: 170px;
}

.logo-img {
  width: 150px;
  height: 150px;
  margin-top: 20px;
}


.front-container {
  padding: 0px 20px 0px 20px;
  word-wrap: break-word;
/* overflow: hidden; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.news-title {
  /* position: absolute;
  top: 50%;
  left: 50%; */
  font-size: 15px;
  /* overflow: hidden; */

  /* text-overflow: ellipsis; */
  /* white-space: nowrap; */
  /* color: white; */
  width: 100%;
  height: 130px;
  font-weight: bolder;
  /* margin-bottom: 2em; */
  /* cursor: pointer; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;

}


.card-back {
  transform: rotateY(180deg);
  /* width: 100%;
  height: 100%; */
  border-radius: 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.news-summary{
  background-color: #172a46;
  padding: 0px 20px 0px 20px;

  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 250px;

  /* flex-flow: row wrap; */
  overflow: hidden;
  border-radius: 10px 10px 0px 0px;
}

.redirectbutton {
  border-radius: 0px 0px 10px 10px;
  /* cursor: pointer; */
  /* background-color: #018786; */
  background-color: white;
  color: #018786;

  height: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  width: 100%;
}

.news-redirect {
  color: #018786;
  font-weight: bolder;
  font-size: 20px;

}

</style>
