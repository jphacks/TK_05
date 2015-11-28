import DS from 'ember-data';

export default DS.Model.extend({
    body: DS.attr('string'),
    user: DS.belongsTo('user'),
    writeup: DS.belongsTo('writeup'),
    isPublic: DS.attr('boolean'),
    isDelete: DS.attr('boolean')
});
