const express = require('express')
const app = express()

app.get('/', function(req, res) {
	res.send("Port set to 3000")
})

app.


app.listen(3000, function () {
	console.log('Example app listening on port 3000!')
})