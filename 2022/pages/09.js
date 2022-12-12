import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/09.txt';


class Action {
    constructor (action, number) {
        this.action = action;
        this.number = parseInt(number);
    }

    getAxis () {
        switch (this.action) {
            case 'R':
            case 'L':
                return 0;
            case 'U':
            case 'D':
                return 1;
        }
    }

    getPosition () {
        switch (this.action) {
            case 'R':
            case 'D':
                return 1;
            case 'U':
            case 'L':
                return -1;
        }
    }
}


class Bridge {
    constructor (data, num=2) {
        this.data = data.map(item => new Action(...item.split(' ')));
        this.knots = [...Array(num).keys()].map(item => [0, 0]);
        this.positions = new Set();
    }

    getDifference (knot) {
        const [headX, headY] = this.knots[knot - 1];
        const [tailX, tailY] = this.knots[knot];
        return [headX - tailX, headY - tailY];
    }

    shouldMoveKnot (knot) {
        const [x, y] = this.getDifference(knot);
        return Math.abs(x) > 1 || Math.abs(y) > 1;
    }

    moveKnot (knot) {
        const [x, y] = this.getDifference(knot);
        const minNum = x === 0 || y === 0 ? -1 : 0; 
        const maxNum = x === 0 || y === 0 ? 1 : 0; 
        let [tailX, tailY] = this.knots[knot];

        if (!this.shouldMoveKnot(knot)) {
            return;
        }

        if (minNum === 0 && (x === 0 || y === 0)) {
            return;
        }

        if (x > maxNum) {
            tailX++;
        } else if (x < minNum) {
            tailX--;
        }

        if (y > maxNum) {
            tailY++;
        } else if (y < minNum) {
            tailY--;
        }

        this.knots[knot] = [tailX, tailY];

        if (knot === this.knots.length - 1) {
            this.positions.add(`${tailX}${tailY}`);
        }
    }

    getTailPositions () {
        this.data.forEach(item => {
            [...Array(item.number).keys()].forEach(num => {
                this.knots[0][item.getAxis()] += item.getPosition();

                [...Array(this.knots.length - 1).keys()].forEach(knot => {
                    this.moveKnot(knot + 1);
                });
            });   
        });

        return this.positions;
    }
}


export default function Day09() {
    const part1 = () => {
        const bridge = new Bridge(formatData({ data }));
        return bridge.getTailPositions().size + 1;
    };

    const part2 = () => {
        const bridge = new Bridge(formatData({ data }), 10);
        return bridge.getTailPositions().size + 1;
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
