import { LOGGER } from '../constant/env';

enum ELogLevel {
    DEBUG = 'DEBUG',
    INFO = 'INFO',
    WARN = 'WARN',
    ERROR = 'ERROR'
}

function getColor(level: ELogLevel): string {
    switch (level) {
        case ELogLevel.DEBUG:
            return 'blue';
        case ELogLevel.INFO:
            return 'green';
        case ELogLevel.WARN:
            return 'orange';
        case ELogLevel.ERROR:
            return 'red';
    }
}

function logger(level: ELogLevel = ELogLevel.DEBUG, message: string, ...args: any[]): void {
    if (LOGGER) {
        const date = new Date();
        const time = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
        const color = getColor(level);
        console.log(`%c[${time}][${level}]: ${message}`, `color: ${color}`, ...args);
    }
}

function debugLog(message: string, ...args: any[]): void {
    logger(ELogLevel.DEBUG, message, ...args);
}

function infoLog(message: string, ...args: any[]): void {
    logger(ELogLevel.INFO, message, ...args);
}

function warnLog(message: string, ...args: any[]): void {
    logger(ELogLevel.WARN, message, ...args);
}

function errorLog(message: string, ...args: any[]): void {
    logger(ELogLevel.ERROR, message, ...args);
}

export { debugLog, infoLog, warnLog, errorLog };
