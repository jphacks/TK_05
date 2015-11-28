import DS from 'ember-data';

export default DS.Model.extend({
	user: DS.belongsTo('user'),
	service: DS.belongsTo('service'),
	token: DS.attr('string')
});
