<template>
  <div class="justify-content-center align-items-center" style="text-align: center; width: 100%">
    <Navbar />
    <h2 class="mt-3 mb-4">예금</h2>
    <p class="mt-3 mb-4" style="text-align: right;">금리 : %</p>
    <div class="d-lg-block col-lg-12 bg-success">
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <!-- <b-table :items="items" :fields="this.fields"></b-table> -->
            <th scope="col">은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col">평균 금리</th>
            <th scope="col">최고 금리</th>
            <th scope="col">가입 경로</th>
            <th scope="col">가입 제한</th>
            <th scope="col">최고 한도(원)</th>
            <th scope="col">상세정보</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in Depo" :key="idx">

            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.intr_rate }}</td>
            <td>{{ element.intr_rate2 }}</td>
            <td>{{ element.join_way }}</td>
            <td>{{ element.join_deny }}</td>
            <td>{{ isEmpty(element.max_limit) | makeComma }}</td>
            <td>
              <!-- modal 방식 -->
                <b-button v-b-modal="'myModal' + idx">상세</b-button>

                <b-modal :id="'myModal' + idx" title="상세페이지">
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
           return "";
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
      // this.items_max = this.Depo.sort((a, b) => {return b.intr_rate2 - a.intr_rate2})
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
