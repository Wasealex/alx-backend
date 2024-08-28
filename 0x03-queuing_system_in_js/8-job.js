import { Queue, Job } from 'kue';

export const createPushNotificationsJobs = (jobList, notificationQueue) => {
  if (!(jobList instanceof Array)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobDetails of jobList) {
    const notificationJob = notificationQueue.create('push_notification_code_3', jobDetails);

    notificationJob
      .on('enqueue', () => {
        console.log('Notification job created:', notificationJob.id);
      })
      .on('complete', () => {
        console.log('Notification job', notificationJob.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', notificationJob.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', notificationJob.id, `${progress}% complete`);
      });

    notificationJob.save();
  }
};

export default createPushNotificationsJobs;
