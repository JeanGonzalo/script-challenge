const AWS = require('aws-sdk');

const credentials = {accessKeyId: 'mykey', secretAccessKey: 'mysecret', region: 'myregion'}
AWS.config.update(credentials);
const s3 = new AWS.S3();

const params = { 
 Bucket: 'coderbytechallengesandbox',
 Prefix: '__cb__'
}

s3.listObjects(params, function (err, data) {
 if(err)throw err;
 console.log(data);
});