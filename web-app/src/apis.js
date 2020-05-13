module.exports = class Api {
	getHostUrl(){
		return 'http://3.23.154.60:5000';
		// return 'http://ec2-18-222-249-229.us-east-2.compute.amazonaws.com:5000';
	}
	getApiVersion(){
		return '';
		// return 'v0';
	}
	getApiUrl(){
		return this.getHostUrl()+'/'+this.getApiVersion();
	}
	getPostApi(){
		return this.getApiUrl()
	}
	
}