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
              <div class="row">
                <div class="col-sm-8">
                  <img v-if="loading2 == false && loading == false" :src="item.image" class="img-responsive" />
                  <img v-if="loading2 == true || loading == true" class="img-responsive"  src="./../assets/loading.gif" />
                  <p>{{results}}</p>
                </div>
                <div class="col-sm-4">
                  
                </div>
              </div>
            </div>      
            <div class="buttons">
              <span style="padding-right: 10px;">
                <a v-on:click="removeImage" class="btn btn-danger btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">
                Next Image
                <i class="fa fa-step-forward"></i>
              </a>
              </span>
              <span style="padding-right: 10px;"><a v-on:click="detectApi" class="btn btn-primary btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">
              <i class="fa fa-spinner fa-spin" v-if="loading2"></i>
              Detect Image
            </a></span>
              <span style="padding-right: 10px;">
                <a v-on:click="callApi" class="btn btn-success btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" data-interaction-type="Button" id="lp-bottom-cta">
                  <i class="fa fa-spinner fa-spin" v-if="loading"></i>
                  CAM
                </a>
            </span>
            <span>
              <a v-if="this.currentApi == 'DETECT' " class="btn btn-primary btn-xl mt-20" data-cta-name="lp-bottom-cta" data-segment-interaction="link" v-on:click="viewSimilarProduct" data-interaction-type="Button" id="lp-bottom-cta">
                  View Similar products <i class="fa fa-angle-down" aria-hidden="true"></i>
                </a>
            </span>
            </div> 
                 
          </div>
          <div class="store-container">
              <h4>Similar products</h4>
              <div class="row">
                <div class="col-sm-4" v-for="(storeData,index) in storeDatas" :key="index">
                  <p>Type: {{storeData.Type}}</p>
                  <p>Name: {{storeData.name}}</p>
                  <p>Price: USD{{storeData.price}}</p>
                  <img class="img-responsive" :src="storeData.URL">
                </div>
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
      currentApi:'',
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
    removeImage: function (e) {
      this.item.image = false; 
      this.results = "";
      this.currentApi = '';
      e.preventDefault();
      window.$(".store-container").slideUp();
    },
    callApi(e){
      window.$(".store-container").slideUp();
      this.currentApi = '';
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
        //this.results = resp.data
        this.item.image = resp.data+"?t=" + new Date().getTime();
        this.currentApi = 'CAM';
        this.loading = false;
      })

      e.preventDefault();
    },
    detectApi(e){

      this.results = "";
      this.currentApi = '';
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
        this.currentApi = 'DETECT';
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

