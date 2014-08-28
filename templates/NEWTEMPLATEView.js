var NEWTEMPLATEViewItem = Backbone.View.extend({
    tagName: 'li',
    className: 'NEWTEMPLATEViewItem',
    initialize: function() {
        this.template = _.template($('#NEWTEMPLATE-item-template').html());
        this.render();
    },
    render: function() {
        this.$el.html(this.template({ item: this.model}));
        return this;
    }
});

var NEWTEMPLATEListView = Backbone.View.extend({
    el: '#NEWTEMPLATEListViewContainer',
    tagName: 'ul',
    className: 'NEWTEMPLATEListView',
    initialize: function() {
        this.template = _.template($('#NEWTEMPLATE-list-template').html());
        this.render();
    },
    render: function() {
        self = this;
        this.$el.empty();
        this.$el.append(this.template());
        this.collection.each(function(model) {
            var tmp = new NEWTEMPLATEViewItem({model: model});
            self.$el.append(tmp.$el);
        });
        return this;
    }
});

