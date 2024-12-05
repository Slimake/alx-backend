import { createQueue } from 'kue';

const queue = createQueue();

const blacklisted = ['4153518780', '4153518781'];


function sendNotification(phoneNumber, message, job, done) {
  // Track progress
  const progress = 0;
  const phoneNumberBlacklisted = blacklisted.includes(phoneNumber);

  job.progress(0, 100);

  if (phoneNumberBlacklisted === true) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
