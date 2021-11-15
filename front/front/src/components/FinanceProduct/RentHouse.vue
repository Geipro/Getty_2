<template>
  <div class="justify-content-center align-items-center" style="text-align: center; width: 100%">
    <Navbar />
    <h2 class="mt-3 mb-4">전세자금대출</h2>
    <div class="d-lg-block col-lg-12 bg-success">
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col" >은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col">대출 한도</th>
            <th scope="col">대출 금리</th>
            <th scope="col">최저 금리</th>
            <th scope="col">최고 금리</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in renthouse" :key="idx">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.loan_lmt }}</td>
            <td>{{ element.lend_rate_avg }}%</td>
            <td>{{ element.lend_rate_min }}%</td>
            <td>{{ element.lend_rate_max }}%</td>
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
  name: 'RentHouse',
  components: {
        Navbar,
    },
  data: function () {
    return {
      renthouse: [],
    }
  },
  created(){

  },
  mounted(){
    axios({
      method: 'get',
      url: 'https://k5a405.p.ssafy.io/backend/renthouse',
    })
    .then((res) =>{
      this.renthouse = res.data

      console.log(this.renthouse[0])
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
