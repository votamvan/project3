<template>
  <div
        class="col-md-12"
      >
        <v-card style="margin-bottom: 15px">
          <div class="row">
              <div class="col-md-6 col-sm-6 col-xs-6">
                <v-card outlined>
                  <v-card-title>Uploads</v-card-title>
                  <v-divider></v-divider>
                  <div class="row same-height">
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
              <div class="col-md-6 col-sm-6 col-xs-6 same-height">
                <v-card outlined>
                  <v-card-title>Result</v-card-title>
                  <v-divider></v-divider>
                  <div class="row same-height">
                    <div class="col-sm-12">
                      {{noResult}}
                    </div>
                </div>
                </v-card>
              </div>

            </div>
        </v-card>
      </div>
</template>
<style>
  .same-height:{
      min-height: 600px;
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
