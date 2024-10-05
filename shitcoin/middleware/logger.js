import express from 'express';


const logger = (req, res, next) => {
    let ip = req.ip.slice(7, req.ip.length);
    console.log(`${ip}  ->  ${req.method}  ->  ${req.url}`);
    next()
}


export default logger;