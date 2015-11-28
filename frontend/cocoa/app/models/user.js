import DS from 'ember-data';

export default DS.Model.extend({
	email: DS.attr('string'),
	isStaff: DS.attr('boolean'),
	isActive: DS.attr('boolean'),
	points:  DS.attr('number'),
	lastScored: DS.attr('date'),
	screenName: DS.attr('string'),
	icon: DS.belongsTo('icon')
});
