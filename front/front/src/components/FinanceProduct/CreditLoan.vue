<template>
  <div class="justify-content-center align-items-center" style="text-align: center; width: 100%">
    <Navbar />
    <div class="inline-block mb-2">
      <a class="mt-3 mb-4 float-left" style="font-size: 30px">신용대출</a>
      <a class="float-right offset-10">금리 : %</a>
    </div>
    <div class="d-lg-block col-lg-12" style="background-color:#23282d">
      <table class="table table-bg-light table-hover">
        <thead>
          <tr class="text-warning">
            <th scope="col" >은행 이름 </th>
            <th scope="col">상품 이름</th>
            <th scope="col">대출 종류명</th>
            <th scope="col">신용평가회사</th>
            <th scope="col">평균 금리</th>
            <th scope="col">900점 초과 금리</th>
            <th scope="col">801 ~ 900</th>
            <th scope="col">701 ~ 800</th>
            <th scope="col">601 ~ 700</th>
            <th scope="col">501 ~ 600</th>
            <th scope="col">401 ~ 500</th>
            <th scope="col">301 ~ 400</th>
            <th scope="col">300 이하</th>
            <th scope="col">상세 정보</th>
          </tr>
        </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in CreditLoan" :key="idx">
            <td>{{ element.bank_name }}</td>
            <td>{{ element.product_name }}</td>
            <td>{{ element.crdt_prdt_type_nm }}</td>
            <td>{{ element.cb_name }}</td>
            <td>{{ isEmpty2(element.crdt_grad_avg) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_1) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_4) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_5) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_6) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_10) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_11) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_12) }}</td>
            <td>{{ isEmpty2(element.crdt_grad_13) }}</td>
            <td><!-- modal 방식 -->
                <b-button v-b-modal="'myModal' + idx">상세</b-button>

                <b-modal :id="'myModal' + idx" title="상세페이지">
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
  name: 'CreditLoan',
  components: {
        Navbar,
    },
  data: function () {
    return {
      CreditLoan: [],
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
      url: 'https://k5a405.p.ssafy.io/backend/credit_loan',
    })
    .then((res) =>{
      this.CreditLoan = res.data
      // 최저 금리 순으로
      this.items_avg = this.CreditLoan.sort((a, b) => {return a.crdt_grad_avg - b.crdt_grad_avg })
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
