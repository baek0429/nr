const request = require('request')

request('https://booking.naver.com/booking/12/bizes/105398/items/2652591?area=bns', { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }

  console.log(res)
});

