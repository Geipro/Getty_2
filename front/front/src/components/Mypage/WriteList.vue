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
              <th scope="col">이름</th>
              <th scope="col">추천</th>
              <th scope="col">날짜</th>
              <th scope="col">조회수</th>
            </tr>
          </thead>
         <tbody>
          <tr class="text-white">
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr class="text-white">
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr class="text-white">
            <th scope="row">3</th>
            <td colspan="2">Larry the Bird</td>
            <td>@twitter</td>
            <td>@twitter</td>
            <td>@twitter</td>
          </tr>
          <!-- 아래 이용해서 돌리기 -->
            <!-- <writingListItem
              v-for="(writing, idx) in writingList"
              :key="idx"
              :writing="writing"
              :movieId="movieId"
            /> -->
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'WriteList',
  data: function () {
    return {
    }
  },

}

</script>

<style>

</style>
