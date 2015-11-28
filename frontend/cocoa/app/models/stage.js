import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  requiredPoints: DS.attr('number'),
  requiredQuestion: DS.belongTo('question')
});
