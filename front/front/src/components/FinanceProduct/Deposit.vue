<template>
  <div class="mt-5 justify-content-center align-items-center" style="text-align: center; width: 100%">
    <h2>예금</h2>
    <div class="d-lg-block col-lg-12 bg-success">
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col" >은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col">가입 경로</th>
            <th scope="col">만기 후 이율</th>
            <th scope="col">우대 조건</th>
            <th scope="col">가입 제한</th>
            <th scope="col">최고 한도</th>
            <th scope="col">유의사항</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in Depo" :key="idx">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.join_way }}</td>
            <td>{{ element.interest_rate }}</td>
            <td>{{ element.preferential_term }}</td>
            <td>{{ element.join_deny }}</td>
            <td>{{ element.max_limit }}</td>
            <td>{{ element.etc_note }}</td>
          </tr>
        </tbody>
      </table>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Deposit',
  data: function () {
    return {
      Depo: [],
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

      console.log(this.Depo[0])
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
