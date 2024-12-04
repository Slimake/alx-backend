import { createClient } from "redis";

const client = createClient();
function nodeRedis() {
  client
    .on('error', err => console.log('Redis client not connected to the server: Error:', err.message))
    .on('connect', () => console.log('Redis client connected to the server'));
}

nodeRedis();
