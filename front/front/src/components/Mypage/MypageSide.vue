<template>
  <div>
    <span>
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link
            :to="{ name: 'Mypage' }"
          >
            개인정보수정
          </router-link>
        </li>
        <br>
        <!-- 사용 안 할 듯 -->
        <!-- <li class="nav-item">
          <router-link
            :to="{ name: 'OrderCheck' }"
          >
            비밀번호 수정
          </router-link>
        </li>
        <br> -->

        <!-- props/ emit으로 해보기 -->
        <li class="nav-item">
          <router-link
            :to="{ name: 'Mywrite' }"
          >
            내가 쓴 글
          </router-link>
        </li>
        <br>
        <li class="nav-item">
          <router-link
            :to="{ name: 'Myreview' }"
          >
            내가 쓴 댓글
          </router-link>
        </li>
      </ul>
    </span>
  </div>
</template>

<script>
export default {
  name: 'MypageSide',
}
</script>

<style>

</style>
