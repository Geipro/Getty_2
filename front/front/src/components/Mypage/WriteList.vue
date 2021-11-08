<template>
  <div>
    <div>
      <div class="row align-items-center">
        <span class="col-8 offset-2 align-self-center"><h5 class="text-white mb-0">내가 쓴 글</h5></span>
      </div>
      <br>
      <div class="d-lg-block col-lg-12">
        <table class="table table-bg-light table-hover">
          <thead>
            <tr class="text-white">
              <th scope="col">번호</th>
              <th scope="col">제목</th>
              <th scope="col">내용</th>
              <th scope="col">조회수</th>
              <th scope="col">작성일</th>
            </tr>
          </thead>
         <tbody>
          <tr class="text-white" v-for="(element, idx) in postinfo" :key="idx">
            <td scope="row">{{ idx + 1 }}</td>
            <td>{{ element.title }}</td>
            <td>{{ element.content }}</td>
            <td>{{ element.hit }}</td>
            <td>{{ element.create_date }}</td>
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
  name: 'WriteList',
  data: function () {
    return {
      token:{
          token : localStorage.getItem('Token'),
        },
      postinfo: []
    }
  },
  created(){

  },
  mounted(){
    axios({
      method: 'get',
      url: 'https://k5a405.p.ssafy.io/backend/my_post',
      headers : {"token" : `${this.token.token}`}
    })
    .then((res) =>{
      this.postinfo = res.data
      console.log(this.postinfo[0])
    }).catch((err) =>{
      console.log(err)
    })
  }
}

</script>

<style>

</style>
