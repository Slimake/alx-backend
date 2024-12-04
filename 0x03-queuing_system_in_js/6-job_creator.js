import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '07035681098',
  message: 'Hello there',
}

const push_notification_code = queue.create('jobData', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${push_notification_code.id}`);
  }
});

push_notification_code.on('job complete', (id) => {
  console.log('Notification job completed');
})
.on('job failed', (id, err) => {
  console.log('Notification job failed');
});
