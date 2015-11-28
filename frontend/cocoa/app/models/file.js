import DS from 'ember-data';

export default DS.Model.extend({
	name: DS.attr('string'),
	file: DS.attr('string'),
	question: DS.belongsTo('question'),
	isPublic: DS.attr('boolean'),
	isDelete: DS.attr('boolean')
});
