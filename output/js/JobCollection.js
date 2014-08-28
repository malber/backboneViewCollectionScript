var JobCollection = Backbone.Collection.extend({
	model: Job,
	url: "models/JobCollection.json",
	initialize: function(){
    	// Do something here
  	},
});