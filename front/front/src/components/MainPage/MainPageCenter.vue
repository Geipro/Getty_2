<template>
  <div class="mt-3 pb-3">
    <iframe width="900px" height="72px" src="https://s.tradingview.com/embed-widget/tickers/?locale=kr#%7B%22symbols%22%3A%5B%7B%22title%22%3A%22S%26P%20500%22%2C%22proName%22%3A%22FOREXCOM%3ASPXUSD%22%7D%2C%7B%22title%22%3A%22NASDAQ%20100%22%2C%22proName%22%3A%22FOREXCOM%3ANSXUSD%22%7D%2C%7B%22title%22%3A%22KOSPI%22%2C%22proName%22%3A%22KRX%3AKOSPI%22%7D%2C%7B%22title%22%3A%22KOSDAQ%22%2C%22proName%22%3A%22KRX%3AKOSDAQ%22%7D%2C%7B%22title%22%3A%22BTC%20Dominance%22%2C%22proName%22%3A%22CRYPTOCAP%3ABTC.D%22%7D%2C%7B%22title%22%3A%22BTC%20Longs%22%2C%22proName%22%3A%22BITFINEX%3ABTCUSDLONGS%22%7D%2C%7B%22title%22%3A%22BTC%20Shorts%22%2C%22proName%22%3A%22BITFINEX%3ABTCUSDSHORTS%22%7D%2C%7B%22title%22%3A%22GOLD%22%2C%22proName%22%3A%22TVC%3AGOLD%22%7D%5D%2C%22colorTheme%22%3A%22dark%22%2C%22showSymbolLogo%22%3Atrue%2C%22isTransparent%22%3Atrue%2C%22largeChartUrl%22%3A%22https%3A%2F%2Fkimpga.com%22%2C%22width%22%3A%22100%25%22%2C%22height%22%3A72%2C%22utm_source%22%3A%22kimpga.com%22%2C%22utm_medium%22%3A%22widget%22%2C%22utm_campai" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen allowtransparency="true" style="background: #FFFFFF;"></iframe>
    <div class="mt-3 mb-3 pb-3" style="text-align: center;">
      <iframe width="900px" height="320px" src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_c4176&symbol=BINANCE%3ABTCUSDT&interval=15&symboledit=1&saveimage=0&toolbarbg=f1f3f6&studies=%5B%5D&theme=Dark&style=1&timezone=Asia%2FSeoul&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=kr&utm_source=kimpga.com&utm_medium=widget&utm_campaign=chart&utm_term=BINANCE%3ABTCUSDT" frameborder="0"></iframe>
    </div>

    <div class="d-lg-block col-lg-12 bg-success">
      <!-- <b-table striped hover :items="items" :fields="fields"></b-table> -->

      <!-- <div><img :src=`https://static.upbit.com/logos/${imgName}.png`>{{ element.name }}</div> -->
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col" >이름</th>
            <th scope="col">현재가</th>
            <th scope="col">전일대비</th>
            <th scope="col">고가대비(52주)</th>
            <th scope="col">저가대비(52주)</th>
            <th scope="col">거래액(일)</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in crypto" :key="idx">
            <td>
              <div>{{ element.name }}</div>
              <div>{{ element.sym }}</div>
            </td>
            <td>{{ element.price | makeComma }}원</td>
            <td>
              <div>{{ (element.day_change_rate * 100).toFixed(2) }}</div>
              <div>{{ element.day_chage_price | makeComma }}원</div>
            </td>
            <td>
              <div>{{ element.highest_52_week_rate }} %</div>
              <div>{{ element.highest_52_week_price | makeComma }}원</div>
            </td>
            <td>
              <div>{{ element.lowest_52_week_rate }} %</div>
              <div>{{ element.lowest_52_week_price | makeComma }}원</div>
            </td>
            <td>
              <div>{{ Math.floor(element.acc_trade_price_24h / 100000000).toFixed(0) | makeComma }}억</div>
              <div>{{ Math.floor(element.acc_trade_volume_24h / 10000).toFixed(0) | makeComma }}개</div>
            </td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'MainPageCenter',
  data: function () {
    return {
      crypto: [],
    }
  },
  created(){

  },
  mounted(){
    axios({
      method: 'get',
      url: 'https://k5a405.p.ssafy.io/backend/sort?reverse_flag=true&case=name',
    })
    .then((res) =>{
      this.crypto = res.data

      console.log(this.crypto[0])
    }).catch((err) =>{
      console.log(err)
    })
  },
}
</script>

<style>

</style>
