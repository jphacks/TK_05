import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('about');
  this.route('questions');
  this.route('ranking');
  this.route('notice');
  this.route('contact');
});

export default Router;
