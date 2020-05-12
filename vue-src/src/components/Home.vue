<template>
  <div
        class="col-md-12"
      >
        <v-card style="margin-bottom: 15px">
          <v-img
            :src="require('../assets/img/home/collections.jpg')"
            class="white--text align-center"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="400px"
          >
            <h1 class="text-center font-size">Collections</h1>
            <div class="text-center">
              <router-link to="/shop" class="white--text v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default">Let's started</router-link>
            </div>
          </v-img>
        </v-card>
        <v-card>
          <div class="col-md-12">
            <h2>How it works</h2>
            <p>...</p>
          </div>
        </v-card>
      </div>
</template>

<script>
    export default {
        data () {
            return {
                items: [
                    { title: 'Click Me' },
                    { title: 'Click Me' },
                    { title: 'Click Me' },
                    { title: 'Click Me 2' },
                ],
                activeBtn: 1,
                colors: [
                    'indigo',
                    'warning',
                    'pink darken-2',
                    'red lighten-1',
                    'deep-purple accent-4',
                ],
                slides: [
                    'First',
                    'Second',
                    'Third',
                    'Fourth',
                    'Fifth',
                ],
            }
        },
    }
</script>
<style>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  }
</style>

