import DS from 'ember-data';

export default DS.Model.extend({
	user: DS.belongsTo('user'),
	question: DS.belongsTo('question'),
	answer: DS.attr('string'),
	isCorrect: DS.attr('boolean')
});
