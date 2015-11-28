import DS from 'ember-data';

export default DS.Model.extend({
  user: DS.belongsTo('user'),
  question: DS.belongsTo('question'),
  importance: DS.belongsTo('importance'),
  title: DS.attr('string'),
  body: DS.attr('string')
});
