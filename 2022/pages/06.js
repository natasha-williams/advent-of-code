import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/06.txt';


class Computer {
    constructor (stream, length) {
        this.stream = stream;
        this.length = length;
    }

    getStart () {
        const maxNum = this.stream.length - this.length + 1;
        let num = 0;

        while (num !== maxNum) {
            const stream = this.stream.slice(num, num + this.length);

            if (stream.length === new Set(stream).size) {
                break;
            }

            num++;
        }

        return num + this.length;
    }
}


export default function Day06() {
    const formattedData = formatData({ data, splitAt: '' });
    
    const part1 = () => {
        return new Computer(formattedData, 4).getStart();
    };

    const part2 = () => {
        return new Computer(formattedData, 14).getStart();
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
