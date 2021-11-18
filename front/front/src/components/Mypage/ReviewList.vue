<template>
  <div>
    <div>
      <div class="row align-items-center">
        <span class="col-8 offset-2 align-self-center text-center"><h5 class="text-white mb-0">내가 쓴 댓글</h5></span>
      </div>
      <br>
      <div class="d-lg-block col-lg-12 text-center">
        <table class="table table-bg-light table-hover">
          <thead>
            <tr class="text-white">
              <th scope="col">번호</th>
              <th scope="col">댓글 내용</th>
              <th scope="col">날짜</th>
            </tr>
          </thead>
        <tbody>
          <tr class="text-white" v-for="(element, idx) in reviewinfo" :key="idx">
            <td class="col-2" scope="row">{{ idx + 1 }}</td>
            <td class="col-8">{{ element.content }}</td>
            <td class="col-2">{{ element.create_date }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ReviewList',
  data: function () {
    return {
      token:{
          token : localStorage.getItem('Token'),
        },
      reviewinfo: []
    }
  },
  created(){

  },
  mounted(){
    axios({
      method: 'get',
      url: 'https://k5a405.p.ssafy.io/backend/my_comment',
      headers : {"token" : `${this.token.token}`}
    })
    .then((res) =>{
      this.reviewinfo = res.data
      // console.log(this.reviewinfo[0])
    }).catch((err) =>{
      console.log(err)
    })
  }
}

</script>

<style>
.table-hover tbody tr:hover td {
    background: #ffffff
}
</style>
