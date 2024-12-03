import { createClient } from "redis";

async function nodeRedis(params) {
  const client = await createClient()
    .on('error', err => console.log('Redis client not connected to the server: ', err.message))
    .connect();  
  console.log('Redis client connected to the server');
}  

nodeRedis();
