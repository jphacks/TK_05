import DS from 'ember-data';

export default DS.Model.extend({
	number: DS.attr('number'),
	title: DS.attr('string'),
	body: DS.attr('string'),
	stage: DS.belongsTo('stage'),
	category: DS.belongsTo('category'),
	isPublic: DS.attr('boolean'),
	isDelete: DS.sttr('boolean')
});
