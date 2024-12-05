import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '07035681098',
  message: 'Hello there',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (id) => {
  console.log('Notification job completed');
})
.on('failed', (id, err) => {
  console.log('Notification job failed');
});
