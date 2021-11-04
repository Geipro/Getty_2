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
a {
   text-decoration:none;
   color: white;
}
</style>
