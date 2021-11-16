<template>
  <div class="card" >
    <div class="card-inner">
      <div class="card-front">
        <img :src="news.thumbnail" class="news-img" >
        <div class="front-container">
          <p class="news-title" :title="news.title"> {{news.title}}</p>
        </div>
      </div>
      <div class="card-back">
        <div class="news-summary">
          <!-- <p>{{news.desc}}</p> -->
          <p>'탭루트' 업데이트로 거래 보안·효율성 개선 정성호 특파원 = 최대 가상화폐 비트코인이 4년 만에 업데이트되면서 비트코인 네트워크에서 중개인 없는 거래가 가능한 '스마트 계약'이 더 활성화될 전망이다. CNBC는... </p>
        </div>
        <div class="redirectbutton">
          <a class="news-redirect" :title="news.title" :href="news.url"> 기사 페이지로 </a>
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
  background-color: #0a192f;
  border-radius: 10px;

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
}

.front-container {
  padding: 18px 18px 18px 18px;
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
  color: white;
  font-weight: bolder;
  margin-bottom: 2em;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
}


.card-back {
  background-color: #172a46;
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
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 250px;

  /* flex-flow: row wrap; */
  overflow: hidden;
  border-radius: 0px 0px 10px 10px;
}

.redirectbutton {
  border-radius: 0px 0px 10px 10px;
  cursor: pointer;
  color: white;

}

</style>
