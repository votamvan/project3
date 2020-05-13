<template>
  <div class="main">
    <div class="container">
      About page
    </div>
  </div>
</template>
<script>
export default {
  name: "About",
  props: {
    msg: String,
    ram: String
  },
  data() {
    alert('about page');
    return {
      sita: ""
    };
  },
  mounted() {}
};
</script>