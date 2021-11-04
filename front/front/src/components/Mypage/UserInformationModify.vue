<template>
  <div>
    <div>
      <h1 style="color:white">
        개인 정보 수정
      </h1>
      <br>
      <!-- 정보는 기존 data를 가져와야 됨 -->
      <b-form @submit="onSubmit" v-if="show">
        <b-form-group id="input-group-2" label="닉네임" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.name"
            placeholder="Enter name"
            required
          ></b-form-input>
        </b-form-group>

        <br>
        <b-form-group
          id="input-group-1"
          label="Email address"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            placeholder="Enter email"
            required
          ></b-form-input>
        </b-form-group>

        <br>
        <b-button type="submit" variant="primary">수정</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>

export default {
  name: 'UserInformationModify',
  data() {
      return {
        form: {
          email: '',
          name: '',
          food: null,
          checked: []
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      // onReset(event) {
      //   event.preventDefault()
      //   // Reset our form values
      //   this.form.email = ''
      //   this.form.name = ''
      //   this.form.food = null
      //   this.form.checked = []
      //   // Trick to reset/clear native browser form validation state
      //   this.show = false
      //   this.$nextTick(() => {
      //     this.show = true
      //   })
      // }
    }
}
</script>

<style>

</style>
