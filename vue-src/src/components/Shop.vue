<template>
  <div>
    <v-container>
      <div class="row">
        <div class="col-md-6 col-sm-6 col-xs-12 min-height">
          <v-card outlined>
            <v-card-title>Uploads</v-card-title>
            <v-divider></v-divider>
            <div class="row">
            <form>
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="col-lg-12">
                  <input type="file">
                </div>
              </div>
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="col-lg-12">
                  <button type="submit" class="primary white--text mt-5 v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default">Submit</button>
                </div>
              </div>
            </form>
          </div>
          </v-card>
        </div>
        <div class="col-md-6 col-sm-6 col-xs-12 min-height">
          <v-card outlined>
            <v-card-title>Result</v-card-title>
            <v-divider></v-divider>
            <div class="row">
            <form>
              <div class="col-md-12 col-sm-12 col-xs-12">
                <div class="col-lg-12">
                    {{noResult}}
                </div>
              </div>
            </form>
          </div>
          </v-card>
        </div>
      </div>
    </v-container>
  </div>
</template>
<style>
  .min-height:{
      min-height: 600px
  }
</style>
<script>
    export default {
      data(){
        return {
          noResult:'No result found.'
        }
      }
    }
</script>
