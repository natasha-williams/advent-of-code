import React from 'react';

import { formatData } from '@lib/utils';

import data from './api/12.txt';


class Square {
    constructor (row, column, letter, start, end='E') {
        this.row = row;
        this.column = column;
        this.letter = letter;
        this.elevation = this.getElevation(start, end);
        this.isStart = letter === start;
        this.isEnd = letter === end;
        this.reset();
    }

    reset () {
        this.steps = 0;
        this.seen = false;
    }

    getElevation (start, end) {
        if (this.letter === start) {
            return 0;
        } else if (this.letter === end) {
            return 'z'.charCodeAt(0) - 'a'.charCodeAt(0);
        } else {
            return this.letter.charCodeAt(0) - 'a'.charCodeAt(0);
        }
    }

    isValid (square) {
        return this.elevation <= square.elevation + 1 && !this.seen;
    }

    getDirections (squares) {
        return [
            squares[this.row + 0]?.[this.column + 1],
            squares[this.row + 1]?.[this.column + 0],
            squares[this.row + 0]?.[this.column - 1],
            squares[this.row - 1]?.[this.column + 0],
        ].filter(item => item?.isValid(squares[this.row][this.column]));
    }
}


class Grid {
    constructor (data, start) {
        this.data = data.map((item, row) => item.split('').map((letter, col) => {
            return new Square(row, col, letter, start);
        }));
        this.starts = this.data.flat().filter(item => item.isStart);
        this.end = this.data.flat().find(item => item.isEnd);
    }

    run () {
        let steps = [];

        this.starts.forEach(item => {
            steps.push(this.getSteps(item));
            this.data.flat().forEach(item => item.reset());
        });

        return Math.min(...steps.filter(Boolean));
    }

    getSteps (start) {
        const queue = [start];

        while (queue.length > 0) {
            const square = queue.shift();

            if (square.seen) {
                continue;
            } else if (square.isEnd) {
                return square.steps;
            }

            square.getDirections(this.data).forEach(item => {
                item.steps = square.steps + 1;
                queue.push(item);
            });

            square.seen = true;
        }
    }
}


export default function Day12() {
    const part1 = () => {
        const grid = new Grid(formatData({ data }), 'S');
        return grid.run();
    };

    const part2 = () => {
        const grid = new Grid(formatData({ data }), 'a');
        return grid.run();
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
