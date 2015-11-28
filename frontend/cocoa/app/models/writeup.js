import DS from 'ember-data';

export default DS.Model.extend({
    title: DS.attr('string'),
    body: DS.attr('string'),
    question: DS.belongsTo('question'),
    user: DS.belongsTo('user'),
    isPublic: DS.attr('boolean'),
    isDelete: DS.attr('boolean')
});
