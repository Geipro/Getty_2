<template>
  <div class="mt-5 justify-content-center align-items-center" style="text-align: center; width: 100%">
    <h2>적금</h2>
    <div class="d-lg-block col-lg-12 bg-success">
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col" >은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col">가입 방법</th>
            <th scope="col">중도상환 수수료</th>
            <th scope="col">연체 이자율</th>
            <th scope="col">대출 한도</th>
            <th scope="col">담보 유형</th>
            <th scope="col">대출 금리</th>
            <th scope="col">최저 금리</th>
            <th scope="col">최고 금리</th>
            <!-- <th scope="col">전월 평균</th> -->
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in mortgage" :key="idx">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.join_way }}</td>
            <td>{{ element.erly_rpay_fee }}</td>
            <td>{{ element.dly_rate }}</td>
            <td>{{ element.loan_lmt }}</td>
            <td>{{ element.mrtg_type_nm }}</td>
            <td>{{ element.lend_rate_avg }}</td>
            <td>{{ element.lend_rate_min }}</td>
            <td>{{ element.lend_rate_max }}</td>
            <td>{{ element.max_limit }}</td>

          </tr>
        </tbody>
      </table>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Savings',
  data: function () {
    return {
      mortgage: [],
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

      console.log(this.mortgage[0])
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
