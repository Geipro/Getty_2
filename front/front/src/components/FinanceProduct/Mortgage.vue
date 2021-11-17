<template>
  <div class="justify-content-center align-items-center" style="text-align: center; width: 100%">
    <Navbar />
    <div class="inline-block mb-2">
      <a class="mt-3 mb-4 float-left" style="font-size: 30px">주택담보대출</a>
      <a class="float-right offset-9">금리 : %</a>
    </div>
    <div class="d-lg-block col-lg-12" style="background-color:#23282d" >
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning" style="text-align: left;">
            <th scope="col" >은행 이름</th>
            <th scope="col">상품 이름</th>
            <th scope="col">대출 한도</th>
            <th scope="col">담보 유형</th>
            <th scope="col" style="text-align: center;">최저 금리</th>
            <th scope="col" style="text-align: center;">최고 금리</th>
            <th scope="col" style="text-align: center;">평균 금리</th>
            <th scope="col" style="text-align: center;">상세 정보</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in mortgage" :key="idx" style="text-align: left;">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.loan_lmt }}</td>
            <td>{{ element.mrtg_type_nm }}</td>
            <td style="text-align: center;">{{ element.lend_rate_min }}</td>
            <td style="text-align: center;">{{ element.lend_rate_max }}</td>
            <td style="text-align: center;">{{ element.lend_rate_avg }}</td>
            <td style="text-align: center;"><!-- modal 방식 -->
                <b-button v-b-modal="'myModal' + idx">상세</b-button>

                <b-modal :id="'myModal' + idx" title="상세페이지" cancel-title="취소" ok-title="확인">
                  <p>중도상환 수수료 <br> {{ element.erly_rpay_fee }}</p>
                  <p>연체 이자율 <br> {{ element.dly_rate }}</p>
                  <p>가입 방법 <br> {{ element.join_way }}</p>
                </b-modal>
            </td>
          </tr>
          <tr class="text-white" v-for="(element, index) in mortgage_no_avg" :key="index" style="text-align: left;">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.loan_lmt }}</td>
            <td>{{ element.mrtg_type_nm }}</td>
            <td style="text-align: center;">{{ isEmpty2(element.lend_rate_min) }}</td>
            <td style="text-align: center;">{{ isEmpty2(element.lend_rate_max) }}</td>
            <td style="text-align: center;">{{ isEmpty2(element.lend_rate_avg) }}</td>
            <td style="text-align: center;"><!-- modal 방식 -->
                <b-button v-b-modal="'myModal2' + index">상세</b-button>

                <b-modal :id="'myModal2' + index" title="상세페이지" cancel-title="취소" ok-title="확인">
                  <p>중도상환 수수료 <br> {{ element.erly_rpay_fee }}</p>
                  <p>연체 이자율 <br> {{ element.dly_rate }}</p>
                  <p>가입 방법 <br> {{ element.join_way }}</p>
                </b-modal>
            </td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Navbar from '@/components/MainPage/Navbar.vue'

export default {
  name: 'Mortgage',
  components: {
        Navbar,
    },
  data: function () {
    return {
      mortgage: [],
      mortgage_no_avg: [],
      items_avg: [],
      isEmpty2(value){
        if(value == null || value.length === 0) {
           return "-";
        } else{
          return value;
        }
      }
    }
  },
  created(){

  },
  mounted(){
    axios({
      method: 'get',
      url: 'https://k5a405.p.ssafy.io/backend/mortgage',
    })
    .then((res) =>{
      // Object.keys(object_1).includes('test_1')
      for(let i = 0; i < res.data.length; ++i){
        if(Object.keys(res.data[i]).includes("lend_rate_avg") === false){
          this.mortgage_no_avg.push(res.data[i])
          continue
        }
        if(res.data[i]["lend_rate_avg"] == "" ||res.data[i]["lend_rate_max"] == "" ||res.data[i]["lend_rate_min"] == ""){
          this.mortgage_no_avg.push(res.data[i])
          continue
        }
        this.mortgage.push(res.data[i])
        // console.log(res.data[i])
      }
      // console.log(this.mortgage)
      // console.log(this.mortgage_no_avg)
      this.items_avg = this.mortgage.sort((a, b) => {return a.lend_rate_avg - b.lend_rate_avg })
      // this.items_min = this.mortgage.sort((a, b) => {return (a === 0) - (b === 0) || a.lend_rate_min - b.lend_rate_min })
    }).catch((err) =>{
      console.log(err)
    })
  },
}
</script>

<style>
.content {
    /* background: #f2f2f2; */
    padding: 50px;
    text-align: center;
    display: table-cell;
    vertical-align: middle;
}
</style>
