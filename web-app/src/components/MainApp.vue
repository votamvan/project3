<template>
  <div class="main" >
    <div class="container">
      <div class="col-sm-8 col-sm-offset-2">
        <div class="color-box__full--large color-box--white" >
          <div>
            <div class="image">
              <div class="row">
                <div class="col-sm-8 col-md-8 col-lg-8">
                  <h3 v-if="!item.image" style="font-size: 40px;font-weight: 300;" class="text-center">Welcome</h3>
                  <h3 v-if="!item.image" style="font-size: 40px;font-weight: 300;" class="text-center">to</h3>
                  <h3 v-if="!item.image" style="font-size: 40px;font-weight: 300;" class="text-center">
                    <span v-if="!item.image" style="font-size: 54px; color: #737272; font-weight: 300;">boot</span>
                    <span v-if="!item.image" style="font-size: 66px; color: #737272; font-weight: 300;">U</span>
                    <span v-if="!item.image" style="font-size: 54px; color: #737272; font-weight: 300;">p</span>
                  </h3>
                  
                  <img v-if="loading2 == false && loading == false" :src="item.image" class="img-responsive" />
                  <img v-if="loading2 == true || loading == true" class="img-responsive"  src="./../assets/loading.gif" />
                  <p>{{results}}</p>
                </div>
                <div class="col-sm-4 col-md-4 col-lg-4">
                  <h4>Step 1. Select an image</h4>
                  <h4>Step 2. Detect product</h4>
                  <h4>Step 3. Grad-CAM</h4>
                  <h4>Step 4. Similar Products</h4>
                </div>
              </div>
            </div>      
            <div class="buttons mt-20">
              <label :class="btnFileInput" ><input style="display: none;" accept="image/*" type="file" name="file" id="file" @change="onFileChange" @click="clearValue"/>Choose a file</label>
              <a style="margin-left: 10px;" v-on:click="detectApi" :class="btnDelect + ((item.image)?'':' disabled')">
                <i class="fa fa-spinner fa-spin" v-if="loading2"></i>
                Detect Product
              </a>
              <a style="margin-left: 10px;" v-on:click="callApi" :class="btnCAM + ((item.image)?'':' disabled')">
                  <i class="fa fa-spinner fa-spin" v-if="loading"></i>
                  Grad-CAM
                </a>
                <a style="margin-left: 10px;" v-if="storeDatas.length > 0" :class="btnViewSimilar + ((item.image)?'':' disabled')" v-on:click="viewSimilarProduct">
                  View Similar products <i class="fa fa-angle-down" aria-hidden="true"></i>
                </a>
            </div> 
          </div>
          <div class="store-container">
              <h4>Similar products</h4>
              <div class="row">
                <div class="col-sm-4 similar-pro" v-for="(storeData,index) in storeDatas" :key="index">
                  <img class="img-responsive" :src="baseUrl+storeData.image">
                  <p><b>Name:</b> <a target="_blank" :href="storeData.URL">{{storeData.name}}</a></p>
                  <p><b>Price:</b> {{storeData.price}}</p>
                </div>
              </div>
          </div>
        </div>
      </div>    
    </div>      
    </div>
</template>
<style type="text/css">
  .similar-pro{
    border-bottom: 1px solid;
    border-radius: 0px 0px 10px 0px;
  }
</style>
<script>
export default {
  name: 'MainApp',
  props: {
    msg: String
  },
  data: function () {
    return {
      btnFileInput:'btn btn-primary btn-xl',
      btnDelect:'btn btn-warning btn-xl',
      btnCAM:'btn btn-success btn-xl',
      btnViewSimilar:'btn btn-info btn-xl',
      baseUrl:this.api.getHostUrl(),
      
      loading:false,
      loading2:false,
      storeDatas:[],
      results:"",
      item: {
        image: false
      }
    }
  },
  methods: {
    clearValue() {
        var element = document.getElementById('file');
        element.value = null;
        
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
      this.storeDatas = [];
    },
    callApi(e){
      window.$(".store-container").slideUp();
      
      this.results = "";
      var api  = this.api.getPostApi();
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

        console.log(resp)
        // var url = URL.createObjectURL(resp);
        // this.item.image = url;

        this.item.image = resp.url+"?t=" + new Date().getTime();
        
        this.loading = false;
        this.storeDatas = resp.store;
        this.results = resp.data;
      })

      e.preventDefault();
    },
    detectApi(e){

      this.results = "";
      
      var api  = this.api.getDetectApi();
      console.log("requested Url:"+api)

      this.loading2 = true;
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
            return response.json();
        }
        throw new Error('Network response was not ok.');
            
      })
      .then((resp)=>{

        console.log(resp);
        this.results = resp.data;
        this.storeDatas = resp.store;
        this.item.image = resp.url+"?t=" + new Date().getTime();
        
        this.loading2 = false;
        
      })

      e.preventDefault();
    },
    viewSimilarProduct(e){
      e.preventDefault();
      window.$(".store-container").slideToggle();
    }
  },
  mounted(){
    document.querySelector(".store-container").style.display = 'none';
  }
}
</script>

