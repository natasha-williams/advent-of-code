import React from 'react';

import { formatData, getTotal } from '@lib/utils';

import data from './api/07.txt';

const ROOT = '/';


class Command {
    ACTION_CD = 'cd'
    CMD = '$'
    CMD_DIR = 'dir'
    PARENT_DIR = '..'

    constructor (command=null, data=[ROOT]) {
        this.command = command && command.split(' ');
        this.workingDirectory = data;
    }

    execute (command) {
        this.command = command.split(' ');

        if (this.isParentDir()) {
            this.workingDirectory.pop();
        } else if (this.isChangeDir()) {
            this.workingDirectory.push(this.command[2]);
        }
    }

    isCommand () {
        const [cmd,] = this.command;
        return cmd === this.CMD;
    }

    isChangeDir () {
        const [, action,] = this.command;
        return this.isCommand() && action === this.ACTION_CD && ROOT !== this.PARENT_DIR;
    }

    isParentDir () {
        const [,, dir] = this.command;
        return this.isCommand() && dir == this.PARENT_DIR;
    }

    isFile () {
        const [cmd,] = this.command;
        return !this.isCommand() && cmd !== this.CMD_DIR;
    }

    getSize () {
        const [cmd,] = this.command;
        return this.isFile() ? parseInt(cmd) : 0;
    }

    getPath () {
        const path = this.workingDirectory.join('.');
        this.workingDirectory.pop();
        return path;
    }
}


class FileSystem {
    SIZE = 70000000

    constructor (data, maxSize=100000) {
        this.command = new Command();
        this.sizes = {};
        this.maxSize = maxSize;
        this.setData(data);
    }

    setData (data) {
        data.forEach(item => {
            this.command.execute(item);

            if (this.command.isFile()) {
                const command = new Command(item, [...this.command.workingDirectory]);

                while (command.workingDirectory.length > 0) {
                    const path = command.getPath();

                    if (!this.sizes[path]) {
                        this.sizes[path] = 0;
                    }

                    this.sizes[path] += command.getSize();
                }
            }
        });
    }

    getLargeDirs () {
        return Object.values(this.sizes).filter(num => num <= this.maxSize);
    }

    getDeleteDir (size) {
        const spaceNeeded = size - (this.SIZE - this.sizes[ROOT]);
        const sizes = Object.values(this.sizes);        
        sizes.sort((a, b) => a - b);
        return sizes.find(item => item >= spaceNeeded);
    }
}


export default function Day07() {
    const formattedData = formatData({ data });
    
    const part1 = () => {
        return getTotal(new FileSystem(formattedData).getLargeDirs());
    };

    const part2 = () => {
        return new FileSystem(formattedData).getDeleteDir(30000000);
    };

    return (
        <React.Fragment>
            <section>
                <h1>Part 1</h1>
                <p>{part1()}</p>
            </section>

            <section>
                <h1>Part 2</h1>
                <p>{part2()}</p>
            </section>
        </React.Fragment>
    );
}
