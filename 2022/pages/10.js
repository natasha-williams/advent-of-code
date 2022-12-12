import React from 'react';

import { formatData, getTotal } from '@lib/utils';

import data from './api/10.txt';


class Instruction {
    constructor (action, number=0) {
        this.action = action;
        this.cycles = action === 'noop' ? 1 : 2;
        this.number = parseInt(number);
    }
}


class Circuit {
    constructor (data) {
        this.data = data.map(item => new Instruction(...item.split(' ')));
        this.x = 1;
        this.interval = 40;
        this.signals = [];
        this.rows = [];
    }

    getSignalStrengths (start=20) {
        let cycles = 0;

        this.data.forEach(item => {
            for (let i = 0; i < item.cycles; i++) {
                cycles++;

                if ((cycles - start) % this.interval === 0) {
                    this.signals.push(cycles * this.x);
                }
            }

            this.x += item.number;
        });

        return this.signals;
    }

    getLetters () {
        let cycles = 0;

        this.data.forEach(item => {
            for (let i = 0; i < item.cycles; i++) {
                const column = cycles % this.interval;
                const char = this.x - 1 <= column && column <= this.x + 1 ? '#' : '.';

                if (column === 0) {
                    this.rows.push([]);
                }

                this.rows[this.rows.length - 1].push(char);
                cycles++;
            }

            this.x += item.number;
        });

        return this.rows;
    }
}


export default function Day10() {
    const part1 = () => {
        const circuit = new Circuit(formatData({ data }));
        return getTotal(circuit.getSignalStrengths());
    };

    const part2 = () => {
        const circuit = new Circuit(formatData({ data }));
        return circuit.getLetters().map(item => item.join(''));
    };

    return (
        <React.Fragment>
            <section>
                <h1>Part 1</h1>
                <p>{part1()}</p>
            </section>

            <section>
                <h1>Part 2</h1>
                {part2().map(item => {
                    return (
                        <div style={{ fontFamily: 'monospace' }}>
                            {item}
                        </div>
                    );
                })}
            </section>
        </React.Fragment>
    );
}
