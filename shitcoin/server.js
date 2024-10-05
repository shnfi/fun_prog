import express from 'express';
import path from 'path';
import logger from './middleware/logger.js';


const server = express()

const dir = path.dirname(path.resolve('.'));
server.use(express.static('public'))


server.route('/').get((req, res) => {
    logger(req, res, () => {
        const fp = path.join(dir, 'shitcoin', 'public', 'main.html');
        res.status(200).sendFile(fp)
    })
})


server.listen(8080, () => {
    console.log('[-] Runing on port 8080...\n')
})
