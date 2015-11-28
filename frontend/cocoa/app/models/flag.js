import DS from 'ember-data';

export default DS.Model.extend({
	question: DS.belongsTo('question'),
	flag: DS.attr('string'),
	point: DS.attr('number')
});
