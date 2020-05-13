<template>
  <div class="main" >
    <div class="container">
      <div class="col-sm-8 col-sm-offset-2">
        <div class="color-box__full--large color-box--white" >
          <div v-if="!item.image">
            <h2>Select an image</h2>
            <input type="file" id="file" @change="onFileChange(item, $event)"/>
            <label for="file" >Choose a file</label>       
          </div>
          <div v-else>
            <div class="image"><img :src="item.image" /></div>      
            <div class="buttons">
              <span style="padding-right: 10px;"><a v-on:click="removeImage" class="btn btn-primary btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">Detect Image</a></span>
              <span><a v-on:click="removeImage" class="btn btn-primary btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">CAM</a></span>
            </div>      
            
          </div>
        </div>
      </div>    
    </div>      
    </div>
</template>

<script>
export default {
  name: 'MainApp',
  props: {
    msg: String
  },
  data: function () {
    return {
      item: {
        image: false
      }
    }
  },
  methods: {
    onFileChange(item, e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(item, files[0]);
    },
    createImage(item, file) {
      // var image = new Image();
      var reader = new FileReader();
      reader.onload = (e) => {
        item.image = e.target.result;
      };
      reader.readAsDataURL(file);

              this.helper.request({
                    type: 'post',
                    withData:'json',
                    url: this.api.getPostApi(),
                    dataType:'json',
                    auth:false,
                    data: {
                      username:this.username,
                      password:this.password
                    },
                    success:(resp)=>{
                      if(resp.status == 'error'){
                        this.message = resp.message;
                        this.alert_status = "alert alert-danger";
                      }else{
                        this.alert_status = "alert alert-success";
                        this.message = resp.message;
                        this.helper.setUserInfo(resp.data);
                        setTimeout(()=>{ 
                          window.location.href = "/";                                      
                        }, 2000);
                      }
                    }
              })
    },
    removeImage: function (e) {
      this.item.image = false; 
      e.preventDefault();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
