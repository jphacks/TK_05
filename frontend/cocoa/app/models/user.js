import DS from 'ember-data';

export default DS.Model.extend({
	email: DS.attr('string'),
	is_staff: DS.attr('boolean'),
	is_active: DS.attr('boolean'),
	points:  DS.attr('number'),
	last_scored: DS.attr('date'),
	screen_name: DS.attr('string'),
	icon: DS.attr('string')
});
