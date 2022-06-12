// Distance between two points
function distance(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
}

// Geometric mean of an array of numbers
function geometricMeanArray(array) {
    return Math.pow(array.reduce((a, b) => a * b), 1 / array.length);
}

// Arithmetic mean of an array of numbers
function arithmeticMeanArray(array) {
    return array.reduce((a, b) => a + b) / array.length;
}

// Check the status of AWS EC2 instance
function checkInstanceStatus(instanceId) {
    return new Promise((resolve, reject) => {
        ec2.describeInstances({ InstanceIds: [instanceId] }, (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}
