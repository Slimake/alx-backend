import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();
client
  .on('error', err => console.log('Redis client not connected to the server: Error:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
