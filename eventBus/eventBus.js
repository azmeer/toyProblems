function EventBus() {
  this.events = {};
}

EventBus.prototype.emit = function(eventName, data) {
  if (this.events[eventName]) {
    this.events[eventName].forEach(cb => cb(data));
  }
}
 
EventBus.prototype.subscribe = function(eventName, callback) {
  this.events[eventName] =
    this.events[eventName] ? this.events[eventName].concat([callback]) : [callback];
}
 
function error1 (data) {
  console.log('Error 1. ' + data.message);
}
 
function error2 (data) {
  console.log('Error 2. ' + data.message);
}
 
function success (data) {
  console.log('SUCCESS! ' + data.message);
}

var emitter = new EventBus();
 
emitter.emit('error', {message: 'Error one.'});
 
emitter.subscribe('error', error1);
emitter.emit('error', {message: 'Second error.'});
 
emitter.subscribe('error', error2);
emitter.emit('error', {message: 'Yet another error.'});
 
emitter.subscribe('success', success)
emitter.emit('success', {message: 'Great success!'});
