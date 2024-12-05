function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (let i = 0; i < jobs.length; i++) {
    const jobData = jobs[i];
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  
    job.on('complete', (result) => {
      console.log(`Notification job #${job.id} completed`);
    })
    .on('failed', (errorMessage) => {
      console.log(`Notification job #${job.id} failed: ${errorMessage}`);
    })
    .on('progress', (progress, data) => {
      console.log(`Notification job #${job.id} ${progress}% complete`);
    });
  }
}

module.exports = createPushNotificationsJobs;
