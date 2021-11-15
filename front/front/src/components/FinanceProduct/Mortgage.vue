<template>
  <div class="justify-content-center align-items-center" style="text-align: center; width: 100%">
    <Navbar />
    <h2 class="mt-3 mb-4">주택담보대출</h2>
    <p class="mt-3 mb-4" style="text-align: right;">금리 : %</p>
    <div class="d-lg-block col-lg-12 bg-success">
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col" >은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col">대출 한도</th>
            <th scope="col">담보 유형</th>
            <th scope="col">최저 금리</th>
            <th scope="col">최고 금리</th>
            <th scope="col">평균 금리</th>
            <th scope="col">상세 정보</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in mortgage" :key="idx">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.loan_lmt }}</td>
            <td>{{ element.mrtg_type_nm }}</td>
            <td>{{ isEmpty2(element.lend_rate_min) }}</td>
            <td>{{ isEmpty2(element.lend_rate_max) }}</td>
            <td>{{ isEmpty2(element.lend_rate_avg) }}</td>
            <td><!-- modal 방식 -->
                <b-button v-b-modal="'myModal' + idx">상세</b-button>

                <b-modal :id="'myModal' + idx" title="상세페이지">
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
      this.mortgage = res.data
      // 최저 금리 순으로(왜 주택담보대출만 정렬이 안되지?)
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
