<template>
  <div class="container">
    <!-- <div class="row"  > -->
    <nav
      id="nav"
      class="navbar navbar-default"
      style="height:100px;width:100%;background-color:#c9c2cf;"
    >
      <!-- style="background-color:#666050" -->
      <div class="container-fluid">
        <!-- <div class="navbar-header">
        <a class="navbar-brand" href="#">{{ram}}</a>
        </div>-->
        <ul class="nav navbar-nav" style="margin:10px;padding-left :70px">
          <!-- margin:30px;padding-left :70px -->
          <li>
            <router-link style="font-size:30px;color:black" class="dropdown-item" to="/">Home</router-link>
          </li>
          <li>
            <router-link
              style="font-size:30px;color:black"
              class="dropdown-item"
              to="/main-app"
            >Detect</router-link>
          </li>
          <li>
            <router-link style="font-size:30px;color:black" class="dropdown-item" to="/about">About</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </div>
  <!-- </div> -->
</template>
<script>
export default {
  name: "Header",
  props: {
    msg: String,
    ram: String
  },
  data() {
    return {
      sita: "hare ram"
    };
  },
  mounted() {}
};
</script>
