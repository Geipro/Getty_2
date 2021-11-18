<template>
  <div class="justify-content-center align-items-center" style="text-align: center; width: 100%">
    <Navbar />
    <div class="inline-block mb-2">
      <a class="mt-3 mb-4 float-left" style="font-size: 30px">예금</a>
      <a class="float-right offset-10">금리 : %</a>
    </div>

    <div class="d-lg-block col-lg-12" style="background-color:#23282d" >
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning" style="text-align: left;">
            <th scope="col">은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col" style="text-align: center;">평균 금리</th>
            <th scope="col" style="text-align: center;">최고 금리</th>
            <th scope="col">가입 경로</th>
            <th scope="col">가입 제한</th>
            <th scope="col" style="text-align: right;">최고 한도(원)</th>
            <th scope="col" style="text-align: center;">상세정보</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in Depo" :key="idx" style="text-align: left;">

            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td style="text-align: center;">{{ element.intr_rate }}</td>
            <td style="text-align: center;">{{ element.intr_rate2 }}</td>
            <td>{{ element.join_way }}</td>
            <td>{{ element.join_deny }}</td>
            <td style="text-align: right;">{{ isEmpty(element.max_limit) | makeComma }}</td>
            <td style="text-align: center;">
              <b-button v-b-modal="'myModal' + idx">상세</b-button>

              <b-modal :id="'myModal' + idx" title="상세페이지" cancel-title="취소" ok-title="확인">
                <p>우대조건 <br> {{ element.preferential_term }}</p>
                <p>유의사항 <br> {{ element.etc_note }}</p>
                <p>만기 후 이율 <br> {{ element.interest_rate }}</p>
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
  name: 'Deposit',
  components: {
        Navbar,
    },
  data: function () {
    return {
      Depo: [],
      items_avg : [],

      isEmpty(value){
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
      url: 'https://k5a405.p.ssafy.io/backend/deposit',
    })
    .then((res) =>{
      this.Depo = res.data
      this.items_avg = this.Depo.sort((a, b) => {return b.intr_rate - a.intr_rate})
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
