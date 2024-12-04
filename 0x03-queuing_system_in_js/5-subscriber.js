import { createClient, print } from "redis";


const subscriber = createClient();
subscriber
  .on('error', err => console.log('Redis client not connected to the server: Error:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

  // Subscribe to a channel
subscriber.subscribe('holberton school channel');

// Listen for messages
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message == 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
