/**
 * Created by danielv.
 */
function buildApp(){
    const PORT = process.env.PORT || 9000;
    const CUSTOMER_API_URL = process.env.CUSTOMER_API_URL || "http://localhost:5000";
    var express = require('express');

    var app = express();
    var http = require('http'); //var https = require('https');
    app.set('views', __dirname + '/public');
    app.engine('html', require('ejs').renderFile);
    app.set('view engine', 'html');
    app.set('views', __dirname);
    app.use(handleAccess);
    app.use(express.static(__dirname + '/public')); //?
    app.use(express.static(__dirname + '/node_modules')); //?

    var server = http.createServer(app); // var server = https.createServer(options, app);
    server.listen(PORT);

    app.get('/jquery.min.js', function (req, res) {
        res.send(__dirname + '/node_modules/jquery/dist/jquery.min.js');
    });

    app.get('/', function (req, res) {
        res.render(__dirname + '/public/main.html', {url: CUSTOMER_API_URL});
    });

    return {
        server: server,
        app: app
    };

    function handleAccess(req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS');
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        if ('OPTIONS' == req.method) {
            res.status(200).json({msg: 'Ok.'});
        } else {
            next();
        }
    }
}

module.exports = buildApp();
