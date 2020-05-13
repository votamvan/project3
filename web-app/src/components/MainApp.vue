<template>
  <div class="main" >
    <div class="container">
      <div class="col-sm-8 col-sm-offset-2">
        <div class="color-box__full--large color-box--white" >
          <div>
            <h2 v-if="!item.image">Select an image</h2>
            <input style="display: none;" type="file" name="file" id="file" @change="onFileChange"/>
            <label for="file" v-if="!item.image" >Choose a file</label>       
          </div>
          <div v-if="item.image">
            <div class="image">
              <img :src="item.image" />
            </div>      
            <div class="buttons">
              <span style="padding-right: 10px;"><a v-on:click="removeImage" class="btn btn-primary btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">Detect Image</a></span>
              <span>
                <a v-on:click="callApi" class="btn btn-primary btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">
                  <i class="fa fa-spinner fa-spin" v-if="loading"></i>
                  CAM
                </a>
            </span>
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
      loading:false,
      item: {
        image: false
      }
    }
  },
  methods: {
    hexToBase64(str) {
        return btoa(String.fromCharCode.apply(null, str.replace(/\r|\n/g, "").replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ")));
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var reader = new FileReader();
      reader.onload = (e) => {
        this.item.image = e.target.result;
      };
      reader.readAsDataURL(file);

    },
    removeImage: function (e) {
      this.item.image = false; 
      e.preventDefault();
    },
    callApi(e){
      //var api  = this.api.getPostApi();
      var api  = this.api.getDetectApi();
      console.log("requested Url:"+api)

      this.loading = true;
      var element = document.getElementById('file');

      var formData = new FormData();
      formData.append('file',element.files[0])

      var myHeaders = new Headers();
      myHeaders.append('pragma', 'no-cache');
      myHeaders.append('cache-control', 'no-cache');

      fetch(api,{
        method: 'POST',
        body: formData,
        headers: myHeaders
      })
      .then(function(response){
        if (response.ok) {
            // return response.blob();
            return response.json();
        }
        throw new Error('Network response was not ok.');
            
      })
      .then((resp)=>{
        console.log(resp.url)
        // var url = URL.createObjectURL(resp);
        // this.item.image = url;

        this.item.image = resp.url+"?t=" + new Date().getTime();

        this.loading = false;
      })

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
