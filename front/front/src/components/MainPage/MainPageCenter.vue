<template>
  <div class="mt-3 pb-3">
    <iframe width="900px" height="72px" src="https://s.tradingview.com/embed-widget/tickers/?locale=kr#%7B%22symbols%22%3A%5B%7B%22title%22%3A%22S%26P%20500%22%2C%22proName%22%3A%22FOREXCOM%3ASPXUSD%22%7D%2C%7B%22title%22%3A%22NASDAQ%20100%22%2C%22proName%22%3A%22FOREXCOM%3ANSXUSD%22%7D%2C%7B%22title%22%3A%22KOSPI%22%2C%22proName%22%3A%22KRX%3AKOSPI%22%7D%2C%7B%22title%22%3A%22KOSDAQ%22%2C%22proName%22%3A%22KRX%3AKOSDAQ%22%7D%2C%7B%22title%22%3A%22BTC%20Dominance%22%2C%22proName%22%3A%22CRYPTOCAP%3ABTC.D%22%7D%2C%7B%22title%22%3A%22BTC%20Longs%22%2C%22proName%22%3A%22BITFINEX%3ABTCUSDLONGS%22%7D%2C%7B%22title%22%3A%22BTC%20Shorts%22%2C%22proName%22%3A%22BITFINEX%3ABTCUSDSHORTS%22%7D%2C%7B%22title%22%3A%22GOLD%22%2C%22proName%22%3A%22TVC%3AGOLD%22%7D%5D%2C%22colorTheme%22%3A%22dark%22%2C%22showSymbolLogo%22%3Atrue%2C%22isTransparent%22%3Atrue%2C%22largeChartUrl%22%3A%22https%3A%2F%2Fkimpga.com%22%2C%22width%22%3A%22100%25%22%2C%22height%22%3A72%2C%22utm_source%22%3A%22kimpga.com%22%2C%22utm_medium%22%3A%22widget%22%2C%22utm_campai" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen allowtransparency="true" style="background: #FFFFFF;"></iframe>
    <div class="mt-3 mb-3 pb-3" style="text-align: center;">
      <iframe width="900px" height="320px" src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_c4176&symbol=BINANCE%3ABTCUSDT&interval=15&symboledit=1&saveimage=0&toolbarbg=f1f3f6&studies=%5B%5D&theme=Dark&style=1&timezone=Asia%2FSeoul&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=kr&utm_source=kimpga.com&utm_medium=widget&utm_campaign=chart&utm_term=BINANCE%3ABTCUSDT" frameborder="0"></iframe>
    </div>

    <!-- table은 data binding해서 하면됨 지금은 보여주기용 데이터 바인딩 후 코드 짧아짐 -->
    <div class="d-lg-block col-lg-12">
      <!-- <table
        id="table"
        data-toggle="table"
        data-sort-class="table-active"
        data-sortable="true"
        data-height="460"
        class="table table-bg-light table-hover"
        data-url="json/data1.json">
        <thead>
          <tr class="text-white">
            <th data-field="id" data-sortable="true">ID</th>
            <th data-field="name" data-sortable="true">Item Name</th>
            <th data-field="price" data-sortable="true">Item Price</th>
            <th data-field="price" data-sortable="true">Item Price</th>
            <th data-field="price" data-sortable="true">Item Price</th>
            <th data-field="price" data-sortable="true">Item Price</th>
          </tr>
        </thead>
         <tbody>
        <tr class="text-white">
          <td scope="row">1</td>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr class="text-white">
          <td scope="row">2</td>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr class="text-white">
          <td scope="row">3</td>
          <td>@twitter</td>
          <td>@twitter</td>
          <td>@twitter</td>
          <td>@twitter</td>
          <td>@twitter</td>
        </tr>
        </tbody>
      </table> -->


      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col">이름</th>
            <th scope="col">현재가</th>
            <th scope="col">전일대비</th>
            <th scope="col">고가대비(52주)</th>
            <th scope="col">저가대비(52주)</th>
            <th scope="col">거래액(일)</th>
          </tr>
        </thead>
        <tbody>
          <!-- 단위 / align 배치 수정 필요 -->
          <tr class="text-white" v-for="(element, idx) in crypto" :key="idx">
            <!-- <td colspan="2">{{ element.name }} <br> {{ element.sym }}</td> -->
            <td>
              <div>{{ element.name }}</div>
              <div>{{ element.sym }}</div>
            </td>
            <td>{{ element.price | makeComma }} </td>
            <td>
              <div>{{ (element.day_change_rate * 100).toFixed(2) }}</div>
              <div>{{ element.day_chage_price | makeComma }}</div>
            </td>
            <td>
              <div>{{ element.highest_52_week_rate }} %</div>
              <div>{{ element.highest_52_week_price | makeComma }}</div>
            </td>
            <td>
              <div>{{ element.lowest_52_week_rate }} %</div>
              <div>{{ element.lowest_52_week_price | makeComma }}</div>
            </td>
            <td>
              <div>{{ Math.floor(element.acc_trade_price_24h / 100000000).toFixed(0) | makeComma }} 억</div>
              <div>{{ Math.floor(element.acc_trade_won_24h / 100000000).toFixed(0) | makeComma }} 억</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</template>

<script>
import axios from 'axios';
import { numToKorean } from 'num-to-korean'



export default {
  name: 'MainPageCenter',
  data: function () {
    return {
      crypto: []
    }
  },
  getVolume(volume) {
    return numToKorean(Math.floor(volume / 100000000) * 100000000, 'mixed')
  },
  //  numberToKorean(number){
  //   var inputNumber  = number < 0 ? false : number;
  //   var unitWords    = ['', '만', '억', '조', '경'];
  //   var splitUnit    = 10000;
  //   var splitCount   = unitWords.length;
  //   var resultArray  = [];
  //   var resultString = '';

  //   for (var i = 0; i < splitCount; i++){
  //        var unitResult = (inputNumber % Math.pow(splitUnit, i + 1)) / Math.pow(splitUnit, i);
  //       unitResult = Math.floor(unitResult);
  //       if (unitResult > 0){
  //           resultArray[i] = unitResult;
  //       }
  //   }

  //   for (var j = 0; j < resultArray.length; j++){
  //       if(!resultArray[j]) continue;
  //       resultString = String(resultArray[j]) + unitWords[j] + resultString;
  //   }

  //   return resultString;
  // },
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
  }
}
</script>

<style>

</style>
